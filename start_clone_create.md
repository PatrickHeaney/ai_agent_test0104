# How to Create a New Project Using this Template

This project is designed to be used as a GitHub Template. This makes it incredibly easy to start a new project with a clean git history.

## ✅ One-Time Setup: Enable the Template Feature

First, you need to mark this `_new_prj` repository as a template on GitHub. You only have to do this once.

1.  Go to the main page of your `_new_prj` repository on GitHub.
2.  Click the **Settings** tab.
3.  Check the box next to **Template repository**.

That's it! Your repository is now a template.

## Creating Your New Project (The Easy Way)

Now, anytime you want to start a new project based on this template, follow these simple steps.

### 1. Use the Template
A new green button, **Use this template**, will now be visible on your repository's page.

1.  Click the **Use this template** button.
2.  Select **Create a new repository**.
3.  Give your new repository a name and description. `ai_agent_test0104`
4.  Click **Create repository**.

GitHub will automatically create a brand-new repository, copying all the files from `_new_prj` but giving it a fresh, clean history.

### 2. Clone Your New Repository
Navigate to the directory on your local machine where you want to store your project and clone the new repository you just created.

```bash
# Replace the URL with your new repository's URL,  Navigate into your new project directory, and rename the Terminal Tab
git clone https://github.com/PatrickHeaney/ai_agent_test0104.git
cd ai_agent_test0104
printf "\e]1;ai_agent_test0104\a"
```

### 3. Download Example Code Submodules
Your new project is linked to complete, working reference projects like `ai_tutor_test2`. Run the following command to download the code for these submodules into the `example_code/` directory.

```bash
git submodule update --init --recursive
```

🎉 Your new project is now set up locally with a clean git history, ready for you to start working.

## Plan

### ☑️ NOTE: Start a new IDE Window, open it to your new folder named `new_project_name` and start your AI Coding asssitant now.
```Bash
Gemini```

### 1. Idea.md
☑️ Update the high level descripiton of your idea in the `idea.md` file.
- save all - cmd + ctrl+ s
- IDE git panel > stage all > add commit msg > commit
- IDE Terminal `Git push`

### 2. PLANNING.md
☑️ `Read @idea.md then read and modify the @PLANNING.md document to align with my ### Iteration 1: The Core Conversation Loop of @idea.md. Explain your modifications.`

## 3. TASK.md
☑️ `Read @idea.md and @PLANNING.md then read and modify @TASK.md document to align with my ### Iteration 1: The Core Conversation Loop of @idea.md and with @PLANNING.md. Explain your modifications.`

## 4. README.md
☑️ `Read @idea.md, @PLANNING.md, and @TASK.md files, then read and modify the @README.md document to align with to align with my ### Iteration 1: The Core Conversation Loop of @idea.md and with @PLANNING.md and TASK.md. Explain your modifications.`

## Implement

### 1. Implement Iteration 1
☑️ ```Create a Pydantic AI Agent implementing Iteration 1 of @TASK.md while adhere to the following guidelines:
  1 following agent example from https://ai.pydantic.dev/examples/weather-agent/ and /Users/pmh/code/_new_prj/example_code/ai-agent-mastery/4_Pydantic_AI_Agent/extras/Basic_Pydantic_AI_Agent. Don't follow them to a tea, just use them to get a grasp of and use the Pydantic framework.
  2 use .env.example to get an understanding of the necessary environment variables for the agent```

#### User Test
After implementing Iteration 1, follow these steps to test the agent manually.

##### 1. Create Environment and Install Dependencies
This command first creates a virtual environment in a `.venv` folder and then installs the required Python packages into it.

```Bash
uv venv && uv pip install -r requirements.txt
```

##### 2. Configure Your LLM
The agent needs to connect to a Large Language Model.

1.  Create a `.env` file by copying the example:
    ```Bash
    # On macOS/Linux
    cp .env.example .env

    # On Windows
    # copy .env.example .env
    ```
2.  Open the newly created `.env` file in a text editor and fill in the values for your chosen LLM provider.

##### 3. Run the Agent
Start the conversational agent using this command:

```Bash
uv run cli.py
```

##### 4. Ask a Question
Once the agent is running, you will see a `You:` prompt. Test the agent with an initial question. For example:

```
You: Tell me a fun fact about the Roman Empire.
```

If the agent responds, congratulations! The core conversational loop is working.

## Learn

### Document Lessons Learned in the test project
`document any deviations we made from the tasks outlined in @TASK by creating a lesson_{{issue_title}}.md file to use as lesson learned that I can apply to the github project I cloned this from.  The document should provide enough information for another coding agent to update the template and avoid this problem in the future.`

`review the lesson_{{issue_title}}.md files and 1, verify the codebase addresses them adhereing to @gemini.md.  Then 2 update @PLANNING.md, @TASK.md, and @README.md so an AI coding assistant does not recreate these issues when using these files in a template.`

### Apply Lessons Learned to the _new_prj
#### Step 1: Add successful project as Submodule

Your task is to perform a upgrade on the _new_prj instructional template. The last usage of the template revealed lessons that need to be applied. Your
goal is to fix these instructions based on the lessons learned from the {{most_recent_test}} project.

First, add the successfully completed {{most_recent_test}} project as a new submodule. This will serve as a complete, working reference for the corrected implementation.

git submodule add https://github.com/PatrickHeaney/ai_agent_test0103.git example_code/{{most_recent_test}}`

#### Step 2: Review Lessons Learned and create Upgrade Plan

your next task is to review all the lesson_* files summarize then create an upgrade_plan0104.md file and save it in the @1_backlog/ folder.  then review and    │
│    update the @start_clone_create.md, @PLANNING.md, @TASK.md, and @README.md so that these issues are not create again by a new ai coading agent assiged to build │
│     out ai_agen_test0104.  The goal is that these 4 files, plus @GEMINI.md will enable an ai coding assistant to implmeent iteration 1 of @idea.md
