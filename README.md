# The Original Problem

![](graphics/original_mit_crew-01.png)

**Computer Vision** has a very interesting history. It's roots really go all the way back to the beginning of computing and **Artifical Intelligence.** In these early days, it was unknown just how easy or difficult it would be to recreate the function of the human visual system. A great example of this is the 1966 MIT Summer Vision Project. Marvin Minsky and Seymour Papert, co-directors of the MIT AI Labratory, begun the summer with some ambitious goals:

![](graphics/summer_project_abstract-01.png)


Minsky and Papert assigned Gerald Sussman, an MIT undergraduate studunt as project lead, and setup specific goals for the group around recognizing specific objects in images, and seperating these objects from their backgrounds. 

![](graphics/summer_project_goals-01.png)

Just how hard is it to acheive the goals Minsky and Papert laid out? How has the field of computer vision advance since that summer? Are these tasks trivial now, 50+ years later? Do we understand how the human visual system works? Just how hard *is* computer vision and how far have we come?


## This Repository

This repository is all about spending some time the with **the original problem** posed by Minsky and Papert. Working through this problem is a great way to begin learning **computer vision.** 

![](graphics/brick_ball_cylinder_2.gif)


The repository is broadly divided into two areas: **notebooks** and a **programming challenge**. The programming challenge is described in more detail below, and closely follows the goals setup by Minsky and Papert back in 1966. The notebooks are here to give you some help along the way. 


## Notebooks

