# Cypress
[Cypress](#cypress)[Cypress](/wiki/cypress)[end-to-end testing](/wiki/end-to-end-testing)[Cypress](/wiki/cypress)[Cypress](/wiki/cypress)[unit testing](/wiki/unit-testing)[end-to-end testing](/wiki/end-to-end-testing)[test runner](/wiki/test-runner)[Cypress](/wiki/cypress)
### Related Terms:
- Web Automation tool
- Playwright
[Web Automation tool](/glossary/web-automation-tool)[Playwright](/glossary/playwright)
### See also:
- Official Website
- Wikipedia
[Official Website](https://www.cypress.io/)[Wikipedia](https://en.wikipedia.org/wiki/Cypress_(software))
## Questions aboutCypress?

#### Basics and Importance
- What is Cypress?Cypressis anend-to-end testingframeworkdesigned for modern web applications. It runs tests in a browser and is built on top of technologies likeJavaScriptandNode.js. Unlike many other testing tools,Cypressexecutes tests in the same run loop as the application, providing native access to every object without the need for a separate driver or server.Cypressoffers arich interactivetest runnerthat allows you to see commands as they execute while also viewing the application under test. The tool providesreal-time reloadsfortest-driven development, with tests rerunning upon file save.Tests inCypressare written using achainableAPIthat works with promises, thus simplifying the handling of asynchronous operations.CypressincludesjQuery-like commandsfor DOM traversal and manipulation, making it familiar to front-end developers.Cypressprovidesautomatic waitingbefore performing actions or assertions, eliminating the need for explicit waits or sleeps in most cases. It also offersspies, stubs, and clocksto verify and control the behavior of server responses, functions, or timers.The tool has ascreenshot and video recordingfeature, which is handy for debugging and understanding test failures.Cypresstests can be run headlessly in Continuous Integration (CI) environments or interactively during development.Cypress's architecture does not useSeleniumorWebDriver, which allows for faster execution and more control but also means it's primarily suited for testing applications that run in a browser. It supportsChrome-family browsers(including Electron) andFirefox.
- Why is Cypress used in testing?Cypressis used in testing primarily for itssimplicityanddeveloper-friendlyapproach toend-to-end testing. It allows for writingflakiness-freetests due to its unique architecture that runs in the same run-loop as the application being tested. This results in morereliableandconsistenttests compared to other tools that operate outside the browser.The use ofCypressis favored for itsreal-time reloads, which provide instant feedback on test code changes, enhancing productivity and reducing the time spent on writing and maintaining tests. Itsautomatic waitingmechanism eliminates the need for manual sleep or wait commands, thus reducing the complexity oftest scripts.Developers and QA engineers opt forCypresswhen they needtight integrationwith modern development tools and workflows, including continuous integration and version control systems.Cypress'srich debugging capabilitiesmake it easier to diagnose and fix issues directly from the browser's developer tools.Cypress'sscreenshot and video recordingfeatures are crucial for visualizing the state of the application at the time of test failure, facilitating quicker troubleshooting. Itsnetwork traffic controlallows for easy stubbing and testing of edge cases without the need for backend dependencies.Overall,Cypressis used for itsall-in-onetesting experience, providing a robust set of tools that cater to the needs of modern web application testing, all within a single, coherent framework.
- What are the key features of Cypress?Key features ofCypressinclude:Real-Time Reloads: Cypress automatically reloads tests upon detecting changes to the test code, providing immediate feedback.Time Travel: Cypress takes snapshots as tests run, allowing you to hover over commands in the Command Log to see exactly what happened at each step.Automatic Waiting: Cypress waits for commands and assertions before moving on, eliminating the need for explicit waits or sleeps.Consistent Results: Tests in Cypress are less flaky and more reliable as it runs in the same run-loop as the application.Debuggability: With readable errors and stack traces, Cypress makes debugging tests easier. You can also use familiar dev tools.Network Traffic Control: Intercept and control every network request, enabling you to test edge cases without involving your server.Screenshots and Videos: Cypress can capture screenshots automatically on failure, or you can take them manually. It also records a video of the entire test run.Cross Browser Testing: Cypress supports testing across multiple browsers, including Chrome, Firefox, Edge, and Electron.Parallelization: Tests can be run in parallel across multiple machines to speed up execution time in Continuous Integration (CI).Dashboard Service: Provides insights into tests with analytics, parallelization, and history when used with the Cypress Dashboard.Spies, Stubs, and Clocks: Verify and control the behavior of functions, server responses, or timers.Accessibility Testing: With plugins likecypress-axe, you can incorporate accessibility checks into your test suite.These features are designed to streamline the testing process, making it more efficient and effective fortest automationengineers.
- How does Cypress differ from other testing tools like Selenium?Cypressdiffers fromSeleniumin several key aspects:Architecture:Cypressruns in the same run-loop as the application being tested, leading to faster execution and more consistent results.Seleniumoperates outside the browser, which can introduce latency and flakiness.Language Support:Cypresstests are written in JavaScript, whileSeleniumsupports multiple languages like Java, C#, Python, and Ruby.Direct Access:Cypresshas direct access to the DOM and can interact with elements more naturally.Seleniumrequires an intermediary (WebDriver) to communicate with the browser, which can slow down interactions.Setupand Configuration:Cypressis easier to set up, with no need for additional drivers or servers.Seleniumoften requires additionalsetupfor theWebDriverand browser-specific drivers.Real-time Reloads:Cypressoffers aTest Runnerthat automatically reloads upon test file changes, providing instant feedback.Seleniumdoes not have a built-in equivalent.Automatic Waiting:Cypressautomatically waits for commands and assertions before moving on.Seleniumrequires explicit waits or sleep commands to manage timing issues.API Testing:Cypressincludes built-in support forAPI testing, allowing for both front-end and back-end tests in one framework.Seleniumis primarily focused on browser-based testing.Screenshots and Videos:Cypresscan take screenshots and record videos natively.Seleniumcan capture screenshots, but video recording often requires additional tools or plugins.Debuggability:Cypressprovides more informative error messages and stack traces, making debugging easier.Selenium's error messages can be less clear, making debugging more challenging.Cross-browser Testing:Seleniumsupports a wider range of browsers and versions.Cypress's cross-browser support is improving but has historically been limited to fewer browsers.
- What types of testing can be performed using Cypress?UsingCypress, testers can perform various types of testing, including:End-to-End Testing(E2E): Simulating real user scenarios from start to finish, ensuring the application behaves as expected in a production-like environment.Integration Testing: Testing the interactions between application layers or between different microservices to verify they work together correctly.Unit Testing: Although not its primary use case, Cypress can be used to test individual functions or components in isolation.Component Testing: Verifying the functionality and rendering of individual components, especially useful in modern JavaScript frameworks like React, Angular, or Vue.Visual Regression Testing: By integrating with tools like Percy or Applitools, Cypress can capture screenshots and compare them to baseline images to detect visual changes.Accessibility Testing: With plugins likecypress-axe, testers can incorporate accessibility checks into their test suites to ensure compliance with standards like WCAG.API Testing: Although Cypress is primarily a browser-based tool, it can be used to test REST or GraphQL APIs by sending HTTP requests and asserting the responses.Performance Testing: While not a full-fledged performance testing tool, Cypress can capture performance metrics like page load times and use assertions to flag performance regressions.Cypress's versatility allows it to cover a broad range of testing needs within a single framework, streamlining the development and testing workflow.

Cypressis anend-to-end testingframeworkdesigned for modern web applications. It runs tests in a browser and is built on top of technologies likeJavaScriptandNode.js. Unlike many other testing tools,Cypressexecutes tests in the same run loop as the application, providing native access to every object without the need for a separate driver or server.
[Cypress](/wiki/cypress)**end-to-end testingframework**[end-to-end testing](/wiki/end-to-end-testing)**JavaScript****Node.js**[Node.js](/wiki/node-js)[Cypress](/wiki/cypress)
Cypressoffers arich interactivetest runnerthat allows you to see commands as they execute while also viewing the application under test. The tool providesreal-time reloadsfortest-driven development, with tests rerunning upon file save.
[Cypress](/wiki/cypress)**rich interactivetest runner**[test runner](/wiki/test-runner)**real-time reloads**[test-driven development](/wiki/test-driven-development)
Tests inCypressare written using achainableAPIthat works with promises, thus simplifying the handling of asynchronous operations.CypressincludesjQuery-like commandsfor DOM traversal and manipulation, making it familiar to front-end developers.
[Cypress](/wiki/cypress)**chainableAPI**[API](/wiki/api)[Cypress](/wiki/cypress)**jQuery-like commands**
Cypressprovidesautomatic waitingbefore performing actions or assertions, eliminating the need for explicit waits or sleeps in most cases. It also offersspies, stubs, and clocksto verify and control the behavior of server responses, functions, or timers.
[Cypress](/wiki/cypress)**automatic waiting****spies, stubs, and clocks**
The tool has ascreenshot and video recordingfeature, which is handy for debugging and understanding test failures.Cypresstests can be run headlessly in Continuous Integration (CI) environments or interactively during development.
**screenshot and video recording**[Cypress](/wiki/cypress)
Cypress's architecture does not useSeleniumorWebDriver, which allows for faster execution and more control but also means it's primarily suited for testing applications that run in a browser. It supportsChrome-family browsers(including Electron) andFirefox.
[Cypress](/wiki/cypress)[Selenium](/wiki/selenium)[WebDriver](/wiki/webdriver)**Chrome-family browsers****Firefox**
Cypressis used in testing primarily for itssimplicityanddeveloper-friendlyapproach toend-to-end testing. It allows for writingflakiness-freetests due to its unique architecture that runs in the same run-loop as the application being tested. This results in morereliableandconsistenttests compared to other tools that operate outside the browser.
[Cypress](/wiki/cypress)**simplicity****developer-friendly**[end-to-end testing](/wiki/end-to-end-testing)**flakiness-free****reliable****consistent**
The use ofCypressis favored for itsreal-time reloads, which provide instant feedback on test code changes, enhancing productivity and reducing the time spent on writing and maintaining tests. Itsautomatic waitingmechanism eliminates the need for manual sleep or wait commands, thus reducing the complexity oftest scripts.
[Cypress](/wiki/cypress)**real-time reloads****automatic waiting**[test scripts](/wiki/test-script)
Developers and QA engineers opt forCypresswhen they needtight integrationwith modern development tools and workflows, including continuous integration and version control systems.Cypress'srich debugging capabilitiesmake it easier to diagnose and fix issues directly from the browser's developer tools.
[Cypress](/wiki/cypress)**tight integration**[Cypress](/wiki/cypress)**rich debugging capabilities**
Cypress'sscreenshot and video recordingfeatures are crucial for visualizing the state of the application at the time of test failure, facilitating quicker troubleshooting. Itsnetwork traffic controlallows for easy stubbing and testing of edge cases without the need for backend dependencies.
[Cypress](/wiki/cypress)**screenshot and video recording****network traffic control**
Overall,Cypressis used for itsall-in-onetesting experience, providing a robust set of tools that cater to the needs of modern web application testing, all within a single, coherent framework.
[Cypress](/wiki/cypress)**all-in-one**
Key features ofCypressinclude:
[Cypress](/wiki/cypress)- Real-Time Reloads: Cypress automatically reloads tests upon detecting changes to the test code, providing immediate feedback.
- Time Travel: Cypress takes snapshots as tests run, allowing you to hover over commands in the Command Log to see exactly what happened at each step.
- Automatic Waiting: Cypress waits for commands and assertions before moving on, eliminating the need for explicit waits or sleeps.
- Consistent Results: Tests in Cypress are less flaky and more reliable as it runs in the same run-loop as the application.
- Debuggability: With readable errors and stack traces, Cypress makes debugging tests easier. You can also use familiar dev tools.
- Network Traffic Control: Intercept and control every network request, enabling you to test edge cases without involving your server.
- Screenshots and Videos: Cypress can capture screenshots automatically on failure, or you can take them manually. It also records a video of the entire test run.
- Cross Browser Testing: Cypress supports testing across multiple browsers, including Chrome, Firefox, Edge, and Electron.
- Parallelization: Tests can be run in parallel across multiple machines to speed up execution time in Continuous Integration (CI).
- Dashboard Service: Provides insights into tests with analytics, parallelization, and history when used with the Cypress Dashboard.
- Spies, Stubs, and Clocks: Verify and control the behavior of functions, server responses, or timers.
- Accessibility Testing: With plugins likecypress-axe, you can incorporate accessibility checks into your test suite.
**Real-Time Reloads****Time Travel****Automatic Waiting****Consistent Results****Debuggability****Network Traffic Control****Screenshots and Videos****Cross Browser Testing****Parallelization****Dashboard Service****Spies, Stubs, and Clocks****Accessibility Testing**[Accessibility Testing](/wiki/accessibility-testing)`cypress-axe`
These features are designed to streamline the testing process, making it more efficient and effective fortest automationengineers.
[test automation](/wiki/test-automation)
Cypressdiffers fromSeleniumin several key aspects:
[Cypress](/wiki/cypress)[Selenium](/wiki/selenium)- Architecture:Cypressruns in the same run-loop as the application being tested, leading to faster execution and more consistent results.Seleniumoperates outside the browser, which can introduce latency and flakiness.
- Language Support:Cypresstests are written in JavaScript, whileSeleniumsupports multiple languages like Java, C#, Python, and Ruby.
- Direct Access:Cypresshas direct access to the DOM and can interact with elements more naturally.Seleniumrequires an intermediary (WebDriver) to communicate with the browser, which can slow down interactions.
- Setupand Configuration:Cypressis easier to set up, with no need for additional drivers or servers.Seleniumoften requires additionalsetupfor theWebDriverand browser-specific drivers.
- Real-time Reloads:Cypressoffers aTest Runnerthat automatically reloads upon test file changes, providing instant feedback.Seleniumdoes not have a built-in equivalent.
- Automatic Waiting:Cypressautomatically waits for commands and assertions before moving on.Seleniumrequires explicit waits or sleep commands to manage timing issues.
- API Testing:Cypressincludes built-in support forAPI testing, allowing for both front-end and back-end tests in one framework.Seleniumis primarily focused on browser-based testing.
- Screenshots and Videos:Cypresscan take screenshots and record videos natively.Seleniumcan capture screenshots, but video recording often requires additional tools or plugins.
- Debuggability:Cypressprovides more informative error messages and stack traces, making debugging easier.Selenium's error messages can be less clear, making debugging more challenging.
- Cross-browser Testing:Seleniumsupports a wider range of browsers and versions.Cypress's cross-browser support is improving but has historically been limited to fewer browsers.

Architecture:Cypressruns in the same run-loop as the application being tested, leading to faster execution and more consistent results.Seleniumoperates outside the browser, which can introduce latency and flakiness.
**Architecture**[Cypress](/wiki/cypress)[Selenium](/wiki/selenium)
Language Support:Cypresstests are written in JavaScript, whileSeleniumsupports multiple languages like Java, C#, Python, and Ruby.
**Language Support**[Cypress](/wiki/cypress)[Selenium](/wiki/selenium)
Direct Access:Cypresshas direct access to the DOM and can interact with elements more naturally.Seleniumrequires an intermediary (WebDriver) to communicate with the browser, which can slow down interactions.
**Direct Access**[Cypress](/wiki/cypress)[Selenium](/wiki/selenium)[WebDriver](/wiki/webdriver)
Setupand Configuration:Cypressis easier to set up, with no need for additional drivers or servers.Seleniumoften requires additionalsetupfor theWebDriverand browser-specific drivers.
**Setupand Configuration**[Setup](/wiki/setup)[Cypress](/wiki/cypress)[Selenium](/wiki/selenium)[setup](/wiki/setup)[WebDriver](/wiki/webdriver)
Real-time Reloads:Cypressoffers aTest Runnerthat automatically reloads upon test file changes, providing instant feedback.Seleniumdoes not have a built-in equivalent.
**Real-time Reloads**[Cypress](/wiki/cypress)[Test Runner](/wiki/test-runner)[Selenium](/wiki/selenium)
Automatic Waiting:Cypressautomatically waits for commands and assertions before moving on.Seleniumrequires explicit waits or sleep commands to manage timing issues.
**Automatic Waiting**[Cypress](/wiki/cypress)[Selenium](/wiki/selenium)
API Testing:Cypressincludes built-in support forAPI testing, allowing for both front-end and back-end tests in one framework.Seleniumis primarily focused on browser-based testing.
**API Testing**[API Testing](/wiki/api-testing)[Cypress](/wiki/cypress)[API testing](/wiki/api-testing)[Selenium](/wiki/selenium)
Screenshots and Videos:Cypresscan take screenshots and record videos natively.Seleniumcan capture screenshots, but video recording often requires additional tools or plugins.
**Screenshots and Videos**[Cypress](/wiki/cypress)[Selenium](/wiki/selenium)
Debuggability:Cypressprovides more informative error messages and stack traces, making debugging easier.Selenium's error messages can be less clear, making debugging more challenging.
**Debuggability**[Cypress](/wiki/cypress)[Selenium](/wiki/selenium)
Cross-browser Testing:Seleniumsupports a wider range of browsers and versions.Cypress's cross-browser support is improving but has historically been limited to fewer browsers.
**Cross-browser Testing**[Cross-browser Testing](/wiki/cross-browser-testing)[Selenium](/wiki/selenium)[Cypress](/wiki/cypress)
UsingCypress, testers can perform various types of testing, including:
[Cypress](/wiki/cypress)- End-to-End Testing(E2E): Simulating real user scenarios from start to finish, ensuring the application behaves as expected in a production-like environment.
- Integration Testing: Testing the interactions between application layers or between different microservices to verify they work together correctly.
- Unit Testing: Although not its primary use case, Cypress can be used to test individual functions or components in isolation.
- Component Testing: Verifying the functionality and rendering of individual components, especially useful in modern JavaScript frameworks like React, Angular, or Vue.
- Visual Regression Testing: By integrating with tools like Percy or Applitools, Cypress can capture screenshots and compare them to baseline images to detect visual changes.
- Accessibility Testing: With plugins likecypress-axe, testers can incorporate accessibility checks into their test suites to ensure compliance with standards like WCAG.
- API Testing: Although Cypress is primarily a browser-based tool, it can be used to test REST or GraphQL APIs by sending HTTP requests and asserting the responses.
- Performance Testing: While not a full-fledged performance testing tool, Cypress can capture performance metrics like page load times and use assertions to flag performance regressions.
**End-to-End Testing(E2E)**[End-to-End Testing](/wiki/end-to-end-testing)**Integration Testing**[Integration Testing](/wiki/integration-testing)**Unit Testing**[Unit Testing](/wiki/unit-testing)**Component Testing****Visual Regression Testing**[Visual Regression Testing](/wiki/visual-regression-testing)**Accessibility Testing**[Accessibility Testing](/wiki/accessibility-testing)`cypress-axe`**API Testing**[API Testing](/wiki/api-testing)**Performance Testing**[Performance Testing](/wiki/performance-testing)
Cypress's versatility allows it to cover a broad range of testing needs within a single framework, streamlining the development and testing workflow.
[Cypress](/wiki/cypress)
#### Installation and Setup
- How to install Cypress?To installCypress, ensure you haveNode.js(version 12 or above) andnpm(version 6 or above) installed on your system. Open your terminal or command prompt and follow these steps:Navigate to your project directory:cd /your/project/pathInstallCypressas a dev dependency using npm:npm install cypress --save-devAlternatively, you can useyarnif you prefer:yarn add cypress --devAfter installation, you can openCypressfor the first time with:npx cypress openOr, if you're using yarn:yarn run cypress openThis will open theCypressTest Runnerand create acypressfolder in your project directory, which contains the default configuration and sample tests.For continuous integration systems or to runCypresstests headlessly, use thecypress runcommand:npx cypress runRemember to addCypresscommands to thescriptssection of yourpackage.jsonfor easier execution:"scripts": {
  "cypress:open": "cypress open",
  "cypress:run": "cypress run"
}To execute with these scripts:npm run cypress:openornpm run cypress:runEnsure you have the necessary permissions to install new packages on your system. If you encounter any issues, refer to the officialCypressdocumentation for troubleshooting.
- What are the system requirements for Cypress?Cypressis compatible withWindows, macOS, and Linuxoperating systems. The specific system requirements include:Node.js: Version 12 or above.npm(usually comes with Node.js) orYarnfor package management.Asupported browserinstalled on your machine. Cypress supports:Chrome (including Canary and Chromium)Firefox (including Developer Edition)EdgeElectron (bundled with Cypress)BraveForCI/CD pipelines, ensure the build agent meets the OS and Node.js requirements.Memory and CPU: Sufficient resources to run the Electron browser, especially when running multiple tests in parallel. At least 2GB of RAM is recommended.Screen resolution: A minimum screen resolution of 1280x720 is recommended for viewing the Cypress Test Runner.Ensure your system haswrite permissionsto the directory whereCypressis installed and runs tests.ForLinux users, you may need to install additional dependencies if they are not already present on your system.Cypressprovides a command that can be run to install these dependencies:sudo apt-get install libgtk2.0-0 libgtk-3-0 libgbm-dev libnotify-dev libgconf-2-4 libnss3 libxss1 libasound2 libxtst6 xauth xvfbNote:Cypressis a desktop application that is installed on your computer, so it requires the above prerequisites to be met for the installation and execution of tests.
- How to set up a project in Cypress?To set up a project inCypress, follow these steps:Create a new directoryfor your project if you haven't already, and navigate into it using your terminal or command prompt.mkdir my-cypress-project
cd my-cypress-projectInitialize a new npm projectwithnpm init. You can skip through the prompts by usingnpm init -y.npm init -yInstallCypressvia npm by running:npm install cypress --save-devOpenCypressfor the first time to scaffold the default directory structure and files by executing:npx cypress openThis command generates acypressfolder containing example tests and acypress.jsonfile for configuration.Configure your testsby editing thecypress.jsonfile. Set up any required environment variables or base URLs.{
  "baseUrl": "http://yourapp.com",
  "env": {
    "login_url": "/login",
    "products_url": "/products"
  }
}Organize your test fileswithin thecypress/integrationdirectory. You may create subdirectories to group related tests.Write your testsusing thedescribeanditfunctions provided byCypress, and save them with a.spec.jsor.spec.tsextension.Run your testseither usingnpx cypress opento open theCypressTest Runnerornpx cypress runto execute tests in headless mode.Remember toadd thenode_modulesdirectory to your.gitignorefileto avoid committing dependencies to version control. Also, consider setting up scripts in yourpackage.jsonfor commonCypresscommands.
- How to configure Cypress for a specific environment?To configureCypressfor a specific environment, you'll need to set environment variables and potentially adjust yourcypress.jsonconfiguration file. Here's a succinct guide:Environment Variables: Define environment-specific variables using theenvkey in yourcypress.jsonfile or by passing them via the command line.{
  "env": {
    "apiUrl": "https://api.staging.example.com"
  }
}Alternatively, use the command line to override:npx cypress run --env apiUrl=https://api.staging.example.comConfiguration Files: For more complexsetups, consider having separate configuration files for each environment, likecypress.staging.jsonandcypress.production.json. Use the--config-fileflag to specify the configuration file when running tests.npx cypress run --config-file cypress.staging.jsonDynamic Configuration: In yourplugins/index.jsfile, you can programmatically alter the configuration based on environment variables or other conditions.module.exports = (on, config) => {
  if (process.env.NODE_ENV === 'staging') {
    config.baseUrl = 'https://staging.example.com';
    // Modify other config settings as needed
  }
  return config;
};Cypress.env(): Access environment variables in your tests usingCypress.env('variableName').const apiUrl = Cypress.env('apiUrl');Remember tonever commit sensitive datato version control. Use environment variables or a secrets management solution for sensitive data.

