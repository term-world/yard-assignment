'[![GatorGrader](../../actions/workflows/main.yml/badge.svg)](../../actions/workflows/main.yml)

Due Date: 18 September 2022, 11:59p

# `BRAND NEW BEAUTIFICATION PROPOSAL PROMPTS term-world TENANTS TO TIDY UP`

*Reported by `The Reporter` from `Roobrik`, on 12 September, 2022*

Last week `The Mayor` unveiled a new beautification program in an effort to make `term-world` *the* spot to be. This is the latest in a long line of proposals, projects, programs, and plans that `The Mayor` has been fervently working on to drive both tourism and residency within `term-world`.

This particular program targets the tight-knit communities that lie on the outskirts of our fair `term-world`. The appeal of neighborhoods like `Roobrik` and `Balzare` has gone under the microscope, and according to `The Mayor`, it has been found sorely wanting.

Partnering with `The Landlord` that exercises ownership over these despondent, dismal, and downright depressing domestic hovels, `The Mayor` has decreed that all building exteriors in the targeted communities must meet certain specific "Beautification Standard" metrics, within a week's time. Once the one week grace period is up, `The Mayor` is planning on leveraging his authority as `The Mayor` to evict non-compliant residents.

## Overview

In this set of activities we cover:

* functions: an essential part of good program design
* comments: writing helpful documentation for yourself and others
* more on variables with a focus on naming and data types

### Key facts about your yard

Across all files, you should have _at least_ 10 single-line comments added to _each_. Recall, a comment looks something like:

```python
# Leaving a comment
```

These should be descriptive and _NOT_ those left by `TODO`s. This assignment is looking for _original_ comments.

#### Treehouse

The dimensions for your treehouse are as follows (it's rectangular):

* `18` units in length
* `27` units in width
* walls are `7` units in height
* windows:
    * `8` units wide
    * `3` units tall
    * i.e.: they are rectangular
    * there are `6` of them
* the tree itself occupies `4` full units
    * it runs throught he center of the floor; how quaint
    * it requires a circular hole
    * the number to use with this is `math.pi`
* entryway is `5` units wide and tall
    * i.e. it is square
    * "squaring" something _may_ use exponents (not necessary)
      * recall from an earlier day that this operator is `**`

Using the above details, you should be able to cobble together `3` functions which represent the shapes you need.

##### Reflection

The `treehouse` also contains a `reflection.md` document. From this point onward in your experience in `term-world`, you'll be required to answer questions in the file as part of the assignment. Go there and have a look at the questions.

#### Tiller

Your flower bed is:

* `9` units wide
* `9` units long
* `6` units of dirt deep

#### FlowerBed

Completed correctly, you should see a `flowerbed.png` created after a successfuly run. This file is more of a mess than something that needs much help with its natural proceses. 

### Supporting media

[![YouTube thumbnail](http://img.youtube.com/vi/gnUwLG_3Jqs/hqdefault.jpg)](https://youtube.com/playlist?list=PLJvBsjwXNdlEzwfwkqA7TtDD0NtrexawE)


## Access `yard` content

The activities for this week primarily take place in your `yard`. This is an extension off of your garage. The grounds of your growing estate should look something like:

```
---------- 
| GARDEN |       ------------   --------   
----------       | WORKSHOP |---| YARD |
    |            ------------   --------
    |               /
----------     ----------
| HOUSE  |     | GARAGE |
---------|     ----------
    |              |
    |--------------|
```


Once you've navigated to the `workshop`, you'll need to follow a link to the repository to be cloned. This link is contained directly within `term-world`, and will be distributed to you at the appropriate time.

The link will direct you to a repository on GitHub. You'll need to click on the green `Code` button, ensure that `SSH` is selected, and then copy the link that appears in the window below. It might look something like `git@github.com.../your-named-repository`.

Once you've copied this link, navigate back to your terminal window and ensure you're still in the appropriate place (in this case, the topmost level of your `workshop`). Then, enter the command:

```
git clone COPIED-LINK-HERE
```

Be sure to replace the fragment `COPIED-LINK-HERE` with the link you copied.

While `pull` is used to *update* the contents of a repository that already exists in your local workspace, `clone` is used to *replicate* the contents of a repository from GitHub and copy them to your local workspace. The `house`, `garage`, and `backyard` all already existed in `term-world` before you showed up--we just needed to `pull` the updated contents for each respective folder in order to work with them.

Going forward most of the content you'll be engaging with will *not* already exist in `term-world`--you will need to `clone` the content first.

## Evaluating `yard` Content

In order to run the `grader` for Week 2, you'll need to be in the topmost level of the `backyard` folder. Once there, run the command:

```
gatorgrade
```

## Submitting `yard` content

Recall the order of operations for submitting repository changes to GitHub: `add`, `commit`, and `push`. Once in the appropriate folder (this should be the topmost folder for the repository in question, in this case, the `backyard`) run the following commands in order:

```
git add -A
```

```
git commit -m "DESCRIPTIVE COMMIT LABEL"
```

```
git push
```

As always, be sure to *frequently* `add`, `commit`, and `push` your work, simply because...

## `term-world Server Backup Policy`

**While we may use this server to store code, you are responsible for using GitHub as your main backup.**

In the event that the `term-world` server goes down for any unforeseen reason, your work may be lost. Though this server is backed up on a regular (i.e., weekly) basis, there is no guarantee that up-to-the-minute data for your work will be restored.

Remember: to err is human; to back up your work is *divine*.