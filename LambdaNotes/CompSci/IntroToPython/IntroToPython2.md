# Lambda's Problem solving Framework

Every problem can be broken down into smaller chunks. It's logical, if you can take an unsolvalble problem and break it into smaller more manageable chunks that are solveable, by solving each individual part you will solve the entire problem.

## UPER

1. Understand
2. Plan
3. Execute
4. Reflect

Almost all problems are a series of sub-problems.

### Understand

The most crucial thing to do before you do anything else is to understand all of the details of what the problem is asking you to do. One helpful starting point is to transcribe the description of the problem from the page into your own words

#### Questions

Here is a list of starter questions that might come up during this step:
- What are the inputs your code receives
- What is the range of input
- How big can the input be(how much data)
- What are the outputs your code produces
- What is the range of output
- How big can the output be(how much data)
- How performant must the code be
- What is missing from the task description
- Are there third-party stakeholders who we should consult
- What assumptions are you making

#### Actions
- The most important thing you can do during this stage is `ask questions`
- Do not fear this part of the process, if you have a question, others will too
- Identify the smaller components that make up the larger problem
- Try to digest the problem and comprehend it by rewriting the problem in your own words
- Diagram how the data flows through the problem
- Think like a villian
  - What inputs would break your program
- Where is the description of the problem incomplete

### Plan

This is where you will ask what steps will I take to solve the problem

You will take your description of the problem and transform it into a complete, actionable plan to solve that problem. If you find shortcomings in your understanding of the problem while you're planning, drop back to step 1 until you resolve the ambiguity

#### Questions
- Do you know the answer to a similar problem that has similar inputs and outputs
- Does my plan meet the performace requirements
- Can sorting the input data ahead of time lead to any improvements in time complexity
- Does your plan cover the edge cases

#### Actions
- Solve the problem like a human
- Break down the steps you take into small enough pieces for a computer to understand
- Approach the problem from many angles
- Get a brute-force solution as quickly as possible, even if it's not as performant as needed
- Come up with many plans of attack
- Try to solve a simpler version of the problem
- List the nouns and verbs in the problem description

### Execute

This is where you take your plan and convert it to actual working code.

This step isn't easy, but it's much easier if you've done agood job with steps 1 and 2.

#### Questions
- Think like a villain, does your implementation handle all inputs
- What language is best to solve this problem
- What is the best way to split this code into functional modules
- Are any of the modules reusable for later projects
- Does this functionality already exist

#### Actions
- Start a source code control repo
- Convert your pseudocode and outlines into actual code
- Remain as DRY as possible
- Document code as you write it
- Write code clearly enough that comments aren't necessary
- If you write code that's hackish or kludgy
- Follow the company style guide
- write unit tests as required
- write end-to-end as required

### Reflect
Is this implementation as good as I can make it?

#### Questions
- Does your solution work in all cases
- Is the solution performant enough
- Is the code documented
- In retrospect, what would you do differently

#### Actions
- Document or implement any changes that you still need to make to the code
- Document or remove any redundant code that you should refactor
- Remove unused code
- Document future shortcomings that you will need to address in the medium or long term
- Identify and document algorithms that you should replace with algorithms with better time complexity
- Identify and document or remove redundant computation
- Document any embarrassing code that you need to fix