To installCypress, ensure you haveNode.js(version 12 or above) andnpm(version 6 or above) installed on your system. Open your terminal or command prompt and follow these steps:
[Cypress](/wiki/cypress)**Node.js**[Node.js](/wiki/node-js)**npm**1. Navigate to your project directory:cd /your/project/path
2. InstallCypressas a dev dependency using npm:npm install cypress --save-devAlternatively, you can useyarnif you prefer:yarn add cypress --dev
3. After installation, you can openCypressfor the first time with:npx cypress openOr, if you're using yarn:yarn run cypress open

Navigate to your project directory:

```
cd /your/project/path
```
`cd /your/project/path`
InstallCypressas a dev dependency using npm:
[Cypress](/wiki/cypress)
```
npm install cypress --save-dev
```
`npm install cypress --save-dev`
Alternatively, you can useyarnif you prefer:
`yarn`
```
yarn add cypress --dev
```
`yarn add cypress --dev`
After installation, you can openCypressfor the first time with:
[Cypress](/wiki/cypress)
```
npx cypress open
```
`npx cypress open`
Or, if you're using yarn:

```
yarn run cypress open
```
`yarn run cypress open`
This will open theCypressTest Runnerand create acypressfolder in your project directory, which contains the default configuration and sample tests.
[Cypress](/wiki/cypress)[Test Runner](/wiki/test-runner)`cypress`
For continuous integration systems or to runCypresstests headlessly, use thecypress runcommand:
[Cypress](/wiki/cypress)`cypress run`
```
npx cypress run
```
`npx cypress run`
Remember to addCypresscommands to thescriptssection of yourpackage.jsonfor easier execution:
[Cypress](/wiki/cypress)`scripts``package.json`
```
"scripts": {
  "cypress:open": "cypress open",
  "cypress:run": "cypress run"
}
```
`"scripts": {
  "cypress:open": "cypress open",
  "cypress:run": "cypress run"
}`
To execute with these scripts:

