export const schema = {
  bench_press_lifted: 'required|between:0,800',
  bench_press_reps: 'required|between:0,15',

  barbell_curl_lifted: 'required|between:0,100',
  barbell_curl_reps: 'required|between:0,15',

  pull_down_lifted: 'required|between:0,200',
  pull_down_reps: 'required|between:0,15',

  leg_press_lifted: 'required|between:0,1000',
  leg_press_reps: 'required|between:0,15',

  leg_extension_lifted: 'required|between:0,300',
  leg_extension_reps: 'required|between:0,15',

  leg_curl_lifted: 'required|between:0,250',
  leg_curl_reps: 'required|between:0,15',
}