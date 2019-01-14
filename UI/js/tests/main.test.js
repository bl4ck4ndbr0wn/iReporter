const puppeteer = require("puppeteer");

let browser, page;

beforeAll(async () => {
  browser = await puppeteer.launch();
  page = await browser.newPage();
});

describe("iReporter Home", () => {
  describe("Landing page redirect to login ", () => {
    beforeEach(async () => {
      await page.goto("https://bl4ck4ndbr0wn.github.io/iReporter/UI");
    }, 10000);

    describe("Page title", () => {
      it("equals IReporter - Login into your Account", async () => {
        const title = await page.title();
        expect(title).toEqual("IReporter - Login into your Account");
      });
    }, 10000);
  }, 10000);
}, 10000);

describe("iReporter Home", () => {
  describe("Login page redirect to all reports  ", () => {
    beforeEach(async () => {
      await page.goto("https://bl4ck4ndbr0wn.github.io/iReporter/UI");
    }, 10000);

    describe("Page on form submit", () => {
      it("equals IReporter - Login into your Account", async () => {
        await page.click("input#auth_username");
        await page.type("input#auth_username", "alpha");

        await page.click("input#auth_password");
        await page.type("input#auth_password", "Ak3Swal(");

        await page.click("input#login_submit");

        const title = await page.title();
        expect(title).toEqual("IReporter - Login into your Account");
      });
    }, 10000);
  }, 10000);
}, 10000);

afterAll(async () => {
  await browser.close();
});