```
npm run cypress:open
```
`npm run cypress:open`
or

```
npm run cypress:run
```
`npm run cypress:run`
Ensure you have the necessary permissions to install new packages on your system. If you encounter any issues, refer to the officialCypressdocumentation for troubleshooting.
[Cypress](/wiki/cypress)
Cypressis compatible withWindows, macOS, and Linuxoperating systems. The specific system requirements include:
[Cypress](/wiki/cypress)**Windows, macOS, and Linux**- Node.js: Version 12 or above.
- npm(usually comes with Node.js) orYarnfor package management.
- Asupported browserinstalled on your machine. Cypress supports:Chrome (including Canary and Chromium)Firefox (including Developer Edition)EdgeElectron (bundled with Cypress)Brave
- ForCI/CD pipelines, ensure the build agent meets the OS and Node.js requirements.
- Memory and CPU: Sufficient resources to run the Electron browser, especially when running multiple tests in parallel. At least 2GB of RAM is recommended.
- Screen resolution: A minimum screen resolution of 1280x720 is recommended for viewing the Cypress Test Runner.
**Node.js**[Node.js](/wiki/node-js)**npm****Yarn****supported browser**- Chrome (including Canary and Chromium)
- Firefox (including Developer Edition)
- Edge
- Electron (bundled with Cypress)
- Brave
**CI/CD pipelines****Memory and CPU****Screen resolution**
Ensure your system haswrite permissionsto the directory whereCypressis installed and runs tests.
**write permissions**[Cypress](/wiki/cypress)
ForLinux users, you may need to install additional dependencies if they are not already present on your system.Cypressprovides a command that can be run to install these dependencies:
**Linux users**[Cypress](/wiki/cypress)
```
sudo apt-get install libgtk2.0-0 libgtk-3-0 libgbm-dev libnotify-dev libgconf-2-4 libnss3 libxss1 libasound2 libxtst6 xauth xvfb
```
`sudo apt-get install libgtk2.0-0 libgtk-3-0 libgbm-dev libnotify-dev libgconf-2-4 libnss3 libxss1 libasound2 libxtst6 xauth xvfb`
Note:Cypressis a desktop application that is installed on your computer, so it requires the above prerequisites to be met for the installation and execution of tests.
**Note**[Cypress](/wiki/cypress)
To set up a project inCypress, follow these steps:
[Cypress](/wiki/cypress)1. Create a new directoryfor your project if you haven't already, and navigate into it using your terminal or command prompt.mkdir my-cypress-project
cd my-cypress-project
2. Initialize a new npm projectwithnpm init. You can skip through the prompts by usingnpm init -y.npm init -y
3. InstallCypressvia npm by running:npm install cypress --save-dev
4. OpenCypressfor the first time to scaffold the default directory structure and files by executing:npx cypress openThis command generates acypressfolder containing example tests and acypress.jsonfile for configuration.
5. Configure your testsby editing thecypress.jsonfile. Set up any required environment variables or base URLs.{
  "baseUrl": "http://yourapp.com",
  "env": {
    "login_url": "/login",
    "products_url": "/products"
  }
}
6. Organize your test fileswithin thecypress/integrationdirectory. You may create subdirectories to group related tests.
7. Write your testsusing thedescribeanditfunctions provided byCypress, and save them with a.spec.jsor.spec.tsextension.
8. Run your testseither usingnpx cypress opento open theCypressTest Runnerornpx cypress runto execute tests in headless mode.

Create a new directoryfor your project if you haven't already, and navigate into it using your terminal or command prompt.
**Create a new directory**
```
mkdir my-cypress-project
cd my-cypress-project
```
`mkdir my-cypress-project
cd my-cypress-project`
Initialize a new npm projectwithnpm init. You can skip through the prompts by usingnpm init -y.
**Initialize a new npm project**`npm init``npm init -y`
```
npm init -y
```
`npm init -y`
InstallCypressvia npm by running:
**InstallCypress**[Cypress](/wiki/cypress)
```
npm install cypress --save-dev
```
`npm install cypress --save-dev`
OpenCypressfor the first time to scaffold the default directory structure and files by executing:
**OpenCypress**[Cypress](/wiki/cypress)
```
npx cypress open
```
`npx cypress open`
This command generates acypressfolder containing example tests and acypress.jsonfile for configuration.
`cypress``cypress.json`
Configure your testsby editing thecypress.jsonfile. Set up any required environment variables or base URLs.
**Configure your tests**`cypress.json`
```
{
  "baseUrl": "http://yourapp.com",
  "env": {
    "login_url": "/login",
    "products_url": "/products"
  }
}
```
`{
  "baseUrl": "http://yourapp.com",
  "env": {
    "login_url": "/login",
    "products_url": "/products"
  }
}`
Organize your test fileswithin thecypress/integrationdirectory. You may create subdirectories to group related tests.
**Organize your test files**`cypress/integration`
Write your testsusing thedescribeanditfunctions provided byCypress, and save them with a.spec.jsor.spec.tsextension.
**Write your tests**`describe``it`[Cypress](/wiki/cypress)`.spec.js``.spec.ts`
Run your testseither usingnpx cypress opento open theCypressTest Runnerornpx cypress runto execute tests in headless mode.
**Run your tests**`npx cypress open`[Cypress](/wiki/cypress)[Test Runner](/wiki/test-runner)`npx cypress run`
Remember toadd thenode_modulesdirectory to your.gitignorefileto avoid committing dependencies to version control. Also, consider setting up scripts in yourpackage.jsonfor commonCypresscommands.
**add thenode_modulesdirectory to your.gitignorefile**`node_modules``.gitignore``package.json`[Cypress](/wiki/cypress)
To configureCypressfor a specific environment, you'll need to set environment variables and potentially adjust yourcypress.jsonconfiguration file. Here's a succinct guide:
[Cypress](/wiki/cypress)`cypress.json`1. Environment Variables: Define environment-specific variables using theenvkey in yourcypress.jsonfile or by passing them via the command line.{
  "env": {
    "apiUrl": "https://api.staging.example.com"
  }
}Alternatively, use the command line to override:npx cypress run --env apiUrl=https://api.staging.example.com
2. Configuration Files: For more complexsetups, consider having separate configuration files for each environment, likecypress.staging.jsonandcypress.production.json. Use the--config-fileflag to specify the configuration file when running tests.npx cypress run --config-file cypress.staging.json
3. Dynamic Configuration: In yourplugins/index.jsfile, you can programmatically alter the configuration based on environment variables or other conditions.module.exports = (on, config) => {
  if (process.env.NODE_ENV === 'staging') {
    config.baseUrl = 'https://staging.example.com';
    // Modify other config settings as needed
  }
  return config;
};
4. Cypress.env(): Access environment variables in your tests usingCypress.env('variableName').const apiUrl = Cypress.env('apiUrl');

Environment Variables: Define environment-specific variables using theenvkey in yourcypress.jsonfile or by passing them via the command line.
**Environment Variables**`env``cypress.json`
```
{
  "env": {
    "apiUrl": "https://api.staging.example.com"
  }
}
```
`{
  "env": {
    "apiUrl": "https://api.staging.example.com"
  }
}`
Alternatively, use the command line to override:

```
npx cypress run --env apiUrl=https://api.staging.example.com
```
`npx cypress run --env apiUrl=https://api.staging.example.com`
Configuration Files: For more complexsetups, consider having separate configuration files for each environment, likecypress.staging.jsonandcypress.production.json. Use the--config-fileflag to specify the configuration file when running tests.
**Configuration Files**[setups](/wiki/setup)`cypress.staging.json``cypress.production.json``--config-file`
```
npx cypress run --config-file cypress.staging.json
```
`npx cypress run --config-file cypress.staging.json`
Dynamic Configuration: In yourplugins/index.jsfile, you can programmatically alter the configuration based on environment variables or other conditions.
**Dynamic Configuration**`plugins/index.js`
```
module.exports = (on, config) => {
  if (process.env.NODE_ENV === 'staging') {
    config.baseUrl = 'https://staging.example.com';
    // Modify other config settings as needed
  }
  return config;
};
```
`module.exports = (on, config) => {
  if (process.env.NODE_ENV === 'staging') {
    config.baseUrl = 'https://staging.example.com';
    // Modify other config settings as needed
  }
  return config;
};`
Cypress.env(): Access environment variables in your tests usingCypress.env('variableName').
**Cypress.env()**[Cypress](/wiki/cypress)`Cypress.env('variableName')`
```
const apiUrl = Cypress.env('apiUrl');
```
`const apiUrl = Cypress.env('apiUrl');`
Remember tonever commit sensitive datato version control. Use environment variables or a secrets management solution for sensitive data.
**never commit sensitive data**
#### Writing and Running Tests
- How to write a basic test in Cypress?To write a basic test inCypress, follow these steps:Create a new test filein yourCypressintegration folder, typically with a.spec.jsextension, for example,login.spec.js.Start by requiringCypressat the top of your test file:/// <reference types="cypress" />Describe yourtest suiteusing thedescribefunction, providing a title and a callback function to contain your tests:describe('Login Test', () => {
  // Your tests will go here
});Write individualtest caseswithin thedescribeblock using theitfunction. Eachitfunction takes a title for the test case and a callback function to execute the test steps:it('successfully logs in', () => {
  // Test steps will go here
});Define the test stepswithin theitcallback. Use Cypress commands to interact with the application:it('successfully logs in', () => {
  cy.visit('/login'); // Navigate to the login page
  cy.get('input[name=username]').type('user@example.com'); // Type the username
  cy.get('input[name=password]').type('password123'); // Type the password
  cy.get('form').submit(); // Submit the login form
  cy.url().should('include', '/dashboard'); // Assert the URL to ensure login was successful
});Run your testusing the Cypress Test Runner or via the command line withcypress openorcypress run.Remember tokeep tests isolatedandindependentfor reliability. UsebeforeEachorbeforehooks if you need to set up state before each test or once before all tests in the suite, respectively.
- What is the structure of a Cypress test?ACypresstest typically follows a structure that includes importing necessary dependencies, describingtest suites, definingtest cases, and implementing test steps with assertions. Here's an example of a basicCypresstest structure:// Import the Cypress module
import cy from 'cypress';

