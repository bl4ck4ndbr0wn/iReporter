const faker = require("faker");
const puppeteer = require("puppeteer");

let browser, page;

const state = {
  firstname: faker.name.firstName(),
  lastname: faker.lorem.word(),
  email: faker.internet.email(),
  username: faker.name.firstName(),
  password: faker.internet.password() + faker.internet.password()
};

beforeEach(async () => {
  browser = await puppeteer.launch();
  page = await browser.newPage();
});

describe("iReporter register", () => {
  describe("register page redirect to login  ", () => {
    beforeEach(async () => {
      await page.goto("http://alphanganga.me/iReporter/UI/register.html");
    }, 10000);

    describe("Page on form submit ", () => {
      it("with correct credentials", async () => {
        await page.click("input#auth_firstname");
        await page.type("input#auth_firstname", state.firstname);

        await page.click("input#auth_lastname");
        await page.type("input#auth_lastname", state.lastname);

        await page.click("input#auth_username");
        await page.type("input#auth_username", state.username);

        await page.click("input#auth_email");
        await page.type("input#auth_email", state.email);

        await page.click("input#auth_password");
        await page.type("input#auth_password", state.password);

        await page.click("input#register_submit");

        await page.waitForSelector("#popuptextmsg");
        const message = await page.$eval(
          "#popuptextmsg",
          response => response.innerText
        );
        expect(message).toMatch("User created Successfully.");
      }, 10000);
    }, 10000);
  }, 10000);
}, 10000);

describe("iReporter register", () => {
  describe("register page redirect to login  ", () => {
    beforeEach(async () => {
      await page.goto("http://alphanganga.me/iReporter/UI/register.html");
    }, 10000);

    describe("Page on form submit ", () => {
      it("with username field empty", async () => {
        await page.click("input#register_submit");

        await page.waitForSelector("#popuptextmsg");
        const message = await page.$eval(
          "#popuptextmsg",
          response => response.innerText
        );
        expect(message).toMatch("username Field can not be blank");
      }, 10000);
    }, 10000);
  }, 10000);
}, 10000);

describe("iReporter register", () => {
  describe("register page redirect to login  ", () => {
    beforeEach(async () => {
      await page.goto("http://alphanganga.me/iReporter/UI/register.html");
    }, 10000);

    describe("Page on form submit ", () => {
      it("with password field empty", async () => {
        await page.click("input#auth_username");
        await page.type("input#auth_username", state.username);

        await page.click("input#register_submit");

        await page.waitForSelector("#popuptextmsg");
        const message = await page.$eval(
          "#popuptextmsg",
          response => response.innerText
        );
        expect(message).toMatch("password Field can not be blank");
      }, 10000);
    }, 10000);
  }, 10000);
}, 10000);

describe("iReporter register", () => {
  describe("register page redirect to login  ", () => {
    beforeEach(async () => {
      await page.goto("http://alphanganga.me/iReporter/UI/register.html");
    }, 10000);

    describe("Page on form submit ", () => {
      it("with firstname field empty", async () => {
        await page.click("input#auth_username");
        await page.type("input#auth_username", state.username);

        await page.click("input#auth_password");
        await page.type("input#auth_password", state.password);

        await page.click("input#register_submit");

        await page.waitForSelector("#popuptextmsg");
        const message = await page.$eval(
          "#popuptextmsg",
          response => response.innerText
        );
        expect(message).toMatch("firstname Field can not be blank");
      }, 10000);
    }, 10000);
  }, 10000);
}, 10000);

describe("iReporter register", () => {
  describe("register page redirect to login  ", () => {
    beforeEach(async () => {
      await page.goto("http://alphanganga.me/iReporter/UI/register.html");
    }, 10000);

    describe("Page on form submit ", () => {
      it("with lastname field empty", async () => {
        await page.click("input#auth_firstname");
        await page.type("input#auth_firstname", state.firstname);

        await page.click("input#auth_username");
        await page.type("input#auth_username", state.username);

        await page.click("input#auth_password");
        await page.type("input#auth_password", state.password);

        await page.click("input#register_submit");

        await page.waitForSelector("#popuptextmsg");
        const message = await page.$eval(
          "#popuptextmsg",
          response => response.innerText
        );
        expect(message).toMatch("lastname Field can not be blank");
      }, 10000);
    }, 10000);
  }, 10000);
}, 10000);

