function toRoman(num){
  var CONVERSION = {
    1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC",
    50: "L", 49: "XLIX", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"
  };

  var romanized = '';
  Object.keys(CONVERSION).reverse().forEach(function(arabic){
    while(num >= arabic){
      num -= arabic;
      romanized += CONVERSION[arabic];
    }
  });
  return romanized;
}

module.exports = toRoman;