// Describe the test suite
describe('User Login', () => {

  // Before each test, do some common setup (optional)
  beforeEach(() => {
    // Visit the login page
    cy.visit('/login');
  });

  // Define a test case
  it('should login with valid credentials', () => {
    // Test steps
    cy.get('input[name="username"]').type('user');
    cy.get('input[name="password"]').type('password');
    cy.get('form').submit();

    // Assertions
    cy.url().should('include', '/dashboard');
    cy.get('.welcome-message').should('contain', 'Welcome, user');
  });

  // Define another test case
  it('should display an error for invalid credentials', () => {
    // Test steps
    cy.get('input[name="username"]').type('wronguser');
    cy.get('input[name="password"]').type('wrongpassword');
    cy.get('form').submit();

    // Assertions
    cy.get('.error-message').should('be.visible');
  });

});In this structure:describeblocks group related tests, known as a test suite.itblocks define individual test cases.beforeEachis a hook for setting up conditions before each test runs.cy.visitnavigates to a URL.cy.getselects DOM elements.typeandsubmitsimulate user actions.shouldis used for assertions to verify the desired state.
- How to run a test in Cypress?To run a test inCypress, follow these steps:Open your terminal or command prompt.Navigate to your project directory where Cypress is installed.Execute the following command to open the Cypress Test Runner:npx cypress openThe Cypress Test Runner GUI will launch, displaying a list of your test files.Click on the test file you want to run. Cypress will execute the tests in that file and display the results in real-time.Alternatively, to run tests headlessly without opening theTest RunnerGUI:Use the following command in your terminal:npx cypress runThis will run all test files in the default headless browser (Electron).For running tests in a specific browser, use the--browserflag:npx cypress run --browser chromeTo run a specific test file, append the--specflag followed by the path to the test file:npx cypress run --spec "cypress/integration/example.spec.js"To run tests with additional configuration options, use the--configflag:npx cypress run --config video=falseThis command will run tests without recording a video.For paralleltest executionand load balancing across multiple machines or CI containers, use theCypressDashboard service, which requires additionalsetupand configuration.
- How to use assertions in Cypress?Using assertions inCypressis crucial for verifying that the application under test behaves as expected.Cypressuses Chai for assertions, which providesexpect,assert, andshouldsyntax.ExpectandshouldareBDD(Behavior-Driven Development) style assertions, whileassertis TDD (Test-Driven Development) style. Here's how you can use them:Expect:expect(variable).to.equal(value);
expect(element).to.have.class(className);Should:cy.get(selector).should('have.class', className);
cy.get(selector).should('contain', text);Assert:assert.equal(variable, value, 'Optional message');
assert.isTrue(condition, 'Optional message');Cypressassertions are automatically retried until they pass or time out, which is defined by thedefaultCommandTimeoutconfiguration.Chain assertions for more complex checks:cy.get(selector).should('be.visible').and('contain', text);Use.andto chain multiple assertions on the same subject.For assertions on network requests:cy.request('GET', '/api/data').then((response) => {
  expect(response.status).to.eq(200);
  expect(response.body).to.have.property('data');
});Remember to leverageCypress's built-in assertions for common conditions, such as visibility or existence of elements, which simplifies the syntax and improves readability:cy.get(selector).should('be.visible');
cy.get(selector).should('exist');By using assertions effectively, you ensure that your tests accurately validate the behavior of your application.
- How to handle events in Cypress?Handling events inCypressis straightforward due to its jQuery-like syntax. To interact with elements and handle events, you can useCypresscommands that simulate user actions.For example, to handle a click event, you would use the.click()command:cy.get('button').click();To handle form submission, you can use the.submit()command:cy.get('form').submit();For keyboard events, such as typing into an input field, use the.type()command:cy.get('input').type('Hello, World!');To handle more complex events like hover,Cypressdoes not natively support thehoverevent as a user would experience it. Instead, you can trigger the same functionality using the.trigger()command:cy.get('div').trigger('mouseover');For events that require waiting for a specific condition, you can use.wait()in combination with other commands:cy.wait(1000); // Waits for 1 second
cy.get('button').click();Remember thatCypressautomatically waits for elements to exist and will retry commands until the elements are actionable. This means you often don't need to manually handle events that depend on previous actions or asynchronous operations.For custom events or more complex scenarios, you can define custom commands usingCypress.Commands.add()to encapsulate reusable event handling logic:Cypress.Commands.add('customEvent', (selector, event) => {
  cy.get(selector).trigger(event);
});

// Usage
cy.customEvent('button', 'customEventName');Always ensure you understand the application's behavior to correctly simulate events and achieve reliable test results.
- How to use fixtures in Cypress?Using fixtures inCypressis a way to managetest dataseparately fromtest scripts, allowing you to load static data that can be used across multiple tests. Here's how to use fixtures inCypress:Create a fixture file: Place a JSON file inside thecypress/fixturesdirectory. For example,user.jsoncould contain:{
  "id": 1,
  "name": "Jane Doe",
  "email": "jane.doe@example.com"
}Load a fixture: Use thecy.fixture()function to load the fixture data. You can then use this data within your test.describe('Test with fixtures', () => {
  it('Loads data from a fixture', () => {
    cy.fixture('user').then((user) => {
      // user now contains the fixture data
    });
  });
});Use fixture data in tests: Once the fixture is loaded, you can use the data in your test logic, such as filling out forms or comparing against expected values.cy.get('input[name="name"]').type(user.name);
cy.get('input[name="email"]').type(user.email);Shortcut for loading fixtures: You can also pass the fixture file directly to commands likecy.get()orcy.route()using the@prefix.cy.get('input[name="name"]').type('@user.name');Alias fixture data: To make fixtures easier to manage within a test, you can assign an alias to the fixture usingas().cy.fixture('user').as('userData');
cy.get('@userData').then((user) => {
  // use user data here
});Remember to keep your fixture data up-to-date and relevant to the tests you are performing. This will ensure your tests remain reliable and maintainable.

To write a basic test inCypress, follow these steps:
[Cypress](/wiki/cypress)1. Create a new test filein yourCypressintegration folder, typically with a.spec.jsextension, for example,login.spec.js.
2. Start by requiringCypressat the top of your test file:

Create a new test filein yourCypressintegration folder, typically with a.spec.jsextension, for example,login.spec.js.
**Create a new test file**[Cypress](/wiki/cypress)`.spec.js``login.spec.js`
Start by requiringCypressat the top of your test file:
**Start by requiringCypress**[Cypress](/wiki/cypress)
```
/// <reference types="cypress" />
```
`/// <reference types="cypress" />`1. Describe yourtest suiteusing thedescribefunction, providing a title and a callback function to contain your tests:
**Describe yourtest suite**[test suite](/wiki/test-suite)`describe`
```
describe('Login Test', () => {
  // Your tests will go here
});
```
`describe('Login Test', () => {
  // Your tests will go here
});`1. Write individualtest caseswithin thedescribeblock using theitfunction. Eachitfunction takes a title for the test case and a callback function to execute the test steps:
**Write individualtest cases**[test cases](/wiki/test-case)`describe``it``it`
```
it('successfully logs in', () => {
  // Test steps will go here
});
```
`it('successfully logs in', () => {
  // Test steps will go here
});`1. Define the test stepswithin theitcallback. Use Cypress commands to interact with the application:
**Define the test steps**`it`
```
it('successfully logs in', () => {
  cy.visit('/login'); // Navigate to the login page
  cy.get('input[name=username]').type('user@example.com'); // Type the username
  cy.get('input[name=password]').type('password123'); // Type the password
  cy.get('form').submit(); // Submit the login form
  cy.url().should('include', '/dashboard'); // Assert the URL to ensure login was successful
});
```
`it('successfully logs in', () => {
  cy.visit('/login'); // Navigate to the login page
  cy.get('input[name=username]').type('user@example.com'); // Type the username
  cy.get('input[name=password]').type('password123'); // Type the password
  cy.get('form').submit(); // Submit the login form
  cy.url().should('include', '/dashboard'); // Assert the URL to ensure login was successful
});`1. Run your testusing the Cypress Test Runner or via the command line withcypress openorcypress run.
**Run your test**`cypress open``cypress run`
Remember tokeep tests isolatedandindependentfor reliability. UsebeforeEachorbeforehooks if you need to set up state before each test or once before all tests in the suite, respectively.
**keep tests isolated****independent**`beforeEach``before`
ACypresstest typically follows a structure that includes importing necessary dependencies, describingtest suites, definingtest cases, and implementing test steps with assertions. Here's an example of a basicCypresstest structure:
[Cypress](/wiki/cypress)[test suites](/wiki/test-suite)[test cases](/wiki/test-case)[Cypress](/wiki/cypress)
```
// Import the Cypress module
import cy from 'cypress';

// Describe the test suite
describe('User Login', () => {

  // Before each test, do some common setup (optional)
  beforeEach(() => {
    // Visit the login page
    cy.visit('/login');
  });

  // Define a test case
  it('should login with valid credentials', () => {
    // Test steps
    cy.get('input[name="username"]').type('user');
    cy.get('input[name="password"]').type('password');
    cy.get('form').submit();

    // Assertions
    cy.url().should('include', '/dashboard');
    cy.get('.welcome-message').should('contain', 'Welcome, user');
  });

  // Define another test case
  it('should display an error for invalid credentials', () => {
    // Test steps
    cy.get('input[name="username"]').type('wronguser');
    cy.get('input[name="password"]').type('wrongpassword');
    cy.get('form').submit();

    // Assertions
    cy.get('.error-message').should('be.visible');
  });

});
```
`// Import the Cypress module
import cy from 'cypress';

// Describe the test suite
describe('User Login', () => {

  // Before each test, do some common setup (optional)
  beforeEach(() => {
    // Visit the login page
    cy.visit('/login');
  });

  // Define a test case
  it('should login with valid credentials', () => {
    // Test steps
    cy.get('input[name="username"]').type('user');
    cy.get('input[name="password"]').type('password');
    cy.get('form').submit();

    // Assertions
    cy.url().should('include', '/dashboard');
    cy.get('.welcome-message').should('contain', 'Welcome, user');
  });

  // Define another test case
  it('should display an error for invalid credentials', () => {
    // Test steps
    cy.get('input[name="username"]').type('wronguser');
    cy.get('input[name="password"]').type('wrongpassword');
    cy.get('form').submit();

    // Assertions
    cy.get('.error-message').should('be.visible');
  });

});`
In this structure:
- describeblocks group related tests, known as a test suite.
- itblocks define individual test cases.
- beforeEachis a hook for setting up conditions before each test runs.
- cy.visitnavigates to a URL.
- cy.getselects DOM elements.
- typeandsubmitsimulate user actions.
- shouldis used for assertions to verify the desired state.
**describe****it****beforeEach****cy.visit****cy.get****type****submit****should**
To run a test inCypress, follow these steps:
[Cypress](/wiki/cypress)1. Open your terminal or command prompt.
2. Navigate to your project directory where Cypress is installed.
3. Execute the following command to open the Cypress Test Runner:

