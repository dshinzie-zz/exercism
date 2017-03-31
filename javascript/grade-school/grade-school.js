var School = function(){
  this.schoolRoster = {};
}

School.prototype.roster = function(){
  return this.schoolRoster;
};

School.prototype.add = function(student, grade){
  this.schoolRoster[grade] = this.schoolRoster[grade] || [];
  this.schoolRoster[grade].push(student);
  this.schoolRoster[grade].sort();
}

School.prototype.grade = function(gradeNumber){
  return this.schoolRoster[gradeNumber] || [];
}

module.exports = School;
