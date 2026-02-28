# Postman


<!-- TOC START -->
- [Related Terms:](#related-terms)
  - [See also:](#see-also)
- [Questions about Postman ?](#questions-about-postman)
  - [Basics and Importance](#basics-and-importance)
    - [What is Postman and what is it used for?](#what-is-postman-and-what-is-it-used-for)
    - [Why is Postman important in software testing?](#why-is-postman-important-in-software-testing)
    - [What are the key features of Postman?](#what-are-the-key-features-of-postman)
    - [How does Postman improve the API development process?](#how-does-postman-improve-the-api-development-process)
  - [Working with Postman](#working-with-postman)
    - [How do you install and set up Postman?](#how-do-you-install-and-set-up-postman)
    - [How do you create a new request in Postman?](#how-do-you-create-a-new-request-in-postman)
    - [How do you send a request in Postman?](#how-do-you-send-a-request-in-postman)
    - [How do you save responses in Postman?](#how-do-you-save-responses-in-postman)
    - [How do you use variables in Postman?](#how-do-you-use-variables-in-postman)
  - [Advanced Features](#advanced-features)
    - [How do you use Postman for automated testing?](#how-do-you-use-postman-for-automated-testing)
    - [What is the Postman Collection Runner and how do you use it?](#what-is-the-postman-collection-runner-and-how-do-you-use-it)
    - [How do you use Postman's scripting capabilities?](#how-do-you-use-postmans-scripting-capabilities)
    - [What is Postman Monitors and how does it work?](#what-is-postman-monitors-and-how-does-it-work)
    - [How do you use Postman for performance testing?](#how-do-you-use-postman-for-performance-testing)
  - [Integration and Collaboration](#integration-and-collaboration)
    - [How do you share a Postman collection with others?](#how-do-you-share-a-postman-collection-with-others)
    - [How does Postman integrate with other tools and systems?](#how-does-postman-integrate-with-other-tools-and-systems)
    - [What is Postman's role in Continuous Integration (CI) and Continuous Deployment (CD)?](#what-is-postmans-role-in-continuous-integration-ci-and-continuous-deployment-cd)
    - [How do you use Postman in a team setting?](#how-do-you-use-postman-in-a-team-setting)
<!-- TOC END -->

Postman

is a widely-used software tool that facilitates

API

(Application Programming Interface) development and testing. It offers a user-friendly interface that allows developers and testers to send requests to and receive responses from web services. With

Postman

, users can create, save, and organize HTTP requests, test

APIs

by sending various request types (GET, POST, PUT, DELETE, etc.), and inspect the responses. Additional features include the ability to automate tests, create mock servers, and document

APIs

.

Postman

also provides collaboration capabilities for teams, enabling them to share collections of requests, environments, and other data. Over time,

Postman

has evolved from a simple

API testing

tool into a comprehensive

API

development environment.

## Related Terms:

- [API testing tool](../A/api-testing-tool.md)
- [Swagger](../S/swagger.md)

### See also:

- [Official Website](https://www.postman.com/)
- [Wikipedia](https://en.wikipedia.org/wiki/Postman_(software))

## Questions about Postman ?

### Basics and Importance

#### What is Postman and what is it used for?

  [Postman](../P/postman.md) is an **[API](../A/api.md) (Application Programming Interface) development tool** that simplifies the process of building, testing, and modifying [APIs](../A/api.md). It provides a user-friendly interface for sending HTTP requests to web services and viewing responses without the need for a dedicated client or writing custom code. [Postman](../P/postman.md) supports various HTTP methods such as GET, POST, PUT, DELETE, and includes features for setting headers, adding body data, and constructing query parameters.
  Developers and testers use [Postman](../P/postman.md) to **verify the behavior of [APIs](../A/api.md)**, ensuring they function as expected, return the correct data, and handle errors properly. It's also used to simulate [API](../A/api.md) requests to check how the server responds under different conditions. With its ability to save requests and responses, [Postman](../P/postman.md) facilitates the reuse and sharing of [API](../A/api.md) calls within teams or across projects.
  [Postman](../P/postman.md)'s functionality extends beyond [manual testing](../M/manual-testing.md). It can be used to **automate [test suites](../T/test-suite.md)** and integrate them into CI/CD pipelines, allowing for regular and systematic validation of [API](../A/api.md) endpoints. This automation capability is enhanced by [Postman](../P/postman.md)'s scripting features, which enable the execution of pre-request or [test scripts](../T/test-script.md) written in JavaScript.
  In a team environment, [Postman](../P/postman.md) provides **collaboration features** that allow sharing of collections, environments, and other configurations, ensuring consistency and efficiency in [API testing](../A/api-testing.md) and development efforts. Its integration capabilities with other tools and systems further streamline workflows and enable a more cohesive development process.

#### Why is Postman important in software testing?

  [Postman](../P/postman.md) is crucial in [software testing](../S/software-testing.md) for its ability to **validate [API](../A/api.md) contracts** and ensure **[API](../A/api.md) endpoints** behave as expected. It streamlines the **creation, maintenance, and execution of [API](../A/api.md) tests**, allowing for quick feedback on the health of services. With [Postman](../P/postman.md), testers can easily organize tests into collections and integrate them into **CI/CD pipelines**, promoting **[test automation](../T/test-automation.md)** and **[regression testing](../R/regression-testing.md)** at scale.
  The tool's **scripting capabilities** enable the simulation of complex user behavior and data-driven testing, enhancing the depth of [API testing](../A/api-testing.md). [Postman](../P/postman.md)'s **monitoring features** are vital for **proactive issue detection** in production environments, and its **sharing functions** facilitate **collaboration** among team members, ensuring consistency and efficiency in [test strategy](../T/test-strategy.md) implementation.
  By supporting various **authentication methods**, [Postman](../P/postman.md) ensures secure testing of [APIs](../A/api.md) that require credentials. Its **[performance testing](../P/performance-testing.md) features** allow for basic [load testing](../L/load-testing.md), helping identify bottlenecks and performance issues early in the development cycle.
  In summary, [Postman](../P/postman.md) is important in [software testing](../S/software-testing.md) for its comprehensive suite of features that support **automated**, **collaborative**, and **efficient testing practices**, essential for modern [API](../A/api.md)-driven applications.

#### What are the key features of Postman?

  Key features of [Postman](../P/postman.md) include:

  - **Built-in Authentication Protocols**: Simplifies the process of setting up various authentication types like OAuth, Basic Auth, Digest Auth, and [API](../A/api.md) Key.
  - **Pre-request Scripts**: Allows writing JavaScript code that runs before sending a request to set up variables or modify the request.
  - **Tests**: Enables writing JavaScript tests to validate response data, status codes, and response times.
  - **Environments**: Offers the ability to create different environments for storing and managing sets of variables, making it easy to switch contexts.
  - **Request Chaining**: Facilitates the extraction of data from responses and chaining requests by using the response data in subsequent requests.
  - **Mock Servers**: Provides the ability to simulate [API](../A/api.md) endpoints before the actual implementation is available.
  - **Documentation Generation**: Automatically generates and hosts beautiful, machine-readable documentation for [API](../A/api.md) collections.
  - **[API](../A/api.md) Publishing**: Allows [APIs](../A/api.md) to be published and shared with others, providing a platform for collaboration.
  - **Version Control**: Integrates with version control systems to keep [API](../A/api.md) collections and environments in sync across team members.
  - **Workspaces**: Supports personal and team workspaces to organize work and collaborate with team members.
  - **[API](../A/api.md) Monitoring**: Offers the ability to set up automated tests that run at scheduled intervals to monitor the performance and health of [APIs](../A/api.md).
  - **Interoperability**: Exports and imports collections in various formats and integrates with the [Swagger](../S/swagger.md)/OpenAPI specification.
  - **Plugins**: Supports a range of plugins and integrations with other tools like Newman for running collections from the command line.
  - **Visualizer**: Renders response data into customizable visual formats, allowing for more intuitive data analysis.
  These features collectively make [Postman](../P/postman.md) a versatile tool for [API testing](../A/api-testing.md) and development workflows.

  - **Built-in Authentication Protocols**: Simplifies the process of setting up various authentication types like OAuth, Basic Auth, Digest Auth, and [API](../A/api.md) Key.
  - **Pre-request Scripts**: Allows writing JavaScript code that runs before sending a request to set up variables or modify the request.
  - **Tests**: Enables writing JavaScript tests to validate response data, status codes, and response times.
  - **Environments**: Offers the ability to create different environments for storing and managing sets of variables, making it easy to switch contexts.
  - **Request Chaining**: Facilitates the extraction of data from responses and chaining requests by using the response data in subsequent requests.
  - **Mock Servers**: Provides the ability to simulate [API](../A/api.md) endpoints before the actual implementation is available.
  - **Documentation Generation**: Automatically generates and hosts beautiful, machine-readable documentation for [API](../A/api.md) collections.
  - **[API](../A/api.md) Publishing**: Allows [APIs](../A/api.md) to be published and shared with others, providing a platform for collaboration.
  - **Version Control**: Integrates with version control systems to keep [API](../A/api.md) collections and environments in sync across team members.
  - **Workspaces**: Supports personal and team workspaces to organize work and collaborate with team members.
  - **[API](../A/api.md) Monitoring**: Offers the ability to set up automated tests that run at scheduled intervals to monitor the performance and health of [APIs](../A/api.md).
  - **Interoperability**: Exports and imports collections in various formats and integrates with the [Swagger](../S/swagger.md)/OpenAPI specification.
  - **Plugins**: Supports a range of plugins and integrations with other tools like Newman for running collections from the command line.
  - **Visualizer**: Renders response data into customizable visual formats, allowing for more intuitive data analysis.

#### How does Postman improve the API development process?

  [Postman](../P/postman.md) streamlines [API](../A/api.md) development by providing a **unified interface** for sending requests, analyzing responses, and sharing [APIs](../A/api.md). It enables developers to **quickly iterate** through [API](../A/api.md) endpoints with features like **pre-request scripts** and **tests** that can be written in JavaScript, allowing for both manual and automated validation of [API](../A/api.md) behavior.
  With **environments and variables**, [Postman](../P/postman.md) facilitates the simulation of different application states, making it easier to test [APIs](../A/api.md) under various conditions without changing the code. This feature is particularly useful for mimicking production, development, or staging environments.
  **Mock servers** in [Postman](../P/postman.md) allow developers to prototype [APIs](../A/api.md) and simulate backend responses before the actual implementation is complete. This can significantly speed up frontend development and enable parallel workstreams.
  **Documentation generation** is another key aspect where [Postman](../P/postman.md) aids in [API](../A/api.md) development. It automatically generates and updates [API](../A/api.md) documentation as requests and responses change, ensuring that documentation stays in sync with the [API](../A/api.md)'s current state.
  [Postman](../P/postman.md)'s **collaboration features** enhance team productivity by allowing team members to share collections and environments, providing a single source of truth for [API](../A/api.md) resources within the team.
  Lastly, [Postman](../P/postman.md)'s **integration capabilities** with version control systems like Git and CI/CD tools ensure that [API testing](../A/api-testing.md) and development practices are seamlessly incorporated into the broader software development lifecycle, promoting a more DevOps-oriented workflow.
  By combining these features, [Postman](../P/postman.md) not only improves the individual developer's experience but also enhances team collaboration, leading to a more efficient and integrated [API](../A/api.md) development process.

### Working with Postman

#### How do you install and set up Postman?

  To install and set up [Postman](../P/postman.md), follow these steps:

  1. **Download [Postman](../P/postman.md)**: Go to the [Postman website](https://www.postman.com/downloads/) and download the appropriate version for your operating system (Windows, macOS, or Linux).
  2. **Install [Postman](../P/postman.md)**:
    - For
      **Windows**
      , run the downloaded
      `.exe`
      file and follow the installation prompts.

    - For
      **macOS**
      , open the downloaded
      `.zip`
      file, then drag the Postman app to your
      `Applications`
      folder.

    - For
      **Linux**
      , depending on the distribution, use the package manager to install the downloaded
      `.tar.gz`
      or
      `.deb`
      file.

    - For
      **Windows**
      , run the downloaded
      `.exe`
      file and follow the installation prompts.

    - For
      **macOS**
      , open the downloaded
      `.zip`
      file, then drag the Postman app to your
      `Applications`
      folder.

    - For
      **Linux**
      , depending on the distribution, use the package manager to install the downloaded
      `.tar.gz`
      or
      `.deb`
      file.

  3. **Launch [Postman](../P/postman.md)**: Open the installed [Postman](../P/postman.md) application.
  4. **Sign In or Create an Account** (optional): You can sign in with an existing [Postman](../P/postman.md) account or create a new one to sync your work across devices and collaborate with others.
  5. **Configure Settings** (if necessary): Access settings by clicking the gear icon in the top right corner. Configure proxy, certificates, and other preferences as needed for your testing environment.
  6. **Update Environment Variables** (if applicable): If you have environment-specific variables, set them up by clicking the 'Environment' quick look (eye icon) in the top right and managing your environments.
  7. **Import Collections or [APIs](../A/api.md)** (optional): If you have existing [Postman](../P/postman.md) collections or [APIs](../A/api.md), import them using the 'Import' button at the top left.
  8. **Verify Installation**: Create a simple GET request to a public [API](../A/api.md) endpoint to ensure [Postman](../P/postman.md) is set up correctly and can send requests.
  [Postman](../P/postman.md) is now installed and set up, ready for you to create, send, and manage your [API](../A/api.md) requests and automate tests.

  1. **Download [Postman](../P/postman.md)**: Go to the [Postman website](https://www.postman.com/downloads/) and download the appropriate version for your operating system (Windows, macOS, or Linux).
  2. **Install [Postman](../P/postman.md)**:
    - For
      **Windows**
      , run the downloaded
      `.exe`
      file and follow the installation prompts.

    - For
      **macOS**
      , open the downloaded
      `.zip`
      file, then drag the Postman app to your
      `Applications`
      folder.

    - For
      **Linux**
      , depending on the distribution, use the package manager to install the downloaded
      `.tar.gz`
      or
      `.deb`
      file.

    - For
      **Windows**
      , run the downloaded
      `.exe`
      file and follow the installation prompts.

    - For
      **macOS**
      , open the downloaded
      `.zip`
      file, then drag the Postman app to your
      `Applications`
      folder.

    - For
      **Linux**
      , depending on the distribution, use the package manager to install the downloaded
      `.tar.gz`
      or
      `.deb`
      file.

  3. **Launch [Postman](../P/postman.md)**: Open the installed [Postman](../P/postman.md) application.
  4. **Sign In or Create an Account** (optional): You can sign in with an existing [Postman](../P/postman.md) account or create a new one to sync your work across devices and collaborate with others.
  5. **Configure Settings** (if necessary): Access settings by clicking the gear icon in the top right corner. Configure proxy, certificates, and other preferences as needed for your testing environment.
  6. **Update Environment Variables** (if applicable): If you have environment-specific variables, set them up by clicking the 'Environment' quick look (eye icon) in the top right and managing your environments.
  7. **Import Collections or [APIs](../A/api.md)** (optional): If you have existing [Postman](../P/postman.md) collections or [APIs](../A/api.md), import them using the 'Import' button at the top left.
  8. **Verify Installation**: Create a simple GET request to a public [API](../A/api.md) endpoint to ensure [Postman](../P/postman.md) is set up correctly and can send requests.

#### How do you create a new request in Postman?

  To create a new request in [Postman](../P/postman.md):

  1. Open Postman and ensure you are in the
    **Workspace**
    where you want to create the request.

  2. Click on the
    **New**
    button (a plus
    `+`
    icon) in the upper-left corner or use the shortcut
    `Ctrl + N`
    (Windows) or
    `Cmd + N`
    (Mac).

  3. Select
    **Request**
    from the dropdown menu.

  4. A dialog box will appear. Enter a
    **name**
    for your request in the "Request name" field.

  5. Optionally, you can add a
    **description**
    to describe the purpose of the request.

  6. To organize your requests, you can choose to save the new request to an existing
    **collection**
    or create a new one by clicking on the
    **Create Collection**
    button.

  7. After selecting or creating a collection, click the
    **Save to**
    button.
  Once saved, you can start configuring your request:

  - In the request tab, select the appropriate
    **HTTP method**
    (GET, POST, PUT, DELETE, etc.) from the dropdown next to the URL field.

  - Enter the
    **URL**
    you want to send the request to.

  - Add
    **headers**
    ,
    **parameters**
    , or
    **body data**
    as needed for your request.

  - Click the
    **Send**
    button to execute the request and view the response.
  Remember to save changes to your request by clicking the **Save** button if you've made any modifications.

  1. Open Postman and ensure you are in the
    **Workspace**
    where you want to create the request.

  2. Click on the
    **New**
    button (a plus
    `+`
    icon) in the upper-left corner or use the shortcut
    `Ctrl + N`
    (Windows) or
    `Cmd + N`
    (Mac).

  3. Select
    **Request**
    from the dropdown menu.

  4. A dialog box will appear. Enter a
    **name**
    for your request in the "Request name" field.

  5. Optionally, you can add a
    **description**
    to describe the purpose of the request.

  6. To organize your requests, you can choose to save the new request to an existing
    **collection**
    or create a new one by clicking on the
    **Create Collection**
    button.

  7. After selecting or creating a collection, click the
    **Save to**
    button.

  - In the request tab, select the appropriate
    **HTTP method**
    (GET, POST, PUT, DELETE, etc.) from the dropdown next to the URL field.

  - Enter the
    **URL**
    you want to send the request to.

  - Add
    **headers**
    ,
    **parameters**
    , or
    **body data**
    as needed for your request.

  - Click the
    **Send**
    button to execute the request and view the response.

#### How do you send a request in Postman?

  To send a request in [Postman](../P/postman.md), follow these steps:

  1. Open Postman and select the
    **workspace**
    where you want to work.

  2. Ensure you have already created a new request or have an existing one open.
  3. In the request tab, choose the appropriate
    **HTTP method**
    (GET, POST, PUT, DELETE, etc.) from the dropdown menu.

  4. Enter the
    **URL**
    you want to send the request to in the address bar.

  5. If needed, add
    **headers**
    by clicking on the 'Headers' tab and entering the key-value pairs.

  6. For methods like POST or PUT, you may need to send a body with the request. Click on the 'Body' tab, select the appropriate format (like raw, form-data, x-www-form-urlencoded), and input the data.
  7. Optionally, you can add
    **parameters**
    to the URL by clicking on the 'Params' tab and entering name-value pairs.

  8. Once you have set up your request, click the
    **Send**
    button.
  The response will appear in the lower section of the [Postman](../P/postman.md) interface. You can view the status code, response time, size, and the body of the response. If you need to make further adjustments, you can modify the request as needed and resend it.
  For [automated testing](../A/automated-testing.md), you can write **tests** in the 'Tests' tab using JavaScript and utilize [Postman](../P/postman.md)'s built-in test snippets for common assertions. After sending the request, the test results will be displayed in the 'Test Results' tab.

  1. Open Postman and select the
    **workspace**
    where you want to work.

  2. Ensure you have already created a new request or have an existing one open.
  3. In the request tab, choose the appropriate
    **HTTP method**
    (GET, POST, PUT, DELETE, etc.) from the dropdown menu.

  4. Enter the
    **URL**
    you want to send the request to in the address bar.

  5. If needed, add
    **headers**
    by clicking on the 'Headers' tab and entering the key-value pairs.

  6. For methods like POST or PUT, you may need to send a body with the request. Click on the 'Body' tab, select the appropriate format (like raw, form-data, x-www-form-urlencoded), and input the data.
  7. Optionally, you can add
    **parameters**
    to the URL by clicking on the 'Params' tab and entering name-value pairs.

  8. Once you have set up your request, click the
    **Send**
    button.

#### How do you save responses in Postman?

  To save responses in [Postman](../P/postman.md), you can utilize the following methods:

  1. **Manual Copy-Paste**: After sending a request, simply select the response body, copy it, and paste it into your desired location, such as a text file or note-taking application.
  2. **Save Response to a File**:
    - Click on the
      **'Save Response'**
      button located next to the response body.

    - Choose
      **'Save to a file'**
      from the dropdown menu.

    - Select the location on your file system and save the file with the appropriate extension.
    - Click on the
      **'Save Response'**
      button located next to the response body.

    - Choose
      **'Save to a file'**
      from the dropdown menu.

    - Select the location on your file system and save the file with the appropriate extension.
  3. **Use Tests and Scripts**:
    - In the
      **'Tests'**
      tab, write a script to save the response to an environment or a global variable:

      ```
      var jsonData = pm.response.json();
      pm.environment.set("responseVariable", JSON.stringify(jsonData));
      ```

    - Access the saved response from the environment or global variables whenever needed.
    - In the
      **'Tests'**
      tab, write a script to save the response to an environment or a global variable:

      ```
      var jsonData = pm.response.json();
      pm.environment.set("responseVariable", JSON.stringify(jsonData));
      ```

    - Access the saved response from the environment or global variables whenever needed.
  4. **Automate with Collection Runner**:
    - Create a test script to save the response as described above.
    - Use the Collection Runner to execute the request.
    - The response will be saved in the environment or global variable for later use or further automation steps.
    - Create a test script to save the response as described above.
    - Use the Collection Runner to execute the request.
    - The response will be saved in the environment or global variable for later use or further automation steps.
  5. **[Postman](../P/postman.md) [API](../A/api.md)**:
    - Use Postman's API to programmatically retrieve and save responses.
    - Send a request to the Postman API with the collection and request ID to get the response data.
    - Save the response from the API call to your desired location.
    - Use Postman's API to programmatically retrieve and save responses.
    - Send a request to the Postman API with the collection and request ID to get the response data.
    - Save the response from the API call to your desired location.
  Remember to handle sensitive data appropriately when saving responses, ensuring that no confidential information is stored insecurely.

  1. **Manual Copy-Paste**: After sending a request, simply select the response body, copy it, and paste it into your desired location, such as a text file or note-taking application.
  2. **Save Response to a File**:
    - Click on the
      **'Save Response'**
      button located next to the response body.

    - Choose
      **'Save to a file'**
      from the dropdown menu.

    - Select the location on your file system and save the file with the appropriate extension.
    - Click on the
      **'Save Response'**
      button located next to the response body.

    - Choose
      **'Save to a file'**
      from the dropdown menu.

    - Select the location on your file system and save the file with the appropriate extension.
  3. **Use Tests and Scripts**:
    - In the
      **'Tests'**
      tab, write a script to save the response to an environment or a global variable:

      ```
      var jsonData = pm.response.json();
      pm.environment.set("responseVariable", JSON.stringify(jsonData));
      ```

    - Access the saved response from the environment or global variables whenever needed.
    - In the
      **'Tests'**
      tab, write a script to save the response to an environment or a global variable:

      ```
      var jsonData = pm.response.json();
      pm.environment.set("responseVariable", JSON.stringify(jsonData));
      ```

    - Access the saved response from the environment or global variables whenever needed.
  4. **Automate with Collection Runner**:
    - Create a test script to save the response as described above.
    - Use the Collection Runner to execute the request.
    - The response will be saved in the environment or global variable for later use or further automation steps.
    - Create a test script to save the response as described above.
    - Use the Collection Runner to execute the request.
    - The response will be saved in the environment or global variable for later use or further automation steps.
  5. **[Postman](../P/postman.md) [API](../A/api.md)**:
    - Use Postman's API to programmatically retrieve and save responses.
    - Send a request to the Postman API with the collection and request ID to get the response data.
    - Save the response from the API call to your desired location.
    - Use Postman's API to programmatically retrieve and save responses.
    - Send a request to the Postman API with the collection and request ID to get the response data.
    - Save the response from the API call to your desired location.

#### How do you use variables in Postman?

  Using variables in [Postman](../P/postman.md) allows you to store and reuse values across your requests and scripts. Here's how to use them:

  1. **Set a variable**: You can set a variable in [Postman](../P/postman.md) using the `Environment` or `Globals` tab. Click on the `Environment quick look` icon in the top right corner, then edit the current environment or globals by adding the variable name and value.

    ```
    pm.environment.set("variable_key", "variable_value");
    ```

  2. **Use a variable in a request**: Insert the variable in the URL, headers, or body by wrapping the variable key in double curly braces.

    ```
    https://api.example.com/users/{{user_id}}
    ```

  3. **Access a variable in scripts**: Retrieve the value of a variable in the pre-request or [test scripts](../T/test-script.md) using the `pm` object.

    ```
    let userId = pm.environment.get("user_id");
    ```

  4. **Update a variable**: Change the value of an existing variable during the execution of scripts.

    ```
    pm.environment.set("user_id", 12345);
    ```

  5. **Clear a variable**: Remove the value of a variable, making it undefined.

    ```
    pm.environment.unset("user_id");
    ```
  Variables in [Postman](../P/postman.md) are scoped hierarchically, allowing you to define them at global, collection, environment, and local (data file) levels. This flexibility enables you to maintain different sets of values for different testing scenarios and stages. Remember to use meaningful names for your variables to maintain clarity and readability in your requests and scripts.

  1. **Set a variable**: You can set a variable in [Postman](../P/postman.md) using the `Environment` or `Globals` tab. Click on the `Environment quick look` icon in the top right corner, then edit the current environment or globals by adding the variable name and value.

    ```
    pm.environment.set("variable_key", "variable_value");
    ```

  2. **Use a variable in a request**: Insert the variable in the URL, headers, or body by wrapping the variable key in double curly braces.

    ```
    https://api.example.com/users/{{user_id}}
    ```

  3. **Access a variable in scripts**: Retrieve the value of a variable in the pre-request or [test scripts](../T/test-script.md) using the `pm` object.

    ```
    let userId = pm.environment.get("user_id");
    ```

  4. **Update a variable**: Change the value of an existing variable during the execution of scripts.

    ```
    pm.environment.set("user_id", 12345);
    ```

  5. **Clear a variable**: Remove the value of a variable, making it undefined.

    ```
    pm.environment.unset("user_id");
    ```

### Advanced Features

#### How do you use Postman for automated testing?

  To automate testing with [Postman](../P/postman.md), follow these steps:

  1. **Create a collection** : Group related API requests into a collection.
  2. **Write tests** : For each request, write tests in the Tests tab using JavaScript and Postman's pm object. Example:

    ```
    pm.test("Status code is 200", function () {
        pm.response.to.have.status(200);
    });
    ```

  3. **Use environment variables** : Set up environment variables for dynamic data in your requests and tests.
  4. **Chain requests** : Use
    `pm.sendRequest`
    to chain requests and use the response of one request as input for another.

  5. **Run collections** : Use the Collection Runner to execute all requests in a collection. Optionally, select an environment and specify iterations and delays.
  6. **View results** : After running, analyze the results in the Collection Runner for passed and failed tests.
  7. **Automate with Newman** : Install Newman, Postman's command-line companion, to run collections outside of Postman. Use the following command:

    ```
    newman run <Collection URL> -e <Environment URL>
    ```

  8. **Integrate with CI/CD** : Incorporate Newman into your CI/CD pipeline using appropriate commands in your build scripts or configuration files.
  By automating tests in [Postman](../P/postman.md), you can ensure your [API](../A/api.md) behaves as expected after changes, and you can integrate these tests into your development workflows for continuous testing.

  1. **Create a collection** : Group related API requests into a collection.
  2. **Write tests** : For each request, write tests in the Tests tab using JavaScript and Postman's pm object. Example:

    ```
    pm.test("Status code is 200", function () {
        pm.response.to.have.status(200);
    });
    ```

  3. **Use environment variables** : Set up environment variables for dynamic data in your requests and tests.
  4. **Chain requests** : Use
    `pm.sendRequest`
    to chain requests and use the response of one request as input for another.

  5. **Run collections** : Use the Collection Runner to execute all requests in a collection. Optionally, select an environment and specify iterations and delays.
  6. **View results** : After running, analyze the results in the Collection Runner for passed and failed tests.
  7. **Automate with Newman** : Install Newman, Postman's command-line companion, to run collections outside of Postman. Use the following command:

    ```
    newman run <Collection URL> -e <Environment URL>
    ```

  8. **Integrate with CI/CD** : Incorporate Newman into your CI/CD pipeline using appropriate commands in your build scripts or configuration files.

#### What is the Postman Collection Runner and how do you use it?

  The **[Postman](../P/postman.md) Collection Runner** is a tool within [Postman](../P/postman.md) that allows you to execute multiple [API](../A/api.md) requests in a specified sequence. It's particularly useful for running tests across a collection of endpoints, simulating workflows, or performing smoke testing.
  To use the Collection Runner:

  1. Open Postman and select the collection you want to run.
  2. Click on the
    **Runner**
    button at the bottom left of the Postman window.

  3. In the Collection Runner window, choose the collection and the environment (if you use environment variables).
  4. Configure options such as iterations, delay between requests, and log responses.
  5. Optionally, select a data file if you want to run the collection with different sets of data (data-driven testing).
  6. Click on the
    **Run [collection name]**
    button to start the execution.
  As the Collection Runner executes the requests, it displays real-time results including passed/failed tests, response times, and log outputs. You can use this feedback to debug and optimize your [API](../A/api.md) requests and tests.
  For automation, you can trigger Collection Runner via the command line using Newman, [Postman](../P/postman.md)'s companion tool for running collections outside of the [Postman](../P/postman.md) app. This is particularly useful for integrating with CI/CD pipelines.

  ```
  newman run <Collection URL or Path> -e <Environment File Path>
  ```
  Remember to leverage **scripts** in your collections to enhance the automation capabilities, such as setting up pre-request scripts or tests that will run with each request in the runner.

  1. Open Postman and select the collection you want to run.
  2. Click on the
    **Runner**
    button at the bottom left of the Postman window.

  3. In the Collection Runner window, choose the collection and the environment (if you use environment variables).
  4. Configure options such as iterations, delay between requests, and log responses.
  5. Optionally, select a data file if you want to run the collection with different sets of data (data-driven testing).
  6. Click on the
    **Run [collection name]**
    button to start the execution.

#### How do you use Postman's scripting capabilities?

  [Postman](../P/postman.md)'s scripting capabilities are leveraged through the **Pre-request Script** and **Tests** tabs within a request. These scripts are written in JavaScript and allow you to programmatically interact with request and response data.
  **Pre-request Script**: Execute JavaScript before a request runs. Use it to set up variables, parameters, or headers. For example:

  ```
  pm.variables.set("timestamp", Date.now());
  ```
  **Tests**: Write test assertions to validate response data, status codes, and response times after a request is sent. [Postman](../P/postman.md) uses the Chai assertion library. Example:

  ```
  pm.test("Status code is 200", function () {
      pm.response.to.have.status(200);
  });
  pm.test("Response time is less than 500ms", function () {
      pm.expect(pm.response.responseTime).to.be.below(500);
  });
  ```
  **Dynamic Variables**: Generate random data for requests using dynamic variables like `{{$randomInt}}`.
  **Data Files**: Use external data files in JSON or CSV format to run iterative tests with different sets of data.
  **pm.* API**: Access a wide range of [Postman](../P/postman.md)-specific objects and functions to interact with the environment, collection, and request/response details.
  **Snippets**: Quickly add common script snippets from the right-hand sidebar to speed up test writing.
  **Console**: Debug scripts by logging output to the [Postman](../P/postman.md) Console (`View` > `Show Postman Console`).
  **Global/Environment Variables**: Scripts can create, modify, or delete global and environment variables to maintain state between requests.
  Combine these scripting features with the **Collection Runner** or **[Postman](../P/postman.md) Monitors** to execute automated [test suites](../T/test-suite.md) and monitor [APIs](../A/api.md) at scheduled intervals.

#### What is Postman Monitors and how does it work?

  [Postman](../P/postman.md) Monitors are automated processes that run collections at scheduled intervals to check for the performance and response of [APIs](../A/api.md). They work by executing a collection, which is a set of pre-defined requests, and can be set to run on various environments, ensuring that [APIs](../A/api.md) are functioning as expected over time.
  To set up a monitor, you select a collection, configure the frequency of the run, and specify the environment. Monitors can run as often as every 5 minutes or on a daily, weekly, or monthly schedule. When a monitor runs, it executes each request in the collection and reports on the results.
  Monitors are useful for:

  - **Continuous Monitoring** : Ensuring that your API is up and running at all times.
  - **Version Checks** : Validating that the latest deployment hasn't broken any existing functionality.
  - **Response Time Alerts** : Notifying when APIs are responding slower than expected, which could indicate performance issues.
  Results from monitors can be viewed in the [Postman](../P/postman.md) app or web dashboard, where you can see the history of runs, response times, and the details of any failures. You can also set up integrations to receive notifications via email, Slack, or other platforms when a monitor fails or detects issues.
  Here's a basic example of how to set up a monitor using [Postman](../P/postman.md)'s [API](../A/api.md):

  ```
  POST /monitors
  {
    "name": "API Health Check",
    "collection_uid": "12345-abcdef",
    "environment_uid": "98765-fedcba",
    "schedule": {
      "interval": 10,
      "unit": "minutes"
    }
  }
  ```
  This would create a monitor named "[API](../A/api.md) Health Check" that runs every 10 minutes using the specified collection and environment.

  - **Continuous Monitoring** : Ensuring that your API is up and running at all times.
  - **Version Checks** : Validating that the latest deployment hasn't broken any existing functionality.
  - **Response Time Alerts** : Notifying when APIs are responding slower than expected, which could indicate performance issues.

#### How do you use Postman for performance testing?

  To use [Postman](../P/postman.md) for [performance testing](../P/performance-testing.md), you'll primarily leverage the **Collection Runner** and **[Postman](../P/postman.md) Monitors**. Here's a concise guide:

  1. **Create a Collection**: Group all the requests you want to test under a single collection.
  2. **Write Pre-request and [Test Scripts](../T/test-script.md)**: Customize your requests and responses handling using JavaScript in the Pre-request and Tests tabs.
  3. **Set Variables**: Use environment or collection variables to simulate different scenarios and data sets.
  4. **Run Collection**: Use the Collection Runner to execute the entire collection. Adjust the [iterations](../I/iteration.md) and delay between requests to simulate load.

    ```
    // Example of setting a variable in pre-request script
    pm.variables.set("dynamicValue", Math.floor(Math.random() * 100));
    ```

  5. **Analyze Results**: After the run, review response times, error rates, and other important metrics to assess performance.
  6. **Monitor Performance**: Set up a [Postman](../P/postman.md) Monitor to run your collection at regular intervals, which helps in tracking performance over time.
  7. **Integrate with CI/CD**: Use [Postman](../P/postman.md)'s Newman command-line tool to integrate your performance tests into your CI/CD pipeline for regular feedback.
  8. **Scale with Cloud Agents**: For more extensive [performance testing](../P/performance-testing.md), use [Postman](../P/postman.md)'s cloud agents to simulate higher loads and more realistic conditions.
  Remember, while [Postman](../P/postman.md) can handle basic [performance testing](../P/performance-testing.md), it's not a substitute for dedicated [performance testing](../P/performance-testing.md) tools like [JMeter](../J/jmeter.md) or LoadRunner when it comes to complex [load testing](../L/load-testing.md) scenarios. Use [Postman](../P/postman.md) for lightweight performance checks and [API](../A/api.md) endpoint [stress testing](../S/stress-testing.md).

  1. **Create a Collection**: Group all the requests you want to test under a single collection.
  2. **Write Pre-request and [Test Scripts](../T/test-script.md)**: Customize your requests and responses handling using JavaScript in the Pre-request and Tests tabs.
  3. **Set Variables**: Use environment or collection variables to simulate different scenarios and data sets.
  4. **Run Collection**: Use the Collection Runner to execute the entire collection. Adjust the [iterations](../I/iteration.md) and delay between requests to simulate load.

    ```
    // Example of setting a variable in pre-request script
    pm.variables.set("dynamicValue", Math.floor(Math.random() * 100));
    ```

  5. **Analyze Results**: After the run, review response times, error rates, and other important metrics to assess performance.
  6. **Monitor Performance**: Set up a [Postman](../P/postman.md) Monitor to run your collection at regular intervals, which helps in tracking performance over time.
  7. **Integrate with CI/CD**: Use [Postman](../P/postman.md)'s Newman command-line tool to integrate your performance tests into your CI/CD pipeline for regular feedback.
  8. **Scale with Cloud Agents**: For more extensive [performance testing](../P/performance-testing.md), use [Postman](../P/postman.md)'s cloud agents to simulate higher loads and more realistic conditions.

### Integration and Collaboration

#### How do you share a Postman collection with others?

  To share a [Postman](../P/postman.md) collection with others, follow these steps:

  1. **Export the Collection**: Click on the collection you want to share, then click on the three dots to open the collection menu. Select "Export" and choose the format version. Save the file to your local system.
  2. **Share via [Postman](../P/postman.md)**: If you're using [Postman](../P/postman.md)'s collaboration features, click on the 'Share' button at the top of the collection tab. You can then invite team members by email or share a link to the collection.
  3. **Use Version Control**: Commit the exported collection file to a version control system like Git. This allows others to pull the collection into their local [Postman](../P/postman.md) environment.
  4. **Email or File Sharing Services**: Attach the exported collection file to an email or upload it to a file sharing service, then share the link with your colleagues.
  5. **[Postman](../P/postman.md) [API](../A/api.md) Network**: Publish your collection to the [Postman](../P/postman.md) [API](../A/api.md) Network for broader access. Go to the [Postman](../P/postman.md) Dashboard, select your collection, and publish it to the [API](../A/api.md) Network.
  6. **[Postman](../P/postman.md) Documentation**: Generate and share the documentation for your collection. This provides a web page with all requests that can be run directly from the documentation.
  Here's an example of how to export a collection using [Postman](../P/postman.md)'s UI:

  ```
  1. Click on the collection in the sidebar.
  2. Click on the three dots to open the menu.
  3. Select "Export" -> "Collection v2.1 (Recommended)" -> "Export".
  4. Save the JSON file to your desired location.
  ```
  Remember to inform recipients about any environment variables or prerequisites needed to use the collection effectively.

  1. **Export the Collection**: Click on the collection you want to share, then click on the three dots to open the collection menu. Select "Export" and choose the format version. Save the file to your local system.
  2. **Share via [Postman](../P/postman.md)**: If you're using [Postman](../P/postman.md)'s collaboration features, click on the 'Share' button at the top of the collection tab. You can then invite team members by email or share a link to the collection.
  3. **Use Version Control**: Commit the exported collection file to a version control system like Git. This allows others to pull the collection into their local [Postman](../P/postman.md) environment.
  4. **Email or File Sharing Services**: Attach the exported collection file to an email or upload it to a file sharing service, then share the link with your colleagues.
  5. **[Postman](../P/postman.md) [API](../A/api.md) Network**: Publish your collection to the [Postman](../P/postman.md) [API](../A/api.md) Network for broader access. Go to the [Postman](../P/postman.md) Dashboard, select your collection, and publish it to the [API](../A/api.md) Network.
  6. **[Postman](../P/postman.md) Documentation**: Generate and share the documentation for your collection. This provides a web page with all requests that can be run directly from the documentation.

#### How does Postman integrate with other tools and systems?

  [Postman](../P/postman.md) integrates with various tools and systems to enhance its capabilities in [test automation](../T/test-automation.md) and [API](../A/api.md) development. It offers a **native integration** with **Newman**, a command-line Collection Runner, allowing you to run and test a [Postman](../P/postman.md) collection directly from the command line. This is particularly useful for integrating with **CI/CD pipelines** such as Jenkins, Travis CI, or CircleCI.

  ```
  newman run collection.json
  ```
  For **version control**, [Postman](../P/postman.md) integrates with **Git** repositories, enabling you to sync your collections with your source code. This allows for better collaboration and versioning of [API](../A/api.md) tests.
  [Postman](../P/postman.md) also provides a **[Postman](../P/postman.md) [API](../A/api.md)** that can be used to integrate with other services. You can use this [API](../A/api.md) to programmatically access and manipulate your collections, environments, and runs, which is useful for custom integrations or extending [Postman](../P/postman.md)'s functionality.

  ```
  const postmanApiKey = 'PMAK-your-api-key';
  const collectionId = 'your-collection-id';
  ```
  **Webhooks** in [Postman](../P/postman.md) can trigger workflows in other systems upon collection runs completion, which is beneficial for triggering actions in other parts of your CI/CD process.
  For **monitoring and reporting**, [Postman](../P/postman.md) integrates with systems like **Datadog**, **BigPanda**, and **PagerDuty**, allowing you to send alerts or log data based on the results of your monitoring runs.
  Lastly, [Postman](../P/postman.md)'s **Interceptor** extension captures and syncs cookies and requests from the browser, facilitating testing of web applications and allowing for seamless integration with browser-based workflows.

#### What is Postman's role in Continuous Integration (CI) and Continuous Deployment (CD)?

  [Postman](../P/postman.md) plays a crucial role in **Continuous Integration (CI)** and **Continuous Deployment (CD)** by enabling automated [API testing](../A/api-testing.md) within these pipelines. By integrating [Postman](../P/postman.md) collections into CI/CD workflows, teams can ensure that [API](../A/api.md) endpoints are tested consistently and automatically every time changes are committed to the codebase.
  In a CI/CD [setup](../S/setup.md), [Postman](../P/postman.md) collections can be executed as part of the build process using **Newman**, [Postman](../P/postman.md)'s command-line Collection Runner. Newman can be integrated with popular CI/CD tools like Jenkins, Travis CI, CircleCI, and GitLab CI, allowing [API](../A/api.md) tests to run whenever a new build is triggered.
  Here's an example of how you might run a [Postman](../P/postman.md) collection using Newman in a CI script:

  ```
  newman run collection.json -e environment.json
  ```
  If the [Postman](../P/postman.md) tests fail, the build can be halted, ensuring that no broken code is deployed to production. This helps maintain the stability and reliability of the application.
  For CD, [Postman](../P/postman.md) can be used to perform **health checks** and **smoke tests** post-deployment, verifying that the live application is functioning as expected. This automated [verification](../V/verification.md) step adds an additional layer of confidence before the application is made available to end-users.
  By integrating [Postman](../P/postman.md) into CI/CD pipelines, teams achieve faster release cycles, higher quality software, and reduced [manual testing](../M/manual-testing.md) efforts, all while ensuring that [APIs](../A/api.md) meet their design and performance standards throughout the development lifecycle.

#### How do you use Postman in a team setting?

  Using [Postman](../P/postman.md) in a team setting involves collaboration and sharing of resources such as collections, environments, and [APIs](../A/api.md). Here's how to effectively use [Postman](../P/postman.md) with your team:

  - **Workspaces**: Create a shared workspace for your team to access all relevant [Postman](../P/postman.md) components. Workspaces can be personal, team, private, or public.
  - **Collections**: Share collections with your team within the workspace. Use the **Share** button or drag and drop collections into the team workspace.
  - **Environments**: Define environments with variables that can be shared across the team. This ensures consistency in testing across different local [setups](../S/setup.md).
  - **Roles and Permissions**: Assign roles to team members to control who can view, edit, or share collections and environments.
  - **Version Control**: Use [Postman](../P/postman.md)’s built-in version control system to track changes to collections. Commit changes and merge updates from teammates.
  - **Comments**: Add comments on collections or requests for communication and feedback within the team.
  - **Forking and Merging**: Fork collections to experiment or make changes without affecting the team's main collection. Merge changes back when ready.
  - **Integrations**: Connect [Postman](../P/postman.md) with version control systems like GitHub for syncing and backup of [Postman](../P/postman.md) collections.
  - **Monitoring**: Set up monitors on collections to regularly run tests and share results with the team.
  - **[API](../A/api.md) Documentation**: Automatically generate and share [API](../A/api.md) documentation with your team or stakeholders for better collaboration.
  - **[Postman](../P/postman.md) [API](../A/api.md)**: Use the [Postman](../P/postman.md) [API](../A/api.md) to programmatically access and update [Postman](../P/postman.md) data, which can be useful for CI/CD pipelines.
  Remember to maintain clear naming conventions and documentation within [Postman](../P/postman.md) to ensure that all team members can easily understand and use shared resources.

  - **Workspaces**: Create a shared workspace for your team to access all relevant [Postman](../P/postman.md) components. Workspaces can be personal, team, private, or public.
  - **Collections**: Share collections with your team within the workspace. Use the **Share** button or drag and drop collections into the team workspace.
  - **Environments**: Define environments with variables that can be shared across the team. This ensures consistency in testing across different local [setups](../S/setup.md).
  - **Roles and Permissions**: Assign roles to team members to control who can view, edit, or share collections and environments.
  - **Version Control**: Use [Postman](../P/postman.md)’s built-in version control system to track changes to collections. Commit changes and merge updates from teammates.
  - **Comments**: Add comments on collections or requests for communication and feedback within the team.
  - **Forking and Merging**: Fork collections to experiment or make changes without affecting the team's main collection. Merge changes back when ready.
  - **Integrations**: Connect [Postman](../P/postman.md) with version control systems like GitHub for syncing and backup of [Postman](../P/postman.md) collections.
  - **Monitoring**: Set up monitors on collections to regularly run tests and share results with the team.
  - **[API](../A/api.md) Documentation**: Automatically generate and share [API](../A/api.md) documentation with your team or stakeholders for better collaboration.
  - **[Postman](../P/postman.md) [API](../A/api.md)**: Use the [Postman](../P/postman.md) [API](../A/api.md) to programmatically access and update [Postman](../P/postman.md) data, which can be useful for CI/CD pipelines.
