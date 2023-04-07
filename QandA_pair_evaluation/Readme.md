{\rtf1\ansi\ansicpg1252\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red113\green184\blue255;\red23\green23\blue23;\red202\green202\blue202;
}
{\*\expandedcolortbl;;\cssrgb\c50980\c77647\c100000;\cssrgb\c11765\c11765\c11765;\cssrgb\c83137\c83137\c83137;
}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # PS\
\uc0\u9679  The task is to build a machine learning model to filter out correct and incorrect\
question answer pairs.\
\
# Solution Approach\
\
\pard\pardeftab720\partightenfactor0

\f1\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 * \cf4 \strokec4 combined Question and Answer with a sep_token.\cb1 \
\cf2 \cb3 \strokec2 * \cf4 \strokec4 created label 1 for the provided question.\cb1 \
\cf2 \cb3 \strokec2 * \cf4 \strokec4 generated negative samples by either copying question into answer or shuffling answers for the question.\cb1 \
\cf2 \cb3 \strokec2 * \cf4 \strokec4 Created a custom classfication model, which takes inputs as embeddings of the sentences (derived from BERT Tokenizer)\cb1 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 and returns the label.\cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 * \cf4 \strokec4 Added the BERT layer in the model, that gives learned excellent representation of the words wrt context to the classifier.\cb1 \
\cf2 \cb3 \strokec2 * \cf4 \strokec4 Achieved 51% accuracy, which can be improved with generalisation techniques and more data and training.\cb1 \
}