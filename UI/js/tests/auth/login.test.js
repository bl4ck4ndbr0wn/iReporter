const puppeteer = require("puppeteer");

let browser, page;

beforeEach(async () => {
  browser = await puppeteer.launch();
  page = await browser.newPage();
});

describe("iReporter Login", () => {
  describe("Login page redirect to all reports  ", () => {
    beforeEach(async () => {
      await page.goto("http://alphanganga.me/iReporter/UI/login.html");
    }, 100000);

    describe("Page on form submit ", () => {
      it("with correct credentials", async () => {
        await page.click("input#auth_username");
        await page.type("input#auth_username", "alpha");

        await page.click("input#auth_password");
        await page.type("input#auth_password", "Ak3Swal(");

        await page.click("input#login_submit");

        await page.waitForSelector("#popuptextmsg");
        const message = await page.$eval(
          "#popuptextmsg",
          response => response.innerText
        );
        expect(message).toMatch("You were successfully logged in alpha");
      }, 100000);
    }, 100000);
  }, 100000);
}, 100000);

describe("iReporter ", () => {
  describe("Login  Form", () => {
    beforeEach(async () => {
      await page.goto("http://alphanganga.me/iReporter/UI/login.html");
    }, 100000);

    describe("Page onSubmit ", () => {
      it("with password field empty", async () => {
        await page.click("input#auth_username");
        await page.type("input#auth_username", "alpha");

        await page.click("input#auth_password");
        await page.type("input#auth_password", "");

        await page.click("input#login_submit");

        await page.waitForSelector("#popuptextmsg");
        const message = await page.$eval(
          "#popuptextmsg",
          response => response.innerText
        );
        expect(message).toMatch("password Field can not be blank");
      }, 100000);
    }, 100000);
  }, 100000);
}, 100000);

describe("iReporter ", () => {
  describe("Login  Form", () => {
    beforeEach(async () => {
      await page.goto("http://alphanganga.me/iReporter/UI/login.html");
    }, 100000);

    describe("Page onSubmit ", () => {
      it("with username and password empty or username empty", async () => {
        await page.click("#auth_username");
        await page.type("#auth_username", "");

        await page.click("#auth_password");
        await page.type("#auth_password", "");

        await page.click("#login_submit");

        await page.waitForSelector("#popuptextmsg");
        const message = await page.$eval(
          "#popuptextmsg",
          response => response.innerText
        );
        expect(message).toMatch("username Field can not be blank");
      });
    }, 100000);
  }, 100000);
}, 100000);

describe("iReporter ", () => {
  describe("Login  Form", () => {
    beforeEach(async () => {
      await page.goto("http://alphanganga.me/iReporter/UI/login.html");
    }, 100000);

    describe("Page onSubmit ", () => {
      it("with incorrect password syntax", async () => {
        await page.click("#auth_username");
        await page.type("#auth_username", "alpha");

        await page.click("#auth_password");
        await page.type("#auth_password", "alpha");

        await page.click("#login_submit");

        await page.waitForSelector("#popuptextmsg");
        const message = await page.$eval(
          "#popuptextmsg",
          response => response.innerText
        );
        expect(message).toMatch(
          "Password field must be at least 8 characters."
        );
      });
    }, 100000);
  }, 100000);
}, 100000);

describe("iReporter ", () => {
  describe("Login  Form", () => {
    beforeEach(async () => {
      await page.goto("http://alphanganga.me/iReporter/UI/login.html");
    }, 100000);

    describe("Page onSubmit ", () => {
      it("with incorrect credentials", async () => {
        await page.click("#auth_username");
        await page.type("#auth_username", "alpha");

        await page.click("#auth_password");
        await page.type("#auth_password", "Alpha1234");

        await page.click("#login_submit");

        await page.waitForSelector("#popuptextmsg");
        const message = await page.$eval(
          "#popuptextmsg",
          response => response.innerText
        );
        expect(message).toMatch("Username or password is incorrect.");
      });
    }, 100000);
  }, 100000);
}, 100000);

//Checks if the login page renders correctly
describe("iReporter Render", () => {
  describe("Login  page", () => {
    beforeEach(async () => {
      await page.goto("http://alphanganga.me/iReporter/UI/login.html");
    }, 100000);

    describe("Page Render ", () => {
      it("Correctly", async () => {
        const loginPage = await page.evaluate(() => {
          let logintitle = document.getElementById("logintitle").innerText;
          let signuplink = document.getElementById("signinLink").innerText;
          let username = document.getElementById("auth_username");
          let password = document.getElementById("auth_password");

          return {
            logintitle: logintitle,
            signuplink: signuplink,
            username: username,
            password: password
          };
        });

        expect(loginPage.logintitle).toBe("Sign in");
        expect(loginPage.signuplink).toBe("Sign up");
        expect(loginPage.username).toBeDefined();
        expect(loginPage.password).toBeDefined();
      }, 100000);
    }, 100000);
  }, 100000);
}, 100000);

afterEach(async () => {
  await browser.close();
});
