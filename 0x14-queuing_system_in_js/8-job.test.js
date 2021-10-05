import kue from "kue";
import { expect } from "chai";
import createPushNotificationsJobs from "./8-job";

const queue = kue.createQueue();

describe("createPushNotificationsJobs", () => {
  before(function() {
    queue.testMode.enter();
  });

  afterEach(function() {
    queue.testMode.clear();
  });

  after(function() {
    queue.testMode.exit();
  });

  it("display a error message if jobs is not an array", function() {
    expect(() => { createPushNotificationsJobs(2, queue);
    }).to.throw("Jobs is not an array");
  });

  it("if jobs is not an array passing Object", function() {
    expect(() => { createPushNotificationsJobs({}, queue);
    }).to.throw("Jobs is not an array");
  });

  it("if jobs is not an array passing integer", function() {
    expect(() => { createPushNotificationsJobs(13121989, queue);
    }).to.throw("Jobs is not an array");
  });

  it("if jobs is not an array passing String", function() {
    expect(() => { createPushNotificationsJobs("TaylorSwift", queue);
    }).to.throw("Jobs is not an array");
  });


});
