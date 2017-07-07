/*BHEADER**********************************************************************
 * Copyright (c) 2006   The Regents of the University of California.
 * Produced at the Lawrence Livermore National Laboratory.
 * Written by the HYPRE team. UCRL-CODE-222953.
 * All rights reserved.
 *
 * This file is part of HYPRE (see http://www.llnl.gov/CASC/hypre/).
 * Please see the COPYRIGHT_and_LICENSE file for the copyright notice, 
 * disclaimer, contact information and the GNU Lesser General Public License.
 *
 * HYPRE is free software; you can redistribute it and/or modify it under the 
 * terms of the GNU General Public License (as published by the Free Software
 * Foundation) version 2.1 dated February 1999.
 *
 * HYPRE is distributed in the hope that it will be useful, but WITHOUT ANY 
 * WARRANTY; without even the IMPLIED WARRANTY OF MERCHANTABILITY or FITNESS 
 * FOR A PARTICULAR PURPOSE.  See the terms and conditions of the GNU General
 * Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public License
 * along with this program; if not, write to the Free Software Foundation,
 * Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
 *
 * $Revision: 2.12 $
 ***********************************************************************EHEADER*/



/******************************************************************************
 *
 * Member functions for hypre_BigCSRMatrix class.
 *
 *****************************************************************************/

#include "headers.h"

/*--------------------------------------------------------------------------
 * hypre_BigCSRMatrixCreate
 *--------------------------------------------------------------------------*/

hypre_BigCSRMatrix *
hypre_BigCSRMatrixCreate( int num_rows,
                          int num_cols,
                          int num_nonzeros )
{
   hypre_BigCSRMatrix  *matrix;

   matrix = hypre_CTAlloc(hypre_BigCSRMatrix, 1);

   hypre_BigCSRMatrixData(matrix) = NULL;
   hypre_BigCSRMatrixI(matrix)    = NULL;
   hypre_BigCSRMatrixJ(matrix)    = NULL;
   hypre_BigCSRMatrixNumRows(matrix) = num_rows;
   hypre_BigCSRMatrixNumCols(matrix) = num_cols;
   hypre_BigCSRMatrixNumNonzeros(matrix) = num_nonzeros;

   /* set defaults */
   hypre_BigCSRMatrixOwnsData(matrix) = 1;


   return matrix;
}
/*--------------------------------------------------------------------------
 * hypre_BigCSRMatrixDestroy
 *--------------------------------------------------------------------------*/

int 
hypre_BigCSRMatrixDestroy( hypre_BigCSRMatrix *matrix )
{
   int  ierr=0;

   if (matrix)
   {
      hypre_TFree(hypre_BigCSRMatrixI(matrix));
      if ( hypre_BigCSRMatrixOwnsData(matrix) )
      {
         hypre_TFree(hypre_BigCSRMatrixData(matrix));
         hypre_TFree(hypre_BigCSRMatrixJ(matrix));
      }
      hypre_TFree(matrix);
   }

   return ierr;
}

/*--------------------------------------------------------------------------
 * hypre_BigCSRMatrixInitialize
 *--------------------------------------------------------------------------*/

int 
hypre_BigCSRMatrixInitialize( hypre_BigCSRMatrix *matrix )
{
   int  num_rows     = hypre_BigCSRMatrixNumRows(matrix);
   int  num_nonzeros = hypre_BigCSRMatrixNumNonzeros(matrix);

   int  ierr=0;

   if ( ! hypre_BigCSRMatrixData(matrix) && num_nonzeros )
      hypre_BigCSRMatrixData(matrix) = hypre_CTAlloc(float, num_nonzeros);
   if ( ! hypre_BigCSRMatrixI(matrix) )
      hypre_BigCSRMatrixI(matrix)    = hypre_CTAlloc(int, num_rows + 1);
   if ( ! hypre_BigCSRMatrixJ(matrix) && num_nonzeros )
      hypre_BigCSRMatrixJ(matrix)    = hypre_CTAlloc(HYPRE_BigInt, num_nonzeros);

   return ierr;
}

/*--------------------------------------------------------------------------
 * hypre_BigCSRMatrixSetDataOwner
 *--------------------------------------------------------------------------*/

int 
hypre_BigCSRMatrixSetDataOwner( hypre_BigCSRMatrix *matrix,
                             int              owns_data )
{
   int    ierr=0;

   hypre_BigCSRMatrixOwnsData(matrix) = owns_data;

   return ierr;
}

/*--------------------------------------------------------------------------
 * hypre_BigCSRMatrixCopy:
 * copys A to B, 
 * if copy_data = 0 only the structure of A is copied to B.
 * the routine does not check if the dimensions of A and B match !!! 
 *--------------------------------------------------------------------------*/

int 
hypre_BigCSRMatrixCopy( hypre_BigCSRMatrix *A, hypre_BigCSRMatrix *B, int copy_data )
{
   int  ierr=0;
   int  num_rows = hypre_BigCSRMatrixNumRows(A);
   int *A_i = hypre_BigCSRMatrixI(A);
   HYPRE_BigInt *A_j = hypre_BigCSRMatrixJ(A);
   float *A_data;
   int *B_i = hypre_BigCSRMatrixI(B);
   HYPRE_BigInt *B_j = hypre_BigCSRMatrixJ(B);
   float *B_data;

   int i, j;

   for (i=0; i < num_rows; i++)
   {
	B_i[i] = A_i[i];
	for (j=A_i[i]; j < A_i[i+1]; j++)
	{
		B_j[j] = A_j[j];
	}
   }
   B_i[num_rows] = A_i[num_rows];
   if (copy_data)
   {
	A_data = hypre_BigCSRMatrixData(A);
	B_data = hypre_BigCSRMatrixData(B);
   	for (i=0; i < num_rows; i++)
   	{
	   for (j=A_i[i]; j < A_i[i+1]; j++)
	   {
		B_data[j] = A_data[j];
	   }
	}
   }
   return ierr;
}

