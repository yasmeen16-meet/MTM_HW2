%module Techniovision
%include "typemaps.i"
%include "Techniovision.h"
%{
#include "Techniovision.h"
typedef struct techniovision_t* Techniovision;
%}

Techniovision TechniovisionCreate();

TODO : insert more code here. add missing functions.

void TechniovisionStudentVotes(Techniovision t, int student, const char*
studentsFaculty, const char* votingFaculty);

void TechniovisionWinningFaculty(Techniovision t);

TODO : insert more code here. add missing functions.


void TechniovisionDestroy(Techniovision t);