```
npx cypress open
```
`npx cypress open`1. The Cypress Test Runner GUI will launch, displaying a list of your test files.
2. Click on the test file you want to run. Cypress will execute the tests in that file and display the results in real-time.

Alternatively, to run tests headlessly without opening theTest RunnerGUI:
[Test Runner](/wiki/test-runner)1. Use the following command in your terminal:

```
npx cypress run
```
`npx cypress run`1. This will run all test files in the default headless browser (Electron).

For running tests in a specific browser, use the--browserflag:
`--browser`
```
npx cypress run --browser chrome
```
`npx cypress run --browser chrome`
To run a specific test file, append the--specflag followed by the path to the test file:
`--spec`
```
npx cypress run --spec "cypress/integration/example.spec.js"
```
`npx cypress run --spec "cypress/integration/example.spec.js"`
To run tests with additional configuration options, use the--configflag:
`--config`
```
npx cypress run --config video=false
```
`npx cypress run --config video=false`
This command will run tests without recording a video.

For paralleltest executionand load balancing across multiple machines or CI containers, use theCypressDashboard service, which requires additionalsetupand configuration.
[test execution](/wiki/test-execution)[Cypress](/wiki/cypress)[setup](/wiki/setup)
Using assertions inCypressis crucial for verifying that the application under test behaves as expected.Cypressuses Chai for assertions, which providesexpect,assert, andshouldsyntax.
[Cypress](/wiki/cypress)[Cypress](/wiki/cypress)`expect``assert``should`
ExpectandshouldareBDD(Behavior-Driven Development) style assertions, whileassertis TDD (Test-Driven Development) style. Here's how you can use them:
**Expect****should**[BDD](/wiki/bdd)**assert**[Test-Driven Development](/wiki/test-driven-development)
Expect:
**Expect:**
```
expect(variable).to.equal(value);
expect(element).to.have.class(className);
```
`expect(variable).to.equal(value);
expect(element).to.have.class(className);`
Should:
**Should:**
```
cy.get(selector).should('have.class', className);
cy.get(selector).should('contain', text);
```
`cy.get(selector).should('have.class', className);
cy.get(selector).should('contain', text);`
Assert:
**Assert:**
```
assert.equal(variable, value, 'Optional message');
assert.isTrue(condition, 'Optional message');
```
`assert.equal(variable, value, 'Optional message');
assert.isTrue(condition, 'Optional message');`
Cypressassertions are automatically retried until they pass or time out, which is defined by thedefaultCommandTimeoutconfiguration.
[Cypress](/wiki/cypress)`defaultCommandTimeout`
Chain assertions for more complex checks:

```
cy.get(selector).should('be.visible').and('contain', text);
```
`cy.get(selector).should('be.visible').and('contain', text);`
Use.andto chain multiple assertions on the same subject.
`.and`
For assertions on network requests:

```
cy.request('GET', '/api/data').then((response) => {
  expect(response.status).to.eq(200);
  expect(response.body).to.have.property('data');
});
```
`cy.request('GET', '/api/data').then((response) => {
  expect(response.status).to.eq(200);
  expect(response.body).to.have.property('data');
});`
Remember to leverageCypress's built-in assertions for common conditions, such as visibility or existence of elements, which simplifies the syntax and improves readability:
[Cypress](/wiki/cypress)
```
cy.get(selector).should('be.visible');
cy.get(selector).should('exist');
```
`cy.get(selector).should('be.visible');
cy.get(selector).should('exist');`
By using assertions effectively, you ensure that your tests accurately validate the behavior of your application.

Handling events inCypressis straightforward due to its jQuery-like syntax. To interact with elements and handle events, you can useCypresscommands that simulate user actions.
[Cypress](/wiki/cypress)[Cypress](/wiki/cypress)
For example, to handle a click event, you would use the.click()command:
`.click()`
```
cy.get('button').click();
```
`cy.get('button').click();`
To handle form submission, you can use the.submit()command:
`.submit()`
```
cy.get('form').submit();
```
`cy.get('form').submit();`
For keyboard events, such as typing into an input field, use the.type()command:
`.type()`
```
cy.get('input').type('Hello, World!');
```
`cy.get('input').type('Hello, World!');`
To handle more complex events like hover,Cypressdoes not natively support thehoverevent as a user would experience it. Instead, you can trigger the same functionality using the.trigger()command:
[Cypress](/wiki/cypress)`hover``.trigger()`
```
cy.get('div').trigger('mouseover');
```
`cy.get('div').trigger('mouseover');`
For events that require waiting for a specific condition, you can use.wait()in combination with other commands:
`.wait()`
```
cy.wait(1000); // Waits for 1 second
cy.get('button').click();
```
`cy.wait(1000); // Waits for 1 second
cy.get('button').click();`
Remember thatCypressautomatically waits for elements to exist and will retry commands until the elements are actionable. This means you often don't need to manually handle events that depend on previous actions or asynchronous operations.
[Cypress](/wiki/cypress)
For custom events or more complex scenarios, you can define custom commands usingCypress.Commands.add()to encapsulate reusable event handling logic:
`Cypress.Commands.add()`
```
Cypress.Commands.add('customEvent', (selector, event) => {
  cy.get(selector).trigger(event);
});

// Usage
cy.customEvent('button', 'customEventName');
```
`Cypress.Commands.add('customEvent', (selector, event) => {
  cy.get(selector).trigger(event);
});

// Usage
cy.customEvent('button', 'customEventName');`
Always ensure you understand the application's behavior to correctly simulate events and achieve reliable test results.

Using fixtures inCypressis a way to managetest dataseparately fromtest scripts, allowing you to load static data that can be used across multiple tests. Here's how to use fixtures inCypress:
[Cypress](/wiki/cypress)[test data](/wiki/test-data)[test scripts](/wiki/test-script)[Cypress](/wiki/cypress)1. Create a fixture file: Place a JSON file inside thecypress/fixturesdirectory. For example,user.jsoncould contain:
**Create a fixture file**`cypress/fixtures``user.json`
```
{
  "id": 1,
  "name": "Jane Doe",
  "email": "jane.doe@example.com"
}
```
`{
  "id": 1,
  "name": "Jane Doe",
  "email": "jane.doe@example.com"
}`1. Load a fixture: Use thecy.fixture()function to load the fixture data. You can then use this data within your test.
**Load a fixture**`cy.fixture()`
```
describe('Test with fixtures', () => {
  it('Loads data from a fixture', () => {
    cy.fixture('user').then((user) => {
      // user now contains the fixture data
    });
  });
});
```
`describe('Test with fixtures', () => {
  it('Loads data from a fixture', () => {
    cy.fixture('user').then((user) => {
      // user now contains the fixture data
    });
  });
});`1. Use fixture data in tests: Once the fixture is loaded, you can use the data in your test logic, such as filling out forms or comparing against expected values.
**Use fixture data in tests**
```
cy.get('input[name="name"]').type(user.name);
cy.get('input[name="email"]').type(user.email);
```
`cy.get('input[name="name"]').type(user.name);
cy.get('input[name="email"]').type(user.email);`1. Shortcut for loading fixtures: You can also pass the fixture file directly to commands likecy.get()orcy.route()using the@prefix.
**Shortcut for loading fixtures**`cy.get()``cy.route()``@`
```
cy.get('input[name="name"]').type('@user.name');
```
`cy.get('input[name="name"]').type('@user.name');`1. Alias fixture data: To make fixtures easier to manage within a test, you can assign an alias to the fixture usingas().
**Alias fixture data**`as()`
```
cy.fixture('user').as('userData');
cy.get('@userData').then((user) => {
  // use user data here
});
```
`cy.fixture('user').as('userData');
cy.get('@userData').then((user) => {
  // use user data here
});`
Remember to keep your fixture data up-to-date and relevant to the tests you are performing. This will ensure your tests remain reliable and maintainable.

#### Advanced Concepts
- How does Cypress handle asynchronous operations?Cypresshandles asynchronous operations by automatically waiting for commands and assertions before moving on to the next step. This means that it will wait for elements to become visible, for animations to complete, and for network requests to finish before executing the next command. There's no need to add explicit waits or sleeps in your tests.For example, when you use a command to get an element,Cypresswill continuously retry this command until the element is found or a timeout is reached. This applies to most commands inCypress:cy.get('.some-element') // Cypress will wait for this element to existWhen dealing with network requests,Cypressprovidescy.wait()to wait for a specific request to complete:cy.wait('@yourRequestAlias')You can also handle the response of asynchronous requests using.then():cy.request('POST', '/yourEndpoint', yourRequestBody)
  .then((response) => {
    expect(response.body).to.have.property('success', true);
  });Cypressensures that the test does not proceed until the asynchronous operation inside.then()is completed.For assertions,Cypressuses a retry-and-timeout mechanism. Assertions will re-run until they pass or until a specified timeout is reached:cy.get('.list-item').should('have.length', 5) // Retries until the condition is met or timeoutThis approach simplifies handling asynchronous operations, making tests more readable and less flaky.
