const fs = require('fs');

const countStudents = (path) => {
  try {
    let fileData = fs.readFileSync(path, 'utf8').toString().split('\n');
    fileData = fileData.slice(1, fileData.length - 1);
    console.log(`Number of students: ${fileData.length}`);
    const arrayOfClasses = {};
    for (const row of fileData) {
      const student = row.split(',');
      if (!arrayOfClasses[student[3]]) arrayOfClasses[student[3]] = [];
      arrayOfClasses[student[3]].push(student[0]);
    }
    for (const cls in arrayOfClasses) {
      if (cls) console.log(`Number of students in ${cls}: ${arrayOfClasses[cls].length}. List: ${arrayOfClasses[cls].join(', ')}`);
    }
  } catch (error) {
    throw new Error('Cannot load the database');
  }
};

module.exports = countStudents;