describe("iReporter register", () => {
  describe("register page redirect to login  ", () => {
    beforeEach(async () => {
      await page.goto("http://alphanganga.me/iReporter/UI/register.html");
    }, 10000);

    describe("Page on form submit ", () => {
      it("with email field empty", async () => {
        await page.click("input#auth_firstname");
        await page.type("input#auth_firstname", state.firstname);

        await page.click("input#auth_username");
        await page.type("input#auth_username", state.username);

        await page.click("input#auth_password");
        await page.type("input#auth_password", state.password);

        await page.click("input#auth_lastname");
        await page.type("input#auth_lastname", state.lastname);

        await page.click("input#register_submit");

        await page.waitForSelector("#popuptextmsg");
        const message = await page.$eval(
          "#popuptextmsg",
          response => response.innerText
        );
        expect(message).toMatch("email Field can not be blank");
      }, 10000);
    }, 10000);
  }, 10000);
}, 10000);

describe("iReporter register", () => {
  describe("register page redirect to login  ", () => {
    beforeEach(async () => {
      await page.goto("http://alphanganga.me/iReporter/UI/register.html");
    }, 10000);

    describe("Page on form submit ", () => {
      it("with username already linked to an account", async () => {
        await page.click("input#auth_firstname");
        await page.type("input#auth_firstname", state.firstname);

        await page.click("input#auth_username");
        await page.type("input#auth_username", "admin");

        await page.click("input#auth_password");
        await page.type("input#auth_password", state.password);

        await page.click("input#auth_lastname");
        await page.type("input#auth_lastname", state.lastname);

        await page.click("input#auth_email");
        await page.type("input#auth_email", state.email);

        await page.click("input#register_submit");

        await page.waitForSelector("#popuptextmsg");
        const message = await page.$eval(
          "#popuptextmsg",
          response => response.innerText
        );
        expect(message).toMatch("A user with that username already exists");
      }, 10000);
    }, 10000);
  }, 10000);
}, 10000);

//Checks if the register page renders correctly
describe("iReporter Render", () => {
  describe("Register  page", () => {
    beforeEach(async () => {
      await page.goto("http://alphanganga.me/iReporter/UI/register.html");
    }, 10000);

    describe("Page Render ", () => {
      it("Correctly", async () => {
        const registerPage = await page.evaluate(() => {
          let registertitle = document.getElementById("registertitle")
            .innerText;
          let signuplink = document.getElementById("signinLink").innerText;
          let username = document.getElementById("auth_username");
          let password = document.getElementById("auth_password");
          let firstname = document.getElementById("auth_firstname");
          let lastname = document.getElementById("auth_lastname");
          let othername = document.getElementById("auth_othername");
          let email = document.getElementById("auth_email");
          let confirm_password = document.getElementById(
            "auth_confirm_password"
          );

          return {
            registertitle,
            signuplink,
            username,
            password,
            firstname,
            othername,
            lastname,
            email,
            confirm_password
          };
        });

        expect(registerPage.registertitle).toBe("Sign up");
        expect(registerPage.signuplink).toBe("Sign in");
        expect(registerPage.username).toBeDefined();
        expect(registerPage.password).toBeDefined();
        expect(registerPage.firstname).toBeDefined();
        expect(registerPage.lastname).toBeDefined();
        expect(registerPage.othername).toBeDefined();
        expect(registerPage.email).toBeDefined();
        expect(registerPage.confirm_password).toBeDefined();
      }, 10000);
    }, 10000);
  }, 10000);
}, 10000);

afterEach(async () => {
  await browser.close();
});