- How to use custom commands in Cypress?Using custom commands inCypresscan enhance yourtest suiteby encapsulating repetitive tasks. To define a custom command, add a function to theCypress.Commands.addmethod in thecommands.jsfile located in thecypress/supportdirectory.Cypress.Commands.add('login', (email, password) => {
  cy.get('input[name=email]').type(email);
  cy.get('input[name=password]').type(password);
  cy.get('form').submit();
});Invoke custom commands in your tests usingcyfollowed by the command name:cy.login('user@example.com', 'password123');Parameterscan be passed to custom commands just like any other function. In the example above,emailandpasswordare the parameters.Chainingis supported by custom commands. Returncyfrom your custom command to continue chainingCypresscommands:Cypress.Commands.add('fillForm', data => {
  return cy.get('form').within(() => {
    cy.get('input[name=firstName]').type(data.firstName);
    cy.get('input[name=lastName]').type(data.lastName);
  });
});Overwritingexisting commands is possible by using the sameCypress.Commands.addmethod with the name of an existing command:Cypress.Commands.overwrite('visit', (originalFn, url, options) => {
  // Custom logic before visit
  return originalFn(url, options);
});Remember todocumentyour custom commands to ensure team members understand their purpose and usage. Keep custom commandsmaintainableby limiting their scope and complexity.
- How to handle network requests in Cypress?Handling network requests inCypresscan be achieved using thecy.intercept()method. This allows you to listen to, modify, or mock network requests and responses.Intercepting a GET request:cy.intercept('GET', '/api/todos').as('getTodos')After setting up an intercept, you can wait for the request to complete usingcy.wait():cy.wait('@getTodos').its('response.statusCode').should('eq', 200)Modifying a response:You can modify the response by providing a static response:cy.intercept('GET', '/api/todos', { fixture: 'todos.json' })Stubbing a response:To stub a response, you can provide the response directly:cy.intercept('POST', '/api/todos', {
  statusCode: 201,
  body: { id: 123, title: 'Stubbed task' },
}).as('createTodo')Accessing request and response:You can access the request and response objects in the intercept callback:cy.intercept('POST', '/api/todos', (req) => {
  req.body.title = 'Modified title'
}).as('createTodo')Chaining assertions:You can chain assertions to the intercepted request:cy.wait('@createTodo').then(({ request, response }) => {
  expect(request.body).to.have.property('title', 'Modified title')
  expect(response.statusCode).to.eq(201)
})Usecy.intercept()to gain full control over network requests and responses, enabling you to test your application's behavior under various scenarios.
- How to work with cookies and local storage in Cypress?Working with cookies and local storage inCypressis straightforward due to its built-in commands.Cookies:To get a cookie by name:cy.getCookie('session_id').should('exist')To get all cookies:cy.getCookies().should('have.length', 1)To set a cookie:cy.setCookie('session_id', 'abc123')To clear a specific cookie:cy.clearCookie('session_id')To clear all cookies:cy.clearCookies()Local Storage:To set an item in local storage:cy.setLocalStorage('cart', JSON.stringify({ items: 1 }))To get an item from local storage:cy.getLocalStorage('cart').should('equal', '{"items":1}')To clear specific item from local storage:cy.removeLocalStorage('cart')To clear all local storage data:cy.clearLocalStorage()Or to clear local storage with a specific key pattern:cy.clearLocalStorage(/cart/)Remember, these commands are asynchronous and return promises, so they should be used withCypress's chaining mechanism. Also, local storage operations are typically performed in the context of the application under test, so ensure the correct page is loaded before attempting to interact with local storage.
- How to handle iframes in Cypress?Handling iframes inCypressrequires a few additional steps becauseCypresscommands are designed to operate within the same-origin context. Here's a succinct guide:Target the iframe- Usecy.get()to grab the iframe element.cy.get('iframe')Access the iframe's content- Use.its('contentDocument.body')to get the body of the iframe, which is subject to same-origin policy restrictions.cy.get('iframe').its('contentDocument.body').should('not.be.empty').then(cy.wrap)Interact with elements- Once wrapped, you can interact with the elements inside the iframe as you would with any other element in Cypress.cy.get('iframe').its('contentDocument.body').should('not.be.empty').then(cy.wrap).find('selector').click()Remember that for cross-origin iframes, you'll need to set"chromeWebSecurity": falsein yourcypress.jsonconfiguration file to bypass these restrictions. However, this is not recommended for security reasons and should only be used when absolutely necessary.If you're dealing with multiple nested iframes, you'll need to repeat the process for each level of iframe nesting, ensuring that you target the correct iframe at each level.Keep in mind thatCypressbest practices recommend avoiding iframes when possible, as they add complexity to your tests. If you have control over the application, consider alternatives to iframes that are more test-friendly.
- How to use plugins in Cypress?Using plugins inCypressenhances its capabilities by extending its core functionality. To use a plugin, follow these steps:Install the pluginvia npm. For example, to install thecypress-file-uploadplugin, run:npm install --save-dev cypress-file-uploadInclude the pluginin your project'scypress/plugins/index.jsfile. This is where you modify or extend the internal behavior ofCypress. For instance:module.exports = (on, config) => {
  // your plugin code here
}Import and use the pluginin your test files as needed. For example, withcypress-file-upload, you would add the following to your test file:import 'cypress-file-upload';Utilize the plugin's featuresin your tests. For thecypress-file-uploadplugin, you can now use the.attachFile()command:cy.get('input[type="file"]').attachFile('file.json');Remember tocheck the plugin's documentationfor specific usage instructions and compatibility with your version ofCypress. Some plugins may require additional configuration or initialization steps.Plugins can provide a variety of functionalities, such as custom commands, improved reporting, or integration with other tools. Alwaysensure that the plugin is actively maintainedand well-suited for your needs before adding it to your project.

Cypresshandles asynchronous operations by automatically waiting for commands and assertions before moving on to the next step. This means that it will wait for elements to become visible, for animations to complete, and for network requests to finish before executing the next command. There's no need to add explicit waits or sleeps in your tests.
[Cypress](/wiki/cypress)
For example, when you use a command to get an element,Cypresswill continuously retry this command until the element is found or a timeout is reached. This applies to most commands inCypress:
[Cypress](/wiki/cypress)[Cypress](/wiki/cypress)
```
cy.get('.some-element') // Cypress will wait for this element to exist
```
`cy.get('.some-element') // Cypress will wait for this element to exist`
When dealing with network requests,Cypressprovidescy.wait()to wait for a specific request to complete:
[Cypress](/wiki/cypress)`cy.wait()`
```
cy.wait('@yourRequestAlias')
```
`cy.wait('@yourRequestAlias')`
You can also handle the response of asynchronous requests using.then():
`.then()`
```
cy.request('POST', '/yourEndpoint', yourRequestBody)
  .then((response) => {
    expect(response.body).to.have.property('success', true);
  });
```
`cy.request('POST', '/yourEndpoint', yourRequestBody)
  .then((response) => {
    expect(response.body).to.have.property('success', true);
  });`
Cypressensures that the test does not proceed until the asynchronous operation inside.then()is completed.
[Cypress](/wiki/cypress)`.then()`
For assertions,Cypressuses a retry-and-timeout mechanism. Assertions will re-run until they pass or until a specified timeout is reached:
[Cypress](/wiki/cypress)
```
cy.get('.list-item').should('have.length', 5) // Retries until the condition is met or timeout
```
`cy.get('.list-item').should('have.length', 5) // Retries until the condition is met or timeout`
This approach simplifies handling asynchronous operations, making tests more readable and less flaky.

Using custom commands inCypresscan enhance yourtest suiteby encapsulating repetitive tasks. To define a custom command, add a function to theCypress.Commands.addmethod in thecommands.jsfile located in thecypress/supportdirectory.
[Cypress](/wiki/cypress)[test suite](/wiki/test-suite)`Cypress.Commands.add``commands.js``cypress/support`
```
Cypress.Commands.add('login', (email, password) => {
  cy.get('input[name=email]').type(email);
  cy.get('input[name=password]').type(password);
  cy.get('form').submit();
});
```
`Cypress.Commands.add('login', (email, password) => {
  cy.get('input[name=email]').type(email);
  cy.get('input[name=password]').type(password);
  cy.get('form').submit();
});`
Invoke custom commands in your tests usingcyfollowed by the command name:
`cy`
```
cy.login('user@example.com', 'password123');
```
`cy.login('user@example.com', 'password123');`
Parameterscan be passed to custom commands just like any other function. In the example above,emailandpasswordare the parameters.
**Parameters**`email``password`
Chainingis supported by custom commands. Returncyfrom your custom command to continue chainingCypresscommands:
**Chaining**`cy`[Cypress](/wiki/cypress)
```
Cypress.Commands.add('fillForm', data => {
  return cy.get('form').within(() => {
    cy.get('input[name=firstName]').type(data.firstName);
    cy.get('input[name=lastName]').type(data.lastName);
  });
});
```
`Cypress.Commands.add('fillForm', data => {
  return cy.get('form').within(() => {
    cy.get('input[name=firstName]').type(data.firstName);
    cy.get('input[name=lastName]').type(data.lastName);
  });
});`
Overwritingexisting commands is possible by using the sameCypress.Commands.addmethod with the name of an existing command:
**Overwriting**`Cypress.Commands.add`
```
Cypress.Commands.overwrite('visit', (originalFn, url, options) => {
  // Custom logic before visit
  return originalFn(url, options);
});
```
`Cypress.Commands.overwrite('visit', (originalFn, url, options) => {
  // Custom logic before visit
  return originalFn(url, options);
});`
Remember todocumentyour custom commands to ensure team members understand their purpose and usage. Keep custom commandsmaintainableby limiting their scope and complexity.
**document****maintainable**
Handling network requests inCypresscan be achieved using thecy.intercept()method. This allows you to listen to, modify, or mock network requests and responses.
[Cypress](/wiki/cypress)`cy.intercept()`
Intercepting a GET request:
**Intercepting a GET request:**
```
cy.intercept('GET', '/api/todos').as('getTodos')
```
`cy.intercept('GET', '/api/todos').as('getTodos')`
After setting up an intercept, you can wait for the request to complete usingcy.wait():
`cy.wait()`
```
cy.wait('@getTodos').its('response.statusCode').should('eq', 200)
```
`cy.wait('@getTodos').its('response.statusCode').should('eq', 200)`
Modifying a response:
**Modifying a response:**
You can modify the response by providing a static response:

```
cy.intercept('GET', '/api/todos', { fixture: 'todos.json' })
```
`cy.intercept('GET', '/api/todos', { fixture: 'todos.json' })`
Stubbing a response:
**Stubbing a response:**
To stub a response, you can provide the response directly:

```
cy.intercept('POST', '/api/todos', {
  statusCode: 201,
  body: { id: 123, title: 'Stubbed task' },
}).as('createTodo')
```
`cy.intercept('POST', '/api/todos', {
  statusCode: 201,
  body: { id: 123, title: 'Stubbed task' },
}).as('createTodo')`
Accessing request and response:
**Accessing request and response:**
You can access the request and response objects in the intercept callback:

```
cy.intercept('POST', '/api/todos', (req) => {
  req.body.title = 'Modified title'
}).as('createTodo')
```
`cy.intercept('POST', '/api/todos', (req) => {
  req.body.title = 'Modified title'
}).as('createTodo')`
Chaining assertions:
**Chaining assertions:**
You can chain assertions to the intercepted request:

```
cy.wait('@createTodo').then(({ request, response }) => {
  expect(request.body).to.have.property('title', 'Modified title')
  expect(response.statusCode).to.eq(201)
})
```
`cy.wait('@createTodo').then(({ request, response }) => {
  expect(request.body).to.have.property('title', 'Modified title')
  expect(response.statusCode).to.eq(201)
})`
Usecy.intercept()to gain full control over network requests and responses, enabling you to test your application's behavior under various scenarios.
`cy.intercept()`
Working with cookies and local storage inCypressis straightforward due to its built-in commands.
[Cypress](/wiki/cypress)
Cookies:
**Cookies:**
To get a cookie by name:

```
cy.getCookie('session_id').should('exist')
```
`cy.getCookie('session_id').should('exist')`
To get all cookies:

```
cy.getCookies().should('have.length', 1)
```
`cy.getCookies().should('have.length', 1)`
To set a cookie:

```
cy.setCookie('session_id', 'abc123')
```
`cy.setCookie('session_id', 'abc123')`
To clear a specific cookie:

```
cy.clearCookie('session_id')
```
`cy.clearCookie('session_id')`
To clear all cookies:

```
cy.clearCookies()
```
`cy.clearCookies()`
Local Storage:
**Local Storage:**
To set an item in local storage:

```
cy.setLocalStorage('cart', JSON.stringify({ items: 1 }))
```
`cy.setLocalStorage('cart', JSON.stringify({ items: 1 }))`
To get an item from local storage:

```
cy.getLocalStorage('cart').should('equal', '{"items":1}')
```
`cy.getLocalStorage('cart').should('equal', '{"items":1}')`
To clear specific item from local storage:

```
cy.removeLocalStorage('cart')
```
`cy.removeLocalStorage('cart')`
To clear all local storage data:

```
cy.clearLocalStorage()
```
`cy.clearLocalStorage()`
Or to clear local storage with a specific key pattern:

