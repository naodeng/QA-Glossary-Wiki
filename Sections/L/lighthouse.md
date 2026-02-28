# Lighthouse


<!-- TOC START -->
- [See also:](#see-also)
- [Questions about Lighthouse ?](#questions-about-lighthouse)
  - [Basics and Importance](#basics-and-importance)
    - [What is Lighthouse?](#what-is-lighthouse)
    - [Why is Lighthouse important in software automation?](#why-is-lighthouse-important-in-software-automation)
    - [What are the key features of Lighthouse?](#what-are-the-key-features-of-lighthouse)
    - [How does Lighthouse differ from other performance auditing tools?](#how-does-lighthouse-differ-from-other-performance-auditing-tools)
    - [What types of audits does Lighthouse perform?](#what-types-of-audits-does-lighthouse-perform)
  - [Usage and Implementation](#usage-and-implementation)
    - [How do you use Lighthouse in Chrome?](#how-do-you-use-lighthouse-in-chrome)
    - [How can Lighthouse be used for automated testing?](#how-can-lighthouse-be-used-for-automated-testing)
    - [What are the steps to run a Lighthouse audit?](#what-are-the-steps-to-run-a-lighthouse-audit)
    - [How can you use Lighthouse in continuous integration processes?](#how-can-you-use-lighthouse-in-continuous-integration-processes)
    - [How can you configure Lighthouse for custom audits?](#how-can-you-configure-lighthouse-for-custom-audits)
  - [Results and Interpretation](#results-and-interpretation)
    - [How are Lighthouse scores calculated?](#how-are-lighthouse-scores-calculated)
    - [What do the different Lighthouse audit categories mean?](#what-do-the-different-lighthouse-audit-categories-mean)
    - [How do you interpret Lighthouse reports?](#how-do-you-interpret-lighthouse-reports)
    - [What actions can be taken based on Lighthouse audit results?](#what-actions-can-be-taken-based-on-lighthouse-audit-results)
    - [How can you improve a low Lighthouse score?](#how-can-you-improve-a-low-lighthouse-score)
  - [Advanced Concepts](#advanced-concepts)
    - [What is Lighthouse CI and how does it work?](#what-is-lighthouse-ci-and-how-does-it-work)
    - [How can you use Lighthouse for performance budgeting?](#how-can-you-use-lighthouse-for-performance-budgeting)
    - [What is the role of Lighthouse in Progressive Web Apps (PWAs)?](#what-is-the-role-of-lighthouse-in-progressive-web-apps-pwas)
    - [How does Lighthouse handle JavaScript execution?](#how-does-lighthouse-handle-javascript-execution)
    - [What are some common issues and solutions when using Lighthouse?](#what-are-some-common-issues-and-solutions-when-using-lighthouse)
<!-- TOC END -->

Lighthouse

is an open-source, automated tool developed by Google for improving the quality of web pages. It provides audits for performance, accessibility, progressive web apps, SEO, and other aspects of web page quality. By running

Lighthouse

against a web page, developers and testers can obtain a set of actionable recommendations and insights that help in optimizing the user experience and overall effectiveness of the website.

## See also:

- [Wikipedia](https://en.wikipedia.org/wiki/Google_Lighthouse)

## Questions about Lighthouse ?

### Basics and Importance

#### What is Lighthouse?

  [Lighthouse](../L/lighthouse.md) is an **open-source**, **automated tool** for improving the quality of web pages. It can be run against any web page, public or requiring authentication. [Lighthouse](../L/lighthouse.md) audits for performance, accessibility, progressive web apps, SEO, and more, providing a well-rounded view of the quality and effectiveness of a web page.
  To use [Lighthouse](../L/lighthouse.md) in **Chrome**, navigate to the page you want to audit, open **DevTools**, and click on the **[Lighthouse](../L/lighthouse.md)** tab. Select the audits you want to run, and then click the **Generate report** button. [Lighthouse](../L/lighthouse.md) will run the selected audits against the page, then generate a report on how well the page did.
  For **[automated testing](../A/automated-testing.md)**, [Lighthouse](../L/lighthouse.md) can be integrated into **continuous integration** systems. It can be run as a Node module, as a command line tool, or programmatically as part of a custom build process. [Lighthouse](../L/lighthouse.md) CI is a set of commands that make it easier to use [Lighthouse](../L/lighthouse.md) for continuous integration.
  Scores are calculated based on the performance metrics and heuristics. Each metric is scored individually, and then the scores are combined into an overall score.
  Improving a low [Lighthouse](../L/lighthouse.md) score involves addressing the specific feedback provided in the report. This could include optimizing images, minifying CSS and JavaScript, implementing lazy loading, improving accessibility features, and more.
  For **JavaScript execution**, [Lighthouse](../L/lighthouse.md) simulates a mid-tier device, even when run on a powerful desktop machine, to create consistent, real-world conditions.
  Common issues when using [Lighthouse](../L/lighthouse.md) include flaky performance metrics, which can be mitigated by running the audit multiple times and considering median values.

#### Why is Lighthouse important in software automation?

  [Lighthouse](../L/lighthouse.md) is crucial in software [test automation](../T/test-automation.md) for its ability to **integrate performance and quality checks** into the development and deployment pipeline. It provides **automated audits** for performance, accessibility, progressive web apps, SEO, and best practices, which are essential for maintaining high-quality web applications.
  By incorporating [Lighthouse](../L/lighthouse.md) into [automated testing](../A/automated-testing.md), engineers can ensure that any code changes are evaluated against these metrics, catching regressions or issues early in the development cycle. This is particularly important for **continuous integration (CI)** and **continuous deployment (CD)** environments, where automated tests must provide quick feedback on the potential impact of code changes.
  [Lighthouse](../L/lighthouse.md)'s role extends to **performance budgeting**, helping teams set and adhere to performance goals. It can be run headlessly, making it suitable for **server-side automation** and integration into CI/CD pipelines. The tool's **configurability** allows for custom audits tailored to specific needs, and its **scoring system** provides a quantifiable measure of a site's quality attributes.
  Moreover, [Lighthouse](../L/lighthouse.md)'s **reports** offer actionable insights, which are invaluable for engineers looking to optimize their web applications. The ability to automate these audits and integrate them into the development workflow makes [Lighthouse](../L/lighthouse.md) an important tool for maintaining and improving the quality and user experience of web applications in an automated and efficient manner.

#### What are the key features of Lighthouse?

  Key features of **[Lighthouse](../L/lighthouse.md)** include:

  - **Performance Metrics**: [Lighthouse](../L/lighthouse.md) provides detailed metrics such as First Contentful Paint (FCP), Speed Index, Largest Contentful Paint (LCP), Time to Interactive (TTI), Total Blocking Time (TBT), and Cumulative Layout Shift (CLS).
  - **Accessibility Audits**: It evaluates the accessibility of a web page against the Web Content Accessibility Guidelines (WCAG) and suggests improvements.
  - **Best Practices**: [Lighthouse](../L/lighthouse.md) checks for adherence to best practices in web development, such as HTTPS usage, correct image aspect ratios, and avoiding deprecated [APIs](../A/api.md).
  - **SEO Audits**: It assesses elements that affect a page's search engine ranking, including meta tags, hreflang tags, and descriptive link text.
  - **Progressive Web App (PWA) Assessment**: [Lighthouse](../L/lighthouse.md) can validate various aspects of PWAs, ensuring they meet certain criteria for reliability, performance, and engagement.
  - **Custom Audits**: Developers can extend [Lighthouse](../L/lighthouse.md) by writing custom audits to check for specific requirements or standards relevant to their projects.
  - **CLI and Programmable [API](../A/api.md)**: [Lighthouse](../L/lighthouse.md) can be run via command line or programmatically through its [API](../A/api.md), allowing integration into automated workflows and CI/CD pipelines.
  - **Configurability**: Users can configure [Lighthouse](../L/lighthouse.md) runs by specifying categories to audit, throttling settings, and other runtime options.
  - **Reporting**: After an audit, [Lighthouse](../L/lighthouse.md) generates a report with scores in each category, detailed explanations, and actionable recommendations for improvement.
  - **Extensibility**: [Lighthouse](../L/lighthouse.md) is open-source and can be extended or customized to fit specific testing needs, and it integrates with other tools like [Lighthouse](../L/lighthouse.md) CI for continuous testing.
  These features make [Lighthouse](../L/lighthouse.md) a versatile tool for web developers and [test automation](../T/test-automation.md) engineers focused on improving the quality of web applications.

  - **Performance Metrics**: [Lighthouse](../L/lighthouse.md) provides detailed metrics such as First Contentful Paint (FCP), Speed Index, Largest Contentful Paint (LCP), Time to Interactive (TTI), Total Blocking Time (TBT), and Cumulative Layout Shift (CLS).
  - **Accessibility Audits**: It evaluates the accessibility of a web page against the Web Content Accessibility Guidelines (WCAG) and suggests improvements.
  - **Best Practices**: [Lighthouse](../L/lighthouse.md) checks for adherence to best practices in web development, such as HTTPS usage, correct image aspect ratios, and avoiding deprecated [APIs](../A/api.md).
  - **SEO Audits**: It assesses elements that affect a page's search engine ranking, including meta tags, hreflang tags, and descriptive link text.
  - **Progressive Web App (PWA) Assessment**: [Lighthouse](../L/lighthouse.md) can validate various aspects of PWAs, ensuring they meet certain criteria for reliability, performance, and engagement.
  - **Custom Audits**: Developers can extend [Lighthouse](../L/lighthouse.md) by writing custom audits to check for specific requirements or standards relevant to their projects.
  - **CLI and Programmable [API](../A/api.md)**: [Lighthouse](../L/lighthouse.md) can be run via command line or programmatically through its [API](../A/api.md), allowing integration into automated workflows and CI/CD pipelines.
  - **Configurability**: Users can configure [Lighthouse](../L/lighthouse.md) runs by specifying categories to audit, throttling settings, and other runtime options.
  - **Reporting**: After an audit, [Lighthouse](../L/lighthouse.md) generates a report with scores in each category, detailed explanations, and actionable recommendations for improvement.
  - **Extensibility**: [Lighthouse](../L/lighthouse.md) is open-source and can be extended or customized to fit specific testing needs, and it integrates with other tools like [Lighthouse](../L/lighthouse.md) CI for continuous testing.

#### How does Lighthouse differ from other performance auditing tools?

  [Lighthouse](../L/lighthouse.md) distinguishes itself from other performance auditing tools through its **integration with the Chrome Developer Tools** and its **emphasis on the user experience** metrics, such as the Core Web Vitals. While tools like WebPageTest provide detailed waterfalls and network information, [Lighthouse](../L/lighthouse.md) focuses on providing a **holistic view** of web performance, accessibility, best practices, SEO, and progressive web app metrics.
  Unlike some tools that require complex [setup](../S/setup.md) or server-side integration, [Lighthouse](../L/lighthouse.md) is **easily accessible** and can be run from the command line, as a Node module, or directly in the browser, making it highly versatile for different workflows. It also offers **custom audit capabilities** through its flexible configuration options.
  [Lighthouse](../L/lighthouse.md)'s **actionable reports** with clear scoring and recommendations stand out, guiding developers on how to improve performance and user experience. It's particularly useful for simulating a page load on a mobile network and a mid-tier device, which is a common [use case](../U/use-case.md) not always covered by other tools.
  Moreover, [Lighthouse](../L/lighthouse.md) is **open-source** and maintained by Google, ensuring regular updates that reflect the latest web development best practices and standards. This contrasts with some proprietary tools that may not be as transparent or up-to-date with web standards.
  Lastly, [Lighthouse](../L/lighthouse.md)'s ability to be integrated into **CI/CD pipelines** through [Lighthouse](../L/lighthouse.md) CI makes it a powerful option for automating performance checks and ensuring that performance standards are met before deployment.

#### What types of audits does Lighthouse perform?

  [Lighthouse](../L/lighthouse.md) performs audits across **five categories**: **Performance**, **Accessibility**, **Best Practices**, **SEO**, and **Progressive Web App (PWA)**. Each category encompasses various checks:

  - **Performance**: Evaluates metrics like First Contentful Paint, Speed Index, and Time to Interactive, focusing on user-perceived loading experience and interactivity.
  - **Accessibility**: Checks for common issues that may prevent users from accessing content, such as missing alt text for images, improper ARIA attributes, and incorrect semantic HTML elements.
  - **Best Practices**: Looks for modern web development practices, including HTTPS usage, correct image aspect ratios, and avoidance of deprecated [APIs](../A/api.md).
  - **SEO**: Assesses elements that affect a page's visibility to search engines, like meta descriptions, hreflang links, and legible font sizes.
  - **PWA**: Verifies the presence of a service worker, a web app manifest, and other criteria that enable a web app to be installed on a device's home screen and function offline.
  Each audit provides specific, actionable feedback and is scored individually, contributing to an overall category score. [Lighthouse](../L/lighthouse.md) also offers **opportunities** and **diagnostics** to help identify areas for improvement and understand underlying issues. These audits can be extended or customized for specific [use cases](../U/use-case.md) through [Lighthouse](../L/lighthouse.md) configuration.

  - **Performance**: Evaluates metrics like First Contentful Paint, Speed Index, and Time to Interactive, focusing on user-perceived loading experience and interactivity.
  - **Accessibility**: Checks for common issues that may prevent users from accessing content, such as missing alt text for images, improper ARIA attributes, and incorrect semantic HTML elements.
  - **Best Practices**: Looks for modern web development practices, including HTTPS usage, correct image aspect ratios, and avoidance of deprecated [APIs](../A/api.md).
  - **SEO**: Assesses elements that affect a page's visibility to search engines, like meta descriptions, hreflang links, and legible font sizes.
  - **PWA**: Verifies the presence of a service worker, a web app manifest, and other criteria that enable a web app to be installed on a device's home screen and function offline.

### Usage and Implementation

#### How do you use Lighthouse in Chrome?

  To use **[Lighthouse](../L/lighthouse.md)** in Chrome for [test automation](../T/test-automation.md), follow these steps:

  1. Open Chrome Developer Tools by pressing
    `Ctrl+Shift+I`
    (or
    `Cmd+Option+I`
    on Mac).

  2. Navigate to the
    **[Lighthouse](../L/lighthouse.md)**
    tab.

  3. Choose the desired audit categories (Performance, Accessibility, Best Practices, SEO, and Progressive Web App).
  4. Select the appropriate device type (Mobile or Desktop) for the simulation.
  5. Click on
    **Generate report**
    to start the audit.
  For automation purposes, you can run [Lighthouse](../L/lighthouse.md) programmatically using the command line or as a Node module. Here's a basic example using [Node.js](../N/node-js.md):

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
  For continuous integration, you can use **[Lighthouse](../L/lighthouse.md) CI** which provides commands to run audits against a website and assert if the scores meet your requirements. It can be integrated into your CI pipeline using configuration files and CLI commands.
  Remember to review the audit results and make necessary code or configuration changes to improve the scores. Automate the process by integrating it into your build and deployment pipeline to ensure continuous performance monitoring.

  1. Open Chrome Developer Tools by pressing
    `Ctrl+Shift+I`
    (or
    `Cmd+Option+I`
    on Mac).

  2. Navigate to the
    **[Lighthouse](../L/lighthouse.md)**
    tab.

  3. Choose the desired audit categories (Performance, Accessibility, Best Practices, SEO, and Progressive Web App).
  4. Select the appropriate device type (Mobile or Desktop) for the simulation.
  5. Click on
    **Generate report**
    to start the audit.

#### How can Lighthouse be used for automated testing?

  [Lighthouse](../L/lighthouse.md) can be integrated into [automated testing](../A/automated-testing.md) workflows to ensure web applications meet performance, accessibility, best practices, and SEO standards. To automate [Lighthouse](../L/lighthouse.md) tests, you can use the [Lighthouse](../L/lighthouse.md) CLI or the [Lighthouse](../L/lighthouse.md) Node module.
  **CLI Approach:**
  Install [Lighthouse](../L/lighthouse.md) globally via npm:

  ```
  npm install -g lighthouse
  ```
  Run [Lighthouse](../L/lighthouse.md) in headless mode to test a URL and output the results to a JSON file:

  ```
  lighthouse https://example.com --output=json --output-path=./report.json --chrome-flags="--headless"
  ```
  **Node Module Approach:**
  Install [Lighthouse](../L/lighthouse.md) as a dev dependency:

  ```
  npm install --save-dev lighthouse
  ```
  Create a script to launch Chrome and run [Lighthouse](../L/lighthouse.md) programmatically:

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
  **Continuous Integration:**
  Incorporate [Lighthouse](../L/lighthouse.md) into CI pipelines using [Lighthouse](../L/lighthouse.md) CI. Set up a `.lighthouserc.js` configuration file and add [Lighthouse](../L/lighthouse.md) CI commands to your CI configuration:

  ```
  lhci autorun --config=.lighthouserc.js
  ```
  This will run audits against the specified URLs during each commit or pull request, ensuring that code changes do not degrade the quality of the application. Use the [Lighthouse](../L/lighthouse.md) CI server for historical tracking and asserting performance budgets.

#### What are the steps to run a Lighthouse audit?

  To run a [Lighthouse](../L/lighthouse.md) audit:

  1. **Open Google Chrome**
    and navigate to the page you want to audit.

  2. **Access Developer Tools**
    by pressing
    `Ctrl+Shift+I`
    (or
    `Cmd+Option+I`
    on Mac), or right-clicking the page and selecting "Inspect".

  3. Click on the
    **[Lighthouse](../L/lighthouse.md)**
    tab within the Developer Tools panel. If it's not visible, you may need to click on the
    `>>`
    icon to find it.

  4. **Select the categories**
    you wish to audit (Performance, Accessibility, Best Practices, SEO, and Progressive Web App).

  5. Choose the
    **device type**
    (mobile or desktop) for the simulation.

  6. (Optional) Click on
    **Advanced Settings**
    to adjust throttling options or to block certain URLs during the audit.

  7. Click on the
    **"Generate report"**
    button to start the audit.
  [Lighthouse](../L/lighthouse.md) will now run a series of tests against the page and generate a report. Once the audit is complete, you'll be presented with a detailed report outlining the performance and quality of the page. You can use this report to identify areas for improvement.
  For [automated testing](../A/automated-testing.md) or continuous integration, you can use [Lighthouse](../L/lighthouse.md) CLI by installing it via npm:

  ```
  npm install -g lighthouse
  ```
  Then run the audit with:

  ```
  lighthouse https://example.com --output json --output-path ./report.json
  ```
  Replace `https://example.com` with your URL and adjust the output format and path as needed. This command will generate a JSON report that can be integrated into your CI/CD pipeline.

  1. **Open Google Chrome**
    and navigate to the page you want to audit.

  2. **Access Developer Tools**
    by pressing
    `Ctrl+Shift+I`
    (or
    `Cmd+Option+I`
    on Mac), or right-clicking the page and selecting "Inspect".

  3. Click on the
    **[Lighthouse](../L/lighthouse.md)**
    tab within the Developer Tools panel. If it's not visible, you may need to click on the
    `>>`
    icon to find it.

  4. **Select the categories**
    you wish to audit (Performance, Accessibility, Best Practices, SEO, and Progressive Web App).

  5. Choose the
    **device type**
    (mobile or desktop) for the simulation.

  6. (Optional) Click on
    **Advanced Settings**
    to adjust throttling options or to block certain URLs during the audit.

  7. Click on the
    **"Generate report"**
    button to start the audit.

#### How can you use Lighthouse in continuous integration processes?

  Integrating **[Lighthouse](../L/lighthouse.md)** into continuous integration (CI) processes ensures that performance, accessibility, and SEO standards are upheld with each code commit. To use [Lighthouse](../L/lighthouse.md) in CI, follow these steps:

  1. **Install [Lighthouse](../L/lighthouse.md) CI**:

    ```
    npm install -g @lhci/cli
    ```

  2. **Configure [Lighthouse](../L/lighthouse.md) CI** by creating a `.lighthouserc.js` or `.lighthouserc.json` file in your project root. Define the URLs to audit, the number of runs, and any other configurations.
  3. **Add a [Lighthouse](../L/lighthouse.md) CI step** in your CI pipeline. For example, in a GitHub Actions workflow, add a job that runs [Lighthouse](../L/lighthouse.md) CI:

    ```
    - name: Run Lighthouse CI
      run: lhci autorun
    ```

  4. **Set up assertions** to enforce performance budgets or specific audit thresholds. Fail the CI build if these are not met:

    ```
    "assertions": {
      "categories:performance": ["error", { "minScore": 0.9 }],
      "categories:accessibility": ["error", { "minScore": 0.9 }]
    }
    ```

  5. **Store reports** for historical comparison and tracking regressions. Use the `--upload.target` option to upload to [Lighthouse](../L/lighthouse.md) CI server or other storage solutions.
  6. **Automate the process** to run on every pull request or push to specific branches, ensuring that new code meets the defined quality standards.
  By integrating [Lighthouse](../L/lighthouse.md) into CI, you create a **feedback loop** that alerts developers to potential issues early, maintaining a high standard for your web application's user experience.

  1. **Install [Lighthouse](../L/lighthouse.md) CI**:

    ```
    npm install -g @lhci/cli
    ```

  2. **Configure [Lighthouse](../L/lighthouse.md) CI** by creating a `.lighthouserc.js` or `.lighthouserc.json` file in your project root. Define the URLs to audit, the number of runs, and any other configurations.
  3. **Add a [Lighthouse](../L/lighthouse.md) CI step** in your CI pipeline. For example, in a GitHub Actions workflow, add a job that runs [Lighthouse](../L/lighthouse.md) CI:

    ```
    - name: Run Lighthouse CI
      run: lhci autorun
    ```

  4. **Set up assertions** to enforce performance budgets or specific audit thresholds. Fail the CI build if these are not met:

    ```
    "assertions": {
      "categories:performance": ["error", { "minScore": 0.9 }],
      "categories:accessibility": ["error", { "minScore": 0.9 }]
    }
    ```

  5. **Store reports** for historical comparison and tracking regressions. Use the `--upload.target` option to upload to [Lighthouse](../L/lighthouse.md) CI server or other storage solutions.
  6. **Automate the process** to run on every pull request or push to specific branches, ensuring that new code meets the defined quality standards.

#### How can you configure Lighthouse for custom audits?

  To configure **[Lighthouse](../L/lighthouse.md)** for custom audits, you need to create custom audit definitions and gatherers. Here's a concise guide:

  1. **Create a Custom Gatherer**:

    ```
    const { Gatherer } = require('lighthouse');
    class CustomGatherer extends Gatherer {
      afterPass(options) {
        // Collect data and return it
      }
    }
    module.exports = CustomGatherer;
    ```

    - A gatherer collects information from the page. Extend the
      `Gatherer`
      class from Lighthouse.

    - A gatherer collects information from the page. Extend the
      `Gatherer`
      class from Lighthouse.

  2. **Develop a Custom Audit**:

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

    - Audits use the data collected by gatherers. Extend the
      `Audit`
      class.

    - Audits use the data collected by gatherers. Extend the
      `Audit`
      class.

  3. **Add to [Lighthouse](../L/lighthouse.md) Config**:

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

    - Include your custom gatherer and audit in the Lighthouse configuration.
    - Include your custom gatherer and audit in the Lighthouse configuration.
  4. **Run [Lighthouse](../L/lighthouse.md)** with your custom config:

    ```
    lighthouse https://example.com --config-path=path/to/custom-config.js
    ```
  Remember to handle exceptions and edge cases in your gatherer and audit logic to ensure robustness.

  1. **Create a Custom Gatherer**:

    ```
    const { Gatherer } = require('lighthouse');
    class CustomGatherer extends Gatherer {
      afterPass(options) {
        // Collect data and return it
      }
    }
    module.exports = CustomGatherer;
    ```

    - A gatherer collects information from the page. Extend the
      `Gatherer`
      class from Lighthouse.

    - A gatherer collects information from the page. Extend the
      `Gatherer`
      class from Lighthouse.

  2. **Develop a Custom Audit**:

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

    - Audits use the data collected by gatherers. Extend the
      `Audit`
      class.

    - Audits use the data collected by gatherers. Extend the
      `Audit`
      class.

  3. **Add to [Lighthouse](../L/lighthouse.md) Config**:

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

    - Include your custom gatherer and audit in the Lighthouse configuration.
    - Include your custom gatherer and audit in the Lighthouse configuration.
  4. **Run [Lighthouse](../L/lighthouse.md)** with your custom config:

    ```
    lighthouse https://example.com --config-path=path/to/custom-config.js
    ```

### Results and Interpretation

#### How are Lighthouse scores calculated?

  [Lighthouse](../L/lighthouse.md) scores are calculated based on a series of audits that fall into five categories: **Performance**, **Accessibility**, **Best Practices**, **SEO**, and **Progressive Web App**. Each category has a set of audits with individual tests. The scores from these tests are then aggregated into a score for each category.
  **Performance** score is heavily weighted by speed metrics such as First Contentful Paint (FCP), Speed Index, Largest Contentful Paint (LCP), Time to Interactive (TTI), Total Blocking Time (TBT), and Cumulative Layout Shift (CLS). These metrics reflect the user's experience in terms of loading, interactivity, and visual stability.
  **Accessibility** audits check for common issues that may prevent users from accessing content due to disability. This includes proper use of HTML elements, ARIA attributes, color contrast ratios, and navigation.
  **Best Practices** score is derived from tests that check for modern web development standards, including HTTPS usage, correct image aspect ratios, and avoidance of deprecated [APIs](../A/api.md).
  **SEO** score evaluates elements that affect a site's visibility to search engines, like meta tags, hreflang tags, and descriptive link text.
  **Progressive Web App** score assesses the readiness of a web app to deliver app-like experiences, looking at factors like service worker registration, web app manifests, and responsiveness to different screen sizes.
  Each category score is a weighted average of its audit scores. The overall [Lighthouse](../L/lighthouse.md) score is a weighted average of the five category scores, with **Performance** typically having the greatest weight. Scores range from 0 to 100, with higher scores indicating better adherence to web development best practices.

#### What do the different Lighthouse audit categories mean?

  [Lighthouse](../L/lighthouse.md) audit categories are benchmarks that evaluate various aspects of web app quality. Each category represents a core area of user experience and technical performance:

  - **Performance**: Measures the speed and efficiency of the site. Metrics include First Contentful Paint, Speed Index, and Time to Interactive.
  - **Accessibility**: Assesses how well the site can be used by people with disabilities. It checks for proper use of ARIA attributes, screen reader support, and navigation accessibility.
  - **Best Practices**: Evaluates the use of modern web development practices. This includes checks for HTTPS usage, correct image aspect ratios, and avoidance of deprecated [APIs](../A/api.md).
  - **SEO**: Analyzes the site's potential to be indexed by search engines. It looks at mobile-friendliness, content best practices, and metadata presence.
  - **Progressive Web App (PWA)**: Determines the site's adherence to PWA standards. It checks for service worker registration, a valid web app manifest, and a [responsive design](../R/responsive-design.md).
  Each category provides specific, actionable insights. For instance, the **Performance** category can highlight opportunities to lazy-load offscreen images, while **Accessibility** might suggest improvements for screen reader users. These insights guide engineers in optimizing their web apps for better user experiences and technical robustness.

  - **Performance**: Measures the speed and efficiency of the site. Metrics include First Contentful Paint, Speed Index, and Time to Interactive.
  - **Accessibility**: Assesses how well the site can be used by people with disabilities. It checks for proper use of ARIA attributes, screen reader support, and navigation accessibility.
  - **Best Practices**: Evaluates the use of modern web development practices. This includes checks for HTTPS usage, correct image aspect ratios, and avoidance of deprecated [APIs](../A/api.md).
  - **SEO**: Analyzes the site's potential to be indexed by search engines. It looks at mobile-friendliness, content best practices, and metadata presence.
  - **Progressive Web App (PWA)**: Determines the site's adherence to PWA standards. It checks for service worker registration, a valid web app manifest, and a [responsive design](../R/responsive-design.md).

#### How do you interpret Lighthouse reports?

  Interpreting [Lighthouse](../L/lighthouse.md) reports involves analyzing the data provided in each audit category to identify areas for improvement in your web application. After running a [Lighthouse](../L/lighthouse.md) audit, you'll receive a report with scores in **Performance**, **Accessibility**, **Best Practices**, **SEO**, and **Progressive Web App**.
  **Performance**: Look at metrics like **First Contentful Paint (FCP)**, **Speed Index**, **Largest Contentful Paint (LCP)**, **Time to Interactive (TTI)**, **Total Blocking Time (TBT)**, and **Cumulative Layout Shift (CLS)**. These metrics give insights into the user-perceived loading experience and interactivity.
  **Accessibility**: Review issues that may prevent users with disabilities from accessing content. This includes missing alt text, improper ARIA attributes, and incorrect semantic HTML usage.
  **Best Practices**: Examine warnings and errors that could impact the application's reliability and security, such as using HTTPS, avoiding deprecated [APIs](../A/api.md), and ensuring correct image aspect ratios.
  **SEO**: Check for factors that could affect your site's search engine ranking, including mobile-friendliness, content best practices, and metadata presence.
  **Progressive Web App**: Evaluate your app against PWA criteria, focusing on aspects like fast load times, a [responsive design](../R/responsive-design.md), and a working offline mode.
  For each audit, [Lighthouse](../L/lighthouse.md) provides:

  - A
    **score**
    (0-100) indicating the quality of the page for that category.

  - **Color-coded metrics**
    (green for good, orange for needs improvement, red for poor).

  - **Actionable recommendations**
    for improving your score.
  Use the detailed suggestions to prioritize fixes and enhancements. Address **red** items first as they represent the most critical issues, followed by **orange**, and then **green** to fine-tune performance. Implement changes, re-run [Lighthouse](../L/lighthouse.md), and compare reports to track progress.

  - A
    **score**
    (0-100) indicating the quality of the page for that category.

  - **Color-coded metrics**
    (green for good, orange for needs improvement, red for poor).

  - **Actionable recommendations**
    for improving your score.

#### What actions can be taken based on Lighthouse audit results?

  Based on [Lighthouse](../L/lighthouse.md) audit results, several actions can be taken to improve the quality and performance of a web application:

  - **Optimize images** : Compress and properly format images to reduce load times.
  - **Minify CSS, JavaScript, and HTML** : Remove unnecessary characters without changing functionality to decrease file sizes.
  - **Leverage browser caching** : Set appropriate cache headers to minimize repeat load times for returning users.
  - **Eliminate render-blocking resources** : Defer non-critical CSS and JavaScript to speed up the first paint.
  - **Use lazy loading** : Load images and iframes on demand to reduce initial load time.
  - **Improve server response times** : Optimize server configuration, use a content delivery network (CDN), or upgrade hosting if necessary.
  - **Remove unused code** : Detect and purge dead code to reduce file sizes and complexity.
  - **Enable compression** : Use Gzip or Brotli to compress text-based resources.
  - **Implement HTTP/2** : Take advantage of multiplexing and server push features for faster load times.
  - **Prioritize above-the-fold content** : Structure HTML to load the most important content first.
  - **Accessibility enhancements** : Address issues that affect users with disabilities, like color contrast and keyboard navigation.
  - **SEO improvements** : Ensure meta tags are present and descriptive, and that content is crawlable.
  Apply these actions iteratively, integrating them into your CI/CD pipeline for continuous improvement. Regularly re-audit with [Lighthouse](../L/lighthouse.md) to measure progress and identify new optimization opportunities.

  - **Optimize images** : Compress and properly format images to reduce load times.
  - **Minify CSS, JavaScript, and HTML** : Remove unnecessary characters without changing functionality to decrease file sizes.
  - **Leverage browser caching** : Set appropriate cache headers to minimize repeat load times for returning users.
  - **Eliminate render-blocking resources** : Defer non-critical CSS and JavaScript to speed up the first paint.
  - **Use lazy loading** : Load images and iframes on demand to reduce initial load time.
  - **Improve server response times** : Optimize server configuration, use a content delivery network (CDN), or upgrade hosting if necessary.
  - **Remove unused code** : Detect and purge dead code to reduce file sizes and complexity.
  - **Enable compression** : Use Gzip or Brotli to compress text-based resources.
  - **Implement HTTP/2** : Take advantage of multiplexing and server push features for faster load times.
  - **Prioritize above-the-fold content** : Structure HTML to load the most important content first.
  - **Accessibility enhancements** : Address issues that affect users with disabilities, like color contrast and keyboard navigation.
  - **SEO improvements** : Ensure meta tags are present and descriptive, and that content is crawlable.

#### How can you improve a low Lighthouse score?

  Improving a low [Lighthouse](../L/lighthouse.md) score involves optimizing various aspects of your web application. Here are some strategies:

  - **Optimize Images** : Compress images without losing quality using tools like ImageOptim or services like TinyPNG.
  - **Minify CSS, JavaScript, and HTML** : Use tools like UglifyJS, cssnano, or HTMLMinifier to reduce file size.
  - **Enable Compression** : Use Gzip or Brotli on your server to compress resources.
  - **Leverage Browser Caching** : Set appropriate
    `Cache-Control`
    headers for assets.

  - **Remove Render-Blocking Resources** : Inline critical CSS, defer non-critical JavaScript, or use
    `async`
    attribute.

  - **Use Efficient CSS Selectors** : Avoid complex selectors that can slow down page rendering.
  - **Minimize Main-Thread Work** : Profile your JavaScript and optimize long tasks that block the main thread.
  - **Reduce JavaScript Payloads** : Split code using dynamic imports and remove unused code with tree shaking.
  - **Implement Lazy Loading** : Load images or modules only when they are needed.
  - **Optimize Web Fonts** : Use
    `font-display: swap`
    to minimize render-blocking, and consider subsetting fonts.

  - **Preconnect to Required Origins** : Use
    `<link rel="preconnect">`
    to establish early connections to important third-party domains.

  - **Use HTTP/2** : Serve resources over HTTP/2 for better multiplexing and parallelism.
  - **Prioritize Content** : Use
    `Priority Hints`
    or the
    `loading`
    attribute to prioritize loading of key resources.

  - **Audit Third-Party Code** : Remove or optimize third-party scripts that are not critical.
  Apply these optimizations iteratively and monitor the [Lighthouse](../L/lighthouse.md) score after each change to understand their impact.

  - **Optimize Images** : Compress images without losing quality using tools like ImageOptim or services like TinyPNG.
  - **Minify CSS, JavaScript, and HTML** : Use tools like UglifyJS, cssnano, or HTMLMinifier to reduce file size.
  - **Enable Compression** : Use Gzip or Brotli on your server to compress resources.
  - **Leverage Browser Caching** : Set appropriate
    `Cache-Control`
    headers for assets.

  - **Remove Render-Blocking Resources** : Inline critical CSS, defer non-critical JavaScript, or use
    `async`
    attribute.

  - **Use Efficient CSS Selectors** : Avoid complex selectors that can slow down page rendering.
  - **Minimize Main-Thread Work** : Profile your JavaScript and optimize long tasks that block the main thread.
  - **Reduce JavaScript Payloads** : Split code using dynamic imports and remove unused code with tree shaking.
  - **Implement Lazy Loading** : Load images or modules only when they are needed.
  - **Optimize Web Fonts** : Use
    `font-display: swap`
    to minimize render-blocking, and consider subsetting fonts.

  - **Preconnect to Required Origins** : Use
    `<link rel="preconnect">`
    to establish early connections to important third-party domains.

  - **Use HTTP/2** : Serve resources over HTTP/2 for better multiplexing and parallelism.
  - **Prioritize Content** : Use
    `Priority Hints`
    or the
    `loading`
    attribute to prioritize loading of key resources.

  - **Audit Third-Party Code** : Remove or optimize third-party scripts that are not critical.

### Advanced Concepts

#### What is Lighthouse CI and how does it work?

  [Lighthouse](../L/lighthouse.md) CI is an open-source, automated tool for improving the quality of web pages and apps. It integrates with continuous integration (CI) systems to run [Lighthouse](../L/lighthouse.md) audits on every commit, providing immediate feedback on potential regressions in performance, accessibility, SEO, and best practices.
  **How it works:**

  1. **Installation**: [Lighthouse](../L/lighthouse.md) CI is installed as an npm package.

    ```
    npm install -g @lhci/cli
    ```

  2. **Configuration**: Create a `.lighthouserc.js` or `.lighthouserc.json` file to configure the audits.

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

  3. **Running Audits**: Use the [Lighthouse](../L/lighthouse.md) CI CLI to run audits against a built version of your app.

    ```
    lhci autorun
    ```

  4. **Assertions**: Define assertions for performance metrics and other audit scores. [Lighthouse](../L/lighthouse.md) CI will fail the CI build if assertions don't meet the specified thresholds.
  5. **Reports**: Results are displayed in the CI output, and detailed reports can be uploaded to the [Lighthouse](../L/lighthouse.md) CI server or other hosting solutions for further analysis.
  6. **Integration**: [Lighthouse](../L/lighthouse.md) CI can be integrated into popular CI services like GitHub Actions, Travis CI, and Jenkins, ensuring that performance and quality checks are part of the development workflow.
  [Lighthouse](../L/lighthouse.md) CI ensures that performance and quality are continuously monitored, helping to prevent regressions and maintain high standards across updates.

  1. **Installation**: [Lighthouse](../L/lighthouse.md) CI is installed as an npm package.

    ```
    npm install -g @lhci/cli
    ```

  2. **Configuration**: Create a `.lighthouserc.js` or `.lighthouserc.json` file to configure the audits.

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

  3. **Running Audits**: Use the [Lighthouse](../L/lighthouse.md) CI CLI to run audits against a built version of your app.

    ```
    lhci autorun
    ```

  4. **Assertions**: Define assertions for performance metrics and other audit scores. [Lighthouse](../L/lighthouse.md) CI will fail the CI build if assertions don't meet the specified thresholds.
  5. **Reports**: Results are displayed in the CI output, and detailed reports can be uploaded to the [Lighthouse](../L/lighthouse.md) CI server or other hosting solutions for further analysis.
  6. **Integration**: [Lighthouse](../L/lighthouse.md) CI can be integrated into popular CI services like GitHub Actions, Travis CI, and Jenkins, ensuring that performance and quality checks are part of the development workflow.

#### How can you use Lighthouse for performance budgeting?

  [Lighthouse](../L/lighthouse.md) can be instrumental in implementing and enforcing a **performance budget** for your web applications. A performance budget is a set of limits on certain metrics that affect site performance, such as the size of images, scripts, and CSS files.
  To use [Lighthouse](../L/lighthouse.md) for performance budgeting, follow these steps:

  1. **Define your performance budget**. Decide on the metrics and thresholds you want to enforce, such as maximum page load time, total image size, or number of HTTP requests.
  2. **Create a [Lighthouse](../L/lighthouse.md) configuration file**. In a JSON file, specify your performance budget constraints. For example:

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

  1. **Run [Lighthouse](../L/lighthouse.md) with your config**
    . Use the CLI to run Lighthouse with your configuration file:

  ```
  lighthouse https://example.com --budget-path=./path-to-your-budget.json
  ```

  1. **Review the output**
    . Lighthouse will include a section in the report that indicates whether your site stays within the defined budgets. If it exceeds any budget, Lighthouse provides details on the overages.
  By integrating this process into your **CI/CD pipeline**, you can automatically check that every build complies with your performance budget, ensuring that performance regressions are caught and addressed early in the development process.

  1. **Define your performance budget**. Decide on the metrics and thresholds you want to enforce, such as maximum page load time, total image size, or number of HTTP requests.
  2. **Create a [Lighthouse](../L/lighthouse.md) configuration file**. In a JSON file, specify your performance budget constraints. For example:
  1. **Run [Lighthouse](../L/lighthouse.md) with your config**
    . Use the CLI to run Lighthouse with your configuration file:

  1. **Review the output**
    . Lighthouse will include a section in the report that indicates whether your site stays within the defined budgets. If it exceeds any budget, Lighthouse provides details on the overages.

#### What is the role of Lighthouse in Progressive Web Apps (PWAs)?

  [Lighthouse](../L/lighthouse.md) plays a crucial role in evaluating and improving the quality of Progressive Web Apps (PWAs) by providing a set of audits that specifically target PWA features and best practices. It assesses PWAs against a baseline of expectations for modern web applications, ensuring they are fast, reliable, and engaging.
  For PWAs, [Lighthouse](../L/lighthouse.md) checks for:

  - **Service Worker** : Verifies if a service worker is registered and that it allows for offline use.
  - **Web App Manifest** : Ensures the presence of a manifest file with appropriate icons, theme colors, and display settings for a full-screen, standalone user experience.
  - **HTTPS** : Confirms the app is served over a secure connection, which is a prerequisite for many PWA features.
  - **Redirects** : Checks that navigations are not redirected, which can slow down the app.
  - **Splash Screen** : Assesses if a custom splash screen is provided during the load, improving the user experience.
  - **Theming** : Evaluates consistency in theming colors for the address bar and the splash screen.
  - **Viewport Configuration** : Ensures the viewport is properly set for responsive design.
  - **User Engagement** : Measures the ability to prompt users to install the web app to their home screens.
  By integrating [Lighthouse](../L/lighthouse.md) into the [test automation](../T/test-automation.md) process, engineers can automate the evaluation of these PWA-specific criteria, identify areas for improvement, and track progress over time. This ensures that PWAs meet high standards for performance, accessibility, and user experience, which are critical for user retention and satisfaction.

  - **Service Worker** : Verifies if a service worker is registered and that it allows for offline use.
  - **Web App Manifest** : Ensures the presence of a manifest file with appropriate icons, theme colors, and display settings for a full-screen, standalone user experience.
  - **HTTPS** : Confirms the app is served over a secure connection, which is a prerequisite for many PWA features.
  - **Redirects** : Checks that navigations are not redirected, which can slow down the app.
  - **Splash Screen** : Assesses if a custom splash screen is provided during the load, improving the user experience.
  - **Theming** : Evaluates consistency in theming colors for the address bar and the splash screen.
  - **Viewport Configuration** : Ensures the viewport is properly set for responsive design.
  - **User Engagement** : Measures the ability to prompt users to install the web app to their home screens.

#### How does Lighthouse handle JavaScript execution?

  [Lighthouse](../L/lighthouse.md) handles JavaScript execution through a **headless Chrome browser**. When a [Lighthouse](../L/lighthouse.md) audit is initiated, it launches Chrome in headless mode, which allows it to programmatically interact with the page as a user might. [Lighthouse](../L/lighthouse.md) then navigates to the target URL and waits for the page to load.
  During the loading process, [Lighthouse](../L/lighthouse.md) **records the execution of JavaScript** on the page. This includes the parsing and execution time of scripts, as well as the time it takes for asynchronous JavaScript tasks to complete. [Lighthouse](../L/lighthouse.md) uses the Chrome DevTools Protocol to gather information about JavaScript execution, which includes:

  - **Script evaluation** : Time spent parsing and compiling scripts.
  - **Task execution** : Time spent executing script tasks.
  - **JavaScript boot-up time** : Time taken for the page to become interactive, which is critical for understanding user experience.
  [Lighthouse](../L/lighthouse.md) also simulates user interactions, if necessary, to trigger JavaScript execution that may be tied to user events. This ensures that the audit captures the performance impact of scripts that only execute on interaction.
  The data collected on JavaScript execution feeds into several [Lighthouse](../L/lighthouse.md) audits, such as:

  - **First Contentful Paint (FCP)**
  - **Time to Interactive (TTI)**
  - **Total Blocking Time (TBT)**
  These metrics help assess the impact of JavaScript on the page's load performance and interactivity, which are crucial for understanding and improving the user experience.

  - **Script evaluation** : Time spent parsing and compiling scripts.
  - **Task execution** : Time spent executing script tasks.
  - **JavaScript boot-up time** : Time taken for the page to become interactive, which is critical for understanding user experience.
  - **First Contentful Paint (FCP)**
  - **Time to Interactive (TTI)**
  - **Total Blocking Time (TBT)**

#### What are some common issues and solutions when using Lighthouse?

  Common issues with [Lighthouse](../L/lighthouse.md) and their solutions:

  - **Fluctuating Scores**: Scores can vary between runs due to network conditions, cache state, or CPU throttling. **Solution**: Run [Lighthouse](../L/lighthouse.md) multiple times and average the scores for consistency.
  - **Large Assets**: Unoptimized images or bulky scripts can negatively impact performance. **Solution**: Compress images, minify CSS/JS, and use lazy loading.
  - **Third-Party Scripts**: External scripts can slow down your site. **Solution**: Use the `rel="preconnect"` attribute for known hosts, defer non-critical scripts, or remove unnecessary third-party scripts.
  - **Cache Configuration**: Improperly configured caching can lead to redundant data fetching. **Solution**: Set appropriate `Cache-Control` headers for static assets.
  - **Accessibility Issues**: [Lighthouse](../L/lighthouse.md) might report accessibility concerns that are not immediately obvious. **Solution**: Review each issue, consult WCAG guidelines, and make necessary HTML/ARIA adjustments.
  - **SEO Shortcomings**: Missing meta tags or improper semantics can affect SEO audits. **Solution**: Ensure proper use of semantic HTML and meta tags like `description`, `viewport`, and structured data.
  - **Progressive Web App Criteria**: [Lighthouse](../L/lighthouse.md) may indicate PWA features are missing. **Solution**: Implement a service worker, create a web app manifest, and ensure your app is served over HTTPS.
  - **Timeouts or Errors**: [Lighthouse](../L/lighthouse.md) might timeout or encounter errors when auditing. **Solution**: Check for server issues, ensure no browser extensions are interfering, and run the audit in incognito mode.
  Use the following command to run [Lighthouse](../L/lighthouse.md) headlessly, which can help with consistency in automated environments:

  ```
  lighthouse <url> --chrome-flags="--headless"
  ```
  Remember to keep your [Lighthouse](../L/lighthouse.md) version updated to benefit from the latest checks and [bug](../B/bug.md) fixes.

  - **Fluctuating Scores**: Scores can vary between runs due to network conditions, cache state, or CPU throttling. **Solution**: Run [Lighthouse](../L/lighthouse.md) multiple times and average the scores for consistency.
  - **Large Assets**: Unoptimized images or bulky scripts can negatively impact performance. **Solution**: Compress images, minify CSS/JS, and use lazy loading.
  - **Third-Party Scripts**: External scripts can slow down your site. **Solution**: Use the `rel="preconnect"` attribute for known hosts, defer non-critical scripts, or remove unnecessary third-party scripts.
  - **Cache Configuration**: Improperly configured caching can lead to redundant data fetching. **Solution**: Set appropriate `Cache-Control` headers for static assets.
  - **Accessibility Issues**: [Lighthouse](../L/lighthouse.md) might report accessibility concerns that are not immediately obvious. **Solution**: Review each issue, consult WCAG guidelines, and make necessary HTML/ARIA adjustments.
  - **SEO Shortcomings**: Missing meta tags or improper semantics can affect SEO audits. **Solution**: Ensure proper use of semantic HTML and meta tags like `description`, `viewport`, and structured data.
  - **Progressive Web App Criteria**: [Lighthouse](../L/lighthouse.md) may indicate PWA features are missing. **Solution**: Implement a service worker, create a web app manifest, and ensure your app is served over HTTPS.
  - **Timeouts or Errors**: [Lighthouse](../L/lighthouse.md) might timeout or encounter errors when auditing. **Solution**: Check for server issues, ensure no browser extensions are interfering, and run the audit in incognito mode.
