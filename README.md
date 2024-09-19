# Github Action Basics Assignment

## Creating a Basic GitHub Action

Follow these steps to create a basic GitHub Action:

1. **Create a workflow file**:
    - In your repository, create a directory named `.github/workflows`.
    - Inside this directory, create a file named `main.yml`.

1. **Define the workflow**:
    - Open `main.yml` and add the following content:
      ```yaml
      name: hello world

      on:
        push:
            branches:
                - main

      jobs:
         hello:
            runs-on: ubuntu-latest

            steps:
            - uses: actions/checkout@v2
            - name: run echo
              run: echo "Hello, world!"
      ```

1. **Commit and push your changes**:
    - Commit the `main.yml` file and push it to your repository.

1. **Check the Actions tab**:
    - Go to the Actions tab in your repository to see your workflow run.

1. **Add additional functionality**:
    - Go ahead and research some interesting things you can do with github actions, and add some extra functionality to this action. Below are some ideas for changes you can make.
    - Be sure that your final action has at least 4 steps.
    - Be sure that your final action adds or changes 1 trigger.


### Change Ideas


- **Trigger Ideas**:
    - Schedule: Trigger the workflow at specific times using cron syntax.
    - Pull Request: Trigger the workflow when a pull request is opened, synchronized, or reopened.
    - Manual: Trigger the workflow when a button is pushed.

- **Step Ideas**:
    - **Run tests**: Add a step to run your project's tests.
        ```yaml
        - name: Run tests
            run: pytest .
        ```
    - **Lint code**: Add a step to lint your code.
        ```yaml
        - name: Lint code
            run: pylint
        ```
    - **Build project**: Add a step to build your project.
        ```yaml
        - name: Build project
            run: docker build .
        ```
**Note**: You may need to add some code to the repo for some of these steps to really run. You may copy other code from previous assignments if you desire.

## Submitting

Before submitting this assignment, ensure that your github actions have run based on their triggers.

Submit a link to your updated repo in canvas.