import random
import time
import math

# This gene map has no relation to actual genes and shortened for ease of use, but would still give opportunities for mutations
# Single stranded sequence for DNA expression, base pairs are not catagorized in anyway. Flexibility for mutation.
# Only stop sequence would be primers that could be represented by "atcatc".
# Sequence would be written (not scientifically accurate) but [target sequence][degree][stop sequence] (repeat).

gene_map = {

    # Utility Decoding Sequences

    "atcatc" : False,
    "at" : 1,
    "ac" : 2,
    "ag" : 3,
    "aa" : 4,
    "ta" : 5,
    "tc" : 6,
    "tg" : 7,
    "ca" : 8,
    "ct" : 9,
    "cg" : 10,

    # Utility Encoding Sequences
    
    1 : "at",
    2 : "ac",
    3 : "ag",
    4 : "aa",
    5 : "ta",
    6 : "tc", 
    7 : "tg",
    8 : "ca",
    9 : "ct",
    10 : "cg",

    # Gene Sequences

    "taa" : "spd", # speed/agility sequence
    "tac" : "str", # strength/power sequence
    "tat" : "int", # intelect sequence
    "tag" : "chr", # charisma sequence
    
    # Mutation Sequences, Negative

    "tca" : "age", # increased aging sequence
    "tcc" : "crs", # cancer risk sequence
    "tct" : "dsp", # decrease speed sequence
    "tcg" : "dsr", # decrease strength sequence
    "tta" : "dsi", # decrease intelegence sequence
    "ttc" : "dsc", # decrease charisma sequence

    # Mutation Sequences, Positive
    
    "ttt" : "isp", # increase speed sequence 
    "ttg" : "isr", # increase strength sequence 
    "tga" : "isi", # increase intelegence sequence 
    "tgc" : "isc", # increase charisma sequence 
    "tgt" : "ghs", # growth hormone sequence (boost to all) - not exactly how GH works, but for simplity sakes.
    "tgg" : "sas" # slowed aging sequence

}

slen = 10 # sequence length is 10 for now for simplicity sakes

def new_encoding(): # create a new gene sequence
    
    bases = ["a", "t", "c", "g"]
    sequence = ""

    for _ in range(slen): # 10 would be "genetic" sequence "length"
        sequence += "t" # This indicates the gene start.
        sequence += bases[random.randint(0,4)]
        sequence += bases[random.randint(0,4)] # target sequence complete
        
        # determining degree of sequence
        sequence += gene_map[random.randint(0,10)]
        sequence += "atcatc"

    return sequence

def decoding(sequence):

    bases = ["a", "t", "c", "g"]
    sequence_spr = []
    
    spr = sequence.split("atcatc")
    decode = ""

    for c1 in range(slen):
        
        # Target Sequence
        for c2 in range(3):
            local += spr[c1][c2]
        
        decode += gene_map[local] # Upload decoded gene.
        local = "" # Wipe local memory.

        for c3 in range(2):
            local += spr[c1][c3]
        
        decode += spr[c1][c3] # Upload Degree of Target Gene
        local = ""

        decode += "/" # separation of decodement in RNA synthesis

    return decode


class organism:
    def __init__(self, ia, ib):
        self.ia = ia # inheritance - dna from p1
        self.ib = ib # inheritance - dna from p2

    def meiosis(self):
        for _ in range(len(self.ia)):
            print("test")
