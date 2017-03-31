var PhoneNumber = function(phone){
  var cleanPhone = phone.replace(/[^\w]/gi, '');

  this.number = function(){
    if ((cleanPhone.length > 10 && cleanPhone[0] != 1) || cleanPhone.length < 10) {
      return "0000000000";
    } else if (cleanPhone.length > 10) {
      return cleanPhone.slice(1, 11);
    } else {
      return cleanPhone;
    }
  }

  this.areaCode = function(){
    return cleanPhone.slice(0, 3);
  }

  this.toString = function(){
    return cleanPhone.replace(/(\d{3})(\d{3})(\d{4})/, '($1) $2-$3');
  }
}


module.exports = PhoneNumber;
