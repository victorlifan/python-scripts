{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "## 9.3 Quiz: Implement my_enumerate"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Lesson 1: Why Python Programming\n",
      "Lesson 2: Data Types and Operators\n",
      "Lesson 3: Control Flow\n",
      "Lesson 4: Functions\n",
      "Lesson 5: Scripting\n"
     ]
    }
   ],
   "source": [
    "lessons = [\"Why Python Programming\", \"Data Types and Operators\", \"Control Flow\", \"Functions\", \"Scripting\"]\n",
    "\n",
    "def my_enumerate(iterable, start=0):\n",
    "    # Implement your generator function here\n",
    "     for starts, classes in enumerate(iterable):\n",
    "         yield start, classes\n",
    "         start += 1            \n",
    "\n",
    "for i, lesson in my_enumerate(lessons, 1):\n",
    "    print(\"Lesson {}: {}\".format(i, lesson))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "##Quiz: Chunker"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0, 1, 2, 3]\n",
      "[4, 5, 6, 7]\n",
      "[8, 9, 10, 11]\n",
      "[12, 13, 14, 15]\n",
      "[16, 17, 18, 19]\n",
      "[20, 21, 22, 23]\n",
      "[24]\n"
     ]
    }
   ],
   "source": [
    "\n",
    "for i in range(0, 25, 4):\n",
    "    x = range(25)[i:i + 4]\n",
    "    print(list(x))\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
