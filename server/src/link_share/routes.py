# pylint: skip-file
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from passlib import pwd
from datetime import datetime
from pytz import utc

from .model import LinkShare
from .schema import NewLinkShare, UpdateLinkShare


link_share_router = APIRouter(prefix='/link_share')


@link_share_router.post('/')
async def new_link_share(data: NewLinkShare):
    link_share = LinkShare()

    link_share.personal_id = data.personal_id
    link_share.salt_link = pwd.genword(entropy=56, charset="ascii_62")
    link_share.status = data.status

    if link_share.save():
        link_share_id = str(link_share.id)
        link_share.salt_link = link_share.salt_link + link_share_id
        link_share.save()
        return link_share.salt_link
    else:
        return JSONResponse({
            "error": True,
            "data": f"Something went wrong and link could not be created."
        }, 422)


@link_share_router.get("/personal_id/{salt_link}")
async def get_personal_id_of_link_share(salt_link):
    personal_id = LinkShare.select('personal_id').where(
        'salt_link', salt_link).first().personal_id
    if personal_id:
        return personal_id
    else:
        return JSONResponse({
            "error": True,
            "data": f"Personal could not be found."
        }, 404)


@link_share_router.get("/available/{salt_link}")
async def check_if_link_is_available(salt_link):
    # last value of salt_link is the link_share unique id
    salt_link_to_id = int(salt_link[-1])
    link_share = LinkShare.find(salt_link_to_id)

    if (link_share.status != 'Available'):
        return False

    current_time = datetime.now(utc)

    input_timestamp = datetime.fromisoformat(str(link_share.created_at))

    # 60 is for minutes, (60 * 60 * 24) for days = minute -> hour -> day 24h
    time_difference = (current_time - input_timestamp).total_seconds() / 60
    if time_difference > 5:
        link_share.status = 'Expired'
        if link_share.save():
            return False
    else:
        return True


@link_share_router.get("/count/{salt_link}")
async def check_if_salt_exists(salt_link):
    counted_link_share = LinkShare.where('salt_link', salt_link).count()
    if counted_link_share > 0:
        return True
    else:
        return False


@link_share_router.put('/{salt_link}')
async def update_link_share(salt_link, data: UpdateLinkShare):
    # last value of salt_link is the link_share unique id
    salt_link_to_id = int(salt_link[-1])
    link_share = LinkShare.find(salt_link_to_id)

    link_share.status = data.status

    if link_share.save():
        return JSONResponse({
            "error": False,
            "data": f"Link was successfully updated."
        }, 200)
    else:
        return JSONResponse({
            "error": True,
            "data": f"Something went wrong and link could not be updated."
        }, 422)
