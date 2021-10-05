import kue from "kue"
const queue = kue.createQueue();
const job = {
    phoneNumber: "13121989",
    message: "This is a msg to verify your subscription for the TaylorSwift newsletter",
  }

const Newjob = queue.create('push_notification_code', job);
Newjob.save();

Newjob.on('enqueue', (id, type) => {
  console.log(`Notification job created: ${Newjob.id}`)
});

Newjob.on('complete', (result) => {
  console.log('Notification job completed');
});
  
Newjob.on('failed', (err) => {
  console.log('Notification job failed');
});
