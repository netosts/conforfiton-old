export function encrypt(value) {
  try {
    const numberValue = Number(value);
    if (!numberValue) {
      return null;
    }
    const mapping = {
      0: ")(*^%$#@!",
      1: "#$&@<>{}~!",
      2: "`=+*[]|:;",
      3: "_-~!@#$%",
      4: "{}:;<=>?",
      5: "!@#^&*()_",
      6: "><}{:)?*+",
      7: "^&*()_+[]",
      8: "{:;-_*<>",
      9: "@#&*?<>[]",
    };

    const numberString = String(numberValue);
    let encryptedString = '';

    for (let i = 0; i < numberString.length; i++) {
      const digit = numberString.charAt(i);
      encryptedString += mapping[digit];
    }

    return encryptedString;

  } catch (e) {
    console.error(e);
    return null;
  }
};


export function decrypt(value) {
  try {
    if (typeof value !== 'string') {
      return null;
    }
    const mapping = {
      ")(*^%$#@!": '0',
      "#$&@<>{}~!": '1',
      "`=+*[]|:;": '2',
      "_-~!@#$%": '3',
      "{}:;<=>?": '4',
      "!@#^&*()_": '5',
      "><}{:)?*+": '6',
      "^&*()_+[]": '7',
      "{:;-_*<>": '8',
      "@#&*?<>[]": '9',
    };

    let decryptedValue = '';
    let encryptedSymbol = '';
    for (let i = 0; i < value.length; i++) {
      encryptedSymbol += value.charAt(i);
      if (mapping.hasOwnProperty(encryptedSymbol)) {
        decryptedValue += mapping[encryptedSymbol];
        encryptedSymbol = ''; // Reset for the next symbol
      }
    }
    return decryptedValue;
  } catch (e) {
    console.error(e);
    return null;
  }
};