```
cy.clearLocalStorage(/cart/)
```
`cy.clearLocalStorage(/cart/)`
Remember, these commands are asynchronous and return promises, so they should be used withCypress's chaining mechanism. Also, local storage operations are typically performed in the context of the application under test, so ensure the correct page is loaded before attempting to interact with local storage.
[Cypress](/wiki/cypress)
Handling iframes inCypressrequires a few additional steps becauseCypresscommands are designed to operate within the same-origin context. Here's a succinct guide:
[Cypress](/wiki/cypress)[Cypress](/wiki/cypress)1. Target the iframe- Usecy.get()to grab the iframe element.
**Target the iframe**`cy.get()`
```
cy.get('iframe')
```
`cy.get('iframe')`1. Access the iframe's content- Use.its('contentDocument.body')to get the body of the iframe, which is subject to same-origin policy restrictions.
**Access the iframe's content**`.its('contentDocument.body')`
```
cy.get('iframe').its('contentDocument.body').should('not.be.empty').then(cy.wrap)
```
`cy.get('iframe').its('contentDocument.body').should('not.be.empty').then(cy.wrap)`1. Interact with elements- Once wrapped, you can interact with the elements inside the iframe as you would with any other element in Cypress.
**Interact with elements**
```
cy.get('iframe').its('contentDocument.body').should('not.be.empty').then(cy.wrap).find('selector').click()
```
`cy.get('iframe').its('contentDocument.body').should('not.be.empty').then(cy.wrap).find('selector').click()`
Remember that for cross-origin iframes, you'll need to set"chromeWebSecurity": falsein yourcypress.jsonconfiguration file to bypass these restrictions. However, this is not recommended for security reasons and should only be used when absolutely necessary.
`"chromeWebSecurity": false``cypress.json`
If you're dealing with multiple nested iframes, you'll need to repeat the process for each level of iframe nesting, ensuring that you target the correct iframe at each level.

Keep in mind thatCypressbest practices recommend avoiding iframes when possible, as they add complexity to your tests. If you have control over the application, consider alternatives to iframes that are more test-friendly.
[Cypress](/wiki/cypress)
Using plugins inCypressenhances its capabilities by extending its core functionality. To use a plugin, follow these steps:
[Cypress](/wiki/cypress)1. Install the pluginvia npm. For example, to install thecypress-file-uploadplugin, run:npm install --save-dev cypress-file-upload
2. Include the pluginin your project'scypress/plugins/index.jsfile. This is where you modify or extend the internal behavior ofCypress. For instance:module.exports = (on, config) => {
  // your plugin code here
}
3. Import and use the pluginin your test files as needed. For example, withcypress-file-upload, you would add the following to your test file:import 'cypress-file-upload';
4. Utilize the plugin's featuresin your tests. For thecypress-file-uploadplugin, you can now use the.attachFile()command:cy.get('input[type="file"]').attachFile('file.json');

Install the pluginvia npm. For example, to install thecypress-file-uploadplugin, run:
**Install the plugin**`cypress-file-upload`
```
npm install --save-dev cypress-file-upload
```
`npm install --save-dev cypress-file-upload`
Include the pluginin your project'scypress/plugins/index.jsfile. This is where you modify or extend the internal behavior ofCypress. For instance:
**Include the plugin**`cypress/plugins/index.js`[Cypress](/wiki/cypress)
```
module.exports = (on, config) => {
  // your plugin code here
}
```
`module.exports = (on, config) => {
  // your plugin code here
}`
Import and use the pluginin your test files as needed. For example, withcypress-file-upload, you would add the following to your test file:
**Import and use the plugin**`cypress-file-upload`
```
import 'cypress-file-upload';
```
`import 'cypress-file-upload';`
Utilize the plugin's featuresin your tests. For thecypress-file-uploadplugin, you can now use the.attachFile()command:
**Utilize the plugin's features**`cypress-file-upload``.attachFile()`
```
cy.get('input[type="file"]').attachFile('file.json');
```
`cy.get('input[type="file"]').attachFile('file.json');`
Remember tocheck the plugin's documentationfor specific usage instructions and compatibility with your version ofCypress. Some plugins may require additional configuration or initialization steps.
**check the plugin's documentation**[Cypress](/wiki/cypress)
Plugins can provide a variety of functionalities, such as custom commands, improved reporting, or integration with other tools. Alwaysensure that the plugin is actively maintainedand well-suited for your needs before adding it to your project.
**ensure that the plugin is actively maintained**
#### Best Practices and Troubleshooting
- What are some best practices for writing tests in Cypress?When writing tests inCypress, consider the following best practices:Organize tests logicallyusingdescribeandcontextblocks for better readability and structure.Useitblocksfor individual test cases, ensuring they are descriptive and reflect the user behavior you're testing.Keep tests isolated and independentto avoid inter-test dependencies that can cause flakiness.EmployPage Object Modelor similar patterns to abstract element selectors and page interactions, enhancing maintainability.UtilizeCypress's built-in retry-abilityfor commands and assertions to handle dynamic content and reduce flakiness.Avoid using arbitrary waits(cy.wait()with a fixed time); instead, rely on Cypress's automatic waiting for elements to exist, be visible, be clickable, etc.LeverageCypressaliaseswithcy.as()for reusing elements or responses in a chain of commands.Write custom commandsfor reusable sequences of actions, but use them judiciously to keep the clarity of the tests.Assert on real user interactionsand outcomes, not implementation details, to ensure tests remain valid with code changes.Test the critical user journeysfirst to provide immediate value and catch significant regressions early.Use environment variablesfor configuration to keep sensitive data out of the test code and allow flexibility across different environments.Implement Continuous Integrationto run tests automatically on code changes, ensuring immediate feedback on the health of the application.// Example of a descriptive test case
describe('User Profile', () => {
  it('should allow a user to update their profile picture', () => {
    cy.get('.profile-pic').click();
    cy.get('input[type="file"]').attachFile('new-pic.jpg');
    cy.get('.save-btn').click();
    cy.get('.profile-pic').should('have.attr', 'src', 'path/to/new-pic.jpg');
  });
});Remember toreview and refactor tests regularlyto adapt to application changes and improvetest suitereliability and performance.
- How to debug tests in Cypress?Debugging tests inCypresscan be approached systematically:Use theCypressTest Runner: It provides a visual representation oftest execution. You can see commands as they run and inspect the state of the application at each step.Time Travel:Cypresstakes snapshots as your tests run. Hover over commands in the Command Log to see exactly what happened at each step.Real-Time Reloads:Cypressautomatically reloads whenever you make changes to your tests. You can see test results instantly.Console Output: Check the browser's developer console for logs.Cypresscommands log additional information here, which can be useful for debugging..debug()Command: Insert.debug()into your chain of commands to inspect the state of the DOM at that point. It will cause the browser's debugger to kick in.cy.get('.selector').debug().should('have.text', 'expected text');Breakpoints: Usedebuggerstatements in your test code to pause execution at a specific line.cy.get('.selector').then(($el) => {
  debugger; // Execution will pause here
});Network Requests: Inspect network requests in theTest Runner's Command Log to ensureAPIcalls are being made as expected and with the correct data.Error Messages: Read error messages carefully.Cypressprovides descriptive error messages that can guide you to the source of the problem.CypressLogs: Enable verbose logging by settingCypress.config('log', true)to get more detailed information about thetest execution.Retry-ability: Understand thatCypresscommands automatically retry until they succeed or time out. If a test is failing because an assertion is running before the application is ready, consider adding waits or assertions for intermediate states.By combining these tools and techniques, you can effectively debug yourCypresstests and resolve issues more quickly.
- How to handle common errors in Cypress?Handling common errors inCypressinvolves understanding the error messages and applying appropriate fixes or workarounds. Here are some strategies:Timeout Errors: Increase default timeout settings usingcy.wait()or globally incypress.jsonif elements take longer to load.cy.get('.some-element', { timeout: 10000 }) // waits for 10 secondsElement Not Found: Ensure elements are available in the DOM before interacting with them. Use.should('be.visible')to wait for elements to appear.cy.get('.some-element').should('be.visible').click()Cross-Origin Errors: ConfigurechromeWebSecuritytofalseincypress.jsonif you need to bypass the same-origin policy.{
  "chromeWebSecurity": false
}Flaky Tests: Address flakiness by using.retry()for assertions or commands that might fail due to timing issues.cy.get('.some-element').should('exist').retry()Assertion Failures: Review the expected conditions and ensure the assertions match the actual application state. Use explicit assertions like.should('have.text', 'expected text').cy.get('.some-element').should('have.text', 'expected text')Network Errors: Stub network requests usingcy.intercept()to control the response and avoid external dependencies.cy.intercept('GET', '/api/data', { fixture: 'data.json' })Unhandled Promise Rejections: Use.catch()to handle promise rejections within tests and avoid uncaught exceptions.cy.task('mightFail').catch((error) => {
  // handle error
})CypressCommand Queue Errors: Remember thatCypresscommands are asynchronous and queued. Avoid using traditional async/await withCypresscommands.For more complex or persistent errors, consult theCypressdocumentation or community forums for specific solutions and troubleshooting tips.
- How to optimize test execution time in Cypress?To optimizetest executiontime inCypress, consider the following strategies:Run tests in parallel: UtilizeCypressDashboard Service to run tests simultaneously across multiple machines. This can significantly reduce the overalltest suiteexecution time.cypress run --record --key <record_key> --parallelSelectivetest execution: Use.onlyto run specific tests ortest suitesduring development to avoid running the entire suite.describe.only('My Test Suite', () => {
  // Only this suite will run
});

it.only('My Test', () => {
  // Only this test will run
});Test retries: Implement test retries to handleflaky testswithout rerunning the entire suite.// Global level
Cypress.config('retries', 2);

// Test-specific level
it('retries test', { retries: 2 }, () => {
  // Test code here
});Smart waiting: UseCypress's automatic waiting for elements and assertions to avoid unnecessary waits and timeouts.Stubbing and intercepting: Replace actual network calls with stubs usingcy.intercept()to save time spent on real network requests.cy.intercept('GET', '/users', { fixture: 'users.json' });Avoid unnecessary UI actions: Use directAPIcalls to set up application state instead of going through UI workflows.cy.request('POST', '/login', { username: 'user', password: 'pass' });Cache resources: Cache data that doesn't change often between tests to avoid reloading.Optimize selectors: Use efficient selectors to reduce the timeCypressspends querying the DOM.Batch actions: Group actions or commands that can be executed together to minimize the number of yieldableCypresscommands.By implementing these strategies, you can achieve faster feedback cycles and more efficienttest executioninCypress.

