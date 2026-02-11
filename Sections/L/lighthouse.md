# Lighthouse
[Lighthouse](#lighthouse)[Lighthouse](/wiki/lighthouse)[Lighthouse](/wiki/lighthouse)
### See also:
- Wikipedia
[Wikipedia](https://en.wikipedia.org/wiki/Google_Lighthouse)
## Questions aboutLighthouse?

#### Basics and Importance
- What is Lighthouse?Lighthouseis anopen-source,automated toolfor improving the quality of web pages. It can be run against any web page, public or requiring authentication.Lighthouseaudits for performance, accessibility, progressive web apps, SEO, and more, providing a well-rounded view of the quality and effectiveness of a web page.To useLighthouseinChrome, navigate to the page you want to audit, openDevTools, and click on theLighthousetab. Select the audits you want to run, and then click theGenerate reportbutton.Lighthousewill run the selected audits against the page, then generate a report on how well the page did.Forautomated testing,Lighthousecan be integrated intocontinuous integrationsystems. It can be run as a Node module, as a command line tool, or programmatically as part of a custom build process.LighthouseCI is a set of commands that make it easier to useLighthousefor continuous integration.Scores are calculated based on the performance metrics and heuristics. Each metric is scored individually, and then the scores are combined into an overall score.Improving a lowLighthousescore involves addressing the specific feedback provided in the report. This could include optimizing images, minifying CSS and JavaScript, implementing lazy loading, improving accessibility features, and more.ForJavaScript execution,Lighthousesimulates a mid-tier device, even when run on a powerful desktop machine, to create consistent, real-world conditions.Common issues when usingLighthouseinclude flaky performance metrics, which can be mitigated by running the audit multiple times and considering median values.
- Why is Lighthouse important in software automation?Lighthouseis crucial in softwaretest automationfor its ability tointegrate performance and quality checksinto the development and deployment pipeline. It providesautomated auditsfor performance, accessibility, progressive web apps, SEO, and best practices, which are essential for maintaining high-quality web applications.By incorporatingLighthouseintoautomated testing, engineers can ensure that any code changes are evaluated against these metrics, catching regressions or issues early in the development cycle. This is particularly important forcontinuous integration (CI)andcontinuous deployment (CD)environments, where automated tests must provide quick feedback on the potential impact of code changes.Lighthouse's role extends toperformance budgeting, helping teams set and adhere to performance goals. It can be run headlessly, making it suitable forserver-side automationand integration into CI/CD pipelines. The tool'sconfigurabilityallows for custom audits tailored to specific needs, and itsscoring systemprovides a quantifiable measure of a site's quality attributes.Moreover,Lighthouse'sreportsoffer actionable insights, which are invaluable for engineers looking to optimize their web applications. The ability to automate these audits and integrate them into the development workflow makesLighthousean important tool for maintaining and improving the quality and user experience of web applications in an automated and efficient manner.
- What are the key features of Lighthouse?Key features ofLighthouseinclude:Performance Metrics:Lighthouseprovides detailed metrics such as First Contentful Paint (FCP), Speed Index, Largest Contentful Paint (LCP), Time to Interactive (TTI), Total Blocking Time (TBT), and Cumulative Layout Shift (CLS).Accessibility Audits: It evaluates the accessibility of a web page against the Web Content Accessibility Guidelines (WCAG) and suggests improvements.Best Practices:Lighthousechecks for adherence to best practices in web development, such as HTTPS usage, correct image aspect ratios, and avoiding deprecatedAPIs.SEO Audits: It assesses elements that affect a page's search engine ranking, including meta tags, hreflang tags, and descriptive link text.Progressive Web App (PWA) Assessment:Lighthousecan validate various aspects of PWAs, ensuring they meet certain criteria for reliability, performance, and engagement.Custom Audits: Developers can extendLighthouseby writing custom audits to check for specific requirements or standards relevant to their projects.CLI and ProgrammableAPI:Lighthousecan be run via command line or programmatically through itsAPI, allowing integration into automated workflows and CI/CD pipelines.Configurability: Users can configureLighthouseruns by specifying categories to audit, throttling settings, and other runtime options.Reporting: After an audit,Lighthousegenerates a report with scores in each category, detailed explanations, and actionable recommendations for improvement.Extensibility:Lighthouseis open-source and can be extended or customized to fit specific testing needs, and it integrates with other tools likeLighthouseCI for continuous testing.These features makeLighthousea versatile tool for web developers andtest automationengineers focused on improving the quality of web applications.
- How does Lighthouse differ from other performance auditing tools?Lighthousedistinguishes itself from other performance auditing tools through itsintegration with the Chrome Developer Toolsand itsemphasis on the user experiencemetrics, such as the Core Web Vitals. While tools like WebPageTest provide detailed waterfalls and network information,Lighthousefocuses on providing aholistic viewof web performance, accessibility, best practices, SEO, and progressive web app metrics.Unlike some tools that require complexsetupor server-side integration,Lighthouseiseasily accessibleand can be run from the command line, as a Node module, or directly in the browser, making it highly versatile for different workflows. It also offerscustom audit capabilitiesthrough its flexible configuration options.Lighthouse'sactionable reportswith clear scoring and recommendations stand out, guiding developers on how to improve performance and user experience. It's particularly useful for simulating a page load on a mobile network and a mid-tier device, which is a commonuse casenot always covered by other tools.Moreover,Lighthouseisopen-sourceand maintained by Google, ensuring regular updates that reflect the latest web development best practices and standards. This contrasts with some proprietary tools that may not be as transparent or up-to-date with web standards.Lastly,Lighthouse's ability to be integrated intoCI/CD pipelinesthroughLighthouseCI makes it a powerful option for automating performance checks and ensuring that performance standards are met before deployment.
- What types of audits does Lighthouse perform?Lighthouseperforms audits acrossfive categories:Performance,Accessibility,Best Practices,SEO, andProgressive Web App (PWA). Each category encompasses various checks:Performance: Evaluates metrics like First Contentful Paint, Speed Index, and Time to Interactive, focusing on user-perceived loading experience and interactivity.Accessibility: Checks for common issues that may prevent users from accessing content, such as missing alt text for images, improper ARIA attributes, and incorrect semantic HTML elements.Best Practices: Looks for modern web development practices, including HTTPS usage, correct image aspect ratios, and avoidance of deprecatedAPIs.SEO: Assesses elements that affect a page's visibility to search engines, like meta descriptions, hreflang links, and legible font sizes.PWA: Verifies the presence of a service worker, a web app manifest, and other criteria that enable a web app to be installed on a device's home screen and function offline.Each audit provides specific, actionable feedback and is scored individually, contributing to an overall category score.Lighthousealso offersopportunitiesanddiagnosticsto help identify areas for improvement and understand underlying issues. These audits can be extended or customized for specificuse casesthroughLighthouseconfiguration.

Lighthouseis anopen-source,automated toolfor improving the quality of web pages. It can be run against any web page, public or requiring authentication.Lighthouseaudits for performance, accessibility, progressive web apps, SEO, and more, providing a well-rounded view of the quality and effectiveness of a web page.
[Lighthouse](/wiki/lighthouse)**open-source****automated tool**[Lighthouse](/wiki/lighthouse)
To useLighthouseinChrome, navigate to the page you want to audit, openDevTools, and click on theLighthousetab. Select the audits you want to run, and then click theGenerate reportbutton.Lighthousewill run the selected audits against the page, then generate a report on how well the page did.
[Lighthouse](/wiki/lighthouse)**Chrome****DevTools****Lighthouse**[Lighthouse](/wiki/lighthouse)**Generate report**[Lighthouse](/wiki/lighthouse)
Forautomated testing,Lighthousecan be integrated intocontinuous integrationsystems. It can be run as a Node module, as a command line tool, or programmatically as part of a custom build process.LighthouseCI is a set of commands that make it easier to useLighthousefor continuous integration.
**automated testing**[automated testing](/wiki/automated-testing)[Lighthouse](/wiki/lighthouse)**continuous integration**[Lighthouse](/wiki/lighthouse)[Lighthouse](/wiki/lighthouse)
Scores are calculated based on the performance metrics and heuristics. Each metric is scored individually, and then the scores are combined into an overall score.

Improving a lowLighthousescore involves addressing the specific feedback provided in the report. This could include optimizing images, minifying CSS and JavaScript, implementing lazy loading, improving accessibility features, and more.
[Lighthouse](/wiki/lighthouse)
ForJavaScript execution,Lighthousesimulates a mid-tier device, even when run on a powerful desktop machine, to create consistent, real-world conditions.
**JavaScript execution**[Lighthouse](/wiki/lighthouse)
Common issues when usingLighthouseinclude flaky performance metrics, which can be mitigated by running the audit multiple times and considering median values.
[Lighthouse](/wiki/lighthouse)
Lighthouseis crucial in softwaretest automationfor its ability tointegrate performance and quality checksinto the development and deployment pipeline. It providesautomated auditsfor performance, accessibility, progressive web apps, SEO, and best practices, which are essential for maintaining high-quality web applications.
[Lighthouse](/wiki/lighthouse)[test automation](/wiki/test-automation)**integrate performance and quality checks****automated audits**
By incorporatingLighthouseintoautomated testing, engineers can ensure that any code changes are evaluated against these metrics, catching regressions or issues early in the development cycle. This is particularly important forcontinuous integration (CI)andcontinuous deployment (CD)environments, where automated tests must provide quick feedback on the potential impact of code changes.
[Lighthouse](/wiki/lighthouse)[automated testing](/wiki/automated-testing)**continuous integration (CI)****continuous deployment (CD)**
Lighthouse's role extends toperformance budgeting, helping teams set and adhere to performance goals. It can be run headlessly, making it suitable forserver-side automationand integration into CI/CD pipelines. The tool'sconfigurabilityallows for custom audits tailored to specific needs, and itsscoring systemprovides a quantifiable measure of a site's quality attributes.
[Lighthouse](/wiki/lighthouse)**performance budgeting****server-side automation****configurability****scoring system**
Moreover,Lighthouse'sreportsoffer actionable insights, which are invaluable for engineers looking to optimize their web applications. The ability to automate these audits and integrate them into the development workflow makesLighthousean important tool for maintaining and improving the quality and user experience of web applications in an automated and efficient manner.
[Lighthouse](/wiki/lighthouse)**reports**[Lighthouse](/wiki/lighthouse)
Key features ofLighthouseinclude:
**Lighthouse**[Lighthouse](/wiki/lighthouse)- Performance Metrics:Lighthouseprovides detailed metrics such as First Contentful Paint (FCP), Speed Index, Largest Contentful Paint (LCP), Time to Interactive (TTI), Total Blocking Time (TBT), and Cumulative Layout Shift (CLS).
- Accessibility Audits: It evaluates the accessibility of a web page against the Web Content Accessibility Guidelines (WCAG) and suggests improvements.
- Best Practices:Lighthousechecks for adherence to best practices in web development, such as HTTPS usage, correct image aspect ratios, and avoiding deprecatedAPIs.
- SEO Audits: It assesses elements that affect a page's search engine ranking, including meta tags, hreflang tags, and descriptive link text.
- Progressive Web App (PWA) Assessment:Lighthousecan validate various aspects of PWAs, ensuring they meet certain criteria for reliability, performance, and engagement.
- Custom Audits: Developers can extendLighthouseby writing custom audits to check for specific requirements or standards relevant to their projects.
- CLI and ProgrammableAPI:Lighthousecan be run via command line or programmatically through itsAPI, allowing integration into automated workflows and CI/CD pipelines.
- Configurability: Users can configureLighthouseruns by specifying categories to audit, throttling settings, and other runtime options.
- Reporting: After an audit,Lighthousegenerates a report with scores in each category, detailed explanations, and actionable recommendations for improvement.
- Extensibility:Lighthouseis open-source and can be extended or customized to fit specific testing needs, and it integrates with other tools likeLighthouseCI for continuous testing.

Performance Metrics:Lighthouseprovides detailed metrics such as First Contentful Paint (FCP), Speed Index, Largest Contentful Paint (LCP), Time to Interactive (TTI), Total Blocking Time (TBT), and Cumulative Layout Shift (CLS).
**Performance Metrics**[Lighthouse](/wiki/lighthouse)
Accessibility Audits: It evaluates the accessibility of a web page against the Web Content Accessibility Guidelines (WCAG) and suggests improvements.
**Accessibility Audits**
Best Practices:Lighthousechecks for adherence to best practices in web development, such as HTTPS usage, correct image aspect ratios, and avoiding deprecatedAPIs.
**Best Practices**[Lighthouse](/wiki/lighthouse)[APIs](/wiki/api)
SEO Audits: It assesses elements that affect a page's search engine ranking, including meta tags, hreflang tags, and descriptive link text.
**SEO Audits**
Progressive Web App (PWA) Assessment:Lighthousecan validate various aspects of PWAs, ensuring they meet certain criteria for reliability, performance, and engagement.
**Progressive Web App (PWA) Assessment**[Lighthouse](/wiki/lighthouse)
Custom Audits: Developers can extendLighthouseby writing custom audits to check for specific requirements or standards relevant to their projects.
**Custom Audits**[Lighthouse](/wiki/lighthouse)
CLI and ProgrammableAPI:Lighthousecan be run via command line or programmatically through itsAPI, allowing integration into automated workflows and CI/CD pipelines.
**CLI and ProgrammableAPI**[API](/wiki/api)[Lighthouse](/wiki/lighthouse)[API](/wiki/api)
Configurability: Users can configureLighthouseruns by specifying categories to audit, throttling settings, and other runtime options.
**Configurability**[Lighthouse](/wiki/lighthouse)
Reporting: After an audit,Lighthousegenerates a report with scores in each category, detailed explanations, and actionable recommendations for improvement.
**Reporting**[Lighthouse](/wiki/lighthouse)
Extensibility:Lighthouseis open-source and can be extended or customized to fit specific testing needs, and it integrates with other tools likeLighthouseCI for continuous testing.
**Extensibility**[Lighthouse](/wiki/lighthouse)[Lighthouse](/wiki/lighthouse)
These features makeLighthousea versatile tool for web developers andtest automationengineers focused on improving the quality of web applications.
[Lighthouse](/wiki/lighthouse)[test automation](/wiki/test-automation)
Lighthousedistinguishes itself from other performance auditing tools through itsintegration with the Chrome Developer Toolsand itsemphasis on the user experiencemetrics, such as the Core Web Vitals. While tools like WebPageTest provide detailed waterfalls and network information,Lighthousefocuses on providing aholistic viewof web performance, accessibility, best practices, SEO, and progressive web app metrics.
[Lighthouse](/wiki/lighthouse)**integration with the Chrome Developer Tools****emphasis on the user experience**[Lighthouse](/wiki/lighthouse)**holistic view**
Unlike some tools that require complexsetupor server-side integration,Lighthouseiseasily accessibleand can be run from the command line, as a Node module, or directly in the browser, making it highly versatile for different workflows. It also offerscustom audit capabilitiesthrough its flexible configuration options.
[setup](/wiki/setup)[Lighthouse](/wiki/lighthouse)**easily accessible****custom audit capabilities**
Lighthouse'sactionable reportswith clear scoring and recommendations stand out, guiding developers on how to improve performance and user experience. It's particularly useful for simulating a page load on a mobile network and a mid-tier device, which is a commonuse casenot always covered by other tools.
[Lighthouse](/wiki/lighthouse)**actionable reports**[use case](/wiki/use-case)
Moreover,Lighthouseisopen-sourceand maintained by Google, ensuring regular updates that reflect the latest web development best practices and standards. This contrasts with some proprietary tools that may not be as transparent or up-to-date with web standards.
[Lighthouse](/wiki/lighthouse)**open-source**
Lastly,Lighthouse's ability to be integrated intoCI/CD pipelinesthroughLighthouseCI makes it a powerful option for automating performance checks and ensuring that performance standards are met before deployment.
[Lighthouse](/wiki/lighthouse)**CI/CD pipelines**[Lighthouse](/wiki/lighthouse)
Lighthouseperforms audits acrossfive categories:Performance,Accessibility,Best Practices,SEO, andProgressive Web App (PWA). Each category encompasses various checks:
[Lighthouse](/wiki/lighthouse)**five categories****Performance****Accessibility****Best Practices****SEO****Progressive Web App (PWA)**- Performance: Evaluates metrics like First Contentful Paint, Speed Index, and Time to Interactive, focusing on user-perceived loading experience and interactivity.
- Accessibility: Checks for common issues that may prevent users from accessing content, such as missing alt text for images, improper ARIA attributes, and incorrect semantic HTML elements.
- Best Practices: Looks for modern web development practices, including HTTPS usage, correct image aspect ratios, and avoidance of deprecatedAPIs.
- SEO: Assesses elements that affect a page's visibility to search engines, like meta descriptions, hreflang links, and legible font sizes.
- PWA: Verifies the presence of a service worker, a web app manifest, and other criteria that enable a web app to be installed on a device's home screen and function offline.

Performance: Evaluates metrics like First Contentful Paint, Speed Index, and Time to Interactive, focusing on user-perceived loading experience and interactivity.
**Performance**
Accessibility: Checks for common issues that may prevent users from accessing content, such as missing alt text for images, improper ARIA attributes, and incorrect semantic HTML elements.
**Accessibility**
Best Practices: Looks for modern web development practices, including HTTPS usage, correct image aspect ratios, and avoidance of deprecatedAPIs.
**Best Practices**[APIs](/wiki/api)
SEO: Assesses elements that affect a page's visibility to search engines, like meta descriptions, hreflang links, and legible font sizes.
**SEO**
PWA: Verifies the presence of a service worker, a web app manifest, and other criteria that enable a web app to be installed on a device's home screen and function offline.
**PWA**
Each audit provides specific, actionable feedback and is scored individually, contributing to an overall category score.Lighthousealso offersopportunitiesanddiagnosticsto help identify areas for improvement and understand underlying issues. These audits can be extended or customized for specificuse casesthroughLighthouseconfiguration.
[Lighthouse](/wiki/lighthouse)**opportunities****diagnostics**[use cases](/wiki/use-case)[Lighthouse](/wiki/lighthouse)
#### Usage and Implementation
- How do you use Lighthouse in Chrome?To useLighthousein Chrome fortest automation, follow these steps:Open Chrome Developer Tools by pressingCtrl+Shift+I(orCmd+Option+Ion Mac).Navigate to theLighthousetab.Choose the desired audit categories (Performance, Accessibility, Best Practices, SEO, and Progressive Web App).Select the appropriate device type (Mobile or Desktop) for the simulation.Click onGenerate reportto start the audit.For automation purposes, you can runLighthouseprogrammatically using the command line or as a Node module. Here's a basic example usingNode.js:const lighthouse = require('lighthouse');
const chromeLauncher = require('chrome-launcher');

async function runLighthouse(url, options, config = null) {
  const chrome = await chromeLauncher.launch({ chromeFlags: options.chromeFlags });
  options.port = chrome.port;
  const results = await lighthouse(url, options, config);
  await chrome.kill();
  return results.lhr;
}

const options = {
  chromeFlags: ['--headless'],
  // Add more options here
};

// Usage
runLighthouse('https://example.com', options)
  .then(results => console.log(results))
  .catch(err => console.error(err));For continuous integration, you can useLighthouseCIwhich provides commands to run audits against a website and assert if the scores meet your requirements. It can be integrated into your CI pipeline using configuration files and CLI commands.Remember to review the audit results and make necessary code or configuration changes to improve the scores. Automate the process by integrating it into your build and deployment pipeline to ensure continuous performance monitoring.
- How can Lighthouse be used for automated testing?Lighthousecan be integrated intoautomated testingworkflows to ensure web applications meet performance, accessibility, best practices, and SEO standards. To automateLighthousetests, you can use theLighthouseCLI or theLighthouseNode module.CLI Approach:InstallLighthouseglobally via npm:npm install -g lighthouseRunLighthousein headless mode to test a URL and output the results to a JSON file:lighthouse https://example.com --output=json --output-path=./report.json --chrome-flags="--headless"Node Module Approach:InstallLighthouseas a dev dependency:npm install --save-dev lighthouseCreate a script to launch Chrome and runLighthouseprogrammatically:const lighthouse = require('lighthouse');
const chromeLauncher = require('chrome-launcher');

async function runLighthouse(url, opts, config = null) {
  const chrome = await chromeLauncher.launch({ chromeFlags: opts.chromeFlags });
  opts.port = chrome.port;
  const results = await lighthouse(url, opts, config);
  await chrome.kill();
  return results.lhr;
}

const options = {
  chromeFlags: ['--headless'],
  output: 'json'
};

runLighthouse('https://example.com', options)
  .then(results => {
    // Process Lighthouse results here
  });Continuous Integration:IncorporateLighthouseinto CI pipelines usingLighthouseCI. Set up a.lighthouserc.jsconfiguration file and addLighthouseCI commands to your CI configuration:lhci autorun --config=.lighthouserc.jsThis will run audits against the specified URLs during each commit or pull request, ensuring that code changes do not degrade the quality of the application. Use theLighthouseCI server for historical tracking and asserting performance budgets.
- What are the steps to run a Lighthouse audit?To run aLighthouseaudit:Open Google Chromeand navigate to the page you want to audit.Access Developer Toolsby pressingCtrl+Shift+I(orCmd+Option+Ion Mac), or right-clicking the page and selecting "Inspect".Click on theLighthousetab within the Developer Tools panel. If it's not visible, you may need to click on the>>icon to find it.Select the categoriesyou wish to audit (Performance, Accessibility, Best Practices, SEO, and Progressive Web App).Choose thedevice type(mobile or desktop) for the simulation.(Optional) Click onAdvanced Settingsto adjust throttling options or to block certain URLs during the audit.Click on the"Generate report"button to start the audit.Lighthousewill now run a series of tests against the page and generate a report. Once the audit is complete, you'll be presented with a detailed report outlining the performance and quality of the page. You can use this report to identify areas for improvement.Forautomated testingor continuous integration, you can useLighthouseCLI by installing it via npm:npm install -g lighthouseThen run the audit with:lighthouse https://example.com --output json --output-path ./report.jsonReplacehttps://example.comwith your URL and adjust the output format and path as needed. This command will generate a JSON report that can be integrated into your CI/CD pipeline.
- How can you use Lighthouse in continuous integration processes?IntegratingLighthouseinto continuous integration (CI) processes ensures that performance, accessibility, and SEO standards are upheld with each code commit. To useLighthousein CI, follow these steps:InstallLighthouseCI:npm install -g @lhci/cliConfigureLighthouseCIby creating a.lighthouserc.jsor.lighthouserc.jsonfile in your project root. Define the URLs to audit, the number of runs, and any other configurations.Add aLighthouseCI stepin your CI pipeline. For example, in a GitHub Actions workflow, add a job that runsLighthouseCI:- name: Run Lighthouse CI
  run: lhci autorunSet up assertionsto enforce performance budgets or specific audit thresholds. Fail the CI build if these are not met:"assertions": {
  "categories:performance": ["error", { "minScore": 0.9 }],
  "categories:accessibility": ["error", { "minScore": 0.9 }]
}Store reportsfor historical comparison and tracking regressions. Use the--upload.targetoption to upload toLighthouseCI server or other storage solutions.Automate the processto run on every pull request or push to specific branches, ensuring that new code meets the defined quality standards.By integratingLighthouseinto CI, you create afeedback loopthat alerts developers to potential issues early, maintaining a high standard for your web application's user experience.
- How can you configure Lighthouse for custom audits?To configureLighthousefor custom audits, you need to create custom audit definitions and gatherers. Here's a concise guide:Create a Custom Gatherer:A gatherer collects information from the page. Extend theGathererclass from Lighthouse.const { Gatherer } = require('lighthouse');

class CustomGatherer extends Gatherer {
  afterPass(options) {
    // Collect data and return it
  }
}

module.exports = CustomGatherer;Develop a Custom Audit:Audits use the data collected by gatherers. Extend theAuditclass.const { Audit } = require('lighthouse');

class CustomAudit extends Audit {
  static get meta() {
    return {
      id: 'custom-audit-id',
      title: 'Custom Audit',
      failureTitle: 'Custom Audit Failed',
      description: 'Description of your custom audit',
      requiredArtifacts: ['CustomGatherer'],
    };
  }

  static audit(artifacts) {
    const loadMetrics = artifacts.CustomGatherer;
    // Perform audit logic and return a score
    return {
      score: Number(loadMetrics < threshold),
    };
  }
}

module.exports = CustomAudit;Add toLighthouseConfig:Include your custom gatherer and audit in the Lighthouse configuration.module.exports = {
  passes: [{
    passName: 'defaultPass',
    gatherers: [
      'path/to/customgatherer',
    ],
  }],
  audits: [
    'path/to/customaudit',
  ],
  categories: {
    customCategory: {
      title: 'Custom Category',
      description: 'Includes custom audits',
      auditRefs: [
        { id: 'custom-audit-id', weight: 1 },
      ],
    },
  },
};RunLighthousewith your custom config:lighthouse https://example.com --config-path=path/to/custom-config.jsRemember to handle exceptions and edge cases in your gatherer and audit logic to ensure robustness.

To useLighthousein Chrome fortest automation, follow these steps:
**Lighthouse**[Lighthouse](/wiki/lighthouse)[test automation](/wiki/test-automation)1. Open Chrome Developer Tools by pressingCtrl+Shift+I(orCmd+Option+Ion Mac).
2. Navigate to theLighthousetab.
3. Choose the desired audit categories (Performance, Accessibility, Best Practices, SEO, and Progressive Web App).
4. Select the appropriate device type (Mobile or Desktop) for the simulation.
5. Click onGenerate reportto start the audit.
`Ctrl+Shift+I``Cmd+Option+I`**Lighthouse**[Lighthouse](/wiki/lighthouse)**Generate report**
For automation purposes, you can runLighthouseprogrammatically using the command line or as a Node module. Here's a basic example usingNode.js:
[Lighthouse](/wiki/lighthouse)[Node.js](/wiki/node-js)
```
const lighthouse = require('lighthouse');
const chromeLauncher = require('chrome-launcher');

async function runLighthouse(url, options, config = null) {
  const chrome = await chromeLauncher.launch({ chromeFlags: options.chromeFlags });
  options.port = chrome.port;
  const results = await lighthouse(url, options, config);
  await chrome.kill();
  return results.lhr;
}

const options = {
  chromeFlags: ['--headless'],
  // Add more options here
};

// Usage
runLighthouse('https://example.com', options)
  .then(results => console.log(results))
  .catch(err => console.error(err));
```
`const lighthouse = require('lighthouse');
const chromeLauncher = require('chrome-launcher');

async function runLighthouse(url, options, config = null) {
  const chrome = await chromeLauncher.launch({ chromeFlags: options.chromeFlags });
  options.port = chrome.port;
  const results = await lighthouse(url, options, config);
  await chrome.kill();
  return results.lhr;
}

const options = {
  chromeFlags: ['--headless'],
  // Add more options here
};

// Usage
runLighthouse('https://example.com', options)
  .then(results => console.log(results))
  .catch(err => console.error(err));`
For continuous integration, you can useLighthouseCIwhich provides commands to run audits against a website and assert if the scores meet your requirements. It can be integrated into your CI pipeline using configuration files and CLI commands.
**LighthouseCI**[Lighthouse](/wiki/lighthouse)
Remember to review the audit results and make necessary code or configuration changes to improve the scores. Automate the process by integrating it into your build and deployment pipeline to ensure continuous performance monitoring.

Lighthousecan be integrated intoautomated testingworkflows to ensure web applications meet performance, accessibility, best practices, and SEO standards. To automateLighthousetests, you can use theLighthouseCLI or theLighthouseNode module.
[Lighthouse](/wiki/lighthouse)[automated testing](/wiki/automated-testing)[Lighthouse](/wiki/lighthouse)[Lighthouse](/wiki/lighthouse)[Lighthouse](/wiki/lighthouse)
CLI Approach:
**CLI Approach:**
InstallLighthouseglobally via npm:
[Lighthouse](/wiki/lighthouse)
```
npm install -g lighthouse
```
`npm install -g lighthouse`
RunLighthousein headless mode to test a URL and output the results to a JSON file:
[Lighthouse](/wiki/lighthouse)
```
lighthouse https://example.com --output=json --output-path=./report.json --chrome-flags="--headless"
```
`lighthouse https://example.com --output=json --output-path=./report.json --chrome-flags="--headless"`
Node Module Approach:
**Node Module Approach:**
InstallLighthouseas a dev dependency:
[Lighthouse](/wiki/lighthouse)
```
npm install --save-dev lighthouse
```
`npm install --save-dev lighthouse`
Create a script to launch Chrome and runLighthouseprogrammatically:
[Lighthouse](/wiki/lighthouse)
```
const lighthouse = require('lighthouse');
const chromeLauncher = require('chrome-launcher');

async function runLighthouse(url, opts, config = null) {
  const chrome = await chromeLauncher.launch({ chromeFlags: opts.chromeFlags });
  opts.port = chrome.port;
  const results = await lighthouse(url, opts, config);
  await chrome.kill();
  return results.lhr;
}

const options = {
  chromeFlags: ['--headless'],
  output: 'json'
};

runLighthouse('https://example.com', options)
  .then(results => {
    // Process Lighthouse results here
  });
```
`const lighthouse = require('lighthouse');
const chromeLauncher = require('chrome-launcher');

async function runLighthouse(url, opts, config = null) {
  const chrome = await chromeLauncher.launch({ chromeFlags: opts.chromeFlags });
  opts.port = chrome.port;
  const results = await lighthouse(url, opts, config);
  await chrome.kill();
  return results.lhr;
}

const options = {
  chromeFlags: ['--headless'],
  output: 'json'
};

runLighthouse('https://example.com', options)
  .then(results => {
    // Process Lighthouse results here
  });`
Continuous Integration:
**Continuous Integration:**
IncorporateLighthouseinto CI pipelines usingLighthouseCI. Set up a.lighthouserc.jsconfiguration file and addLighthouseCI commands to your CI configuration:
[Lighthouse](/wiki/lighthouse)[Lighthouse](/wiki/lighthouse)`.lighthouserc.js`[Lighthouse](/wiki/lighthouse)
```
lhci autorun --config=.lighthouserc.js
```
`lhci autorun --config=.lighthouserc.js`
This will run audits against the specified URLs during each commit or pull request, ensuring that code changes do not degrade the quality of the application. Use theLighthouseCI server for historical tracking and asserting performance budgets.
[Lighthouse](/wiki/lighthouse)
To run aLighthouseaudit:
[Lighthouse](/wiki/lighthouse)1. Open Google Chromeand navigate to the page you want to audit.
2. Access Developer Toolsby pressingCtrl+Shift+I(orCmd+Option+Ion Mac), or right-clicking the page and selecting "Inspect".
3. Click on theLighthousetab within the Developer Tools panel. If it's not visible, you may need to click on the>>icon to find it.
4. Select the categoriesyou wish to audit (Performance, Accessibility, Best Practices, SEO, and Progressive Web App).
5. Choose thedevice type(mobile or desktop) for the simulation.
6. (Optional) Click onAdvanced Settingsto adjust throttling options or to block certain URLs during the audit.
7. Click on the"Generate report"button to start the audit.
**Open Google Chrome****Access Developer Tools**`Ctrl+Shift+I``Cmd+Option+I`**Lighthouse**[Lighthouse](/wiki/lighthouse)`>>`**Select the categories****device type****Advanced Settings****"Generate report"**
Lighthousewill now run a series of tests against the page and generate a report. Once the audit is complete, you'll be presented with a detailed report outlining the performance and quality of the page. You can use this report to identify areas for improvement.
[Lighthouse](/wiki/lighthouse)
Forautomated testingor continuous integration, you can useLighthouseCLI by installing it via npm:
[automated testing](/wiki/automated-testing)[Lighthouse](/wiki/lighthouse)
```
npm install -g lighthouse
```
`npm install -g lighthouse`
Then run the audit with:

```
lighthouse https://example.com --output json --output-path ./report.json
```
`lighthouse https://example.com --output json --output-path ./report.json`
Replacehttps://example.comwith your URL and adjust the output format and path as needed. This command will generate a JSON report that can be integrated into your CI/CD pipeline.
`https://example.com`
IntegratingLighthouseinto continuous integration (CI) processes ensures that performance, accessibility, and SEO standards are upheld with each code commit. To useLighthousein CI, follow these steps:
**Lighthouse**[Lighthouse](/wiki/lighthouse)[Lighthouse](/wiki/lighthouse)1. InstallLighthouseCI:npm install -g @lhci/cli
2. ConfigureLighthouseCIby creating a.lighthouserc.jsor.lighthouserc.jsonfile in your project root. Define the URLs to audit, the number of runs, and any other configurations.
3. Add aLighthouseCI stepin your CI pipeline. For example, in a GitHub Actions workflow, add a job that runsLighthouseCI:- name: Run Lighthouse CI
  run: lhci autorun
4. Set up assertionsto enforce performance budgets or specific audit thresholds. Fail the CI build if these are not met:"assertions": {
  "categories:performance": ["error", { "minScore": 0.9 }],
  "categories:accessibility": ["error", { "minScore": 0.9 }]
}
5. Store reportsfor historical comparison and tracking regressions. Use the--upload.targetoption to upload toLighthouseCI server or other storage solutions.
6. Automate the processto run on every pull request or push to specific branches, ensuring that new code meets the defined quality standards.

InstallLighthouseCI:
**InstallLighthouseCI**[Lighthouse](/wiki/lighthouse)
```
npm install -g @lhci/cli
```
`npm install -g @lhci/cli`
ConfigureLighthouseCIby creating a.lighthouserc.jsor.lighthouserc.jsonfile in your project root. Define the URLs to audit, the number of runs, and any other configurations.
**ConfigureLighthouseCI**[Lighthouse](/wiki/lighthouse)`.lighthouserc.js``.lighthouserc.json`
Add aLighthouseCI stepin your CI pipeline. For example, in a GitHub Actions workflow, add a job that runsLighthouseCI:
**Add aLighthouseCI step**[Lighthouse](/wiki/lighthouse)[Lighthouse](/wiki/lighthouse)
```
- name: Run Lighthouse CI
  run: lhci autorun
```
`- name: Run Lighthouse CI
  run: lhci autorun`
Set up assertionsto enforce performance budgets or specific audit thresholds. Fail the CI build if these are not met:
**Set up assertions**
```
"assertions": {
  "categories:performance": ["error", { "minScore": 0.9 }],
  "categories:accessibility": ["error", { "minScore": 0.9 }]
}
```
`"assertions": {
  "categories:performance": ["error", { "minScore": 0.9 }],
  "categories:accessibility": ["error", { "minScore": 0.9 }]
}`
Store reportsfor historical comparison and tracking regressions. Use the--upload.targetoption to upload toLighthouseCI server or other storage solutions.
**Store reports**`--upload.target`[Lighthouse](/wiki/lighthouse)
Automate the processto run on every pull request or push to specific branches, ensuring that new code meets the defined quality standards.
**Automate the process**
By integratingLighthouseinto CI, you create afeedback loopthat alerts developers to potential issues early, maintaining a high standard for your web application's user experience.
[Lighthouse](/wiki/lighthouse)**feedback loop**
To configureLighthousefor custom audits, you need to create custom audit definitions and gatherers. Here's a concise guide:
**Lighthouse**[Lighthouse](/wiki/lighthouse)1. Create a Custom Gatherer:A gatherer collects information from the page. Extend theGathererclass from Lighthouse.const { Gatherer } = require('lighthouse');

class CustomGatherer extends Gatherer {
  afterPass(options) {
    // Collect data and return it
  }
}

module.exports = CustomGatherer;
2. Develop a Custom Audit:Audits use the data collected by gatherers. Extend theAuditclass.const { Audit } = require('lighthouse');

class CustomAudit extends Audit {
  static get meta() {
    return {
      id: 'custom-audit-id',
      title: 'Custom Audit',
      failureTitle: 'Custom Audit Failed',
      description: 'Description of your custom audit',
      requiredArtifacts: ['CustomGatherer'],
    };
  }

  static audit(artifacts) {
    const loadMetrics = artifacts.CustomGatherer;
    // Perform audit logic and return a score
    return {
      score: Number(loadMetrics < threshold),
    };
  }
}

module.exports = CustomAudit;
3. Add toLighthouseConfig:Include your custom gatherer and audit in the Lighthouse configuration.module.exports = {
  passes: [{
    passName: 'defaultPass',
    gatherers: [
      'path/to/customgatherer',
    ],
  }],
  audits: [
    'path/to/customaudit',
  ],
  categories: {
    customCategory: {
      title: 'Custom Category',
      description: 'Includes custom audits',
      auditRefs: [
        { id: 'custom-audit-id', weight: 1 },
      ],
    },
  },
};
4. RunLighthousewith your custom config:lighthouse https://example.com --config-path=path/to/custom-config.js

Create a Custom Gatherer:
**Create a Custom Gatherer**- A gatherer collects information from the page. Extend theGathererclass from Lighthouse.
`Gatherer`
```
const { Gatherer } = require('lighthouse');

class CustomGatherer extends Gatherer {
  afterPass(options) {
    // Collect data and return it
  }
}

module.exports = CustomGatherer;
```
`const { Gatherer } = require('lighthouse');

class CustomGatherer extends Gatherer {
  afterPass(options) {
    // Collect data and return it
  }
}

module.exports = CustomGatherer;`
Develop a Custom Audit:
**Develop a Custom Audit**- Audits use the data collected by gatherers. Extend theAuditclass.
`Audit`
```
const { Audit } = require('lighthouse');

class CustomAudit extends Audit {
  static get meta() {
    return {
      id: 'custom-audit-id',
      title: 'Custom Audit',
      failureTitle: 'Custom Audit Failed',
      description: 'Description of your custom audit',
      requiredArtifacts: ['CustomGatherer'],
    };
  }

  static audit(artifacts) {
    const loadMetrics = artifacts.CustomGatherer;
    // Perform audit logic and return a score
    return {
      score: Number(loadMetrics < threshold),
    };
  }
}

module.exports = CustomAudit;
```
`const { Audit } = require('lighthouse');

class CustomAudit extends Audit {
  static get meta() {
    return {
      id: 'custom-audit-id',
      title: 'Custom Audit',
      failureTitle: 'Custom Audit Failed',
      description: 'Description of your custom audit',
      requiredArtifacts: ['CustomGatherer'],
    };
  }

  static audit(artifacts) {
    const loadMetrics = artifacts.CustomGatherer;
    // Perform audit logic and return a score
    return {
      score: Number(loadMetrics < threshold),
    };
  }
}

module.exports = CustomAudit;`
Add toLighthouseConfig:
**Add toLighthouseConfig**[Lighthouse](/wiki/lighthouse)- Include your custom gatherer and audit in the Lighthouse configuration.

```
module.exports = {
  passes: [{
    passName: 'defaultPass',
    gatherers: [
      'path/to/customgatherer',
    ],
  }],
  audits: [
    'path/to/customaudit',
  ],
  categories: {
    customCategory: {
      title: 'Custom Category',
      description: 'Includes custom audits',
      auditRefs: [
        { id: 'custom-audit-id', weight: 1 },
      ],
    },
  },
};
```
`module.exports = {
  passes: [{
    passName: 'defaultPass',
    gatherers: [
      'path/to/customgatherer',
    ],
  }],
  audits: [
    'path/to/customaudit',
  ],
  categories: {
    customCategory: {
      title: 'Custom Category',
      description: 'Includes custom audits',
      auditRefs: [
        { id: 'custom-audit-id', weight: 1 },
      ],
    },
  },
};`
RunLighthousewith your custom config:
**RunLighthouse**[Lighthouse](/wiki/lighthouse)
```
lighthouse https://example.com --config-path=path/to/custom-config.js
```
`lighthouse https://example.com --config-path=path/to/custom-config.js`
Remember to handle exceptions and edge cases in your gatherer and audit logic to ensure robustness.

#### Results and Interpretation
- How are Lighthouse scores calculated?Lighthousescores are calculated based on a series of audits that fall into five categories:Performance,Accessibility,Best Practices,SEO, andProgressive Web App. Each category has a set of audits with individual tests. The scores from these tests are then aggregated into a score for each category.Performancescore is heavily weighted by speed metrics such as First Contentful Paint (FCP), Speed Index, Largest Contentful Paint (LCP), Time to Interactive (TTI), Total Blocking Time (TBT), and Cumulative Layout Shift (CLS). These metrics reflect the user's experience in terms of loading, interactivity, and visual stability.Accessibilityaudits check for common issues that may prevent users from accessing content due to disability. This includes proper use of HTML elements, ARIA attributes, color contrast ratios, and navigation.Best Practicesscore is derived from tests that check for modern web development standards, including HTTPS usage, correct image aspect ratios, and avoidance of deprecatedAPIs.SEOscore evaluates elements that affect a site's visibility to search engines, like meta tags, hreflang tags, and descriptive link text.Progressive Web Appscore assesses the readiness of a web app to deliver app-like experiences, looking at factors like service worker registration, web app manifests, and responsiveness to different screen sizes.Each category score is a weighted average of its audit scores. The overallLighthousescore is a weighted average of the five category scores, withPerformancetypically having the greatest weight. Scores range from 0 to 100, with higher scores indicating better adherence to web development best practices.
- What do the different Lighthouse audit categories mean?Lighthouseaudit categories are benchmarks that evaluate various aspects of web app quality. Each category represents a core area of user experience and technical performance:Performance: Measures the speed and efficiency of the site. Metrics include First Contentful Paint, Speed Index, and Time to Interactive.Accessibility: Assesses how well the site can be used by people with disabilities. It checks for proper use of ARIA attributes, screen reader support, and navigation accessibility.Best Practices: Evaluates the use of modern web development practices. This includes checks for HTTPS usage, correct image aspect ratios, and avoidance of deprecatedAPIs.SEO: Analyzes the site's potential to be indexed by search engines. It looks at mobile-friendliness, content best practices, and metadata presence.Progressive Web App (PWA): Determines the site's adherence to PWA standards. It checks for service worker registration, a valid web app manifest, and aresponsive design.Each category provides specific, actionable insights. For instance, thePerformancecategory can highlight opportunities to lazy-load offscreen images, whileAccessibilitymight suggest improvements for screen reader users. These insights guide engineers in optimizing their web apps for better user experiences and technical robustness.
- How do you interpret Lighthouse reports?InterpretingLighthousereports involves analyzing the data provided in each audit category to identify areas for improvement in your web application. After running aLighthouseaudit, you'll receive a report with scores inPerformance,Accessibility,Best Practices,SEO, andProgressive Web App.Performance: Look at metrics likeFirst Contentful Paint (FCP),Speed Index,Largest Contentful Paint (LCP),Time to Interactive (TTI),Total Blocking Time (TBT), andCumulative Layout Shift (CLS). These metrics give insights into the user-perceived loading experience and interactivity.Accessibility: Review issues that may prevent users with disabilities from accessing content. This includes missing alt text, improper ARIA attributes, and incorrect semantic HTML usage.Best Practices: Examine warnings and errors that could impact the application's reliability and security, such as using HTTPS, avoiding deprecatedAPIs, and ensuring correct image aspect ratios.SEO: Check for factors that could affect your site's search engine ranking, including mobile-friendliness, content best practices, and metadata presence.Progressive Web App: Evaluate your app against PWA criteria, focusing on aspects like fast load times, aresponsive design, and a working offline mode.For each audit,Lighthouseprovides:Ascore(0-100) indicating the quality of the page for that category.Color-coded metrics(green for good, orange for needs improvement, red for poor).Actionable recommendationsfor improving your score.Use the detailed suggestions to prioritize fixes and enhancements. Addressreditems first as they represent the most critical issues, followed byorange, and thengreento fine-tune performance. Implement changes, re-runLighthouse, and compare reports to track progress.
- What actions can be taken based on Lighthouse audit results?Based onLighthouseaudit results, several actions can be taken to improve the quality and performance of a web application:Optimize images: Compress and properly format images to reduce load times.Minify CSS, JavaScript, and HTML: Remove unnecessary characters without changing functionality to decrease file sizes.Leverage browser caching: Set appropriate cache headers to minimize repeat load times for returning users.Eliminate render-blocking resources: Defer non-critical CSS and JavaScript to speed up the first paint.Use lazy loading: Load images and iframes on demand to reduce initial load time.Improve server response times: Optimize server configuration, use a content delivery network (CDN), or upgrade hosting if necessary.Remove unused code: Detect and purge dead code to reduce file sizes and complexity.Enable compression: Use Gzip or Brotli to compress text-based resources.Implement HTTP/2: Take advantage of multiplexing and server push features for faster load times.Prioritize above-the-fold content: Structure HTML to load the most important content first.Accessibility enhancements: Address issues that affect users with disabilities, like color contrast and keyboard navigation.SEO improvements: Ensure meta tags are present and descriptive, and that content is crawlable.Apply these actions iteratively, integrating them into your CI/CD pipeline for continuous improvement. Regularly re-audit withLighthouseto measure progress and identify new optimization opportunities.
- How can you improve a low Lighthouse score?Improving a lowLighthousescore involves optimizing various aspects of your web application. Here are some strategies:Optimize Images: Compress images without losing quality using tools like ImageOptim or services like TinyPNG.Minify CSS, JavaScript, and HTML: Use tools like UglifyJS, cssnano, or HTMLMinifier to reduce file size.Enable Compression: Use Gzip or Brotli on your server to compress resources.Leverage Browser Caching: Set appropriateCache-Controlheaders for assets.Remove Render-Blocking Resources: Inline critical CSS, defer non-critical JavaScript, or useasyncattribute.Use Efficient CSS Selectors: Avoid complex selectors that can slow down page rendering.Minimize Main-Thread Work: Profile your JavaScript and optimize long tasks that block the main thread.Reduce JavaScript Payloads: Split code using dynamic imports and remove unused code with tree shaking.Implement Lazy Loading: Load images or modules only when they are needed.Optimize Web Fonts: Usefont-display: swapto minimize render-blocking, and consider subsetting fonts.Preconnect to Required Origins: Use<link rel="preconnect">to establish early connections to important third-party domains.Use HTTP/2: Serve resources over HTTP/2 for better multiplexing and parallelism.Prioritize Content: UsePriority Hintsor theloadingattribute to prioritize loading of key resources.Audit Third-Party Code: Remove or optimize third-party scripts that are not critical.Apply these optimizations iteratively and monitor theLighthousescore after each change to understand their impact.

Lighthousescores are calculated based on a series of audits that fall into five categories:Performance,Accessibility,Best Practices,SEO, andProgressive Web App. Each category has a set of audits with individual tests. The scores from these tests are then aggregated into a score for each category.
[Lighthouse](/wiki/lighthouse)**Performance****Accessibility****Best Practices****SEO****Progressive Web App**
Performancescore is heavily weighted by speed metrics such as First Contentful Paint (FCP), Speed Index, Largest Contentful Paint (LCP), Time to Interactive (TTI), Total Blocking Time (TBT), and Cumulative Layout Shift (CLS). These metrics reflect the user's experience in terms of loading, interactivity, and visual stability.
**Performance**
Accessibilityaudits check for common issues that may prevent users from accessing content due to disability. This includes proper use of HTML elements, ARIA attributes, color contrast ratios, and navigation.
**Accessibility**
Best Practicesscore is derived from tests that check for modern web development standards, including HTTPS usage, correct image aspect ratios, and avoidance of deprecatedAPIs.
**Best Practices**[APIs](/wiki/api)
SEOscore evaluates elements that affect a site's visibility to search engines, like meta tags, hreflang tags, and descriptive link text.
**SEO**
Progressive Web Appscore assesses the readiness of a web app to deliver app-like experiences, looking at factors like service worker registration, web app manifests, and responsiveness to different screen sizes.
**Progressive Web App**
Each category score is a weighted average of its audit scores. The overallLighthousescore is a weighted average of the five category scores, withPerformancetypically having the greatest weight. Scores range from 0 to 100, with higher scores indicating better adherence to web development best practices.
[Lighthouse](/wiki/lighthouse)**Performance**
Lighthouseaudit categories are benchmarks that evaluate various aspects of web app quality. Each category represents a core area of user experience and technical performance:
[Lighthouse](/wiki/lighthouse)- Performance: Measures the speed and efficiency of the site. Metrics include First Contentful Paint, Speed Index, and Time to Interactive.
- Accessibility: Assesses how well the site can be used by people with disabilities. It checks for proper use of ARIA attributes, screen reader support, and navigation accessibility.
- Best Practices: Evaluates the use of modern web development practices. This includes checks for HTTPS usage, correct image aspect ratios, and avoidance of deprecatedAPIs.
- SEO: Analyzes the site's potential to be indexed by search engines. It looks at mobile-friendliness, content best practices, and metadata presence.
- Progressive Web App (PWA): Determines the site's adherence to PWA standards. It checks for service worker registration, a valid web app manifest, and aresponsive design.

Performance: Measures the speed and efficiency of the site. Metrics include First Contentful Paint, Speed Index, and Time to Interactive.
**Performance**
Accessibility: Assesses how well the site can be used by people with disabilities. It checks for proper use of ARIA attributes, screen reader support, and navigation accessibility.
**Accessibility**
Best Practices: Evaluates the use of modern web development practices. This includes checks for HTTPS usage, correct image aspect ratios, and avoidance of deprecatedAPIs.
**Best Practices**[APIs](/wiki/api)
SEO: Analyzes the site's potential to be indexed by search engines. It looks at mobile-friendliness, content best practices, and metadata presence.
**SEO**
Progressive Web App (PWA): Determines the site's adherence to PWA standards. It checks for service worker registration, a valid web app manifest, and aresponsive design.
**Progressive Web App (PWA)**[responsive design](/wiki/responsive-design)
Each category provides specific, actionable insights. For instance, thePerformancecategory can highlight opportunities to lazy-load offscreen images, whileAccessibilitymight suggest improvements for screen reader users. These insights guide engineers in optimizing their web apps for better user experiences and technical robustness.
**Performance****Accessibility**
InterpretingLighthousereports involves analyzing the data provided in each audit category to identify areas for improvement in your web application. After running aLighthouseaudit, you'll receive a report with scores inPerformance,Accessibility,Best Practices,SEO, andProgressive Web App.
[Lighthouse](/wiki/lighthouse)[Lighthouse](/wiki/lighthouse)**Performance****Accessibility****Best Practices****SEO****Progressive Web App**
Performance: Look at metrics likeFirst Contentful Paint (FCP),Speed Index,Largest Contentful Paint (LCP),Time to Interactive (TTI),Total Blocking Time (TBT), andCumulative Layout Shift (CLS). These metrics give insights into the user-perceived loading experience and interactivity.
**Performance****First Contentful Paint (FCP)****Speed Index****Largest Contentful Paint (LCP)****Time to Interactive (TTI)****Total Blocking Time (TBT)****Cumulative Layout Shift (CLS)**
Accessibility: Review issues that may prevent users with disabilities from accessing content. This includes missing alt text, improper ARIA attributes, and incorrect semantic HTML usage.
**Accessibility**
Best Practices: Examine warnings and errors that could impact the application's reliability and security, such as using HTTPS, avoiding deprecatedAPIs, and ensuring correct image aspect ratios.
**Best Practices**[APIs](/wiki/api)
SEO: Check for factors that could affect your site's search engine ranking, including mobile-friendliness, content best practices, and metadata presence.
**SEO**
Progressive Web App: Evaluate your app against PWA criteria, focusing on aspects like fast load times, aresponsive design, and a working offline mode.
**Progressive Web App**[responsive design](/wiki/responsive-design)
For each audit,Lighthouseprovides:
[Lighthouse](/wiki/lighthouse)- Ascore(0-100) indicating the quality of the page for that category.
- Color-coded metrics(green for good, orange for needs improvement, red for poor).
- Actionable recommendationsfor improving your score.
**score****Color-coded metrics****Actionable recommendations**
Use the detailed suggestions to prioritize fixes and enhancements. Addressreditems first as they represent the most critical issues, followed byorange, and thengreento fine-tune performance. Implement changes, re-runLighthouse, and compare reports to track progress.
**red****orange****green**[Lighthouse](/wiki/lighthouse)
Based onLighthouseaudit results, several actions can be taken to improve the quality and performance of a web application:
[Lighthouse](/wiki/lighthouse)- Optimize images: Compress and properly format images to reduce load times.
- Minify CSS, JavaScript, and HTML: Remove unnecessary characters without changing functionality to decrease file sizes.
- Leverage browser caching: Set appropriate cache headers to minimize repeat load times for returning users.
- Eliminate render-blocking resources: Defer non-critical CSS and JavaScript to speed up the first paint.
- Use lazy loading: Load images and iframes on demand to reduce initial load time.
- Improve server response times: Optimize server configuration, use a content delivery network (CDN), or upgrade hosting if necessary.
- Remove unused code: Detect and purge dead code to reduce file sizes and complexity.
- Enable compression: Use Gzip or Brotli to compress text-based resources.
- Implement HTTP/2: Take advantage of multiplexing and server push features for faster load times.
- Prioritize above-the-fold content: Structure HTML to load the most important content first.
- Accessibility enhancements: Address issues that affect users with disabilities, like color contrast and keyboard navigation.
- SEO improvements: Ensure meta tags are present and descriptive, and that content is crawlable.
**Optimize images****Minify CSS, JavaScript, and HTML****Leverage browser caching****Eliminate render-blocking resources****Use lazy loading****Improve server response times****Remove unused code****Enable compression****Implement HTTP/2****Prioritize above-the-fold content****Accessibility enhancements****SEO improvements**
Apply these actions iteratively, integrating them into your CI/CD pipeline for continuous improvement. Regularly re-audit withLighthouseto measure progress and identify new optimization opportunities.
[Lighthouse](/wiki/lighthouse)
Improving a lowLighthousescore involves optimizing various aspects of your web application. Here are some strategies:
[Lighthouse](/wiki/lighthouse)- Optimize Images: Compress images without losing quality using tools like ImageOptim or services like TinyPNG.
- Minify CSS, JavaScript, and HTML: Use tools like UglifyJS, cssnano, or HTMLMinifier to reduce file size.
- Enable Compression: Use Gzip or Brotli on your server to compress resources.
- Leverage Browser Caching: Set appropriateCache-Controlheaders for assets.
- Remove Render-Blocking Resources: Inline critical CSS, defer non-critical JavaScript, or useasyncattribute.
- Use Efficient CSS Selectors: Avoid complex selectors that can slow down page rendering.
- Minimize Main-Thread Work: Profile your JavaScript and optimize long tasks that block the main thread.
- Reduce JavaScript Payloads: Split code using dynamic imports and remove unused code with tree shaking.
- Implement Lazy Loading: Load images or modules only when they are needed.
- Optimize Web Fonts: Usefont-display: swapto minimize render-blocking, and consider subsetting fonts.
- Preconnect to Required Origins: Use<link rel="preconnect">to establish early connections to important third-party domains.
- Use HTTP/2: Serve resources over HTTP/2 for better multiplexing and parallelism.
- Prioritize Content: UsePriority Hintsor theloadingattribute to prioritize loading of key resources.
- Audit Third-Party Code: Remove or optimize third-party scripts that are not critical.
**Optimize Images****Minify CSS, JavaScript, and HTML****Enable Compression****Leverage Browser Caching**`Cache-Control`**Remove Render-Blocking Resources**`async`**Use Efficient CSS Selectors****Minimize Main-Thread Work****Reduce JavaScript Payloads****Implement Lazy Loading****Optimize Web Fonts**`font-display: swap`**Preconnect to Required Origins**`<link rel="preconnect">`**Use HTTP/2****Prioritize Content**`Priority Hints``loading`**Audit Third-Party Code**
Apply these optimizations iteratively and monitor theLighthousescore after each change to understand their impact.
[Lighthouse](/wiki/lighthouse)
#### Advanced Concepts
- What is Lighthouse CI and how does it work?LighthouseCI is an open-source, automated tool for improving the quality of web pages and apps. It integrates with continuous integration (CI) systems to runLighthouseaudits on every commit, providing immediate feedback on potential regressions in performance, accessibility, SEO, and best practices.How it works:Installation:LighthouseCI is installed as an npm package.npm install -g @lhci/cliConfiguration: Create a.lighthouserc.jsor.lighthouserc.jsonfile to configure the audits.module.exports = {
  ci: {
    collect: {
      /* ... */
    },
    assert: {
      /* ... */
    },
    upload: {
      /* ... */
    },
  },
};Running Audits: Use theLighthouseCI CLI to run audits against a built version of your app.lhci autorunAssertions: Define assertions for performance metrics and other audit scores.LighthouseCI will fail the CI build if assertions don't meet the specified thresholds.Reports: Results are displayed in the CI output, and detailed reports can be uploaded to theLighthouseCI server or other hosting solutions for further analysis.Integration:LighthouseCI can be integrated into popular CI services like GitHub Actions, Travis CI, and Jenkins, ensuring that performance and quality checks are part of the development workflow.LighthouseCI ensures that performance and quality are continuously monitored, helping to prevent regressions and maintain high standards across updates.
- How can you use Lighthouse for performance budgeting?Lighthousecan be instrumental in implementing and enforcing aperformance budgetfor your web applications. A performance budget is a set of limits on certain metrics that affect site performance, such as the size of images, scripts, and CSS files.To useLighthousefor performance budgeting, follow these steps:Define your performance budget. Decide on the metrics and thresholds you want to enforce, such as maximum page load time, total image size, or number of HTTP requests.Create aLighthouseconfiguration file. In a JSON file, specify your performance budget constraints. For example:{
  "extends": "lighthouse:default",
  "settings": {
    "budgets": [{
      "resourceSizes": [
        {
          "resourceType": "script",
          "budget": 125
        },
        {
          "resourceType": "total",
          "budget": 300
        }
      ],
      "resourceCounts": [
        {
          "resourceType": "third-party",
          "budget": 10
        }
      ]
    }]
  }
}RunLighthousewith your config. Use the CLI to run Lighthouse with your configuration file:lighthouse https://example.com --budget-path=./path-to-your-budget.jsonReview the output. Lighthouse will include a section in the report that indicates whether your site stays within the defined budgets. If it exceeds any budget, Lighthouse provides details on the overages.By integrating this process into yourCI/CD pipeline, you can automatically check that every build complies with your performance budget, ensuring that performance regressions are caught and addressed early in the development process.
- What is the role of Lighthouse in Progressive Web Apps (PWAs)?Lighthouseplays a crucial role in evaluating and improving the quality of Progressive Web Apps (PWAs) by providing a set of audits that specifically target PWA features and best practices. It assesses PWAs against a baseline of expectations for modern web applications, ensuring they are fast, reliable, and engaging.For PWAs,Lighthousechecks for:Service Worker: Verifies if a service worker is registered and that it allows for offline use.Web App Manifest: Ensures the presence of a manifest file with appropriate icons, theme colors, and display settings for a full-screen, standalone user experience.HTTPS: Confirms the app is served over a secure connection, which is a prerequisite for many PWA features.Redirects: Checks that navigations are not redirected, which can slow down the app.Splash Screen: Assesses if a custom splash screen is provided during the load, improving the user experience.Theming: Evaluates consistency in theming colors for the address bar and the splash screen.Viewport Configuration: Ensures the viewport is properly set for responsive design.User Engagement: Measures the ability to prompt users to install the web app to their home screens.By integratingLighthouseinto thetest automationprocess, engineers can automate the evaluation of these PWA-specific criteria, identify areas for improvement, and track progress over time. This ensures that PWAs meet high standards for performance, accessibility, and user experience, which are critical for user retention and satisfaction.
- How does Lighthouse handle JavaScript execution?Lighthousehandles JavaScript execution through aheadless Chrome browser. When aLighthouseaudit is initiated, it launches Chrome in headless mode, which allows it to programmatically interact with the page as a user might.Lighthousethen navigates to the target URL and waits for the page to load.During the loading process,Lighthouserecords the execution of JavaScripton the page. This includes the parsing and execution time of scripts, as well as the time it takes for asynchronous JavaScript tasks to complete.Lighthouseuses the Chrome DevTools Protocol to gather information about JavaScript execution, which includes:Script evaluation: Time spent parsing and compiling scripts.Task execution: Time spent executing script tasks.JavaScript boot-up time: Time taken for the page to become interactive, which is critical for understanding user experience.Lighthousealso simulates user interactions, if necessary, to trigger JavaScript execution that may be tied to user events. This ensures that the audit captures the performance impact of scripts that only execute on interaction.The data collected on JavaScript execution feeds into severalLighthouseaudits, such as:First Contentful Paint (FCP)Time to Interactive (TTI)Total Blocking Time (TBT)These metrics help assess the impact of JavaScript on the page's load performance and interactivity, which are crucial for understanding and improving the user experience.
- What are some common issues and solutions when using Lighthouse?Common issues withLighthouseand their solutions:Fluctuating Scores: Scores can vary between runs due to network conditions, cache state, or CPU throttling.Solution: RunLighthousemultiple times and average the scores for consistency.Large Assets: Unoptimized images or bulky scripts can negatively impact performance.Solution: Compress images, minify CSS/JS, and use lazy loading.Third-Party Scripts: External scripts can slow down your site.Solution: Use therel="preconnect"attribute for known hosts, defer non-critical scripts, or remove unnecessary third-party scripts.Cache Configuration: Improperly configured caching can lead to redundant data fetching.Solution: Set appropriateCache-Controlheaders for static assets.Accessibility Issues:Lighthousemight report accessibility concerns that are not immediately obvious.Solution: Review each issue, consult WCAG guidelines, and make necessary HTML/ARIA adjustments.SEO Shortcomings: Missing meta tags or improper semantics can affect SEO audits.Solution: Ensure proper use of semantic HTML and meta tags likedescription,viewport, and structured data.Progressive Web App Criteria:Lighthousemay indicate PWA features are missing.Solution: Implement a service worker, create a web app manifest, and ensure your app is served over HTTPS.Timeouts or Errors:Lighthousemight timeout or encounter errors when auditing.Solution: Check for server issues, ensure no browser extensions are interfering, and run the audit in incognito mode.Use the following command to runLighthouseheadlessly, which can help with consistency in automated environments:lighthouse <url> --chrome-flags="--headless"Remember to keep yourLighthouseversion updated to benefit from the latest checks andbugfixes.

LighthouseCI is an open-source, automated tool for improving the quality of web pages and apps. It integrates with continuous integration (CI) systems to runLighthouseaudits on every commit, providing immediate feedback on potential regressions in performance, accessibility, SEO, and best practices.
[Lighthouse](/wiki/lighthouse)[Lighthouse](/wiki/lighthouse)
How it works:
**How it works:**1. Installation:LighthouseCI is installed as an npm package.npm install -g @lhci/cli
2. Configuration: Create a.lighthouserc.jsor.lighthouserc.jsonfile to configure the audits.module.exports = {
  ci: {
    collect: {
      /* ... */
    },
    assert: {
      /* ... */
    },
    upload: {
      /* ... */
    },
  },
};
3. Running Audits: Use theLighthouseCI CLI to run audits against a built version of your app.lhci autorun
4. Assertions: Define assertions for performance metrics and other audit scores.LighthouseCI will fail the CI build if assertions don't meet the specified thresholds.
5. Reports: Results are displayed in the CI output, and detailed reports can be uploaded to theLighthouseCI server or other hosting solutions for further analysis.
6. Integration:LighthouseCI can be integrated into popular CI services like GitHub Actions, Travis CI, and Jenkins, ensuring that performance and quality checks are part of the development workflow.

Installation:LighthouseCI is installed as an npm package.
**Installation**[Lighthouse](/wiki/lighthouse)
```
npm install -g @lhci/cli
```
`npm install -g @lhci/cli`
Configuration: Create a.lighthouserc.jsor.lighthouserc.jsonfile to configure the audits.
**Configuration**`.lighthouserc.js``.lighthouserc.json`
```
module.exports = {
  ci: {
    collect: {
      /* ... */
    },
    assert: {
      /* ... */
    },
    upload: {
      /* ... */
    },
  },
};
```
`module.exports = {
  ci: {
    collect: {
      /* ... */
    },
    assert: {
      /* ... */
    },
    upload: {
      /* ... */
    },
  },
};`
Running Audits: Use theLighthouseCI CLI to run audits against a built version of your app.
**Running Audits**[Lighthouse](/wiki/lighthouse)
```
lhci autorun
```
`lhci autorun`
Assertions: Define assertions for performance metrics and other audit scores.LighthouseCI will fail the CI build if assertions don't meet the specified thresholds.
**Assertions**[Lighthouse](/wiki/lighthouse)
Reports: Results are displayed in the CI output, and detailed reports can be uploaded to theLighthouseCI server or other hosting solutions for further analysis.
**Reports**[Lighthouse](/wiki/lighthouse)
Integration:LighthouseCI can be integrated into popular CI services like GitHub Actions, Travis CI, and Jenkins, ensuring that performance and quality checks are part of the development workflow.
**Integration**[Lighthouse](/wiki/lighthouse)
LighthouseCI ensures that performance and quality are continuously monitored, helping to prevent regressions and maintain high standards across updates.
[Lighthouse](/wiki/lighthouse)
Lighthousecan be instrumental in implementing and enforcing aperformance budgetfor your web applications. A performance budget is a set of limits on certain metrics that affect site performance, such as the size of images, scripts, and CSS files.
[Lighthouse](/wiki/lighthouse)**performance budget**
To useLighthousefor performance budgeting, follow these steps:
[Lighthouse](/wiki/lighthouse)1. Define your performance budget. Decide on the metrics and thresholds you want to enforce, such as maximum page load time, total image size, or number of HTTP requests.
2. Create aLighthouseconfiguration file. In a JSON file, specify your performance budget constraints. For example:

Define your performance budget. Decide on the metrics and thresholds you want to enforce, such as maximum page load time, total image size, or number of HTTP requests.
**Define your performance budget**
Create aLighthouseconfiguration file. In a JSON file, specify your performance budget constraints. For example:
**Create aLighthouseconfiguration file**[Lighthouse](/wiki/lighthouse)
```
{
  "extends": "lighthouse:default",
  "settings": {
    "budgets": [{
      "resourceSizes": [
        {
          "resourceType": "script",
          "budget": 125
        },
        {
          "resourceType": "total",
          "budget": 300
        }
      ],
      "resourceCounts": [
        {
          "resourceType": "third-party",
          "budget": 10
        }
      ]
    }]
  }
}
```
`{
  "extends": "lighthouse:default",
  "settings": {
    "budgets": [{
      "resourceSizes": [
        {
          "resourceType": "script",
          "budget": 125
        },
        {
          "resourceType": "total",
          "budget": 300
        }
      ],
      "resourceCounts": [
        {
          "resourceType": "third-party",
          "budget": 10
        }
      ]
    }]
  }
}`1. RunLighthousewith your config. Use the CLI to run Lighthouse with your configuration file:
**RunLighthousewith your config**[Lighthouse](/wiki/lighthouse)
```
lighthouse https://example.com --budget-path=./path-to-your-budget.json
```
`lighthouse https://example.com --budget-path=./path-to-your-budget.json`1. Review the output. Lighthouse will include a section in the report that indicates whether your site stays within the defined budgets. If it exceeds any budget, Lighthouse provides details on the overages.
**Review the output**
By integrating this process into yourCI/CD pipeline, you can automatically check that every build complies with your performance budget, ensuring that performance regressions are caught and addressed early in the development process.
**CI/CD pipeline**
Lighthouseplays a crucial role in evaluating and improving the quality of Progressive Web Apps (PWAs) by providing a set of audits that specifically target PWA features and best practices. It assesses PWAs against a baseline of expectations for modern web applications, ensuring they are fast, reliable, and engaging.
[Lighthouse](/wiki/lighthouse)
For PWAs,Lighthousechecks for:
[Lighthouse](/wiki/lighthouse)- Service Worker: Verifies if a service worker is registered and that it allows for offline use.
- Web App Manifest: Ensures the presence of a manifest file with appropriate icons, theme colors, and display settings for a full-screen, standalone user experience.
- HTTPS: Confirms the app is served over a secure connection, which is a prerequisite for many PWA features.
- Redirects: Checks that navigations are not redirected, which can slow down the app.
- Splash Screen: Assesses if a custom splash screen is provided during the load, improving the user experience.
- Theming: Evaluates consistency in theming colors for the address bar and the splash screen.
- Viewport Configuration: Ensures the viewport is properly set for responsive design.
- User Engagement: Measures the ability to prompt users to install the web app to their home screens.
**Service Worker****Web App Manifest****HTTPS****Redirects****Splash Screen****Theming****Viewport Configuration****User Engagement**
By integratingLighthouseinto thetest automationprocess, engineers can automate the evaluation of these PWA-specific criteria, identify areas for improvement, and track progress over time. This ensures that PWAs meet high standards for performance, accessibility, and user experience, which are critical for user retention and satisfaction.
[Lighthouse](/wiki/lighthouse)[test automation](/wiki/test-automation)
Lighthousehandles JavaScript execution through aheadless Chrome browser. When aLighthouseaudit is initiated, it launches Chrome in headless mode, which allows it to programmatically interact with the page as a user might.Lighthousethen navigates to the target URL and waits for the page to load.
[Lighthouse](/wiki/lighthouse)**headless Chrome browser**[Lighthouse](/wiki/lighthouse)[Lighthouse](/wiki/lighthouse)
During the loading process,Lighthouserecords the execution of JavaScripton the page. This includes the parsing and execution time of scripts, as well as the time it takes for asynchronous JavaScript tasks to complete.Lighthouseuses the Chrome DevTools Protocol to gather information about JavaScript execution, which includes:
[Lighthouse](/wiki/lighthouse)**records the execution of JavaScript**[Lighthouse](/wiki/lighthouse)- Script evaluation: Time spent parsing and compiling scripts.
- Task execution: Time spent executing script tasks.
- JavaScript boot-up time: Time taken for the page to become interactive, which is critical for understanding user experience.
**Script evaluation****Task execution****JavaScript boot-up time**
Lighthousealso simulates user interactions, if necessary, to trigger JavaScript execution that may be tied to user events. This ensures that the audit captures the performance impact of scripts that only execute on interaction.
[Lighthouse](/wiki/lighthouse)
The data collected on JavaScript execution feeds into severalLighthouseaudits, such as:
[Lighthouse](/wiki/lighthouse)- First Contentful Paint (FCP)
- Time to Interactive (TTI)
- Total Blocking Time (TBT)
**First Contentful Paint (FCP)****Time to Interactive (TTI)****Total Blocking Time (TBT)**
These metrics help assess the impact of JavaScript on the page's load performance and interactivity, which are crucial for understanding and improving the user experience.

Common issues withLighthouseand their solutions:
[Lighthouse](/wiki/lighthouse)- Fluctuating Scores: Scores can vary between runs due to network conditions, cache state, or CPU throttling.Solution: RunLighthousemultiple times and average the scores for consistency.
- Large Assets: Unoptimized images or bulky scripts can negatively impact performance.Solution: Compress images, minify CSS/JS, and use lazy loading.
- Third-Party Scripts: External scripts can slow down your site.Solution: Use therel="preconnect"attribute for known hosts, defer non-critical scripts, or remove unnecessary third-party scripts.
- Cache Configuration: Improperly configured caching can lead to redundant data fetching.Solution: Set appropriateCache-Controlheaders for static assets.
- Accessibility Issues:Lighthousemight report accessibility concerns that are not immediately obvious.Solution: Review each issue, consult WCAG guidelines, and make necessary HTML/ARIA adjustments.
- SEO Shortcomings: Missing meta tags or improper semantics can affect SEO audits.Solution: Ensure proper use of semantic HTML and meta tags likedescription,viewport, and structured data.
- Progressive Web App Criteria:Lighthousemay indicate PWA features are missing.Solution: Implement a service worker, create a web app manifest, and ensure your app is served over HTTPS.
- Timeouts or Errors:Lighthousemight timeout or encounter errors when auditing.Solution: Check for server issues, ensure no browser extensions are interfering, and run the audit in incognito mode.

Fluctuating Scores: Scores can vary between runs due to network conditions, cache state, or CPU throttling.Solution: RunLighthousemultiple times and average the scores for consistency.
**Fluctuating Scores****Solution**[Lighthouse](/wiki/lighthouse)
Large Assets: Unoptimized images or bulky scripts can negatively impact performance.Solution: Compress images, minify CSS/JS, and use lazy loading.
**Large Assets****Solution**
Third-Party Scripts: External scripts can slow down your site.Solution: Use therel="preconnect"attribute for known hosts, defer non-critical scripts, or remove unnecessary third-party scripts.
**Third-Party Scripts****Solution**`rel="preconnect"`
Cache Configuration: Improperly configured caching can lead to redundant data fetching.Solution: Set appropriateCache-Controlheaders for static assets.
**Cache Configuration****Solution**`Cache-Control`
Accessibility Issues:Lighthousemight report accessibility concerns that are not immediately obvious.Solution: Review each issue, consult WCAG guidelines, and make necessary HTML/ARIA adjustments.
**Accessibility Issues**[Lighthouse](/wiki/lighthouse)**Solution**
SEO Shortcomings: Missing meta tags or improper semantics can affect SEO audits.Solution: Ensure proper use of semantic HTML and meta tags likedescription,viewport, and structured data.
**SEO Shortcomings****Solution**`description``viewport`
Progressive Web App Criteria:Lighthousemay indicate PWA features are missing.Solution: Implement a service worker, create a web app manifest, and ensure your app is served over HTTPS.
**Progressive Web App Criteria**[Lighthouse](/wiki/lighthouse)**Solution**
Timeouts or Errors:Lighthousemight timeout or encounter errors when auditing.Solution: Check for server issues, ensure no browser extensions are interfering, and run the audit in incognito mode.
**Timeouts or Errors**[Lighthouse](/wiki/lighthouse)**Solution**
Use the following command to runLighthouseheadlessly, which can help with consistency in automated environments:
[Lighthouse](/wiki/lighthouse)
```
lighthouse <url> --chrome-flags="--headless"
```
`lighthouse <url> --chrome-flags="--headless"`
Remember to keep yourLighthouseversion updated to benefit from the latest checks andbugfixes.
[Lighthouse](/wiki/lighthouse)[bug](/wiki/bug)