| Section |   Notebook    | Required Reading/Viewing | Additional Reading/Viewing | Code Developed | 
| ------- | ------------- | --------------------------- | -------------------------- | -------------- |
| 1       | [The Original Problem](http://www.welchlabs.io/unccv/the_original_problem/notebooks/top.html) | [The Summer Vision Project](papers/summer_vision_project.pdf) | - | - |
| 2       | [Robert's Cross](http://www.welchlabs.io/unccv/the_original_problem/notebooks/roberts_cross.html) | [Only Abstact and Pages 25-27 - Machine perception of 3d solids](papers/roberts_thesis.pdf)| - | convert_to_grayscale, roberts_cross |
| 3       | [Image Filtering](http://www.welchlabs.io/unccv/the_original_problem/notebooks/image_filtering.html) | [How Blurs & Filters Work - Computerphile](https://youtu.be/C_zFhWdM4ic) | - | make_gaussian_kernel, filter_2d |
| 4 | [The Sobel–Feldman Operator](http://www.welchlabs.io/unccv/the_original_problem/notebooks/sobel.html) | [Finding the Edges (Sobel Operator) - Computerphile](https://youtu.be/uihBwtPIBxM) | [History of Sobel](papers/history_and_def_of_sobel_operator.pdf) | - |
| 5 | [The Hough Transform [Part 1]](http://www.welchlabs.io/unccv/the_original_problem/notebooks/hough_1.html) | | [Pattern classification Section 9.2.3](http://a.co/4o6oefR),  [Bubble Chamber Video](https://www.youtube.com/watch?v=basLNz6frO8)| - |
| 6 | [The Hough Transform [Part 2]](http://www.welchlabs.io/unccv/the_original_problem/notebooks/hough_2.html) | [How the Hough Transform was Invented](http://www.rci.rutgers.edu/~shunsun/resource/Hough_Transform.pdf) | [Use of the Hough transformation to detect lines and curves in pictures.](https://www.cse.unr.edu/~bebis/CS474/Handouts/HoughTransformPaper.pdf) | HoughAccumulator|

### Viewing Notebooks
The links in the table above take you to externally hosted HTML exports of the notebooks. This works pretty well, except html won't render embedded slide shows unfortunately. The best way to view the notebooks is to clone this repo and run them yourself! Checkout the [setup instructions below](https://github.com/unccv/the_original_problem#setup).

### Animations
The notebooks in this repository make frequent use of gif animations. These files are pretty large, so we don't store them on github, and they unfortunately won't show up when viewing the notebooks via github. The ideal way to view the notebooks is to clone the repo, download the videos, and use the recommended jupyterthemes below. Instructions on downloading videos are [below](http://github.com/unccv/the_original_problem#downloading-videos).

### Note on Launching the Jupyter Notebooks
To properly view the images and animations, please launch your jupyter notebook from the root directory of this repository. 


## Programming Challenge

### Instructions

- Write a method `classify.py` that takes in an image and returns a prediction - ball, brick, or cylinder.
- An example script in located in challenge/sample_student.py
- Your script will be automatically evaluated on a set of test images. 
- The testing images are quite similar to the training images, and organized into the same difficulty categories. 
- You are allowed 10 submissions to the evaluation server, which will provide immediate feedback.

### The Data

#### Easy Examples
![](graphics/easy_examples.png)

### Grading 
Following the progression set out the MIT the summer project, we'll start with easy images, and move to more difficult image with more complex backgrounds as we progress. For each difficulty level, we will compute the average accuracy of your classifier. We will then compute an average overall accuracy, weighting easier examples more: 

````
overall_accuracy = 0.5*accuracy_easy 
                 + 0.2*accuracy_medium_1 
                 + 0.2*accuracy_medium_2 
                 + 0.1*accuracy_hard 
````

| Overall Accuracy | Points |
| ------------- |:-------------:| 
| >= 0.6         | 10/10 | 
| 0.55 <= a < 0.6  | 9/10|  
| 0.5 <= a < 0.55 | 8/10 |   
| 0.45 <= a < 0.5 | 7/10 | 
| 0.40 <= a < 0.45 | 6/10 | 
| 0.35 <= a < 0.40 | 5/10 | 
| a < 0.35 | 4/10 |
| Non-running code | 0/10|

#### A quick note on difficulty
Depending on your background, this challenge may feel a bit like getting thrown into the deep end. If it feels a bit daunting - that's ok! Half of the purpose of this assignement is to help you develop an appreciation for **why** computer vision is so hard. As you may have already guessed, Misky, Sussman, and Papert did **not** reach their summer goals - and I'm not expecting you to either. The grading table above reflects this - for example, if you're able to get 90% accuracy on the easy examples, and simply guess randomly on the rest of the examples, you'll earn 10/10 points. 

## Setup 

The Python 3 [Anaconda Distribution](https://www.anaconda.com/download) is the easiest way to get going with the notebooks and code presented here. 

(Optional) You may want to create a virtual environment for this repository: 

~~~
conda create -n cv python=3 
source activate cv
~~~

You'll need to install the jupyter notebook to run the notebooks:

~~~
conda install jupyter

# You may also want to install nb_conda (Enables some nice things like change virtual environments within the notebook)
conda install nb_conda
~~~

This repository requires the installation of a few extra packages, you can install them all at once with:
~~~
pip install -r requirements.txt
~~~

(Optional) [jupyterthemes](https://github.com/dunovank/jupyter-themes) can be nice when presenting notebooks, as it offers some cleaner visual themes than the stock notebook, and makes it easy to adjust the default font size for code, markdown, etc. You can install with pip: 

~~~
pip install jupyterthemes
~~~

Recommend jupyter them for **presenting** these notebook (type into terminal before launching notebook):
~~~
jt -t grade3 -cellw=90% -fs=20 -tfs=20 -ofs=20 -dfs=20
~~~

Recommend jupyter them for **viewing** these notebook (type into terminal before launching notebook):
~~~
jt -t grade3 -cellw=90% -fs=14 -tfs=14 -ofs=14 -dfs=14
~~~

### Downloading Data
For larger files such as data and videos, I've provided download scripts to download these files from welchlabs.io. These files can be pretty big, so you may want to grab a cup of your favorite beverage to enjoy while downloading. The script can be run from within the jupyter notebooks or from the terminal:

~~~
python util/get_and_unpack.py -url http://www.welchlabs.io/unccv/the_original_problem/data/data.zip
~~~

Alternatively, you can download [download data manually](http://www.welchlabs.io/unccv/the_original_problem/data/data.zip), unzip and place in this directory. 


### Downloading Videos

Run the script below or call it from the notebooks:

~~~
python util/get_and_unpack.py -url http://www.welchlabs.io/unccv/the_original_problem/videos.zip
~~~

Alternatively, you can download [download videos manually](http://www.welchlabs.io/unccv/the_original_problem/videos.zip), unzip and place in this directory. 



