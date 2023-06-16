{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "89b80363",
   "metadata": {},
   "outputs": [],
   "source": [
    "#q1\n",
    "#store the data in 4d array(4,4,2,7)\n",
    "\n",
    "import numpy as np\n",
    "\n",
    "x=np.array([[[[11,8,6,12,7,9,8],[28,32,24,25,28,27,32]],        \n",
    "                 [[7,10,10,-13,8,14,9],[26,31,25,21,28,30,22]],\n",
    "                 [[9,6,13,8,6,6,13],[24,30,24,27,25,20,25]],\n",
    "                 [[13,13,13,6,15,7,9],[29,20,24,23,21,24,29]]],\n",
    " \n",
    "                [[[11,8,11,9,13,11,9],[24,24,24,31,20,23,32]],\n",
    "                 [[13,7,10,15,13,7,10],[29,29,24,25,28,32,28]],                      [[8,13,8,8,15,12,11],[30,27,28,21,27,31,25]],\n",
    "                 [[13,12,15,13,11,7,6],[29,26,30,26,22,32,27]]],\n",
    "\n",
    "                [[[5,3,4,5,3,3,21],[19,18,18,18,22,2,5]],\n",
    "                 [[5,6,6,4,7,7,21],[20,18,19,20,20,7,2]],\n",
    "                 [[7,6,5,7,7,5,19],[20,20,22,18,20,4,3]],\n",
    "                 [[8,7,6,2,6,4,18],[20,19,22,18,19,4,7]]],\n",
    "                \n",
    "                [[[7,10,-10,11,11,11,22],[21,20,19,18,20,71,12]],\n",
    "                 [[10,7,8,7,10,7,19],[21,22,21,18,20,7,8]],\n",
    "                 [[10,10,12,7,7,7,21],[20,22,22,21,21,12,12]],\n",
    "                 [[7,7,8,10,11,12,18],[21,22,21,18,18,10,7]]]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "f30bb409",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Shape of the stored data (4, 4, 2, 7)\n",
      "Shape of the stored data 4\n"
     ]
    }
   ],
   "source": [
    "#q2\n",
    "print(\"Shape of the stored data\",x.shape)\n",
    "print(\"Shape of the stored data\",x.ndim)\n",
    "\n",
    "#here we find the shape and dimension of the array"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "72164876",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[[ 11,   8,   6,  12,   7,   9,   8],\n",
       "        [ 28,  32,  24,  25,  28,  27,  32]],\n",
       "\n",
       "       [[ 11,   8,  11,   9,  13,  11,   9],\n",
       "        [ 24,  24,  24,  31,  20,  23,  32]],\n",
       "\n",
       "       [[  5,   3,   4,   5,   3,   3,  21],\n",
       "        [ 19,  18,  18,  18,  22,   2,   5]],\n",
       "\n",
       "       [[  7,  10, -10,  11,  11,  11,  22],\n",
       "        [ 21,  20,  19,  18,  20,  71,  12]]])"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#q3\n",
    "print(x[:,0,:,:])\n",
    "\n",
    "\n",
    "#Here we find the daily temperature for the first week of each month"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "dea6a6b7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[[ 8 32]\n",
      "  [10 31]\n",
      "  [ 6 30]\n",
      "  [13 20]]\n",
      "\n",
      " [[ 8 24]\n",
      "  [ 7 29]\n",
      "  [13 27]\n",
      "  [12 26]]\n",
      "\n",
      " [[ 3 18]\n",
      "  [ 6 18]\n",
      "  [ 6 20]\n",
      "  [ 7 19]]\n",
      "\n",
      " [[10 20]\n",
      "  [ 7 22]\n",
      "  [10 22]\n",
      "  [ 7 22]]]\n"
     ]
    }
   ],
   "source": [
    "#q4\n",
    "print(x[:,:,:,1])\n",
    "\n",
    "#temperature for tuesday of each month and week"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "cfce6135",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[[24 24 24 31 20]\n",
      "  [29 29 24 25 28]\n",
      "  [30 27 28 21 27]\n",
      "  [29 26 30 26 22]]\n",
      "\n",
      " [[21 20 19 18 20]\n",
      "  [21 22 21 18 20]\n",
      "  [20 22 22 21 21]\n",
      "  [21 22 21 18 18]]]\n"
     ]
    }
   ],
   "source": [
    "#q5\n",
    "a=x[1:4:2,:,1,0:5]\n",
    "print(a)\n",
    "\n",
    "#the maximum temperature for all the weekdays of Dec and Feb"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "9419539f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(array([0, 0, 1, 1, 2, 2, 2, 3, 3]), array([2, 4, 0, 3, 1, 4, 5, 3, 5]))\n",
      "6\n"
     ]
    }
   ],
   "source": [
    "#q6\n",
    "b=x[0,:,0,:]\n",
    "w1={0:\"week(1)\",1:\"week(2)\",2:\"week(3)\",3:\"week(4)\"}\n",
    "d1={0:\"monday\",1:\"tuesday\",2:\"wednesday\",3:\"thrusday\",4:\"friday\",5:\"saturday\",7:\"sunday\"}\n",
    "\n",
    "c=np.where(b<8)\n",
    "print(c)\n",
    "print(b[0,2])\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "6c75cd55",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "week(1)   wednesday\n",
      "week(1)   friday\n",
      "week(2)   monday\n",
      "week(2)   thrusday\n",
      "week(3)   tuesday\n",
      "week(3)   friday\n",
      "week(3)   saturday\n",
      "week(4)   thrusday\n",
      "week(4)   saturday\n"
     ]
    }
   ],
   "source": [
    "for i in range(len(c[0])):\n",
    "    print(w1[c[0][i]],\" \",d1[c[1][i]])\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "7cab5499",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[[24 24 24 31 20 23 32]\n",
      "  [29 29 24 25 28 32 28]\n",
      "  [30 27 28 21 27 31 25]\n",
      "  [29 26 30 26 22 32 27]]\n",
      "\n",
      " [[19 18 18 18 22  2  5]\n",
      "  [20 18 19 20 20  7  2]\n",
      "  [20 20 22 18 20  4  3]\n",
      "  [20 19 22 18 19  4  7]]]\n"
     ]
    }
   ],
   "source": [
    "ba=x[1:3,:,1,:]\n",
    "print(ba)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5094a855",
   "metadata": {},
   "source": [
    "All the days along with the week number in November when the\n",
    "minimum temperature was less than 8 degrees."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "00428316",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\n",
       "        0, 0, 0, 0, 0, 1, 1, 1]),\n",
       " array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3,\n",
       "        3, 3, 3, 3, 3, 0, 2, 3]),\n",
       " array([0, 1, 2, 3, 5, 6, 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, 0, 1,\n",
       "        2, 3, 4, 5, 6, 4, 2, 2]))"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#q7\n",
    "xp=np.where(ba>20)\n",
    "xp"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "940c4e23",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Data of dec and jan when max day temp greator than 20\n",
      "dec jan\n",
      "0    0\n",
      "0    0\n",
      "0    0\n",
      "0    0\n",
      "0    0\n",
      "0    0\n",
      "0    1\n",
      "0    1\n",
      "0    1\n",
      "0    1\n",
      "0    1\n",
      "0    1\n",
      "0    1\n",
      "0    2\n",
      "0    2\n",
      "0    2\n",
      "0    2\n",
      "0    2\n",
      "0    2\n",
      "0    2\n",
      "0    3\n",
      "0    3\n",
      "0    3\n",
      "0    3\n",
      "0    3\n",
      "0    3\n",
      "0    3\n",
      "1    0\n",
      "1    2\n",
      "1    3\n"
     ]
    }
   ],
   "source": [
    "print(\"Data of dec and jan when max day temp greator than 20\")\n",
    "print(\"dec jan\")\n",
    "for i in range(len(xp[0])):\n",
    "    print(xp[0][i],\"  \",xp[1][i])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "58a20428",
   "metadata": {},
   "source": [
    "All the weeks in Dec and Jan where the maximum temperature has\n",
    "crossed a threshold of 20 degrees.\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "188edbd1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(array([1]), array([0]), array([3]))\n",
      "(array([], dtype=int64), array([], dtype=int64), array([], dtype=int64))\n"
     ]
    }
   ],
   "source": [
    "#q8\n",
    "mean=np.mean(x[:,:,:,:])\n",
    "q1=np.percentile(x[:,:,:,:],25)\n",
    "q3=np.percentile(x[:,:,:,:],75)\n",
    "iqr=q3-q1\n",
    "outlier_1=mean-1.5*iqr\n",
    "outlier_2=mean+1.5*iqr\n",
    "y=np.where(x[0]<outlier_1)\n",
    "z=np.where(x[0]>outlier_2)\n",
    "print(y)\n",
    "print(z)\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7095e2c3",
   "metadata": {},
   "source": [
    "Absurd values present in the dataset(like some temp\n",
    "which should not be present in the data)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9680ba4c",
   "metadata": {},
   "outputs": [],
   "source": [
    "# q9\n",
    "#To find the outliers we have to follow following steps\n",
    "#step1:-find mean of the array\n",
    "#step2:-find quartile1 and quartile 3\n",
    "#step3:-find iqr(q3-q1)\n",
    "#step4:-find outliers using mean and iqr"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "e119c212",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-5.8705357142857135\n",
      "36.879464285714285\n",
      "(array([0, 3]), array([1, 0]), array([0, 0]), array([3, 2]))\n",
      "(array([3]), array([0]), array([1]), array([5]))\n"
     ]
    }
   ],
   "source": [
    "#q10\n",
    "mean=np.mean(x[:,:,:,:])\n",
    "q1=np.percentile(x[:,:,:,:],25)\n",
    "q3=np.percentile(x[:,:,:,:],75)\n",
    "iqr=q3-q1\n",
    "outlier_1=mean-1.5*iqr\n",
    "outlier_2=mean+1.5*iqr\n",
    "print(outlier_1)\n",
    "print(outlier_2)\n",
    "print(np.where(x[:,:,:,:]<outlier_1))\n",
    "print(np.where(x[:,:,:,:]>outlier_2))\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0d287c80",
   "metadata": {},
   "source": [
    "print the indexes of all the outlier(unusual) values present in\n",
    "the above dataset."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "f06d5b71",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[[11  8  6 12  7  9  8]\n",
      "  [28 32 24 25 28 27 32]]\n",
      "\n",
      " [[ 7 10 10  8  8 14  9]\n",
      "  [26 31 25 21 28 30 22]]\n",
      "\n",
      " [[ 9  6 13  8  6  6 13]\n",
      "  [24 30 24 27 25 20 25]]\n",
      "\n",
      " [[13 13 13  6 15  7  9]\n",
      "  [29 20 24 23 21 24 29]]]\n",
      "[[[11  8  6 12  7  9  8]\n",
      "  [28 32 24 25 28 27 32]]\n",
      "\n",
      " [[ 7 10 10  8  8 14  9]\n",
      "  [26 31 25 21 28 30 22]]\n",
      "\n",
      " [[ 9  6 13  8  6  6 13]\n",
      "  [24 30 24 27 25 20 25]]\n",
      "\n",
      " [[13 13 13  6 15  7  9]\n",
      "  [29 20 24 23 21 24 29]]]\n"
     ]
    }
   ],
   "source": [
    "#q11\n",
    "x[0][x[0]<outlier_1]=np.mean(x[0,:,0,:])\n",
    "print(x[0])\n",
    "x[0][x[0]>outlier_2]=np.mean(x[0,:,1,:])\n",
    "print(x[0])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c897e663",
   "metadata": {},
   "source": [
    " Replace the outliers with an Mean value."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "064f4ab7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "21.848214285714285"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#q12\n",
    "np.average(x[:,:,1,:])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b9471310",
   "metadata": {},
   "source": [
    " The average max temperature for the winter months in Jaipur."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "0ee798f0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "week 1 minimum temp of nov 10.285714285714286\n",
      "week 2 minimum temp of nov 10.714285714285714\n",
      "week 3 minimum temp of nov 10.714285714285714\n",
      "week 4 minimum temp of nov 11.0\n"
     ]
    }
   ],
   "source": [
    "#q13\n",
    "min=x[1,0,0,:]\n",
    "print(\"week 1 minimum temp of nov\",np.average(min))\n",
    "print(\"week 2 minimum temp of nov\",np.average(x[1,1,0,:]))\n",
    "print(\"week 3 minimum temp of nov\",np.average(x[1,2,0,:]))\n",
    "print(\"week 4 minimum temp of nov\",np.average(x[1,3,0,:]))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "11de4966",
   "metadata": {},
   "source": [
    "The weekly min avg temp for the month of Dec in Jaipur"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "def321a6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "average temp of dec and jan 15.035714285714286\n"
     ]
    }
   ],
   "source": [
    "#q14\n",
    "x[1:3,:,:,:]\n",
    "print(\"average temp of dec and jan\",np.average(x[1:3,:,:,:]))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0e0fe287",
   "metadata": {},
   "source": [
    " The overall avg temp for the months Dec and Jan"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "1ad55a00",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n",
      "(array([1, 1, 1]), array([0, 1, 3]), array([1, 1, 0]), array([5, 6, 3]))\n",
      "janurary   week(1)   saturday\n",
      "janurary   week(2)   sunday\n",
      "janurary   week(4)   thrusday\n"
     ]
    }
   ],
   "source": [
    "#q15\n",
    "k=np.amin(x[1:3,:,:,:])\n",
    "z=np.where(x[1:3,:,:,:]==k)\n",
    "m1={0:\"dec\",1:\"janurary\"}\n",
    "w1={0:\"week(1)\",1:\"week(2)\",2:\"week(3)\",3:\"week(4)\"}\n",
    "d1={0:\"monday\",1:\"tuesday\",2:\"wednesday\",3:\"thrusday\",4:\"friday\",5:\"saturday\",6:\"sunday\"}\n",
    "print(k)\n",
    "print(z)\n",
    "for i in range(len(z[0])):\n",
    "    print(m1[z[0][i]],\" \",w1[z[1][i]],\" \",d1[z[3][i]])\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "76734c3f",
   "metadata": {},
   "source": [
    " The least temp experienced by the city in the month of Dec and\n",
    "Jan. Also exact date( Day/Week/Month) for the same."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "de158271",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "feb   week(1)   saturday\n"
     ]
    }
   ],
   "source": [
    "#q16\n",
    "x[3,:,:,:]\n",
    "q16=np.amax(x[3,:,:,:])\n",
    "m1={0:\"nov\",1:\"dec\",2:\"jan\",3:\"feb\"}\n",
    "w1={0:\"week(1)\",1:\"week(2)\",2:\"week(3)\",3:\"week(4)\"}\n",
    "d1={0:\"monday\",1:\"tuesday\",2:\"wednesday\",3:\"thrusday\",4:\"friday\",5:\"saturday\",6:\"sunday\"}\n",
    "q1=np.where(x[3,:,:,:]==q16)\n",
    "for i in range(len(q1[0])):\n",
    "    print(\"feb\",\" \",w1[z[1][i]],\" \",d1[z[3][i]])\n",
    "    \n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c434b233",
   "metadata": {},
   "source": [
    " The max temp in the month of Feb and return its\n",
    "date(Day/Week/Month)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "d8dca9dc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "17.642857142857142"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#q17\n",
    "nov=x[0,:,1,:]\n",
    "z=np.average(x[0,:,:,:])\n",
    "print(z)\n",
    "np.where(nov<z)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bd0f6cc4",
   "metadata": {},
   "source": [
    " The days in the month of Nov where the max temp of the day\n",
    "dropped below the avg temp of the month. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "12ae489d",
   "metadata": {},
   "outputs": [],
   "source": [
    "#q18\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "186ca4c3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[[[ 43,  40,  38,  44,  39,  41,  40],\n",
       "         [ 60,  64,  56,  57,  60,  59,  64]],\n",
       "\n",
       "        [[ 39,  42,  42,  19,  40,  46,  41],\n",
       "         [ 58,  63,  57,  53,  60,  62,  54]],\n",
       "\n",
       "        [[ 41,  38,  45,  40,  38,  38,  45],\n",
       "         [ 56,  62,  56,  59,  57,  52,  57]],\n",
       "\n",
       "        [[ 45,  45,  45,  38,  47,  39,  41],\n",
       "         [ 61,  52,  56,  55,  53,  56,  61]]],\n",
       "\n",
       "\n",
       "       [[[ 43,  40,  43,  41,  45,  43,  41],\n",
       "         [ 56,  56,  56,  63,  52,  55,  64]],\n",
       "\n",
       "        [[ 45,  39,  42,  47,  45,  39,  42],\n",
       "         [ 61,  61,  56,  57,  60,  64,  60]],\n",
       "\n",
       "        [[ 40,  45,  40,  40,  47,  44,  43],\n",
       "         [ 62,  59,  60,  53,  59,  63,  57]],\n",
       "\n",
       "        [[ 45,  44,  47,  45,  43,  39,  38],\n",
       "         [ 61,  58,  62,  58,  54,  64,  59]]],\n",
       "\n",
       "\n",
       "       [[[ 37,  35,  36,  37,  35,  35,  53],\n",
       "         [ 51,  50,  50,  50,  54,  34,  37]],\n",
       "\n",
       "        [[ 37,  38,  38,  36,  39,  39,  53],\n",
       "         [ 52,  50,  51,  52,  52,  39,  34]],\n",
       "\n",
       "        [[ 39,  38,  37,  39,  39,  37,  51],\n",
       "         [ 52,  52,  54,  50,  52,  36,  35]],\n",
       "\n",
       "        [[ 40,  39,  38,  34,  38,  36,  50],\n",
       "         [ 52,  51,  54,  50,  51,  36,  39]]],\n",
       "\n",
       "\n",
       "       [[[ 39,  42,  22,  43,  43,  43,  54],\n",
       "         [ 53,  52,  51,  50,  52, 103,  44]],\n",
       "\n",
       "        [[ 42,  39,  40,  39,  42,  39,  51],\n",
       "         [ 53,  54,  53,  50,  52,  39,  40]],\n",
       "\n",
       "        [[ 42,  42,  44,  39,  39,  39,  53],\n",
       "         [ 52,  54,  54,  53,  53,  44,  44]],\n",
       "\n",
       "        [[ 39,  39,  40,  42,  43,  44,  50],\n",
       "         [ 53,  54,  53,  50,  50,  42,  39]]]])"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#q19\n",
    "y=x+32\n",
    "y"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "40cbf6ea",
   "metadata": {},
   "source": [
    " The above data is appropriate for an audience who follow the metric system of measurement. Create an array that holds the same data but presented in Fahrenheit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "6c458ae8",
   "metadata": {},
   "outputs": [],
   "source": [
    "#q20\n",
    "a=np.average(x[1,0,:,:])\n",
    "b=np.average(x[1,1,:,:])\n",
    "c=np.average(x[1,2,:,:])\n",
    "d=np.average(x[1,3,:,:])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "c967f16b",
   "metadata": {},
   "outputs": [],
   "source": [
    "e=np.array([a,b,c,d])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "d62f195d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([19.28571429, 19.21428571, 18.85714286, 17.85714286])"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "f=np.sort(e)[::-1]\n",
    "f"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9ed5df9c",
   "metadata": {},
   "source": [
    " Sort the above data in descending order on the basis of weekly average for the month of Dec."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "244e53e2",
   "metadata": {},
   "outputs": [],
   "source": [
    "#q21"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "369f1a8f",
   "metadata": {},
   "outputs": [],
   "source": [
    "a=np.average(x[0,:,:,0:3])\n",
    "b=np.average(x[1,:,:,0:3])\n",
    "c=np.average(x[2,:,:,0:3])\n",
    "d=np.average(x[3,:,:,0:3])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "0643c5ec",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([18.875     , 18.16666667, 14.08333333, 12.625     ])"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "e=np.array([a,b,c,d])\n",
    "f=np.sort(e)[::-1]\n",
    "f"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7826a548",
   "metadata": {},
   "source": [
    " Sort the temp of the first three days of each month in descending order on the basis of overall average for the whole winter."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "97caa84c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[[ 17,  24,  18,  13,  21,  18,  24],\n",
       "        [ 19,  21,  15,  34,  20,  16,  13],\n",
       "        [ 15,  24,  11,  19,  19,  14,  12],\n",
       "        [ 16,   7,  11,  17,   6,  17,  20]],\n",
       "\n",
       "       [[ 13,  16,  13,  22,   7,  12,  23],\n",
       "        [ 16,  22,  14,  10,  15,  25,  18],\n",
       "        [ 22,  14,  20,  13,  12,  19,  14],\n",
       "        [ 16,  14,  15,  13,  11,  25,  21]],\n",
       "\n",
       "       [[ 14,  15,  14,  13,  19,  -1, -16],\n",
       "        [ 15,  12,  13,  16,  13,   0, -19],\n",
       "        [ 13,  14,  17,  11,  13,  -1, -16],\n",
       "        [ 12,  12,  16,  16,  13,   0, -11]],\n",
       "\n",
       "       [[ 14,  10,  29,   7,   9,  60, -10],\n",
       "        [ 11,  15,  13,  11,  10,   0, -11],\n",
       "        [ 10,  12,  10,  14,  14,   5,  -9],\n",
       "        [ 14,  15,  13,   8,   7,  -2, -11]]])"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#q22\n",
    "x[:,:,1,:]-x[:,:,0,:]\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bafca444",
   "metadata": {},
   "source": [
    " Create an array that stores the difference between the min and max temp for each day in all the winter months."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "2b7fa2fd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[[  4,  -8,   1,   3,  -1,   5],\n",
       "        [  5,  -6,  -4,   7,   2,  -8],\n",
       "        [  6,  -6,   3,  -2,  -5,   5],\n",
       "        [ -9,   4,  -1,  -2,   3,   5]],\n",
       "\n",
       "       [[  0,   0,   7, -11,   3,   9],\n",
       "        [  0,  -5,   1,   3,   4,  -4],\n",
       "        [ -3,   1,  -7,   6,   4,  -6],\n",
       "        [ -3,   4,  -4,  -4,  10,  -5]],\n",
       "\n",
       "       [[ -1,   0,   0,   4, -20,   3],\n",
       "        [ -2,   1,   1,   0, -13,  -5],\n",
       "        [  0,   2,  -4,   2, -16,  -1],\n",
       "        [ -1,   3,  -4,   1, -15,   3]],\n",
       "\n",
       "       [[ -1,  -1,  -1,   2,  51, -59],\n",
       "        [  1,  -1,  -3,   2, -13,   1],\n",
       "        [  2,   0,  -1,   0,  -9,   0],\n",
       "        [  1,  -1,  -3,   0,  -8,  -3]]])"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#q23\n",
    "t1=x[:,:,1,:]\n",
    "t2=np.diff(t1,axis=2)\n",
    "t2"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fd451f84",
   "metadata": {},
   "source": [
    " The difference between The max temp of two consecutive days for each month of winter season."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "4f6f7095",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[[  4,  -8,   1,   3,  -1,   5],\n",
       "        [  5,  -6,  -4,   7,   2,  -8],\n",
       "        [  6,  -6,   3,  -2,  -5,   5],\n",
       "        [ -9,   4,  -1,  -2,   3,   5]],\n",
       "\n",
       "       [[  0,   0,   7, -11,   3,   9],\n",
       "        [  0,  -5,   1,   3,   4,  -4],\n",
       "        [ -3,   1,  -7,   6,   4,  -6],\n",
       "        [ -3,   4,  -4,  -4,  10,  -5]],\n",
       "\n",
       "       [[ -1,   0,   0,   4, -20,   3],\n",
       "        [ -2,   1,   1,   0, -13,  -5],\n",
       "        [  0,   2,  -4,   2, -16,  -1],\n",
       "        [ -1,   3,  -4,   1, -15,   3]],\n",
       "\n",
       "       [[ -1,  -1,  -1,   2,  51, -59],\n",
       "        [  1,  -1,  -3,   2, -13,   1],\n",
       "        [  2,   0,  -1,   0,  -9,   0],\n",
       "        [  1,  -1,  -3,   0,  -8,  -3]]])"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#q24\n",
    "t3=x[:,:,0,:]\n",
    "t4=np.diff(t1,axis=2)\n",
    "t4\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3abdd0d0",
   "metadata": {},
   "source": [
    " The difference between the minimum temp of two consecutive days for each month of the winter season."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "be9c5787",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([  4,  -8,   1,   3,  -1,   5,   5,  -6,  -4,   7,   2,  -8,   6,\n",
       "        -6,   3,  -2,  -5,   5,  -9,   4,  -1,  -2,   3,   5,   0,   0,\n",
       "         7, -11,   3,   9,   0,  -5,   1,   3,   4,  -4,  -3,   1,  -7,\n",
       "         6,   4,  -6,  -3,   4,  -4,  -4,  10,  -5,  -1,   0,   0,   4,\n",
       "       -20,   3,  -2,   1,   1,   0, -13,  -5,   0,   2,  -4,   2, -16,\n",
       "        -1,  -1,   3,  -4,   1, -15,   3,  -1,  -1,  -1,   2,  51, -59,\n",
       "         1,  -1,  -3,   2, -13,   1,   2,   0,  -1,   0,  -9,   0,   1,\n",
       "        -1,  -3,   0,  -8,  -3,   4,  -8,   1,   3,  -1,   5,   5,  -6,\n",
       "        -4,   7,   2,  -8,   6,  -6,   3,  -2,  -5,   5,  -9,   4,  -1,\n",
       "        -2,   3,   5,   0,   0,   7, -11,   3,   9,   0,  -5,   1,   3,\n",
       "         4,  -4,  -3,   1,  -7,   6,   4,  -6,  -3,   4,  -4,  -4,  10,\n",
       "        -5,  -1,   0,   0,   4, -20,   3,  -2,   1,   1,   0, -13,  -5,\n",
       "         0,   2,  -4,   2, -16,  -1,  -1,   3,  -4,   1, -15,   3,  -1,\n",
       "        -1,  -1,   2,  51, -59,   1,  -1,  -3,   2, -13,   1,   2,   0,\n",
       "        -1,   0,  -9,   0,   1,  -1,  -3,   0,  -8,  -3])"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#q25\n",
    "z=np.concatenate((t2,t4))\n",
    "z.flatten()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "97874170",
   "metadata": {},
   "source": [
    " Create an array by combining the data present in arrays created in q.23 and q.24, to store the difference between the min and max temp of each day of all the months for the whole winter season, in a single array."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d6f72715",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