When writing tests inCypress, consider the following best practices:
[Cypress](/wiki/cypress)- Organize tests logicallyusingdescribeandcontextblocks for better readability and structure.
- Useitblocksfor individual test cases, ensuring they are descriptive and reflect the user behavior you're testing.
- Keep tests isolated and independentto avoid inter-test dependencies that can cause flakiness.
- EmployPage Object Modelor similar patterns to abstract element selectors and page interactions, enhancing maintainability.
- UtilizeCypress's built-in retry-abilityfor commands and assertions to handle dynamic content and reduce flakiness.
- Avoid using arbitrary waits(cy.wait()with a fixed time); instead, rely on Cypress's automatic waiting for elements to exist, be visible, be clickable, etc.
- LeverageCypressaliaseswithcy.as()for reusing elements or responses in a chain of commands.
- Write custom commandsfor reusable sequences of actions, but use them judiciously to keep the clarity of the tests.
- Assert on real user interactionsand outcomes, not implementation details, to ensure tests remain valid with code changes.
- Test the critical user journeysfirst to provide immediate value and catch significant regressions early.
- Use environment variablesfor configuration to keep sensitive data out of the test code and allow flexibility across different environments.
- Implement Continuous Integrationto run tests automatically on code changes, ensuring immediate feedback on the health of the application.
**Organize tests logically**`describe``context`**Useitblocks**`it`**Keep tests isolated and independent****EmployPage Object Model**[Page Object Model](/wiki/page-object-model)**UtilizeCypress's built-in retry-ability**[Cypress](/wiki/cypress)**Avoid using arbitrary waits**`cy.wait()`**LeverageCypressaliases**[Cypress](/wiki/cypress)`cy.as()`**Write custom commands****Assert on real user interactions****Test the critical user journeys****Use environment variables****Implement Continuous Integration**
```
// Example of a descriptive test case
describe('User Profile', () => {
  it('should allow a user to update their profile picture', () => {
    cy.get('.profile-pic').click();
    cy.get('input[type="file"]').attachFile('new-pic.jpg');
    cy.get('.save-btn').click();
    cy.get('.profile-pic').should('have.attr', 'src', 'path/to/new-pic.jpg');
  });
});
```
`// Example of a descriptive test case
describe('User Profile', () => {
  it('should allow a user to update their profile picture', () => {
    cy.get('.profile-pic').click();
    cy.get('input[type="file"]').attachFile('new-pic.jpg');
    cy.get('.save-btn').click();
    cy.get('.profile-pic').should('have.attr', 'src', 'path/to/new-pic.jpg');
  });
});`
Remember toreview and refactor tests regularlyto adapt to application changes and improvetest suitereliability and performance.
**review and refactor tests regularly**[test suite](/wiki/test-suite)
Debugging tests inCypresscan be approached systematically:
[Cypress](/wiki/cypress)1. Use theCypressTest Runner: It provides a visual representation oftest execution. You can see commands as they run and inspect the state of the application at each step.
2. Time Travel:Cypresstakes snapshots as your tests run. Hover over commands in the Command Log to see exactly what happened at each step.
3. Real-Time Reloads:Cypressautomatically reloads whenever you make changes to your tests. You can see test results instantly.
4. Console Output: Check the browser's developer console for logs.Cypresscommands log additional information here, which can be useful for debugging.
5. .debug()Command: Insert.debug()into your chain of commands to inspect the state of the DOM at that point. It will cause the browser's debugger to kick in.cy.get('.selector').debug().should('have.text', 'expected text');
6. Breakpoints: Usedebuggerstatements in your test code to pause execution at a specific line.cy.get('.selector').then(($el) => {
  debugger; // Execution will pause here
});
7. Network Requests: Inspect network requests in theTest Runner's Command Log to ensureAPIcalls are being made as expected and with the correct data.
8. Error Messages: Read error messages carefully.Cypressprovides descriptive error messages that can guide you to the source of the problem.
9. CypressLogs: Enable verbose logging by settingCypress.config('log', true)to get more detailed information about thetest execution.
10. Retry-ability: Understand thatCypresscommands automatically retry until they succeed or time out. If a test is failing because an assertion is running before the application is ready, consider adding waits or assertions for intermediate states.

Use theCypressTest Runner: It provides a visual representation oftest execution. You can see commands as they run and inspect the state of the application at each step.
**Use theCypressTest Runner**[Cypress](/wiki/cypress)[Test Runner](/wiki/test-runner)[test execution](/wiki/test-execution)
Time Travel:Cypresstakes snapshots as your tests run. Hover over commands in the Command Log to see exactly what happened at each step.
**Time Travel**[Cypress](/wiki/cypress)
Real-Time Reloads:Cypressautomatically reloads whenever you make changes to your tests. You can see test results instantly.
**Real-Time Reloads**[Cypress](/wiki/cypress)
Console Output: Check the browser's developer console for logs.Cypresscommands log additional information here, which can be useful for debugging.
**Console Output**[Cypress](/wiki/cypress)
.debug()Command: Insert.debug()into your chain of commands to inspect the state of the DOM at that point. It will cause the browser's debugger to kick in.
**.debug()Command**`.debug()``.debug()`
```
cy.get('.selector').debug().should('have.text', 'expected text');
```
`cy.get('.selector').debug().should('have.text', 'expected text');`
Breakpoints: Usedebuggerstatements in your test code to pause execution at a specific line.
**Breakpoints**`debugger`
```
cy.get('.selector').then(($el) => {
  debugger; // Execution will pause here
});
```
`cy.get('.selector').then(($el) => {
  debugger; // Execution will pause here
});`
Network Requests: Inspect network requests in theTest Runner's Command Log to ensureAPIcalls are being made as expected and with the correct data.
**Network Requests**[Test Runner](/wiki/test-runner)[API](/wiki/api)
Error Messages: Read error messages carefully.Cypressprovides descriptive error messages that can guide you to the source of the problem.
**Error Messages**[Cypress](/wiki/cypress)
CypressLogs: Enable verbose logging by settingCypress.config('log', true)to get more detailed information about thetest execution.
**CypressLogs**[Cypress](/wiki/cypress)`Cypress.config('log', true)`[test execution](/wiki/test-execution)
Retry-ability: Understand thatCypresscommands automatically retry until they succeed or time out. If a test is failing because an assertion is running before the application is ready, consider adding waits or assertions for intermediate states.
**Retry-ability**[Cypress](/wiki/cypress)
By combining these tools and techniques, you can effectively debug yourCypresstests and resolve issues more quickly.
[Cypress](/wiki/cypress)
Handling common errors inCypressinvolves understanding the error messages and applying appropriate fixes or workarounds. Here are some strategies:
[Cypress](/wiki/cypress)
Timeout Errors: Increase default timeout settings usingcy.wait()or globally incypress.jsonif elements take longer to load.
**Timeout Errors**`cy.wait()``cypress.json`
```
cy.get('.some-element', { timeout: 10000 }) // waits for 10 seconds
```
`cy.get('.some-element', { timeout: 10000 }) // waits for 10 seconds`
Element Not Found: Ensure elements are available in the DOM before interacting with them. Use.should('be.visible')to wait for elements to appear.
**Element Not Found**`.should('be.visible')`
```
cy.get('.some-element').should('be.visible').click()
```
`cy.get('.some-element').should('be.visible').click()`
Cross-Origin Errors: ConfigurechromeWebSecuritytofalseincypress.jsonif you need to bypass the same-origin policy.
**Cross-Origin Errors**`chromeWebSecurity``false``cypress.json`
```
{
  "chromeWebSecurity": false
}
```
`{
  "chromeWebSecurity": false
}`
Flaky Tests: Address flakiness by using.retry()for assertions or commands that might fail due to timing issues.
**Flaky Tests**[Flaky Tests](/wiki/flaky-test)`.retry()`
```
cy.get('.some-element').should('exist').retry()
```
`cy.get('.some-element').should('exist').retry()`
Assertion Failures: Review the expected conditions and ensure the assertions match the actual application state. Use explicit assertions like.should('have.text', 'expected text').
**Assertion Failures**`.should('have.text', 'expected text')`
```
cy.get('.some-element').should('have.text', 'expected text')
```
`cy.get('.some-element').should('have.text', 'expected text')`
Network Errors: Stub network requests usingcy.intercept()to control the response and avoid external dependencies.
**Network Errors**`cy.intercept()`
```
cy.intercept('GET', '/api/data', { fixture: 'data.json' })
```
`cy.intercept('GET', '/api/data', { fixture: 'data.json' })`
Unhandled Promise Rejections: Use.catch()to handle promise rejections within tests and avoid uncaught exceptions.
**Unhandled Promise Rejections**`.catch()`
```
cy.task('mightFail').catch((error) => {
  // handle error
})
```
`cy.task('mightFail').catch((error) => {
  // handle error
})`
CypressCommand Queue Errors: Remember thatCypresscommands are asynchronous and queued. Avoid using traditional async/await withCypresscommands.
**CypressCommand Queue Errors**[Cypress](/wiki/cypress)[Cypress](/wiki/cypress)[Cypress](/wiki/cypress)
For more complex or persistent errors, consult theCypressdocumentation or community forums for specific solutions and troubleshooting tips.
[Cypress](/wiki/cypress)
To optimizetest executiontime inCypress, consider the following strategies:
[test execution](/wiki/test-execution)[Cypress](/wiki/cypress)- Run tests in parallel: UtilizeCypressDashboard Service to run tests simultaneously across multiple machines. This can significantly reduce the overalltest suiteexecution time.cypress run --record --key <record_key> --parallel
- Selectivetest execution: Use.onlyto run specific tests ortest suitesduring development to avoid running the entire suite.describe.only('My Test Suite', () => {
  // Only this suite will run
});

it.only('My Test', () => {
  // Only this test will run
});
- Test retries: Implement test retries to handleflaky testswithout rerunning the entire suite.// Global level
Cypress.config('retries', 2);

// Test-specific level
it('retries test', { retries: 2 }, () => {
  // Test code here
});
- Smart waiting: UseCypress's automatic waiting for elements and assertions to avoid unnecessary waits and timeouts.
- Stubbing and intercepting: Replace actual network calls with stubs usingcy.intercept()to save time spent on real network requests.cy.intercept('GET', '/users', { fixture: 'users.json' });
- Avoid unnecessary UI actions: Use directAPIcalls to set up application state instead of going through UI workflows.cy.request('POST', '/login', { username: 'user', password: 'pass' });
- Cache resources: Cache data that doesn't change often between tests to avoid reloading.
- Optimize selectors: Use efficient selectors to reduce the timeCypressspends querying the DOM.
- Batch actions: Group actions or commands that can be executed together to minimize the number of yieldableCypresscommands.

Run tests in parallel: UtilizeCypressDashboard Service to run tests simultaneously across multiple machines. This can significantly reduce the overalltest suiteexecution time.
**Run tests in parallel**[Cypress](/wiki/cypress)[test suite](/wiki/test-suite)
```
cypress run --record --key <record_key> --parallel
```
`cypress run --record --key <record_key> --parallel`
Selectivetest execution: Use.onlyto run specific tests ortest suitesduring development to avoid running the entire suite.
**Selectivetest execution**[test execution](/wiki/test-execution)`.only`[test suites](/wiki/test-suite)
```
describe.only('My Test Suite', () => {
  // Only this suite will run
});

it.only('My Test', () => {
  // Only this test will run
});
```
`describe.only('My Test Suite', () => {
  // Only this suite will run
});

it.only('My Test', () => {
  // Only this test will run
});`
Test retries: Implement test retries to handleflaky testswithout rerunning the entire suite.
**Test retries**[flaky tests](/wiki/flaky-test)
```
// Global level
Cypress.config('retries', 2);

// Test-specific level
it('retries test', { retries: 2 }, () => {
  // Test code here
});
```
`// Global level
Cypress.config('retries', 2);

// Test-specific level
it('retries test', { retries: 2 }, () => {
  // Test code here
});`
Smart waiting: UseCypress's automatic waiting for elements and assertions to avoid unnecessary waits and timeouts.
**Smart waiting**[Cypress](/wiki/cypress)
Stubbing and intercepting: Replace actual network calls with stubs usingcy.intercept()to save time spent on real network requests.
**Stubbing and intercepting**`cy.intercept()`
```
cy.intercept('GET', '/users', { fixture: 'users.json' });
```
`cy.intercept('GET', '/users', { fixture: 'users.json' });`
Avoid unnecessary UI actions: Use directAPIcalls to set up application state instead of going through UI workflows.
**Avoid unnecessary UI actions**[API](/wiki/api)
```
cy.request('POST', '/login', { username: 'user', password: 'pass' });
```
`cy.request('POST', '/login', { username: 'user', password: 'pass' });`
Cache resources: Cache data that doesn't change often between tests to avoid reloading.
**Cache resources**
Optimize selectors: Use efficient selectors to reduce the timeCypressspends querying the DOM.
**Optimize selectors**[Cypress](/wiki/cypress)
Batch actions: Group actions or commands that can be executed together to minimize the number of yieldableCypresscommands.
**Batch actions**[Cypress](/wiki/cypress)
By implementing these strategies, you can achieve faster feedback cycles and more efficienttest executioninCypress.
[test execution](/wiki/test-execution)[Cypress](/wiki/cypress)
