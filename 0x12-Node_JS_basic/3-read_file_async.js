const fs = require('fs');

const countStudents = (path) => {
  const promise = (res, rej) => {
    fs.readFile(path, (error, data) => {
      if (error) rej(Error('Cannot load the database'));
      if (data) {
        let total = data.toString().split('\n');
        total = total.slice(1, total.length - 1);
        console.log(`Number of students: ${total.length}`);
        const arrayOfClasses = {};
        for (const row of total) {
          const student = row.split(',');
          if (!arrayOfClasses[student[3]]) arrayOfClasses[student[3]] = [];
          arrayOfClasses[student[3]].push(student[0]);
        }
        for (const cls in arrayOfClasses) {
          if (cls) console.log(`Number of students in ${cls}: ${arrayOfClasses[cls].length}. List: ${arrayOfClasses[cls].join(', ')}`);
        }
      }
      res();
    });
  };
  return new Promise(promise);
};

module.exports = countStudents;
