#!/bin/bash -x
tr -s '\n' < 1_lesson | tr [:lower:] [:upper:] > 1_out_lesson
