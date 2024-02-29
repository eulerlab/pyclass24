## Exam programming project guidelines

- [Rules and grading of projects](https://github.com/eulerlab/python_course/blob/master/exams/Readme.md#rules-and-grading-of-projects)
- [Project deadlines and presentations](https://github.com/eulerlab/python_course/blob/master/exams/Readme.md#project-deadlines-and-presentations)
- [Guidelines for code](https://github.com/eulerlab/python_course/blob/master/exams/Readme.md#guidelines-for-code)
- [Projects](https://github.com/eulerlab/python_course/blob/master/exams/Readme.md#projects)

### Rules and grading of projects

- **Master students of the Neural & Behavioural class** must work on and present a programming project; the project will
  be not graded (pass/fail).
- All **other participants** must do the following in order to get credits for the course: Work on and submit a project.
  No assistance before submission.
- The projects may be one of the proposals listed below or one of your own ideas. Projects based on your own ideas are
  very welcome!
- __After project submission, we will select 3-4 projects for presentations, which means that the team needs to demonstrate their solution (likely in a Zoom call).__ 
- Your programming job will be evaluated according to the following criteria:

  | Criterion                                                                                                                                                                             | Weight |
    |---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
  | Complexity and scope of project ('difficulty and programming effort')                                                                                                                 | 20%    |
  | Functionality (program accomplishes job described in project description)                                                                                                             | 30%    |
  | Readability of code: compartmentalization, variable names, documentation (help text for function, particularly description of input & output variables, and comments throughout code) | 20%    |
  | Efficiency (speed, usage of memory, vectorized code, preallocation, etc.)                                                                                                             | 10%    |
  | Versatility of code: input & output arguments and error-checking and -handling                                                                                                        | 10%    |
  | Presentation                                                                                                                                                                          | 10%    |

Note that students are expected to choose a project with appropriate difficulty to their Python skills in order to
receive the best grade. Do not bite more than you can chew! Simple, but well written and documented program may score as
well as or even better than a sloppily written complex program.

**Warning** _Copying existing solutions or having AIs like chatGPT do your job will result in failing the exam!
Therefore, try to solve your selected project on your own._

### Project deadlines and presentations

Please submit your exam project as a **single .zip file** that contains **all files** (or folders) that are required for
your program to run:

- the name of the .zip file should be your last name(s).
- as a starting point for us, the .zip file has to contain a .ipynb (Jupyter notebook) file with instructions how to use
  your program. Give it the same name as the exam project (e.g., `exam_conways_game.ipynb`). In addition to the startup
  instructions, the notebook could contain example code how to use your program.
- executables (.exe files) are not allowed in the .zip file

When you are done but **no later that March 31, 2024**, drop the .zip file into the `Final exam projects` folder on
ILIAS.

### Guidelines for code

- If you choose to write a 'traditional' program, the 'core' code must reside within a central function, plus other
  functions, if needed. This function may be called by a script for the presentation (see below). Please give your
  central function a telling name, not something like 'main.py'.
- Also, if you choose a Jupyter notebook as basis for your project, your program needs to be well-organized into
  functions.
- The (central) function shall take input arguments and possibly produce output arguments to make the code versatile.
  For example, the spike threshold detector would certainly need a data array (or a data file name) and a threshold as
  inputs and return timestamp lists. Sanity checks of input variables must be performed and some precautionary measures
  against nonsense input should be taken. Try to catch common errors.
- The purpose of the function(s) and the nature of the input and output variables must be well explained in your code (
  e.g. the size of variables, data type, what kind of data etc.).
- Extensive documentation of the code should be provided. Place comments on top of the code lines they are supposed to
  comment, not in the same line as the code itself, and keep your comment in the visible part of the screen by starting
  new lines.
- Check out again the recommendations for good (Python) coding practice as discussed in Lectures 1 and 2. Your final
  code should be designed to be adaptable to other similar programming tasks and it should be comprehensible by others (
  e.g., your instructor).
- In terms of complexity and workload, the projects are designed for teams of a maximum of three. In the (exceptional)
  case of more people, you have to incorporate a few more features, which we will decide upon in individual
  negotiations.
- Make sure the data which your program will digest or generate during the presentation is of a manageable size so that
  your demo computations finish in finite time.
- For some of the projects there is already Python code around on the internet. It goes without saying that the task is
  NOT to do a simple copy-and-paste job. Detecting large chunks of verbatim copies of publicly available code or of code
  from the previous terms students will result in failing the course.
- Make sure that you observe any copyrights when using material (e.g., data, images, resources) of others.

### Projects

Most projects come as Jupyter notebooks with the instruction on top.

Rating of projects: The number (4 to 8) indicates programming effort, corresponding to the score for complexity and
scope mentioned above; The plus signs (+ to +++) indicated difficulty of the underlying science/analysis concepts.

- Spike threshold detector and time stamp generator (6,+)
- Reichardt motion detector (6, ++)
- Conway's game of life (7, ++)
- Langton’s ant (7,++)
- Crytography ABC (7, ++)
- Structure from motion (7,++)
- Forest fires (8,++)
- Kaggle challenge ()
- Pacman (7,++)

