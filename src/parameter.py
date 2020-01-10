import numpy as np


drug_list_with_protein_links = np.array([
          1,  10,  12,  13,  14,  15,  17,  18,  19,  20,  25,  27,  28,
         31,  33,  36,  37,  40,  41,  42,  43,  45,  50,  52,  53,  54,
         56,  57,  59,  62,  64,  66,  68,  70,  72,  73,  75,  77,  79,
         80,  82,  84,  87,  88,  92,  97,  99, 100, 103, 105, 106, 109,
        111, 114, 116, 119, 124, 125, 126, 127, 133, 134, 136, 137, 138,
        143, 146, 151, 152, 153, 154, 157, 158, 161, 163, 167, 168, 171,
        173, 174, 177, 180, 181, 183, 184, 185, 189, 190, 199, 201, 202,
        204, 205, 208, 210, 213, 215, 219, 222, 223, 224, 225, 229, 234,
        236, 237, 241, 252, 253, 254, 255, 257, 258, 259, 260, 263, 264,
        265, 269, 270, 271, 272, 274, 277, 278, 279, 281, 285, 288, 294,
        296, 299, 300, 304, 305, 308, 309, 310, 311, 313, 315, 317, 323,
        324, 325, 332, 334, 336, 338, 340, 344, 345, 346, 347, 348, 349,
        350, 354, 355, 356, 359, 363, 367, 369, 371, 372, 377, 379, 380,
        381, 383, 385, 386, 388, 389, 392, 393, 394, 396, 399, 401, 402,
        403, 407, 408, 409, 411, 414, 416, 418, 420, 421, 425, 428, 429,
        431, 432, 435, 438, 445, 446, 447, 454, 458, 459, 460, 461, 467,
        471, 479, 480, 481, 485, 487, 489, 490, 492, 493, 499, 502, 508,
        512, 514, 517, 518, 523, 524, 527, 528, 529, 530, 533, 534, 535,
        536, 537, 538, 540, 541, 542, 544, 545, 547, 548, 549, 550, 551,
        553, 557, 558, 561, 565, 566, 568, 570, 571, 572, 573, 574, 577,
        584, 585, 593, 597, 599, 602, 606, 609, 611, 614, 615, 616, 617,
        621, 624, 628, 631, 632, 636, 637, 639, 642, 643, 644])


drug_mask_with_protein_links = np.array([
         False,  True, False, False, False, False, False, False, False,
         False,  True, False,  True,  True,  True,  True, False,  True,
          True,  True,  True, False, False, False, False,  True, False,
          True,  True, False, False,  True, False,  True, False, False,
          True,  True, False, False,  True,  True,  True,  True, False,
          True, False, False, False, False,  True, False,  True,  True,
          True, False,  True,  True, False,  True, False, False,  True,
         False,  True, False,  True, False,  True, False,  True, False,
          True,  True, False,  True, False,  True, False,  True,  True,
         False,  True, False,  True, False, False,  True,  True, False,
         False, False,  True, False, False, False, False,  True, False,
          True,  True, False, False,  True, False,  True,  True, False,
         False,  True, False,  True, False, False,  True, False,  True,
         False, False,  True, False, False, False, False,  True,  True,
          True,  True, False, False, False, False, False,  True,  True,
         False,  True,  True,  True, False, False, False, False,  True,
         False, False,  True, False, False, False, False,  True,  True,
          True,  True, False, False,  True,  True, False, False,  True,
         False,  True, False, False, False,  True,  True, False, False,
          True, False,  True,  True, False, False,  True, False, False,
          True,  True, False,  True,  True,  True, False, False, False,
          True,  True, False, False, False, False, False, False, False,
         False,  True, False,  True,  True, False,  True,  True, False,
         False,  True, False,  True, False, False,  True, False,  True,
         False, False, False,  True, False, False,  True,  True,  True,
          True, False, False, False,  True, False, False, False, False,
          True, False,  True,  True, False, False, False,  True, False,
         False, False, False, False, False, False, False, False, False,
          True,  True,  True,  True, False,  True,  True,  True,  True,
         False, False,  True,  True,  True, False, False, False,  True,
          True,  True,  True, False,  True, False, False,  True,  True,
          True, False,  True, False, False, False,  True, False, False,
          True, False, False, False, False, False,  True, False,  True,
         False, False,  True,  True, False, False, False,  True,  True,
         False, False,  True,  True,  True,  True, False,  True, False,
          True, False,  True, False, False, False, False, False,  True,
          True,  True, False, False, False, False, False, False,  True,
         False,  True, False,  True, False,  True, False,  True, False,
         False, False,  True,  True,  True,  True,  True,  True,  True,
         False, False, False,  True,  True,  True, False, False,  True,
         False, False, False,  True, False, False, False,  True, False,
          True, False,  True,  True, False, False, False, False,  True,
         False,  True,  True,  True, False,  True, False,  True,  True,
         False,  True,  True, False, False,  True,  True,  True, False,
          True, False, False,  True, False,  True,  True,  True, False,
         False, False,  True,  True,  True, False,  True, False, False,
          True, False,  True, False,  True, False,  True,  True, False,
         False, False,  True, False, False,  True,  True, False,  True,
          True, False, False,  True, False, False,  True, False, False,
         False, False, False, False,  True,  True,  True, False, False,
         False, False, False, False,  True, False, False, False,  True,
          True,  True,  True, False, False, False, False, False,  True,
         False, False, False,  True, False, False, False, False, False,
         False, False,  True,  True,  True, False, False, False,  True,
         False,  True, False,  True,  True, False,  True,  True, False,
         False, False, False, False,  True, False, False,  True, False,
         False, False, False, False,  True, False, False, False,  True,
         False,  True, False, False,  True,  True, False, False, False,
         False,  True,  True, False, False,  True,  True,  True,  True,
         False, False,  True,  True,  True,  True,  True,  True, False,
          True,  True,  True, False,  True,  True, False,  True,  True,
          True,  True,  True, False,  True, False, False, False,  True,
          True, False, False,  True, False, False, False,  True,  True,
         False,  True, False,  True,  True,  True,  True,  True, False,
         False,  True, False, False, False, False, False, False,  True,
          True, False, False, False, False, False, False, False,  True,
         False, False, False,  True, False,  True, False, False,  True,
         False, False, False,  True, False, False,  True, False,  True,
         False, False,  True,  True,  True,  True, False, False, False,
          True, False, False,  True, False, False, False,  True, False,
         False,  True,  True, False, False, False,  True,  True, False,
          True, False, False,  True,  True,  True])