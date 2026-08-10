# Vectors Tensors and the Basic Equations of Fluid Mechanics Aris Rutherford Z Library

> 来源文件：pre_Vectors_Tensors_and_the_Basic_Equations_of_Fluid_Mechanics_Aris_Rutherford_Z_Library.txt
> 字符数（约）：255016
> 语言：en
> 处理说明：确定性忠实结构化（无 LLM 改写）。仅检测显式章节标记、合并被换行打断的段落、剔除页码噪声；未改动任何实质性内容。

Vectors, Tensors, and the Basic Equations of Fluid Mechanics Rutherford Aris Regents' Professor, University of Minnesota DOVER PUBLICATIONS, INC.

New York Copyright © 1962 by Rutherford Aris.

This Dover edition, first published in 1989, is an unabridged and corrected republication of the work first published by Prentice-Hall, Inc., Englewood Cliffs, New Jersey, in 1962.

Library of Congress Cataloging-in-Publication Data Aris, Rutherford.

Vectors, tensors, and the basic equations of fluid mechanics / Rutherford Aris.

p. cm.

ISBN 0-486-66110-5

## 1. Fluid dynamics. 2. Calculus of tensors. 3. Vector

analysis. I. Title.

QA911.A69 1989 532-dc20 89-23501 CIP Manufactured in the United States by Courier Corporation 66110512 www.doverpublications.com Preface "What! another book on vectors and tensors?" The cry goes up alike from the student searching the bookstore for a beginning text as from the savant who learned his stuff years ago from some tome on de Rham Calculus. "What conceivable reason can this fellow have for inflicting another book on us?"

First let it be said that this is a text intended for the engineering scien- tist, for the physicist or applied mathematician perhaps, but not for the differential geometer or pure mathematician. Second, it is an introductory text, intended for a reader with some acquaintance with the calculus of partial differentiation and multiple integration but nothing more. There- fore, being for a reader with interest in the physical world, it sets out to show that the calculus of tensors is the language most appropriate to the rational examination of physical field theories. Of these theories I have selected the theory of fluid mechanics as being of central importance and wide appeal. The idea behind this treatment is to use the physical theory to motivate the thorough study of the mathematical subject and, con- versely, to show how the mathematical theory can give a truer insight into the physical situation.

The day is quickly passing when it is necessary to make any apology for giving engineers the "straight stuff" in mathematics. It is realised increasingly that his knowledge of mathematics must go beyond a nodding acquaintance with its notions and notation. Even if mathematics is to remain merely a tool for him, he will never be its master until he has under- stood why it is so formed and is practiced in its manipulations. I have attempted therefore to keep the presentation both elementary and physi- cally motivated but at the same time not to shun the more difficult ideas or applications. Some of the topics introduced are close to the present frontiers of research and it is hoped that the development of fluid mechanics that has been followed is thoroughly in accord with the best current understanding.

In the last decade there has been a renascence of interest in rational mechanics in the mathematical world. It has been fairly widespread and attracted the attention of many mathematicians whose abilities are of the first order. If one name is to be singled out, it is probably not unfair to the others to select that of Truesdell, whose deep scholarship and extensive writing have been of great influence. The work that has been done, and is still proceeding, on the foundations of continuum mechanics will be the basis for future advances in the engineering of continuous media and the sooner the engineer becomes acquainted with it the better. He should not be put off by a certain astringency of aside or hauteur de mathématicien which sometimes marks the style of this work. It is not easy reading, nor would one wish it to be, but if this introduction makes the literature appear less formidable, one of its chief purposes will have been fulfilled. If it whets the reader's appetite for more substantial fare, I shall be more than content.

Many applied mathematical texts treat only of Cartesian tensors since these suffice for the principal applications. More purely mathematical texts will properly regard Cartesian tensors as a special case. For certain applica- tions of current importance, Cartesian tensors are not sufficient, and since the understanding of tensors is intended to serve the student in fields other than fluid mechanics, I have not hesitated to treat them generally. How- ever, the ideas are first introduced in the Cartesian framework and then redeveloped more generally. Though this may appear to involve duplica- tion, it is a sound pedagogical principle to introduce the basic ideas in their most elementary form and to go over the ground again building on the understanding that has been gained. This has the effect of dividing the book into two parts and the first six chapters form a complete course in themselves, which may be suitable at an undergraduate level. The whole book is founded on a course of lectures given to graduate students, and, in as much as their knowledge of matrix algebra is sometimes in need of refreshment and to make the book more self-contained for the independent reader, a short appendix gives the necessary background. The last chapter may be read after Chapter 6, since it in no way requires the intervening chapters. Indeed it is less permeated with the ideas of tensor analysis and is a topic whose foundations are still being strengthened. The treatment I have attempted is therefore not a very deep one, but in a book emanating from a chemical engineering department its entire omission would have been unpardonable. To have gone further and treated of relativity and magnetohydrodynamics would have been to enlarge the book beyond the bounds of an introduction. The exercises, few of which are at all difficult, are an integral part of the text. They provide practice in manipulation and extensions of the preceding sections. Results which are to be used later are frequently given as exercises and they are not to be regarded as less important than the equations of the text. They are always obvious, in the technical sense of lying right in the way, and are the type of minor hurdle that has to be cleared in reading the literature.

I am indebted to many colleagues for helpful suggestions, but particu- larly to L. E. Scriven for his careful criticism and timely insistence that a vector is a vector is a vector. I am particularly grateful to J. Serrin, whose lectures at this university first really showed me the structure of fluid mechanics. It is good that the substance of his lectures is available to a wider public in the Handbuch der Physik article referred to frequently below. As usual I have received most valuable encouragement from N. R.

Amundson. I need hardly add that the book's faults are entirely my own.

Only those who have typed such a manuscript as this will properly appreciate the care and patience of my sister-in-law, Mrs. A. Blair, who penetrated my scribbling and scratchings to produce a first rate typescript.

Perhaps only the wives of authors will understand that growing irasci- bility which mine has had to tolerate and her relief at finally seeing the thing in print.

The compositors who work on a text so burdened with affixes deserve the gratitude of an author even if they are unknown to him: they certainly have mine. I would also like to thank Mr. D. Yesberg for his valuable help in proofreading and in compiling the index.

## RUTHERFORD ARIS

Contents

## 1. Introduction

1.1. Mathematical theories and engineering science, 1. 1.2. Scalars, vectors, and tensors, 3. 1.3. Preface, 6.

## 2. Cartesian Vectors and Tensors: Their Algebra

2.11. Definition of a vector, 8. 2.12. Examples of vectors, 10. 2.13.

Scalar multiplication, 11. 2.14. Addition of vectors - Coplanar vectors, 11. 2.15. Unit vectors, 13. 2.16. Linear independence - coplanar and linear vectors, 13. 2.17.

Scalar product - Orthogonality, 15. 2.18. Vector product, 16. 2.19. Ve- locity of a rigid body rotation, 17. 2.20. Triple scalar product, 18. 2.21.

Triple vector product, 19. 2.22. Reciprocal base system, 20. 2.31. Second order tensors, 21. 2.32. Examples of second order tensors, 22. 2.33. Scalar multiplication and addition, 23. 2.34. Contraction and multiplication, 23.

2.35. The vector of an antisymmetric tensor, 24. 2.36. Canonical form of a symmetric tensor, 25. 2.41. Higher order tensors, 26. 2.42. The quotient rule, 29. 2.43. Isotropic tensors, 30. 2.44. Dyadics and other notations, 34.

2.45. Axial vectors, 36.

## 3. Cartesian Vectors and Tensors: Their Calculus

3.11. Tensor functions of a time-like variable, 38. 3.12. Differentiation in space, 39. 3.13. Line integrals, 42. 3.14. Surface integrals, 44. 3.15. Volume in- tegrals, 48. 3.16. Change of variable with multiple integrals, 50. 3.21.

Vector fields, 51. 3.22. The vector operator ∇ Gradient of a scalar, 51.

3.23. The divergence of a vector field, 53. 3.24. The curl of a vector field, 55.

3.31. Green's theorem and some of its variants, 58. 3.32. Stokes' theorem, 61.

3.41. The classification and representation of vector fields, 63. 3.42. Irrota- tional vector fields, 65. 3.43. Solenoidal vector fields, 67. 3.44. Helmholtz' representation, 70. 3.45. Other representations, 72.

## 4. The Kinematics of Fluid Motion

4.11. Particle paths, 76. 4.12. Streamlines, 79. 4.13. Streaklines, 81.

4.21. Motion, 83. 4.22. Reynolds' transport theorem, 85. 4.3. Conserva- tion of mass and the equation of continuity, 87. 4.41. Deformation and rate of strain, 88. 4.42. Physical interpretation of the deformation tensor, 89.

4.43. Principal axes of deformation, 92. 4.5. Vorticity, vortex lines and tubes, 95.

## 5. Stress in Fluids

5.11. Cauchy's stress principle and the conservation of momentum, 99. 5.12.

The stress tensor, 101.

## 5. The Stress Tensor

5.13. The symmetry of the stress tensor.

5.14. Hydrostatic pressure.

5.15. Principal axes of stress and the notion of isotropy.

5.16. The Stokesian fluid.

5.21. Constitutive equations of the Stokesian fluid.

5.22. The Newtonian fluid.

5.23. Interpretation of the constants lambda and mu.

## 6. Equations of Motion and Energy in Cartesian Coordinates

6.11. Equations of motion of a Newtonian fluid.

6.12. Boundary conditions.

6.13. The Reynolds number.

6.14. Dissipation of energy by viscous forces.

6.15. Equations for a Stokesian fluid.

6.16. The energy equation.

6.17. Remarks on the development of the equations.

6.18. Special cases of the equations.

6.19. Bernoulli theorems.

6.20. Some further properties of barotropic flow.

## 7. Tensors

7.11. Coordinate systems and transformations.

7.12. Proper transformations.

7.13. General plan of presentation.

7.21. Contravariant vectors.

7.22. Covariant vectors.

7.23. The metric tensor.

7.24. Absolute and relative tensor fields.

7.25. Isotropic tensors.

7.31. Tensor algebra.

7.32. The quotient rule.

7.33. Length of a vector and angle between vectors.

7.34. Principal directions of a symmetric second order tensor.

7.35. Covariant and contravariant base vectors.

7.41. Physical components of vectors in orthogonal coordinate systems.

7.42. Physical components of vectors in nonorthogonal coordinate systems.

7.51. Physical components of tensors.

7.52. An example.

7.53. Anholonomic components of a tensor.

7.61. Differentials of tensors.

7.62. Parallel vector fields.

7.63. Christoffel symbols.

7.64. Christoffel symbols in orthogonal coordinates.

7.65. Covariant differentiation.

7.66. The Laplacian, divergence, and curl.

7.67. Green's and Stokes' theorems.

7.71. Euclidean and other spaces.

## 8. Equations of Fluid Flow in Euclidean Space

8.11. Intrinsic derivatives.

8.12. The transport theorem and equation of continuity.

8.13. The equations of motion.

8.14. The Newtonian fluid.

8.15. The Navier-Stokes equations.

8.21. Convected coordinates.

8.22. Convective differentiation.

8.23. Strain and rate of strain in convected coordinates.

8.24. Constitutive equations.

8.31. The general theory of constitutive equations.

## 9. The Geometry of Surfaces in Space

9.11. Surface coordinates.

9.12. Transformations of surface coordinates-surface tensors.

9.13. The metric tensor.

9.14. Length and direction of surface vectors.

9.15. Christoffel symbols.

9.21. Geodesics.

9.22. Coordinates.

9.23. Parallel vectors in a surface.

9.24. Covariant surface differentiation.

9.25. The Gaussian and mean curvature of a surface.

9.31. The surface in space.

9.32. The first fundamental form of the surface.

9.33. The normal to the surface.

9.34. Covariant differentiation of hybrid tensors.

9.35. The second fundamental form of the surface.

9.36. The third fundamental form.

9.37. The relation between the three fundamental forms-Gauss-Codazzi equations.

9.38. Curves in the surface.

9.41. Differential operators in a surface.

9.42. Green's and Stokes' theorems in a surface.

## 10. The Equations of Surface Flow

10.11. Velocity in a surface.

10.12. Operations with a time dependent metric.

10.13. Strain in the surface.

10.14. Stress in the surface.

10.15. Constitutive relations for the surface.

10.16. Intrinsic equations of surface motion.

10.17. Intrinsic equations for a Newtonian surface fluid.

10.21. The continuity of the surface and its surroundings.

10.22. Connection between surface strain and the surroundings.

10.23. Dynamical connection between the surface and its surroundings.

10.31. Surface equations as boundary conditions at an interface.

10.32. The plane interface.

10.33. The cylindrical interface.

10.34. The spherical interface.

## 11. Equations for Reacting Fluids

11.11. The conservation of mass.

11.12. Mass flux.

11.13. Stoichiometric and kinetic relations.

11.21. The conservation of momentum.

11.22. The conservation of energy.

11.23. The diffusion of heat and mass.

11.31. Transport in binary mixtures.

## Appendix A. Resume of Three-dimensional Coordinate Geometry and Matrix Theory

A.1. Cartesian coordinate systems.

A.2. The projection of one line on another-Orthogonality.

A.3. The line, plane, and surface.

A.4. Row and column vectors-change of origin and scale.

A.5. Matrices and quadratics.

A.6. Matrices and rotations of axes.

A.7. The laws of matrix algebra.

A.8. Determinants-the inverse of a matrix.

A.9. Partitioned matrices-Laplacian expansion-product of determinants.

A.10. Latent roots and vectors of a symmetric matrix.

A.11. Canonical form of symmetric matrices and quadratics.

A.12. Stationary properties.

## Appendix B. Implicit Functions and Jacobians

Index

Introduction

1.1. Mathematical theories and engineering science

At the turn of the century Bertrand Russell described the mathematician as one who neither knows what he is talking about nor cares whether what he says is true. The engineer sometimes prides himself on being the man who can do for a reasonable cost what another would expend a fortune on, if indeed he could do it at all. Between such extremes of abstraction and practicality it would hardly seem possible that there should be much commerce. The philosopher and artisan must tread diverging paths. Yet the trend has been quite otherwise and today the engineer is increasingly aware of his need for mathematical insight and the mathematician proves more and more the stimulation of physical problems. Russell was referring to the logical foundations of pure mathematics, to which he had made his own contributions, and constructing a paradox which would throw into relief the debate that was then at its height. There are, of course, regions of pure mathematics which have developed into such abstraction as to have no apparent contact with the commonplace world. Equally, there are engineering skills that have been developed for particular purposes with no apparent application to other situations. The progress of the moment, at any rate in the science of engineering, lies in the region where the two disciplines have common interests: engineering education, worthy of the name, has always lain there.

If the mathematician has little care whether what he says is true, it is only in the sense that his primary concern is with the inner consistency and deductive consequences of an axiomatic theory. He is content with certain undefined quantities and his satisfaction lies in the structure into which they can be built. Even if the engineer regards himself as dedicated to doing a job economically he cannot rest content with its particular details and still retain a reputation for economy. It is his understanding of the common features of diverse problems that allows him to be economical and hence he must be concerned with abstraction and generalization. It is the business of mathematical theory to provide just such an abstraction and generalization, but it will do it in its own fashion and use the axiomatic method. From what at first seem rather farfetched abstractions and assumptions, it will produce a coherent body of consequences. In so far as these consequences correspond to the observable behavior of the materials the engineer handles, he will have confidence in the mathematical theory and its foundations. The theory itself will have been used to design the critical experiments and to interpret their results. If there is complete discordance between the valid expectations of the theory and the results of critically performed experiments the theory may be rejected. Some measure of disagreement may suggest modification of the theory. Agreement within the limits of experimental error gives confidence in the mathematical model and opens the way for further progress. Continuum mechanics in general, and fluid mechanics in particular, provide mathematical models of the real world in which the engineer can have a high degree of confidence.

The idea of a continuum is an abstraction. Modern physics leads us to believe that matter is composed of elementary particles. For many purposes we need not look within the molecule, but this is to be regarded as an entity of small but finite dimensions which interacts with its fellows according to certain laws. Matter is thus not continuous but discrete and its gross properties are averages over a large number of molecules. The equations of fluid motion have been obtained from this viewpoint, but, though at first sight it seems a much more fundamental one, it stands on the same footing as continuum mechanics-a mathematical model worthy of a certain degree of confidence.

For many purposes it is not necessary to know much of the molecular structure, and the continuum hypothesis is an equally satisfactory basis for a mathematical model. In this model the material is not regarded as aggregated at certain points within the medium, so that at most one can speak of the probability of a molecule being at a particular point at a particular time. Rather, we think of the material as continuously filling the region it occupies or, more precisely, that the transformation between two regions it may occupy at different times is a continuous transformation. With this abstraction we can speak of the velocity at a point in a way that is inherently more satisfying than with the molecular model. For with the latter it is necessary to take the average velocity of molecules in the neighborhood of the point. But how large should this neighborhood be? If it is too large its relevance to the point in question is Point 8.1.2. Scalars, Vectors, and Tensors is in question; if it is too small the validity of the average is destroyed. We might hope that there is some range of intermediate sizes for which the average is virtually constant, but this is an unsatisfactory compromise and, in fact, much more sophisticated averages must be invoked to link the molecular and continuum models. In the continuum model velocity is a certain time derivative of the transformation.

The reader may wonder why we start with such a discussion in a book primarily devoted to vectors and tensors. It is because tensor calculus is the natural language of continuum or field theories and we wish to motivate the study of it by considering the basic equations of fluid mechanics. As any language is more than its grammar, so the language of tensor analysis is more than a mere notation. It embodies an outlook or cast of thought just as surely as the speech of a people is redolent with their habit of mind. In this case it is the idea that the "physical" entity is the same though its mathematical description may vary. It follows that there must be a relation between any two mathematical descriptions if they refer to the same entity, and it is this relation that gives the language its character.

1.2. Scalars, vectors, and tensors There are many physical quantities with which only a single magnitude can be associated. For example, when suitable units of mass and length have been adopted the density of a fluid may be measured. This density, or mass per unit volume, perhaps varies throughout the bulk of a fluid, but in the neighborhood of a given point is found to be sensibly constant. We may associate this density with the point but that is all; there is no sense of direction associated with the density. Such quantities are called scalars and in any system of units they are specified by a single real number. If the units in which a scalar is expressed are changed, the real number will change but the physical entity remains the same. Thus the density of water at 4°C is 1 g/cm³ or 62.427 lb/ft³; the two different numbers 1 and 62.427 express the same density.

There are other quantities associated with a point that have not only a magnitude but also a direction. If a force of 1 lb weight is said to act at a certain point, we can still ask in what direction the force acts and it is not fully specified until this direction is given. Such a physical quantity is a vector. A change of units will change the numerical value of the magnitude in precisely the same way as the real number associated with a scalar is changed, but there is also another change that may be made. Direction has to be specified in relation to a given frame of reference and this frame of reference is just as arbitrary as the system of units in which the magnitude is expressed. For example, a system of three mutually perpendicular axes might be constructed at a point O as follows. Take O₁ to be the direction of the magnetic north in a horizontal plane, O₂ to be the direction due west in this plane, and O₃ to be the direction vertically upwards. Then a direction can be fixed by giving the cosine of the angle between it and each of the three axes in turn. If l₁, l₂, and l₃ are these direction cosines they are not independent but l₁² + l₂² + l₃² = 1. If F is the magnitude of the force, the three numbers F_i = l_i F allow us to reconstruct the force, for its magnitude F = (F₁² + F₂² + F₃²)^{1/2} and the direction cosines are given by l_i = F_i/F, i = 1, 2, 3. Thus the three numbers F₁, F₂, F₃ completely specify the force and are called its components in the system of axes we have set up. However, this system was quite arbitrary and another system with O₁ due south, O₂ due east, and O₃ vertically upwards would have been just as valid. In this new system the same direction would be given by direction cosines equal respectively to -l₁, -l₂, and l₃ and so the components of the force would be -F₁, -F₂, and F₃. Thus the components of the physical entity, force, change with changing description of direction though the entity itself remains the same just as the real number representing the scalar, density, changed with changing units though the density remained the same. We distinguish therefore between the vector as an entity and its components which allow us to reconstruct it in a particular system of reference. The set of components is meaningless unless the system of reference is also prescribed just as the magnitude 62.427 is meaningless as a density until the units are also prescribed.

If then the components of the same entity change with changing frame of reference we need to find out how they will change so as to be sure that the same entity is retained. In three-dimensional space a reference frame consists of three different directions which do not all lie in the same plane. We should also specify the units in which measurements are made in these directions for these need not be the same. These base vectors need not be the same at different points in space and any transformation of base vectors is valid provided the transformed vectors do not lie in a plane. A plane is a space with only two dimensions so that three vectors lying in a plane cannot get a grip on three-dimensional space. Without trying to define things precisely at this point, let us denote the three base vectors by a, b, c then the components of a vector v with respect to this frame of reference are the three numbers α, β, and γ such that v = αa + βb + γc.

If the base vectors are transformed to x, y, z the new components α', β', γ' must satisfy v = α'x + β'y + γ'z.

If then we know how the base vectors of the new system can be expressed in terms of the old, we shall be able to see how the components should transform. In ordinary three-dimensional space the system defined by three mutually orthogonal directions with equal units of measurement is called Cartesian. The base vectors may be thought of as lines of unit length lying along the three axes. The cardinal virtue of this system is that these base vectors can be the same everywhere. In the first few chapters we will consider Cartesian vectors, that is, vectors whose components are expressed with a Cartesian frame of reference and the only transformation we shall consider is from one Cartesian system to another. Later we consider more general systems of reference in which new features arise because of the variability of the base vectors. If the space is not Euclidean, as for example the surface of a sphere, the variability of base vectors is inevitable.

We shall construct an algebra and calculus of vectors showing how a sum, product, or derivative may be defined. In fact, two distinct products of two vectors can be defined both of which have great significance. We cannot, however, define the reciprocal of a vector in a unique way, as can be done with a scalar. A scalar can be thought of as a vector in one dimension and its one component gives it a grip on its one-dimensional space and the reciprocal of a scalar u is simply 1/u. A single vector does not have sufficient grip on the three-dimensional space to allow its reciprocal to be defined, but we can construct an analog of the reciprocal for a triad of vectors not all in one plane. In particular, it will be found that the reciprocal of the triad of base vectors has great importance.

Although the quotient of two vectors cannot be defined satisfactorily, tensors arise physically in situations that make them look rather like this. For example, a stress is a force per unit area. We have seen that force is a vector and so is an element of area if we remember that we have to specify both its size and orientation, that is, the direction of its normal. If f denotes the vector of force and A the vector of magnitude equal to the area in the direction of its normal, the stress T might be thought of as f/A. However, because division by a vector is undefined, it does not arise quite in this way. Rather we find that the stress system is such that given A we can find f by multiplying A by a new entity T which is like f/A only in the sense that f = T · A.

This new mathematical entity corresponds to a physical entity, namely, the stress system at a point. It is a quantity with which two directions seem to be associated and not just one, as in the case of the vector, or none at all, as with the scalar. In fact it needs nine numbers to specify it in any reference system corresponding to the nine possible combinations of two base vectors. Again we want to be sure that the same physical entity is described when we change the system of reference and hence must require that the components should transform appropriately. What we do is to lay down the transformation rules of the components and when confronted by a set of nine components satisfying these requirements we know they are components of a single mathematical entity. This entity is called a tensor (or more properly a second order tensor) and is thus a suitable representation of the kind of physical entity with which two directions can be associated.

As with a vector, we distinguish carefully between the tensor as an entity and its components which must be with reference to a specified system of reference. Some writers speak of the entity as a dyadic whose components form a tensor, a usage soundly grounded in the history of vector analysis. However, we have felt it sufficient to maintain the distinction where necessary by speaking of the tensor and its components. The word tensor is quite general and where necessary its order must be specifically mentioned, for it will appear that a scalar is a tensor of order zero and a vector a tensor of order one. Physical quantities are rarely associated with tensors of higher order than the second but tensors up to the fourth order will arise. Progress in a language is marked by those small liberties taken with its forms.

that impart a certain style without detracting from the meaning. It is hoped that no real ambiguity has been concealed by the free use of the word tensor, but to emphasize this point as much as is possible at this stage we repeat: the distinction must always be borne in mind between the tensor, as a mathematical entity representing a physical entity, and the components of the tensor which are only meaningful when the system of reference has been specified.

1.3. Preview In the next two chapters we shall develop first the algebra and then the calculus of Cartesian vectors and tensors. The general theorems and ideas of this are applicable in the whole of continuum mechanics as well as in electricity and other fields. Our application of them to fluid mechanics begins with a discussion of kinematics in Chapter 4. Chapter 5 considers the relations between stress and strain in a fluid and allows the basic equations of fluid motion to be discussed in the following chapter. This part of the book is essentially complete in itself. The last chapter on reaction and flow may be read at this point since it does not depend on more general tensor methods. The groundwork laid in Cartesian tensors allows us to fake up the more general calculus of tensors fairly concisely in Chapter 7 and apply these notions to fluid flow in space in Chapter 8. The discussion of flow in a surface given in Chapter 10 requires some understanding of the geometry of surfaces which is given in the preceding chapter.

## BIBLIOGRAPHY

1.1. A relatively elementary exposition of the molecular approach to the theory of fluids is well given in Patterson, G. N., Molecular flow of gases. New York: John Wiley, 1957.

The standard reference is Hirschfelder, J. O., C. F. Curtiss and R. B. Bird, Molecular theory of gases and liquids. New York: John Wiley, 1954.

A further discussion of the averaging involved in passing from the molecular to the continuum models may be found in Morse, P. M., and H. Feshbach. Methods of theoretical physics, Vol. 1, pp. 1-3. New York: McGraw-Hill, 1953.

The viewpoint we have briefly outlined is more fully and forcefully presented in the opening sections of Truesdell, C., and R. Toupin, The classical field theories, in Handbuch der Physik III/1, ed. S. Flugge. Berlin: Springer-Verlag, 1960.

Cartesian Vectors and Tensors: Their Algebra Until Chapter 8 the unqualified words vector and tensor will refer to the Cartesian vector and tensor about to be defined and if it is necessary to refer to the more general concept of the tensor this will be specifically stated.

In this chapter we shall develop the algebra of Cartesian vectors and tensors.

2.11. Definition of a vector We shall define a vector by first giving an example of one and isolating the particular feature of its behavior that characterizes it as a vector. We may then say that a vector is anything which has this characteristic behavior. To establish that any quantity is a vector we shall have to show that it behaves in this way.

In the ordinary three-dimensional space of everyday life, known technically as Euclidean [3]-space, the position of a point may be specified by three Cartesian coordinates. To determine these we must first establish a frame of reference by taking any point O as the origin and drawing through it three mutually perpendicular straight lines O1, O2, O3. These will have positive senses disposed according to Fig. 2.1 for the right-handed Cartesian coordinates which we adopt as standard. The name right-handed is used since the disposition is the same as the thumb, first, and second fingers of the right hand, or, alternatively because a right-handed screw turned from O1 to O2 would travel in the positive O3 direction. The coordinates of a point P are the lengths of the projections of OP on to the three axes O1, O2, and O3. Let these three lengths be x1, x2, and x3 respectively. We call them the Cartesian coordinates of P or the components of the position vector of P with respect to the Cartesian frame of reference O123.

Now suppose that the coordinate system is rigidly rotated to a new position O1'O2'O3' as shown in Fig. 2.2 and the new coordinates of P are R1, R2, R3. The rotation can be specified by giving the angles between the old and new axes. Let lij be the cosine of the angle between the old Oi axis and the new one Oj', then the new coordinates are related to the old by the formulae Rj = lij x_i, j = 1,2,3, (2.11.1)

and conversely xi = li j Rj, i = 1,2, 3. (2.11.2)

The reader unfamiliar with this transformation should consult the appendix.

Another way of describing this transformation is to say that if R1, R2, R3 are to be the coordinates (or components of the position vector) in the new coordinate system of the same point P as x1, x2, x3 are in the old then they must be related by Eqs. (2.11.1) and (2.11.2).

We now introduce a very valuable abbreviation, the Cartesian summation convention.

In any product of terms a repeated suffix is held to be summed over its three values, 1, 2, and 3. A suffix not repeated in any product can take any of the values 1, 2, or 3. Thus the equations above can be written Rj = lij x_i, (2.11.1)

xi = li j Rj, (2.11.2)

i being the repeated suffix in the first case and j in the second. The other suffix (j in the first case and i in the second) is called the free suffix and may take any of the values 1, 2, or 3 so that it is unnecessary to write i or j = 1,2,3 after the formula. The repeated or dummy suffix as it is sometimes called may be assigned any letter; thus lij x_i and lim x_m mean the same thing and it is sometimes convenient in manipulating these formulae to make such changes.

The position vector is our standard Cartesian vector and its components are the coordinates of P. The directed line segment OP gives a convenient geometrical representation of this vector. Since the position vector is to represent the same physical point P its components xi in the frame of reference O123 must transform into Rj = lij x_i in the rotated frame of reference O1'O2'O3'.

Accordingly, we make the following definition.

Definition. A Cartesian vector, a, in three dimensions is a quantity with three components a1, a2, a3 in the frame of reference O123, which, under rotation of the coordinate frame to O1'O2'O3', become components a1', a2', a3', where aj' = lij ai. (2.11.3)

The vector a is to be regarded as an entity, just as the physical quantity it represents is an entity. It is sometimes convenient to use the bold face a to show this. In any particular coordinate system it has components (a1, a2, a3) and it is at other times convenient to use the typical component ai.

It is convenient here to introduce the Kronecker delta, denoted by δij. It is such that δij = 1 if i = j, δij = 0 if i ≠ j, (2.11.4)

and represents the identical transformation. If δij occurs in any formula with a repeated suffix all it does is to replace the dummy suffix by the other suffix of the Kronecker delta. For example, δij aj = δ1j aj + δ2j aj + δ3j aj = aj, since only the term in which the second suffix is j is not zero.

2.12. Example of vectors The position vector is the prototype of Cartesian vectors and much of our terminology is drawn from it. Thus we may speak of the length or magnitude of a vector a |a| = (Σ ai^2)^(1/2). (2.12.1)

If |a| = 1 it is called a unit vector and its components may be thought of as direction cosines. Thus for any vector a with components ai the vector with components ai/|a| is a unit vector and so represents the direction of the vector. Since there are only two arbitrary elements to a unit vector (the third being fixed by the requirement of unit length), the specification of the magnitude and direction of a vector involves three quantities and is equivalent to specifying the three components.

If the position of a point P is a function of time, we may write xi = xi(t) and Rj = Rj(t) where Rj(t) = lij xi(t). The lij, connecting two coordinate frames are of course independent of time so we may differentiate these formulae with respect to t as many times as we wish d^n Rj / dt^n = lij d^n xi / dt^n, (2.12.2)

This equation shows that all the derivatives of position are vectors and in particular the velocity (n = 1) and the acceleration (n = 2).

A force is specified by its magnitude F and the direction (n1, n2, n3) in which it acts. Let f = Fn, then f1, f2, f3 are the components of a vector. To see this we observe that since direction cosines are simply coordinates of a point on the unit sphere, they transform as coordinates. The direction cosines of this line in the frame of reference O123 will therefore be ni', where ni' = li j nj Hence fi' = F ni' = F li j nj = li j (F nj) = li j fj so that force is indeed a vector.

Exercise 2.12.1. If ρ is any scalar property per unit volume of a fluid in motion, show how to define a flux vector f such that fi is the rate of flow of ρ per unit area across a small element perpendicular to the axis Oi.

2.13. Scalar multiplication If α is any scalar number the product of this scalar and the vector a is a vector with components α ai. We see that the length or magnitude of α a is simply α times the length of a and the direction of α a is the same as that of a. Thus scalar multiplication really amounts to a change of length scale as its name suggests. By multiplying both sides of (2.11.3) by the scalar α it is evident that the vector character of a is unchanged by scalar multiplication.

2.21. Addition of vectors-Coplanar vectors If a and b are two vectors with components ai and bi, their sum is the vector with components ai + bi. By phrasing the definition in this way we have really begged the question of whether the sum of two vectors is a vector. However, this is very easily answered; for if we say that the sum of a and b is an entity with components ai + bi then, if the definition of the sum is to be independent of rotation, it must have components \(l_{ij}b_j\) in the frame of reference 0123. However, \[ a_i + b_i = l_{ip}a_p + l_{ij}b_j = l_{ij}(a_j + b_j) \tag{2.21.1} \]

which shows that the sum is indeed a vector. Geometrically we see in Fig. 2.3 that if a and b are represented by two directed line segments OP and OQ, then their sum is represented by OR where PR is OQ translated parallel to itself. This is sometimes known as the parallelogram rule of addition. The geometrical representation makes it clear that the order of addition is immaterial, so that \[ a + b = b + a \tag{2.21.2} \]

This procedure can be continued for the addition of more than two vectors, the sum of a, b, ... k being the vector with components \(a_i, b_i, \dots, k_i\). The order and association of vectors in addition is immaterial, for example \[ (a + b) + c = a + (b + c) \tag{2.21.3} \]

Subtraction may be defined by combining addition with scalar multiplication by -1. Thus, \[ a - b = a + (-1)b \tag{2.21.4} \]

is evidently the vector with components \(a_i - b_i\). We also see that any vector c which is in the same plane as a and b can be represented in the form \[ c = \alpha a + \beta b \tag{2.21.5} \]

For in Fig. 2.4 let OR represent the vector c in the plane of OP and OQ. Draw RM parallel to OQ and RN parallel to OP and let \(\alpha = OM/OP\), \(\beta = ON/OQ\). Then OM and ON represent the vectors \(\alpha a\) and \(\beta b\) and c is their sum. Geometrically it is clear that if OR points out of the plane of OP and OQ then its component out of the plane cannot be represented as a combination of a and b. Thus the condition for c to lie in the plane of a and b is that it can be expressed in the form (2.21.5). (An analytical demonstration of this is given as an exercise later.) These equations written in component form are \[ \alpha a_i + \beta b_i = c_i \]

and if \(\alpha\) and \(\beta\) are eliminated between the three equations we have the relation \[ \begin{vmatrix} a_1 & b_1 & c_1 \\ a_2 & b_2 & c_2 \\ a_3 & b_3 & c_3 \end{vmatrix} = 0 \tag{2.21.6} \]

2.22. Unit vectors The three unit vectors that have only one nonvanishing component are of special importance. They are \[ e_{(1)} = (1, 0, 0) \\ e_{(2)} = (0, 1, 0) \\ e_{(3)} = (0, 0, 1). \tag{2.22.1} \]

The suffixes on the e are enclosed in parentheses to show that they do not denote components. The j-th component of \(e_{(i)}\) is denoted by \(e_{(i)j}\), and \[ e_{(i)j} = \delta_{ij} \tag{2.22.2} \]

The components \(a_1, a_2,\) and \(a_3\) of a are themselves scalars and the sum of the scalar products \(a_i e_{(i)}\) is a vector. But by comparing components we see that \[ a = a_1 e_{(1)} + a_2 e_{(2)} + a_3 e_{(3)} = a_i e_{(i)}. \tag{2.22.3} \]

In the last expression we allow the summation convention to apply also to the parenthetical index.

2.23. A basis of non-coplanar vectors The three unit vectors are said to form a basis for the representation of any vector. They are not the only basis, though they are the natural one. We shall show that any three vectors a, b, and c can be used as a basis provided \[ \begin{vmatrix} a_1 & b_1 & c_1 \\ a_2 & b_2 & c_2 \\ a_3 & b_3 & c_3 \end{vmatrix} \neq 0.

\]

If \(a_i, b_i, c_i\) are the components of a, b, c and \(M = \begin{vmatrix} a_1 & b_1 & c_1 \\ a_2 & b_2 & c_2 \\ a_3 & b_3 & c_3 \end{vmatrix}\), then the components of any vector x can be found by \[ x_i = \alpha a_i + \beta b_i + \gamma c_i \]

where the coefficients are given by \[ \alpha = \frac{1}{M} \begin{vmatrix} x_1 & b_1 & c_1 \\ x_2 & b_2 & c_2 \\ x_3 & b_3 & c_3 \end{vmatrix}, \quad \beta = \frac{1}{M} \begin{vmatrix} a_1 & x_1 & c_1 \\ a_2 & x_2 & c_2 \\ a_3 & x_3 & c_3 \end{vmatrix}, \quad \gamma = \frac{1}{M} \begin{vmatrix} a_1 & b_1 & x_1 \\ a_2 & b_2 & x_2 \\ a_3 & b_3 & x_3 \end{vmatrix}.

\]

Exercise 2.23.1. Show how to find the vector which lies in the intersection of the plane of a and b with the plane of c and d.

Exercise 2.23.2. Let the vectors \(b_{(i)}\) be a basis and form a new basis \(a_{(i)} = m_{ij}b_{(j)}\). Show that if \(d = \alpha_i b_{(i)} = \beta_j a_{(j)}\), then \(\alpha_i = m_{ji} \beta_j\), where M is the matrix whose \(ij\)-th element is \(m_{ij}\).

2.31. Scalar product-orthogonality The scalar product of two vectors a and b is defined as \[ a \cdot b = a_i b_i \tag{2.31.1} \]

and read as "a dot b." It is invariant under rotation of axes and so it is a scalar. For let \(a'_i = l_{ij}a_j\) and \(b'_i = l_{ij}b_j\) be the components in a new frame of reference. Then \(a' \cdot b' = a'_i b'_i = l_{ij}a_j l_{ik}b_k = l_{ij}l_{ik}a_j b_k = \delta_{jk}a_j b_k = a_j b_j = a \cdot b\), \tag{2.31.2} since \(l_{ij}l_{ik} = \delta_{jk}\) by the orthogonality of the rotated axes [see Appendix, Eqs. (A6.6) and (A6.7)].

If m and n are unit vectors in the directions of a and b respectively, \(m \cdot n = \cos \theta\), where \(\theta\) is the angle between the two directions [see Appendix, Eq. (A2.5)]. Then since \(a = |a|m\) and \(b = |b|n\) we have \[ a \cdot b = |a| |b| \cos \theta. \tag{2.31.3} \]

The scalar product \(a \cdot n = |a| \cos \theta\) is the projection of the vector a on the direction of the vector b. If the angle between the two vectors is a right angle, \(\theta = \pi/2\) and \(\cos \theta = 0\). Such vectors are said to be orthogonal and the condition for orthogonality is \[ a \cdot b = 0. \tag{2.31.4} \]

The unit vectors of 2.22 are mutually orthogonal. We may remark that the scalar product can be written as \(a_i b_i\) and that it is commutative, that is, \(a \cdot b = b \cdot a\).

Exercise 2.31.1. Show that if \(c = \alpha a + \beta b\) it is coplanar with a and b.

Exercise 2.31.2. If f is the flux vector of some scalar property of a fluid in motion and n the unit normal to an element of area dS, show that \(f \cdot n dS\) is the flux of that property through the element of area.

2.32. Vector product Of the nine possible products of the components the scalar product is a linear combination of three of them to form a scalar. The other six can be combined in pairs to form the components of a vector. We shall define it as a vector and show how its components can be calculated. The vector or cross product \(a \times b\) (read "a cross b") is the vector normal to the plane of a and b of magnitude \(|a| |b| \sin \theta\). To fix the sense of the vector product we require that a, b and \(a \times b\) should form a right-handed system. The notation \(a \wedge b\) is also commonly used for the vector product. We notice that \(|a| |b| \sin \theta\) is the area of the parallelogram two of whose sides are the vectors a and b. Also it is clear that if we reverse the order of the factors the vector product must point in the opposite direction. Therefore the vector is not commutative, but \[ b \times a = - a \times b. \tag{2.32.1} \]

Consider now the vector products of the unit vectors. They are all of unit length and mutually orthogonal so their vector products will be unit vectors. Remembering the right-handed rule we therefore have \[ e_{(2)} \times e_{(3)} = - e_{(3)} \times e_{(2)} = e_{(1)} \\ e_{(3)} \times e_{(1)} = - e_{(1)} \times e_{(3)} = e_{(2)} \tag{2.32.2} \\ e_{(1)} \times e_{(2)} = - e_{(2)} \times e_{(1)} = e_{(3)} \]

Now let us write \(a \times b\) in the form \((a_1 e_{(1)} + a_2 e_{(2)} + a_3 e_{(3)}) \times (b_1 e_{(1)} + b_2 e_{(2)} + b_3 e_{(3)})\) and using the relations (2.32.2) to collect together the nine products we have \[ a \times b = (a_2 b_3 - a_3 b_2)e_{(1)} + (a_3 b_1 - a_1 b_3)e_{(2)} + (a_1 b_2 - a_2 b_1)e_{(3)}. \tag{2.32.3} \]

This shows how the components of the vector product are obtained from the products of the components of the two factors. The symbolic determinant \[ \begin{vmatrix} e_{(1)} & e_{(2)} & e_{(3)} \\ a_1 & a_2 & a_3 \\ b_1 & b_2 & b_3 \end{vmatrix} \]

is sometimes used to represent this, for expanding on the elements of the first row we have (2.32.3).

A very valuable notation can be introduced with the permutation symbol \(\epsilon_{ijk}\). This is defined by \[ \epsilon_{ijk} = \begin{cases} 0, & \text{if any two of } i, j, k \text{ are the same} \\ 1, & \text{if } ijk \text{ is an even permutation of } 1,2,3 \\ -1, & \text{if } ijk \text{ is an odd permutation of } 1,2,3 \end{cases} \tag{2.32.4} \]

The vector product can then be written as \[ (a \times b)_i = \epsilon_{ijk} a_j b_k. \tag{2.32.5} \]

If \(a \times b = 0\) the two vectors are parallel. The cross product of a vector with itself always vanishes.

Exercise 2.32.1. Show by enumerating typical cases that \(\epsilon_{ijk}\epsilon_{klm} = \delta_{il}\delta_{jm} - \delta_{im}\delta_{jl}\).

Exercise 2.32.2. Show that the condition for the vectors a, b, and c to be coplanar can be written \(\epsilon_{ijk}a_i b_j c_k = 0\).

Exercise 2.32.3. Show that if \(d = \alpha a + \beta b + \gamma c\), where a, b, and c are not coplanar then \(\alpha = \frac{\epsilon_{ijk} d_i b_j c_k}{\epsilon_{lmn} a_l b_m c_n}\), and find similar expressions for \(\beta\) and \(\gamma\).

Exercise 2.32.4. If a and b are any vectors, show that \((a \times b) \cdot (a \times b) + (a \cdot b)^2 = |a|^2 |b|^2\).

2.33. Velocity due to rigid body rotation A rigid body is one in which the mutual distance of any two points does not change. Suppose such a body rotates about an axis through the origin of coordinates with direction given by a unit vector \(\mathbf{n}\). If \(\omega\) is the angular velocity we can represent this rotation by a vector \[ \omega = \omega \mathbf{n}. \tag{2.33.1} \]

Let P be any point in the body at position x (see Fig. 2.5). Then \(\mathbf{n} \times x\) is a vector in the direction of PR of magnitude \(|x| \sin \theta\). However, \(|x| \sin \theta = PQ\) is the perpendicular distance from P to the axis of rotation. In a very short interval of time \(\delta t\) the radius PQ moves through an angle \(\omega \delta t\) and hence P through a distance \((PQ)\omega \delta t\). It follows that the very short distance PR is a vector \(\delta x\) perpendicular to the plane of OP and the axis of rotation and hence \[ \delta x = (\mathbf{n} \omega \delta t \times x) = (\omega \times x) \delta t.

\]

However, the limit as \(\delta t \to 0\) of \(\delta x / \delta t\) is the velocity v of the point P. Thus the linear velocity v of the point x due to a rotation \(\omega\) is \[ v = \omega \times x. \tag{2.33.2} \]

Whenever the velocity of the point at position x can be represented as a vector product of the position vector with a constant vector then the motion is due to a solid body rotation. If x and y are two points with velocities v and w due to a rigid body rotation, then also \(w = \omega \times y\) and by subtraction \[ (v - w) = \omega \times (x - y). \tag{2.33.3} \]

This shows that if the relative velocity of two points is related to their relative position in this way then their motion is due to a rigid body rotation.

Exercise 2.33.1. If a force f acts at a point x show that its moments about the three coordinate axes are the components of a vector, \(x \times f\).

Exercise 2.33.2. If a, b, and c are three non-coplanar vectors forming three edges of a tetrahedron, show that the vectors normal to each face of magnitude equal to the area of the face are \(n_1 = \frac{1}{2}(b \times c)\), \(n_2 = \frac{1}{2}(c \times a)\), \(n_3 = \frac{1}{2}(a \times b)\), \(n_4 = -\frac{1}{2}(a \times b + b \times c + c \times a)\).

Exercise 2.33.3. If n is the unit outward normal at any point of the surface of a tetrahedron and dS the element of surface area, show that \(\iint n \, dS\) taken over the whole surface is zero. Extend this result to a polyhedron and interpret it geometrically.

Exercise 2.33.4. Show that Snell's law of the refraction of light can be written \(\mu_1 m_1 \times n = \mu_2 m_2 \times n\) where \(\mu_1\) and \(\mu_2\) are the refractive indices of the two media either side of the interface to which the normal at the point of incidence is n. \(m_1\) and \(m_2\) are unit vectors in directions of the incident and refracted beams. Find a vectorial expression for the law of reflection of light.

2.34. Triple scalar product Of the possible products of three vectors a, b, and c the simplest is the scalar product of one with the vector product of the other two. This is known as the triple scalar product \(a \cdot (b \times c)\).

product a · (b × c) = ε_{ijk} a_i b_j c_k. (2.34.1)

We observe that the vanishing of this is just the condition for coplanarity of a, b, and c, for this says that a is orthogonal to the normal to the plane of b and c and so lies in it. (Cf. Ex. 2.32.2). Physically it may be interpreted as the volume of the parallelepiped with sides a, b, and c for b × c has magnitude equal to the area of one face and direction n normal to it and a · n is the height.

Notice that an even permutation may be applied to a, b, and c without changing the triple scalar product but that an odd permutation will change its sign. The notation [a, b, c] or (abc) is sometimes used for the triple scalar product.

2.35. Triple vector product Another product may be formed from three vectors a × (b × c). This is known as the triple vector product. Since b × c is a vector normal to the plane of b and c and a × (b × c) is a vector normal to b × c, the triple vector product must be in the plane of b and c and so can be expressed in the form a × (b × c) = βb + γc.

In component notation this is ε_{ijk} a_j ε_{klm} b_l c_m = β b_i + γ c_i.

However, by Ex. 2.32.1, ε_{ijk} ε_{klm} a_j b_l c_m = (δ_{il} δ_{jm} - δ_{im} δ_{jl}) a_j b_l c_m = b_i (a_j c_j) - c_i (a_j b_j)

and hence a × (b × c) = (a · c)b - (a · b)c. (2.35.1)

Permuting the letters in this equation we have the identity a × (b × c) + b × (c × a) + c × (a × b) = 0. (2.35.2)

There are a number of other identities and extensions to products of a larger number of factors. Some of these are given as exercises and are valuable practice in these elementary manipulations.

Exercise 2.35.1. Show a · (b × c) vanishes identically if two of the three vectors are proportional to one another.

Exercise 2.35.2. If e is any unit vector and a an arbitrary vector show that a = (a · e)e - e × (a × e).

This shows that a can be resolved into a component parallel to and one perpendicular to an arbitrary direction e.

Exercise 2.35.3. Prove that (i) (a × b) · (c × d) = (a · c)(b · d) - (a · d)(b · c)

(ii) (a × b) × (c × d) = [c · (d × a)]b - [c · (d × b)]a = [a · (b × d)]c - [a · (b × c)]d (iii) [a · (b × c)]d = [d · (b × c)]a - [a · (d × c)]b + [a · (b × d)]c

Exercise 2.35.4. Show that the two lines x = a + lr, x = b + ms, where r and s are parameters and l and m are two unit vectors, will intersect if a · (l × m) = b · (l × m) and find their point of intersection.

2.36. Reciprocal base systems We have seen (Section 2.23) that any triad of vectors can serve as a basis provided that they are not coplanar. Suppose b^{(1)}, b^{(2)}, and b^{(3)} are three vectors (the parenthetical index applies to the vector and not to the component but the summation convention will still apply) and B = b^{(1)} · (b^{(2)} × b^{(3)}) ≠ 0. (2.36.1)

They provide a basis and any vector a can be expressed in the form a = a^i b^{(i)}, (2.36.2)

where a^i are the components of the vector with respect to this basis.

From the triad of base vectors, three new base vectors can be constructed by putting b^{(1)} = (b^{(2)} × b^{(3)}) / B, b^{(2)} = (b^{(3)} × b^{(1)}) / B, b^{(3)} = (b^{(1)} × b^{(2)}) / B. (2.36.3)

This new triad has the property that the scalar product of b^{(i)} with b^{(j)} is unity but its scalar product with b^{(j)}, i ≠ j, is zero. We may write b^{(i)} · b^{(j)} = δ_{ij}. (2.36.4)

This proves the statement made earlier that no consistent definition of a single vector can be constructed but that a reciprocal triad to a triad of non- coplanar vectors does exist.

If the components of a with respect to the reciprocal base system are denoted by a_j then a = a_j b^{(j)}. (2.36.4)

However, comparing with Eq. 2.36.2 we have a_i b^{(i)} = a_j b^{(j)} and scalar multiplying each side by b^{(j)} gives a_j = a_i b^{(i)} · b_j. (2.36.5)

The components with respect to the reciprocal basis are thus related rather simply to the original components.

In particular, if the base vectors are a right-handed set of orthogonal unit vectors B = 1 and b^{(i)} = b_i. Thus for a Cartesian basis the reciprocal set is identical with the original. Therefore, for Cartesian vectors we have no need to make the distinction between reciprocal bases that will prove fruitful in a more general context.

Exercise 2.36.1. Show that b^{(i)} · (b^{(2)} × b^{(3)}) = B^{-1} and that b^{(i)} · b^{(j)} = δ_{ij} (b^{(2)} × b^{(3)}) etc.

Notice that the formula b^{(i)} = ε_{ijk} (b^{(j)} × b^{(k)}) / B expresses all three of these relations.

Exercise 2.36.2. If the basis is a right-handed triad of orthogonal vectors not of equal lengths, show that the reciprocal basis vectors have the same three directions but lengths reciprocal to the original vectors.

2.41. Second order tensors The vector or first order tensor was defined as an entity with three com- ponents which transformed in a certain fashion under rotation of the coordi- nate frame. We define a second order Cartesian tensor similarly as an entity having nine components A_{ij}, i, j = 1,2,3, in the Cartesian frame of reference Ox_1x_2x_3 which on rotation of the frame of reference to Ox'_1x'_2x'_3 become A'_{rs} = l_{ri} l_{sj} A_{ij}. (2.41.1)

By the orthogonality properties of the direction cosines l_{ij} we have the inverse transformation A_{ij} = l_{ir} l_{js} A'_{rs}. (2.41.2)

To establish that a given entity is a second order tensor we have to demon- strate that its components transform according to Eq. (2.41.1). A valuable means of establishing tensor character is the quotient rule which will be discussed later in Section 2.6.

A second order tensor may be written down as a 3 x 3 matrix A = [ A_{11} A_{12} A_{13} ]

[ A_{21} A_{22} A_{23} ]

[ A_{31} A_{32} A_{33} ]

and it is occasionally convenient to treat it as such. In the notation of matrices (see Appendix, paragraphs A5 and A6) the transformations above would be written L' A L = A' or A = L A' L'. We shall use a boldface A to denote the tensor as such but more frequently use the typical component A_{ij}.

If A_{ij} = A_{ji} the tensor is said to be symmetric and a symmetric tensor has only six distinct components. If A_{ij} = -A_{ji} the tensor is called antisym- metric and such a tensor is characterized by only three scalar quantities for the diagonal terms A_{ii} are zero. The tensor whose ij^{th} element is A_{ji} is called the transpose A' of A.

The analogy with a matrix allows us to define a conjugate second order tensor. The determinant of a tensor A is the determinant of the matrix A, namely, det A = ε_{ijk} A_{1i} A_{2j} A_{3k}. (2.41.3)

If this is not zero we can find the inverse matrix by dividing the cofactor of each element by the determinant and transposing. This is called the conjugate tensor and is as close as we come to division in tensor analysis. It will have been evident from the very variety of the definitions of multiplication that no definition of the quotient of vectors is possible. If we denote the elements of the conjugate tensor by A^{ij}, then from matrix theory we see that A^{ij} A_{jk} = δ_{ik}.

We shall not pursue this topic here but will prove later, in a more general context, that the conjugate is a tensor with these properties (see Section 7.24).

2.42. Examples of second order tensors A second order tensor we have already encountered is the Kronecker delta δ_{ij}. Of its nine components six vanish and the remaining three are all equal to unity. However, it transforms as a tensor for its components in the frame Ox'_1x'_2x'_3 are δ'_{rs} = l_{ri} l_{sj} δ_{ij} = l_{ri} l_{rj} = δ_{rs}, (2.42.1)

by the orthogonality relations between the direction cosines l_{ij}. In fact, the components of δ_{ij} in all coordinate systems are the same, namely, 1 if i = j but zero otherwise. δ_{ij} is called an isotropic tensor for this reason.

If a and b are two vectors the set of nine products a_i b_j = A_{ij} is a second order tensor, for A'_{rs} = a'_r b'_s = (l_{ri} a_i) (l_{sj} a_j) = l_{ri} l_{sj} (a_i a_j)

= l_{ri} l_{sj} A_{ij}. (2.42.2)

An important example of this is the momentum flux tensor for a fluid. If ρ is the density and v the velocity, ρ v_i is the i^{th} component in the direction Ox_i.

The rate at which this momentum crosses a unit area normal to Ox_j is ρ v_i v_j.

We will reserve a discussion of two important second order tensors until the next chapter. These are the rate of strain and stress tensors.

Exercise 2.42.1. Prove that for any vector a, ε_{ijk} a_k are the components of a second order tensor.

Exercise 2.42.2. Show that the flux of any vector property of a flowing fluid can be represented as a second order tensor.

Exercise 2.42.3. If r^2 = x_i x_i and f(r) is any twice differentiable function, show that the nine derivatives ∂^2 f / ∂ x_i ∂ x_j are the components of a tensor.

2.43. Scalar multiplication and addition If α is a scalar and A a second order tensor, the scalar product of α and A is a tensor αA each of whose components is α times the corresponding com- ponent of A.

The sum of two second order tensors is a second order tensor each of whose components is the sum of the corresponding components of the two tensors.

Thus the ij^{th} component of A + B is A_{ij} + B_{ij}. Notice that tensors must be of the same order to be added; a vector cannot be added to a second order tensor. A linear combination of tensors results from using both scalar multiplication and addition. αA + βB is the tensor whose ij^{th} component is αA_{ij} + βB_{ij}. Subtraction may therefore be defined by putting α = 1, β = -1.

Any tensor may be represented as the sum of a symmetric part and an antisymmetric part. For A_{ij} = ½(A_{ij} + A_{ji}) + ½(A_{ij} - A_{ji}) (2.43.1)

and interchanging i and j in the first factor leaves it unchanged but changes the sign of the second. Thus, A = ½(A + A') + ½(A - A') (2.43.2)

represents A as the sum of a symmetric tensor and antisymmetric tensor.

Exercise 2.43.1. Prove that αA_{ij} + βB_{ij} are the components of a second order tensor, if A_{ij} and B_{ij} are.

2.44. Contraction and multiplication The operation of identifying two indices of a tensor and so summing on them is known as contraction. A_{ii} is the only contraction of A_{ij}, A_{ii} = A_{11} + A_{22} + A_{33} (2.44.1)

and this is no longer a tensor of the second order but a scalar, or tensor of order zero. To show that it is a zero order tensor we must show that it is invariant under rotation of axes. Now in the frame of reference Ox'_1x'_2x'_3 the contracted tensor is obtained by identifying the suffixes of A'_{rs}. Thus, A'_{rr} = l_{ri} l_{rj} A_{ij} = δ_{ij} A_{ij} = A_{ii}. (2.44.1)

笛卡尔向量与张量：其代数

2.44 由于 δ_ip δ_jp = δ_ij，基于 l_ij 的正交性。标量 A_ii 称为二阶张量的迹。有时使用记号 tr A。

若 A 和 B 是两个二阶张量，我们可以从每个张量的 9 个分量的乘积中形成 81 个数，A_ij B_km，i, j, k, m = 1, 2, 3。这些乘积的完整集合构成一个四阶张量的分量，我们尚未定义该四阶张量。在带横杠的坐标系中，相应的乘积集是 A'_ij B'_km，但这明显是方程 (2.42.1) 的类比，但现在每边有四个自由指标，并由四个方向余弦的乘积变换。这就是四阶张量的定义，将在第 2.6 节正式给出。

然而，这个一般乘积的缩并是二阶张量。它们是 A_ij B_kj, A_ij B_ik, A_ij B_jk。（缩并 A_ii B_kk 和 A_ij B_jk 当然是标量 A_ii 和 B_kk 与张量 A 和 B 的标量积。）

后缀表示法清楚地指明了涉及哪种缩并。然而，标量积的记号有时很有用。在此记号中，分量为 A_ij B_jk 的张量写作 A B，求和在相邻后缀上进行。上面列出的四种形式因此分别是 B A, A' B, A B', 和 A B。

向量 a 与张量 A 的乘积 A·a 是一个向量，其第 i 个分量是 A_ij a_j。这两个量可能的另一个乘积是 A_ji a_j。它们可以分别写作 A a 和 a A。

双重缩并乘积 A_ij B_ji 是一个标量，可以写作 A : B。

练习 2.44.1. 直接证明 A_ij B_ji 是一个二阶张量。

练习 2.44.2. 证明练习 2.42.3 中张量的迹为

2.45. 反对称张量的向量三维空间中的一个向量与反对称二阶张量之间有一个非常重要的关系。两者都有三个独立分量，两者可以表示为如下形式： ω = [0 -ω_3 ω_2; ω_3 0 -ω_1; -ω_2 ω_1 0] (2.45.1)

在我们已经建立的记号中，P 的分量可以写作 Ω_ij = ε_ijk ω_k (2.45.2)

在从 P 推导 Ω 的分量时，我们注意到如果形成 ε_ijk P_kl，那么对于任何固定的 k，只有 i ≠ k 和 j ≠ k 的项会出现。因此， Ω_ij = ε_ij1 P_13 + ε_ij2 P_21 + ε_ij3 P_32 等等。由此得出 ω_k = (1/2) ε_kij Ω_ij (2.45.3)

利用排列符号的性质，这些公式中的指标可以互换。例如， ω_k = (1/2) ε_kij Ω_ij = - (1/2) ε_kji Ω_ij 或者 Ω_ij = ε_ijk ω_k。

记号 ω 和 vec P 有时用于 2ω 和 ω。

这个关系的重要性在于向量 a 与 ω 的叉积与反对称张量和 a 的缩并乘积的恒等性。因为 a × ω 的第 i 个分量是 ε_ijk a_j ω_k，而缩并乘积 Ω · a 是一个向量，其第 i 个分量是 Ω_ij a_j。因此， a × ω = Ω · a 或 a × a = ω × a。 (2.45.4)

第 2.33 节的结果可以用反对称张量重新解释：如果任意两点的相对速度 v 等于 Ω × x，其中 Ω 是一个与两点相对位置向量 x 无关的反对称二阶张量，则该运动是刚体转动。在此情况下，角速度由 -vec Ω 给出。这个结果在解释应变率张量时至关重要。

练习 2.45.1. 解释当速度的第 i 个分量为 ε_ijk c_j x_k（c 为常向量，x 为位置向量）时的运动。

2.5. 对称张量的标准形如果能够将张量化为对角形式，那么张量的解释和操作通常会大大简化。例如，如果告诉我们变形后一组点位于表面 A_ij x_i x_j = 1 上，那么我们对变形就了解了很多。如果 A_ij = A_ji，该表面具有方程 A_11 x_1^2 + A_22 x_2^2 + A_33 x_3^2 + 2 A_12 x_1 x_2 + 2 A_13 x_1 x_3 + 2 A_23 x_2 x_3 = 1。 (2.5.1)

这显然是一个二次曲面（椭球面、双曲面、抛物面、锥面或平面偶），关于原点对称，但除非具备高度发展的几何洞察力，否则很难说更多。然而，如果张量是 A_ij = a_i^{-2} δ_ij 且 i ≠ j 时为 0，那么该表面将是 x_1^2 / a_1^2 + x_2^2 / a_2^2 + x_3^2 / a_3^2 = 1。 (2.5.2)

任何学童都会知道他处理的是一个半轴为 a_1, a_2 和 a_3 的椭球面。或者，假设他只熟悉椭圆的方程，他会立即论证该表面关于所有坐标平面都是对称的，并且由平面 x_3 = 常数所截的截面是椭圆，其半轴为 a_1 √(1 - x_3^2/a_3^2) 和 a_2 √(1 - x_3^2/a_3^2)。

这两者的比值是常数，因此这些截面是相似的椭圆，它们的大小与 √(1 - x_3^2/a_3^2) 成正比，当 x_3 从 0 增加到 a_3 时，该值从 1 减小到 0。因此，通过初等推理，可以对该表面的性质获得非常好的印象。我们将证明，总存在一个坐标系 Oxyz，其中张量 A 具有对角形式。该方法严格遵循将矩阵化为标准形的对应步骤，该步骤在附录第 10-12 节中处理。因此，我们将仅在特征值互异的情况下给出化简过程，并将更一般情况转换为张量表示法的工作留给读者。

如果 a 是一个任意向量，A a 是一个向量，对于特定的 a，它可能具有与 a 本身相同的方向。向量 A a 和 a 将仅在大小上不同，我们可以写作 A a = λa。将其写成分量形式 A_ij a_j = λ a_i = λ δ_ij a_j 或 (A_ij - λ δ_ij) a_j = 0。 (2.5.3)

然而，这是关于未知量 a_j 的三个齐次方程组，因此只有在系数行列式为零时才有解。因此，λ 的值必须满足三次方程 det(A_ij - λ δ_ij) = λ^3 - A_ii λ^2 + Θ λ - Y = 0。 (2.5.4)

在此方程中，通过展开行列式，我们有 Θ = A_11 A_22 + A_22 A_33 + A_33 A_11 - A_12^2 - A_23^2 - A_31^2 Y = det A_ij。

并且这些被称为张量的三个不变量，因为它们的值在坐标系旋转下保持不变。方程 (2.5.4) 称为张量的特征方程，三个 λ 值称为其特征值。与矩阵一样，有时也使用固有根或本征值这些名称。

如果 λ 满足特征方程，则可以找到对应的 a_i。然而，尽管 (2.5.3) 中有三个方程，行列式为零意味着第三个方程线性依赖于前两个，否则唯一解将是平凡解 a = 0。两个独立方程可以求解得出 a_1/a_3 和 a_2/a_3 的比值，a_1, a_2, a_3 的大小现在可以通过要求 a_1^2 + a_2^2 + a_3^2 = 1 来固定。

如果 λ_k，k = 1, 2, 3，是三个特征值，我们可以将对应的特征向量写作 a_{(k)i}，其中第一个指标是分量的指标，第二个指标是它所属特征值的指标。我们现在要证明，如果 A_{(p)}, A_{(q)}, 和 A_{(r)} 互不相同，那么当 A 对称时，a_{(p)i}, a_{(q)i}, 和 a_{(r)i} 两两正交。

考虑两个具有指标 p 和 q 的固有根。我们有 A_ij a_{(p)j} = A_{(p)} a_{(p)i} 且 A_ij a_{(q)j} = A_{(q)} a_{(q)i}。 (2.5.6)

（注意：这些方程右边对 p 或 q 不求和：为此，A 上的后缀 q 被放在括号中）。将第一个方程乘以 a_{(q)i}，第二个方程乘以 a_{(p)i}，则 A_ij a_{(q)i} a_{(p)j} = A_{(p)} a_{(p)i} a_{(q)i} 且 A_ij a_{(p)i} a_{(q)j} = A_{(q)} a_{(q)i} a_{(p)i}。

然而，A 是对称的，所以 A_ij = A_ji，我们可以在第一个方程中交换哑指标而不改变其值。因此 A_ij a_{(p)i} a_{(q)j} = A_{(p)} a_{(p)i} a_{(q)i} = A_{(q)} a_{(q)i} a_{(p)i}。 (2.5.7)

并且 A_{(p)} 和 A_{(q)} 被假设为互异，因此方程只能在 a_{(p)i} a_{(q)i} = 0 时成立。然而，这意味着 a_{(p)} · a_{(q)} = 0，因此向量是正交的。同样，由它们的构造，a_{(p)} · a_{(p)} = 1，所以 a_{(p)i} a_{(q)i} = δ_{pq}。 (2.5.8)

然而，这是方向余弦 l_{ij} 所满足的关系，它指定坐标系的旋转，这个解释可以放在特征向量上。因此，如果坐标 X_j = l_{ji} x_i，那么张量 A 在参考系 O'X'Y'Z' 中的分量为 A'_{pq} = l_{pi} l_{qj} A_ij = A_{(p)} l_{pi} l_{qj} = A_{(p)} δ_{pq}， (2.5.9)

由 (2.5.7) 和 (2.5.8) 得出。这仅仅说明 A 具有对角形式，其对角分量为 A_{(1)}, A_{(2)}, 和 A_{(3)}。

由归一化特征向量给出的方向称为张量的主方向或主轴。当使用坐标轴与所涉及张量之一的主轴重合的坐标系时，通常可以很容易地证明张量关系。一旦建立了这种关系并以正确的张量形式表达，它必须对所有坐标系都成立，因为所涉及的张量作为张量进行变换，因此它们的关系保持不变。这就是张量分析的巨大优点。一个显著的例子将在第 4 章给出，其中展示了 Serrin 关于应力-应变率关系的优雅处理。

练习 2.5.1. 证明 Θ, Λ, 和 Y 在旋转轴下是不变量。

练习 2.5.2. 追踪附录（第 A.11 节）中给出的特征值相等的情况，将矩阵表示法转换为张量表示法。

练习 2.5.3.（凯莱-哈密顿定理）证明 A^3 - Θ A^2 + Λ A - Y I = 0。

练习 2.5.4. 如果 A_ij 和 B_ij 有一个公共主方向，证明这也是张量 A_ik B_kj 和 B_ik A_kj 的主方向。

2.61. 高阶张量我们现在可以相当简洁地陈述任意阶笛卡尔张量的一般定义和运算定律，因为读者应该通过看到更简单的例子而熟悉它们的行为。

定义。n 阶张量 A_{i1i2...in} 是一个由 3^n 个分量定义的量，这些分量可以写为 written A_{ij...n} provided that under rotation to a new coordinate frame they transform according to the law (2.61.1).

Symmetries. If interchange of two of the indices does not change the value of the component the tensor is said to be symmetric with respect to these indices. If the absolute value is unchanged but the sign reversed it is antisymmetric with respect to the indices.

Contraction. The 3^{n-2} quantities formed by identifying two of the indices of an nth order tensor and invoking the summation convention are components of a tensor of order n-2.

Scalar multiplication. If μ is any scalar μA is the tensor with components μA_{ij...n}.

Addition. If A and B are tensors of the same order they may be added to give a tensor with components A_{ij...n} + B_{ij...n}.

Multiplication. If A_{ij...n} and B_{k...l} are tensors of order n and m respectively, the set of products A_{ij...n} B_{k...l} are the components of a tensor of order n + m. This tensor can be contracted in different ways to form tensors of orders n + m - 2, n + m - 4, ..., 1 or 0.

The laws of tensor algebra are: aA = Aa, a(A + B) = aA + aB, a(AB) = (aA)B = A(aB), A + B = B + A, A + (B + C) = (A + B) + C, A(B + C) = AB + AC.

Since a great variety of products of two tensors are possible, nothing comparable to AB = BA can be asserted in general.

Exercise 2.61.1. Prove that contraction preserves the tensor character while lowering the order by two.

Exercise 2.61.2. Prove that A_{ij} b_j is a third order tensor.

§2.62. The quotient rule We have constantly remarked that to prove that a given set of quantities forms the set of the components of a tensor requires that we show that they transform according to the rule of tensor transformation. A short cut in establishing tensorial character is the so-called quotient rule. The simple case we shall prove is as follows: If A_{ij}, i,j = 1,2,3 are nine quantities and b and c are vectors, b being quite independent of the A_{ij}, and A_{ij} b_j = c_i, then the A_{ij} are components of a tensor A. The value of this is that a relation Ab = c may arise in the study of a physical situation in which it is known that b and c are vectors. Then the quotient rule establishes that A is a tensor and we are now assured that the equation holds in all coordinate frames.

To prove the rule we observe that if A really is a tensor it must satisfy two requirements. First, the equation Ab = c being a tensor equation must transform to A' b' = c', that is, A'_{ij} b'_j = c'_i. Second, the components must transform as tensor components, that is, A'_{ij} = I_{i'i} I_{j'j} A_{ij}. Let us define A'_{ij} = I_{i'i} I_{j'j} A_{ij} so that the first relation is satisfied, and see if these quantities have the correct transformation property. Now b and c are vectors, so b'_i = I_{i'i} b_i and c'_i = I_{i'i} c_i.

Hence, A'_{ij} b'_j = c'_i = I_{i'i} c_i = I_{i'i} A_{ij} b_j = I_{i'i} I_{j'j} A_{ij} I_{j'j}^{-1} b'_j, or (A'_{ij} - I_{i'i} I_{j'j} A_{ij}) b'_j = 0. (2.62.2)

However, b is independent of A so that this relation can only hold if the expression in the brackets vanishes, that is, A'_{ij} = I_{i'i} I_{j'j} A_{ij}. (2.62.3)

This shows that A_{ij} transforms as a tensor. The proof can be easily adapted to the following more general rule.

If A_{ij...n} is a set of 3^n quantities and B_{k...l} a tensor of order m independent of A and the k times contracted product A_{ij...n} B_{...} is a tensor of order m + n - 2k, 1 ≤ k ≤ ½(n-1)n, then A_{ij...n} is a tensor of order n.

A special case arises if B is the product of n vectors and A_{ij...n} b_i c_j ... e_n can be shown to be a scalar. This again establishes that A is an nth order tensor.

Exercise 2.62.1. Prove the quotient rule in detail for A_{ij} B_{ik} = C_{jk} and A_{ij} b_i c_j = scalar.

§2.7. Isotropic tensors An isotropic tensor is one whose components are unchanged by rotation of the frame of reference. The trivial cases of this are the tensors of all orders whose components are all zero. All tensors of the zeroth order are isotropic and there are no first order isotropic tensors. We have already met the only isotropic second order tensor, namely, δ_{ij}, but it is of interest to prove that it is the only one.

Consider a general second order tensor A_{ij} and apply some particular rotations to it. The first of these is a rotation about a line equally inclined to all three coordinate axes, that is, with direction cosines all equal to 3^{-1/2}. A rotation of 120° such as is shown in Fig. 2.6 can be made to carry the 01 axis into the 03 position, the 02 into the 01, and the 03 into the 02. Thus, l_{11} = l_{22} = l_{33} = 1/3 and the other l_{ij} are zero. Hence, for example, A'_{11} = A_{33} and A'_{33} = A_{13}.

However, if A is isotropic, A'_{11} = A_{11} and A'_{33} = A_{33}, and so A_{11} = A_{22} = A_{33}, and A_{12} = A_{23} = A_{31}, etc.

Applying this to each component in turn we see that A_{11} = A_{22} = A_{33} (2.7.1)

A_{12} = A_{23} = A_{31} = A_{13} = A_{21} = A_{32} (2.7.2)

Now apply a rotation through a right angle about 03, so that l_{12} = -l_{21} = 1 and the other l_{ij} are zero. Then A'_{12} = -A_{12} by the transformation and A'_{12} = A_{12} by the requirement of isotropy. Thus by (2.7.2) A_{12} = A_{12} and now A_{12} = -A_{12} and the only way these can be simultaneously true is for them both to be zero. It follows that all the off-diagonal components (i ≠ j) are zero and all the diagonal ones are equal. Clearly a scalar multiple of an isotropic tensor is isotropic and so we may take A_{ij} = δ_{ij}.

The idea of isotropy for a second order tensor is connected with the geometrical figure of a sphere. We have noticed that A_{ij} x_i x_j = 1 is the equation of a quadric surface. The ellipsoid may be regarded as the typical quadric and clearly if its axes are unequal a rotation of the coordinate frame will require a different equation. A sphere, however, is invariant as a whole under rotation of axes and has the equation x_1^2 + x_2^2 + x_3^2 = r^2. This corresponds to the tensor A_{ij} = δ_{ij}/r^2, so that isotropy is to be interpreted as geometrical invariance under rotation. (Cf. Fig. 2.7.)

Of tensors of the third order the only isotropic one is ε_{ijk}. We may see the isotropic character of this by writing T_{ijk} = ε_{ijk} which is evidently the determinant | l_{i1} l_{i2} l_{i3} | | l_{j1} l_{j2} l_{j3} | | l_{k1} l_{k2} l_{k3} | and if ijk is an even permutation of 123 the determinant is unchanged, but if it is an odd permutation, 2_{ijk} = 1. However, this is just the definition of ε_{ijk} and so the components are unchanged by rotation.

The isotropic tensors of the fourth order are of some importance and there are three independent ones. It is clear that a product of isotropic tensors is isotropic so that we can immediately write down two such, namely, δ_{ij}δ_{kl} and δ_{ik}δ_{jl}, but we need to work harder to find all the independent isotropic tensors. To outline the reasoning which is necessary to be sure we have all, it is convenient to divide the 81 components of a fourth order tensor T_{ijpq} into classes as follows.

Class Character Typical member I All suffixes the same T_{1111} II Three suffixes the same T_{1112} III(i) Suffixes the same in pairs T_{1122} III(ii) T_{1212} III(iii) T_{1221} IV Only two suffixes the same T_{1123}

(Since the suffixes must be equal to either 1,2, or 3, it follows that at least two of them are the same.)

We now apply special rotations of the type shown in Fig. 2.6. These are listed in the table opposite by giving the nonzero l_{ij} of the transformation, and their effect on the typical member of each class is shown. We can write the transformation as an equality since the isotropic requirement is for the component to be unchanged. The second line is the effect of the transformation on another member of the class needed for the conclusion. Under class II, for example, we find T'_{1112} = T_{2223} = -T_{1112}, and T'_{1112} = T_{1112} and the conclusion is that T_{1112} = T_{2223} = 0 and consequently all members of the class are zero. In the tensor representation of the class we put T_{ijpq} = 1 if i = j = p = q but zero otherwise. Then the representation of the subclasses of class III is given by a combination of Kronecker deltas and T_{ijpq}. For example, δ_{ij}δ_{pq} will be 1 if i = j and p = q, but the definition of the class excludes the possibility i = j = p = q so that δ_{ij}δ_{pq} - T_{ijpq} represents it.

Suppose then we make a linear combination of these and write T_{ijpq} = aδ_{ij}δ_{pq} + bδ_{ip}δ_{jq} + cδ_{iq}δ_{jp} + (d - a - b - c)T_{ijpq}, (2.7.4)

This certainly has isotropic properties under the rotations A, B, and C of the table but these are rather special since they leave a cube invariant as a whole. If we take a rotation that does not leave the cube invariant, for example, a rotation about 03 through an angle θ, then T_{ijpq} is not invariant. Hence we must put d = a + b + c and the general isotropic tensor can be written as a linear combination of the first three.

We observe that δ_{ij}δ_{pq} is the product of two second order isotropic tensors and that the contracted product ε_{ijk}ε_{pqk} is the difference of the other two. It is sometimes convenient to take the general isotropic tensor to be T_{ijpq} = λδ_{ij}δ_{pq} + μ(δ_{ip}δ_{jq} + δ_{iq}δ_{jp}) + ν(δ_{ip}δ_{jq} - δ_{iq}δ_{jp}). (2.7.5)

The second term is symmetric with respect to the first and second or third and fourth indices and the third term is antisymmetric with respect to them.

Exercise 2.7.1. Show that ε_{ijk} is the only isotropic tensor of the third order.

Exercise 2.7.2. Show that if T_{ijpq} is an isotropic fourth order tensor then the symmetric tensors A_{ij} and T_{ijpq} A_{pq} have the same principal axes.

Exercise 2.7.3. Show that under a suitable rotation any component of T_{ijpq} can be made nonzero.

§2.81. Dyadics and other notations There is no need to give a full discussion of the history of vector and tensor notations, but it will be useful to mention some other forms that appear in the literature and to define by comparison the usage of this book.

The notation on which we have largely depended is sometimes known as the kernel-index method. The tensor is Represented by its typical component, Aij, A being the kernel letter and i and j the indices. It is quite useful, but not at all necessary, to use a lower case letter for the tensor of the first order. This notation is entirely adequate but it is often convenient to use a single bold-face symbol without suffixes for the tensor. We have done this more with vectors than with second order tensors, for such expressions as a b, a A b, etc. are unambiguous whereas some care is needed in distinguishing tensor products A B, A' B, etc. In general it is probably easier in manipulations to have the suffixes written explicitly and so avoid the danger of mistakes that the suppression of suffixes induces. However, the physical meaning of the final formulae is often brought out more clearly by the dyadic notation of bold face symbols.

The name “dyad” is applied to the product of two vectors ab and is a tensor with components a_i b_j. If

C = Σ a^{(r)} b^{(r)} (2.81.1)

is the sum of n dyads, it is called a dyadic. The products C c and c C are defined by

C c = Σ a^{(r)} (b^{(r)} · c)

and

c C = Σ (c · a^{(r)}) b^{(r)}.

* See, for example, J. A. Schouten, Tensor Analysis for Physicists (Oxford University Press, Oxford, 1951), p. 110.

The dyads formed from the three unit vectors e^{(i)} give a convenient representation of the dyadic or second order tensor

A = e^{(i)} e^{(j)} A_{ij} (2.81.3)

where A_{ij} is the component of the tensor and the summation convention is invoked even on the bracketed indices. Another standard form of dyadic is composed from three vectors a, b, and c in the form

A = a^{(1)} a^{(2)} b^{(3)} c (2.81.4)

and the transposed tensor is called the conjugate dyadic

A_t = b^{(1)} c^{(2)} a^{(3)} (2.81.5)

If we replace the dyads in these forms by scalar and vector products, we have the scalar of the dyadic

A_s or A = e^{(1)} · a e^{(2)} · b e^{(3)} · c (2.81.6)

and the vector of the dyadic

A_v or A_v = e^{(1)} × a e^{(2)} × b e^{(3)} × c. (2.81.7)

The scalar of the dyadic is the same as the trace or spur of the tensor for it is simply the contraction. For an antisymmetric dyadic (A_t = -A) the vector of the dyadic is twice the vector of the antisymmetric tensor.

In multiplication of dyadics the rule is that summation should always be on adjacent indices. For example, the corresponding dyadic and tensor forms are:

A_{ij} B_{jk}

A_{ij} B_{jk}

a A_i B_{jk} A_{km}

A A_i B_{jk} A_{kl}

The symbol × is more commonly used with dyadics than is A, but we retain the latter to be consistent with the vector notation to which we have given preference.

Exercise 2.81.1. Translate the equations of Section 2.5 into dyadic notation.

Exercise 2.81.2. Show that a × (b ∧ A) = (a ∧ b) ∧ A.

Exercise 2.81.3. Prove that if A_t = -A, then A_t ∧ a = 2a ∧ A.

§2.82. Axial vectors

The only transformation of coordinates we have considered is the rotation of a right-handed Cartesian system. A slight extension of this would be to allow reflections in the coordinate planes as well as rotations. In this case a right-handed coordinate frame is transformed into a left-handed one. The matrix L of the direction cosines l_{ij} is still an orthogonal one but its determinant is -1 instead of 1. Now certain items in our constructions have depended on our maintaining the convention of right-handedness. Thus a = b × c, for example, gives a definite sense to the direction of a by the requirement that b, c, a should form a right-handed system in that order. If we transform to a left-handed system, the vector product changes sign, for

A' = L_{ip} L_{jq} L_{kr} A_{pqr}

= -ε_{ijk} l_{ip} l_{jq} l_{kr} b_p c_r = -A,

since the determinant of the l_{ij} is -1. A vector which does this is called an axial vector or pseudo vector. It can be thought of as a vector with given direction and magnitude but reversible sense of direction. We do not have much need of the distinction at this stage, but will find later that it is the same as the distinction between an absolute tensor and one of weight 1.

## BIBLIOGRAPHY

The wealth of texts on vectors and tensors makes it an invidious task to give a brief list. Those mentioned here are mentioned in connection with the specific point of reference and omission casts no aspersion.

2.1. Many accounts of Cartesian vectors and tensors are included in the various volumes of “Mathematical Methods of ...” and “Applied Mathematics for ...”. In particular H. Jeffreys’ “Cartesian Tensors” (Cambridge 1931) is largely contained in

Jeffreys, H. and B. S., Methods of mathematical physics, (2nd Ed.). Cambridge: Cambridge University Press, 1950.

The classic text on dyadics is that founded on Gibbs’ lectures.

Wilson, E. B., Vector analysis. New Haven: Yale University Press, 1901.

A discussion of dyadics as well as of vector and tensor formalism will be found in

Morse, P. M., and H. Feshbach, Methods of theoretical physics. New York: McGraw-Hill, 1953.

A more elementary account of dyadics is given in

Phillips, H. B., Vector analysis, Chapter 10. New York: John Wiley, 1933.

Often an account of fluid mechanics will open with a brief résumé of the vector notation to be used. See, for example,

Serrin, J., Mathematical principles of classical fluid mechanics, in Handbuch der Physik, Bd. VIII/1, ed. Flugge and C. Truesdell. Berlin: Springer-Verlag, 1959.

or

Truesdell, C., The kinematics of vorticity. Bloomington: Indiana University Press, 1954.

Cartesian Vectors and Tensors: Their Calculus

§3.11. Tensor functions of a time-like variable

In the last chapter we considered only the algebraic manipulations and relationships of tensors. We now want to find out what we can say about the behavior of tensors when they are functions of continuous variables. Certainly this will be necessary in applications, for if we think of an unsteady fluid motion we realise that we shall have to consider its velocity at any point or time. Now velocity is a vector so we shall have a vector v whose components are functions of the coordinates x1, x2, x3 and time t. Any variable which is independent of the coordinates can be called time-like since in many applications it will be the time. We will consider first tensors whose components are functions of one such variable, t.

Suppose A_{ij} = A_{ij}(t) is a tensor function; then it is clear that all the derivatives of it that exist are themselves tensors, for the l_{ip} of the transformation are independent of t and we may differentiate the relation

A'_{ij}(t) = l_{ip} l_{jq} A_{pq}(t) (3.11.1)

as many times as we are able, to give

d^n A'_{ij}/dt^n = l_{ip} l_{jq} d^n A_{pq}/dt^n. (3.11.2)

We may integrate the tensor components and preserve their character equally well.

The most important example of this has already been cited. If x, the position vector of a particle, is a function of time, then its first derivative is the velocity

v(t) = ẋ(t), v_i = dx_i/dt (3.11.3)

and its acceleration is

a(t) = ẍ(t), a_i = d^2 x_i/dt^2. (3.11.4)

The differentiation of products of tensors proceeds according to the usual rules of differentiation of products. In particular,

d(a b)/dt = (da/dt) b + a (db/dt), (3.11.5)

and

d(a × b)/dt = (da/dt) × b + a × (db/dt). (3.11.6)

Exercise 3.11.1. Show that if a particle moves with constant speed its acceleration is normal to its velocity.

Exercise 3.11.2. Show that the acceleration of a particle moving in the surface of a sphere of radius r has a radial component -v^2/r, where v is its speed.

Exercise 3.11.3. If a(t), b(t), and c(t) are three mutually orthogonal unit vectors, show that their first derivatives are coplanar.

Exercise 3.11.4. Show that if the position vector of a particle, its velocity, and its acceleration are coplanar, then all the higher derivatives are in the same plane.

Exercise 3.11.5. Show that x ∧ (dx/dt) = 0 is the condition that x(t) should remain parallel to itself.

Exercise 3.11.6. If a is the component of a vector a with respect to a system of base vectors b^{(1)}, b^{(2)}, b^{(3)}, show that b^{(j)} = ∂a/∂a_j.

§3.12. Curves in space

The variable position vector x(t) describes the motion of a particle. For a finite interval of t, say a ≤ t ≤ b, we can plot the position as a curve in space. If the curve does not cross itself (that is, if x(t) ≠ x(t'), a ≤ t < t' ≤ b) it is called simple; if x(a) = x(b) the curve is closed. The variable t is now just a parameter along the curve which may be thought of as the time in the motion of the particle only if such picturesqueness is desired. If t and t' are the parameters of two points, the chord joining them is the vector x(t') - x(t). As t → t' this vector approaches (t' - t) ẋ(t) and so in the limit it is proportional to ẋ(t). However, the limit of the chord is the tangent so that ẋ(t) is in the direction of the tangent. If v^2 = ẋ · ẋ we can construct a unit tangent

If x(t) and x(t + dt) are two very close points, then

x(t + dt) = x(t) + dt ẋ(t) + O(dt^2)

and the distance between them is

|x(t A = T so far as in the since T·T = 1 T·i = 0 (3.12.4)

so that the vector i is at right angles to the tangent. Let n = i (3.12.5)

and v = T × i (3.12.6)

Then v is a unit normal and defines the direction of the so-called principal normal to the curve.

To interpret ρ, we observe that the small angle dσ between the tangents at s and s + ds is given by cos dσ = T(s)·T(s + ds)

or 1 = T·T + T·(dT/ds)ds + (1/2)T·(d²T/ds²)(ds)² + ...

= 1 + T·(dT/ds)ds + ...

Since T·T = 1, then d(T·T)/ds = 2T·(dT/ds) = 0. Thus, ρ = ds/dσ (3.12.7)

is the reciprocal of the rate of change of the angle of the tangent with arc length, that is, the radius of curvature. Its reciprocal 1/ρ is the curvature.

A second normal to the curve may be taken to form a right-hand system with T and v. This is called the unit binormal, b = T × v. (3.12.8)

Since b·b = 1, db/ds is perpendicular to b. However, b·T = 0 so (db/ds)·T + b·(dT/ds) = 0. As b·(dT/ds) = b·(v/ρ) = (T×v)·v/ρ = 0, then (db/ds)·T = 0 so db/ds is also at right angles to T and so must be in the direction of v. Let db/ds = -v/τ (3.12.9)

where 1/τ is a scalar known as the torsion. Clearly, 1/τ is the magnitude rate of change of the direction of the binormal, just as 1/ρ was the rate of change of the tangent.

Further, since v = b × T, we have dv/ds = (db/ds) × T + b × (dT/ds) = (-v/τ) × T + b × (v/ρ)

= (b × T)/τ - (b × v)/ρ = v/τ - T/ρ These three formulae, dT/ds = v/ρ dv/ds = -T/ρ + b/τ (3.12.11)

db/ds = -v/τ, are known as the Serret-Frenet formulae.

It may be shown that if two curves have the same dependence of curvature and torsion upon arc length, then they are the same curve apart from some translation or rotation in space. These two functions ρ(s) and τ(s) are the intrinsic equations of the curve.

Exercise 3.12.1. Interpret the curve given by x₁ = a cos (s cos α/a), x₂ = a sin (s cos α/a), x₃ = s sin α and find its curvature and torsion.

Exercise 3.12.2. Show that if the tangent to a curve makes a constant angle with a fixed direction then the ratio of its curvature and torsion is constant. Such a curve is called a helix.

Exercise 3.12.3. Prove that ρ²τ (d/ds)(T × dT/ds) = 1, and hence that the curve lies in a plane if dT/ds × T = 0.

3.13. Line Integrals If F(x₁, x₂, x₃), or more briefly F(x), is a function of position and C is the arc of a simple curve x = x(t), a ≤ t ≤ b, we can define the integral of F along C as ∫_C F·T ds = ∫_a^b F[x(t)]·(dx/dt) dt (3.13.1)

provided this second integral exists. If the curve C is composed of a number of arcs which have to be given by different equations, then an integral like the right-hand side of (3.13.1) must be calculated for each arc. If A and B are the end points of the curve (given by t = a and t = b, respectively) the integral above is the integral along C from A to B. The integral in the opposite direction from B to A is obtained by reversing the limits and therefore has the same absolute value but the opposite sign. If x(a) = x(b), the curve C is closed and the integral is sometimes written ∮ F·T ds.

An important case, and one which we shall frequently use, occurs when the parameter t is the arc length s.

∫_C F·T ds = ∫_a^b F[x(t)]·|dx/dt| dt. (3.13.2)

In general the line integral depends on F, the two end points and the path between them. If, however, the integral around any simple closed curve vanishes, the value of the integral from A to B is independent of the path. To see this we take any two paths between A and B, say C₁ and C₂, and denote by C the closed curve formed by following C₁ from A to B and C₂ back from B to A. Now ∮_C F·T ds = ∫_{C₁} F·T ds + ∫_{C₂ (reversed)} F·T ds = ∫_{C₁} F·T ds - ∫_{C₂} F·T ds and this vanishes by hypothesis, so that the integrals along the two different paths are equal.

If a(x₁, x₂, x₃) is any vector function of position, a·T is the projection of a on the tangent to the curve. The integral around a simple closed curve C of a·T is called the circulation of a around C, ∮_C a·T ds.

Since dxi/ds = Tᵢ, this integral is sometimes written ∫ aᵢ dxᵢ or ∫ a·dx; we shall prefer however to write the integral with the unit tangent vector explicit.

Exercise 3.13.1. Evaluate the integral ∫_C a·T ds where C is the circle of radius b and center the origin lying in the plane x₃ = 0 and a = (1/b) x × i₃. T is the unit tangent to C.

Exercise 3.13.2. Show that if C is a simple closed curve in the plane 012 then it encloses an area (1/2) ∮ x₁T₂ ds = -(1/2) ∮ x₂T₁ ds = (1/2) ∮ (x₁T₂ - x₂T₁) ds; all the integrals being taken around C.

Exercise 3.13.3. C is any simple closed curve in space and T its tangent; C₃ is the projection of C on a plane 012 and C₃ is also a simple closed curve. Show that the area of C₃ is given by the same formulae as in the previous question.

3.14. Surface Integrals We shall need also to consider integrals over surfaces and should say something about their construction and the surfaces for which they can be constructed. A closed surface is one which lies within a bounded region of space and has an inside and an outside. We can pass from any inside point to another inside point by a curve which does not cross the surface and, similarly, from any outside point to any other. However, to pass from an inside point to an outside point the path must cross the surface. Familiar examples of closed surfaces are the sphere and surfaces that could be deformed into a sphere. A continuous surface which has no inside or outside, known as the Klein bottle, is shown in Fig. 3.2d. These pathological surfaces are the happy hunting ground of the topologist; they serve to preserve the engineer from becoming complacent in his assumed normality. If the normal to the surface varies continuously over a part of the surface that part is called smooth. Some closed surfaces (see for example Fig. 3.2a) are smooth everywhere, others are made up of a number of subregions which are smooth (Fig. 3.2b) and are called piece-wise smooth. A closed curve on a surface which can be continuously shrunk to a point is called reducible, as for example the equator of a sphere which can be continuously moved to any line of latitude until it shrinks to a pole. If all closed curves on a surface are reducible, the surface is called simply connected. The sphere is simply connected but the torus or anchor ring is not, for a closed curve such as is shown in Fig. 3.2c is not reducible.

If a surface is not closed it normally has a space curve as its boundary, as for example a hemisphere with the equator as boundary. It has two sides if it is impossible to go from a point on one side to a point on the other (in particular the point, which is just on the other side) along a continuous curve that does not cross the boundary. The surface is sometimes called the cap of the space curve. Again it is not necessary for a surface to have two sides; the Möbius strip (Fig. 3.2e) is the well-known example of this. Indeed a closed curve could be capped by either a one- or a two-sided surface for the boundary curve of the hemisphere (Fig. 3.2f) would be distorted into the boundary of the Möbius strip and the hemisphere would be a two-sided cap. These sophisticated considerations need not daunt us however, for given a simple closed curve we can imagine a soap film across it which can then be distorted into a piece-wise smooth cap.

Just as the line integral is a natural extension of the common integral over an interval, so the surface integral is an extension of the double integral. The double integral over a region R in the 012 plane of a function F(x₁, x₂) is written ∬_R F(x₁, x₂) dx₁ dx₂ and is constructed as follows. The region R is divided into a large number of small areas by a grid of lines x₁ = a₀, a₁, . . . , a_M, x₂ = b₀, b₁, . . . , b_N which cover the region (see Fig. 3.3). If we consider any typical rectangle, say a_{i-1} < x₁ ≤ a_i, b_{j-1} < x₂ ≤ b_j, which is wholly or partly in R, we may select a point (ξᵢ, ηⱼ) in this and in R and evaluate F at this point. Then the sum over all the small areas ∑∑ F(ξᵢ, ηⱼ) ΔS_{ij}, where ΔS_{ij} is the area of the part of the rectangle which is within R, is an approximation to the integral. We now let M and N increase without limit but always insist that the largest subdivision of area ΔS_{ij} must tend to zero, then if the sum tends to a limit that limit is the integral.

Now if S is a piece-wise smooth surface with two sides in three-dimensional space, we can divide it up into a large number of small regions by a grid in much the same way as with a plane region R. If we are given a function F defined on the surface, it can be evaluated for some point of each subregion of the surface and the sum ∑ F ΔS_{ij} computed. Then, as the subdivisions increase in number and become finer, the limit that this may tend to is called the double integral of F over S, ∬_S F dS.

The arguments of F have been left vague here. It may be that F is given as a function of position in space and we therefore evaluate it at a point on the surface, or it may be defined only on the surface itself.

The area of a curved surface is not an easy thing to define though more mystery than is necessary is often accorded it (see J. Serrin, Amer. Math. Mon. 68, May, 1961, p. 435 for an elegant discussion). For many common surfaces however, we may relate the area of an element of the curved surface dS to the area of its projection on a coordinate plane (say 012) by dA₁₂ = n₃ dS where n₃ is the third component of the normal. This is shown in Fig. 3.4 from which it is clear what must be done to calculate the areas of a cap. The cap S with boundary curve Γ has to have a projection on the 012 plane consisting of the simply connected region R with boundary C and for any point (x₁, x₂) of R there must correspond only one point of S. If the normal to the surface n is defined everywhere on it, and n₃ ≠ 0, then dS = (1/n₃) dA₁₂ and Area of S = ∬_R (1/n₃) dx₁ dx₂. (3.14.1)

Such a cap could be called 3-elementary.

A surface might fail to be 3-elementary either by having a sharp ridge at which n is discontinuous or by having more than one point of S correspond to each point of R or by having a whole region where n₃ = 0.

= 0. Except in the last case we can divide the surface up into parts that are 3-elementary, and evaluate the integral as the sum of the integrals over the several parts. If n3 = 0 then the surface is either 1-elementary or 2-elementary meaning that we can project the area on to the 023 or the 031 planes in a similar way.

Exercise 3.14.1. S is the hemisphere x3 = 0, x1^2 + x2^2 + x3^2 = a^2, where m is a fixed unit vector. Calculate a·n dS for an arbitrary constant vector a. S

Exercise 3.14.2. A surface can be given parametrically by three functions xi = gi(u1, u2). Show that n dS = (∂a/∂u1 × ∂a/∂u2) du1 du2.

Deduce that area is independent of the choice of Cartesian coordinates.

3.15. Volume integrals We shall also have occasion to integrate over the volume inside or outside of a closed surface. If a volume is such that a line parallel to 03 meets its bounding surface in two and only two points (say x3 = f+(x1, x2), x3 = f-(x1, x2), f+ ≥ f-) we may call it 3-elementary.* A sphere is the most obvious example of this. Similar definitions apply to the terms 1- and 2-elementary. If a volume can be divided into a number of smaller volumes each of which is 3-elementary, the volume may be called 3-composite. A region which is 1-, 2- and 3-composite will be called a composite volume.

An integration throughout the volume V is written ∫∫∫_V F dV and is, as before, the limit of a sum of the products of a very small subdivision of the volume and the function F evaluated somewhere within it. The limit is taken by letting the number of subdivisions increase without limit and the size of the largest tends to zero. If the volume V is 3-elementary and its projection on the 012 plane is a region R, then ∫∫∫_V F dV = ∫∫_R G dx1 dx2, where G = F(x1, x2, f+) - F(x1, x2, f-). This is shown in Fig. 3.5. The integral over a 3-composite volume may be calculated as the sum of such parts.

The double integral may be similarly reduced. We can call a simple closed curve C in the plane elementary if it can be traversed so that the slope of its tangent does not decrease. A composite curve is one that can be divided into elementary curves, as in Fig. 3.6. If R is bounded by an elementary closed curve C whose projection on the 01 axis is the interval (a,b), it can be specified by two functions g+(x1) and g-(x1) as shown in Fig. 3.6. Then ∫∫_R G dA = ∫_a^b H(x1) dx1, where H(x1) = ∫_{g-(x1)}^{g+(x1)} G(x1, x2) dx2.

Exercise 3.15.1. Evaluate ∫∫∫_V x1 x2 x3 dV when V is the sphere r = a and re = xix_j?

3.16. Change of variable with multiple integrals In Cartesian coordinates the element of volume dV is simply the volume of a rectangular parallelepiped of sides dx1, dx2, dx3 and so dV = dx1 dx2 dx3. (3.16.1)

Suppose, however, that it is convenient to describe the position by some other coordinates, say ξ1, ξ2, ξ3. We may ask what volume is to be associated with the three small changes dξ1, dξ2, dξ3.

The change of coordinates must be given by specifying the Cartesian point x that is to correspond to a given set ξ1, ξ2, ξ3, by xi = Xi(ξ1, ξ2, ξ3). (3.16.2)

Then by partial differentiation the small differences corresponding to a change dξj are dxi = (∂xi/∂ξj) dξj.

Let dx(j) be the vectors with components (∂xi/∂ξj) dξj for j = 1, 2, and 3. Then the volume element is dV = dx(1) · (dx(2) × dx(3)) = (∂(x1,x2,x3)/∂(ξ1,ξ2,ξ3)) dξ1 dξ2 dξ3, where ∂(x1,x2,x3)/∂(ξ1,ξ2,ξ3) = det(∂xi/∂ξj)

is called the Jacobian of the transformation of variables.

Exercise 3.16.1. Show that the volume element in the frame Oξ1ξ2ξ3 of coordinates ξi = l_ij xj is dξ1 dξ2 dξ3.

Exercise 3.16.2. Obtain the volume elements in cylindrical and spherical polars by the Jacobian and check with a simple geometrical picture.

3.21. Vector fields When the components of a vector or tensor depend on the coordinates we speak of a vector or tensor field. The flow of a fluid is a perfect realization of a vector field for at each point in the region of flow we have a certain velocity vector v(x1, x2, x3). If the flow is unsteady then the velocity depends on the time as well as position, v = v(x1, x2, x3, t). When it is necessary to be specific we shall refer to this as a time dependent vector field. It is sometimes convenient to abbreviate these to v(x) and v(x, t), or to use the index notation and write vi(x, t), Aij(x, t), etc.

Associated with any vector field a(x) are its trajectories, which is the name given to the family of curves everywhere tangent to the local vector a. They are the solutions of the simultaneous equations dx/ds = a(x); that is, dxi/ds = a_i(x), (i=1,2,3), (3.21.1)

where s is a parameter along the trajectory. (It will be the arc length if a is always a unit vector.) Though we have yet to define them, the streamlines of a steady flow are probably sufficiently familiar to be mentioned as the realization of these trajectories. For a time dependent vector field the trajectories will also be time dependent since they are solutions of dxi/dt = a_i(x, t). (3.21.2)

If C is any closed curve in the vector field and we take the trajectories through all points of C, they describe a surface known as a vector tube of the field.

3.22. The vector operator ∇-gradient of a scalar The symbol ∇ (enunciated as “del” or “nabla”) is used for the symbolic vector operator whose ith component is ∂/∂xi. Thus if ∇ operates on a scalar function of position φ, it produces a vector ∇φ, with components ∂φ/∂xi. We should of course establish that ∇φ is indeed a vector. In the coordinate frame Oξ1ξ2ξ3 the vector will have components ∂φ/∂ξβ. However, ∂φ/∂ξβ = (∂xi/∂ξβ) (∂φ/∂xi) = l_{βi} ∂φ/∂xi, (3.22.1)

since xi = l_{ij} ξ_j, so that ∇φ is a vector.

In Cartesian coordinates the operation of partial differentiation with respect to three coordinates gives the components of a tensor of the next higher order. To show this, suppose that A(x1, x2, x3) is a second order tensor field; then the 81 quantities ∂A_{ij}/(∂x_k ∂x_l) are the components of a fourth order tensor. For since x_i = l_{im} ξ_m, ∂^2/(∂x_k ∂x_l) = (∂ξ_p/∂x_k) (∂ξ_q/∂x_l) (∂^2/(∂ξ_p ∂ξ_q)) = l_{pk} l_{ql} ∂^2/(∂ξ_p ∂ξ_q). (3.22.2)

If we write A_{ij,km} for the second derivative ∂^2 A_{ij}/(∂x_k ∂x_l), then in the frame Oξ1ξ2ξ3 (∂^2 A_{ij})/(∂ξ_k ∂ξ_l) = l_{pk} l_{ql} (∂^2 A_{ij})/(∂ξ_p ∂ξ_q) = l_{pk} l_{ql} l_{im} l_{jn} A_{mn,pq}, which shows that the A_{ij,km} are components of a fourth order tensor.

The suffix notation ,i for the partial derivative with respect to xi is a very convenient one and will be taken over for the generalization of this operation that must be made for non-Cartesian frames of reference. The notation “grad” for ∇ is often used and referred to as the gradient operator. Thus grad φ = ∇φ is the vector which is the gradient of the scalar, and grad A would be a tensor A_{ij,k}. ∇ is also sometimes written ∂/∂x and can be expanded in the form ∇ = e_i (∂/∂x_i). (3.22.3)

If φ(x1, x2, x3) = φ(x) is a scalar function of position and δx = n δr is a small displacement in the direction n, then lim_{δr→0} (φ(x + n δr) - φ(x))/δr is the derivative in the direction n and is sometimes denoted by ∂φ/∂n. By Taylor’s theorem, φ(x + n δr) = φ(x) + (n δr) · ∇φ + O(δr^2), (3.22.4)

Exercise 3.22.1. If F(p) = ∫^p f(q) dq is the indefinite integral of f(p), show that ∇F(p) = f(p) ∇p.

It will be convenient to refer to the following formulae (2)-(4) later. They are all elementary but the exercise of establishing them is valuable.

∇(uv) = u∇v + v∇u.

Exercise 3.22.2. ∇(φψ) = φ∇ψ + ψ∇φ.

Exercise 3.22.3. ∇(A_{ij} x_i x_j) = (A_{ij} + A_{ji}) x_j, if A is constant. (Summation on i).

Exercise 3.22.4. ∇(f(r)) = (f’(r)/r) x, here r^2 = x·x.

Exercise 3.22.5. Show that if ψ(x) = c is a surface, ∇ψ is normal to the surface.

Exercise 3.22.6. If A_{ij} x_i x_j = 1 is a central quadric defined by a symmetric tensor A_{ij}, then A_{ij} x_j transforms the radius vector x into a vector normal to the surface. The angle between the radius and the normal is given by tan^2 θ = (x·x)(x·A^{-1}·x) / (x·A·x)^2 - 1.

3.23. The divergence of a vector field The symbolic scalar or dot product of a vector and the operator ∇ is called the divergence of the vector field. Thus for any differentiable a(x1, x2, x3), we write div a = ∇ · a = ∂a_i/∂x_i = ∂a1/∂x1 + ∂a2/∂x2 + ∂a3/∂x3. (3.23.1)

The divergence is a scalar since it is the contraction (or trace) of the second order tensor ∂a_i/∂x_j.

Suppose that an elementary parallelepiped is set up with one corner P at x1, x2, x3 and the diagonally opposite one Q at x1+dx1, x2+dx2, x3+dx3 as shown in Fig. 3.7. The outward unit normal to the face through Q which is perpendicular to 01 is e01, whereas the outward normal to the parallel face through P is -e01. On the first of these faces a = a(x1+dx1, x2, x3), whereas on the second it is a(x1, x2, x3). Thus if n denotes the outward normal and dS is the area dx2 dx3 of these faces, we have a contribution from them to the surface integral ∫∫ a·n dS of [a1(x1+dx1, x2, x3) - a1(x1, x2, x3)] dx2 dx3 ≈ (∂a1/∂x1) dx1 dx2 dx3 + O(d^4), where O(d^4) denotes terms proportional to fourth powers of the dx. Similar terms with ∂a2/∂x2, ∂a3/∂x3 will be given by the contributions of the other faces so that for the whole parallelepiped whose volume dV = dx1 dx2 dx3 we have ∫∫ a·n dS ≈ (∂a1/∂x1 + ∂a2/∂x2 + ∂a3/∂x3) dV. (3.23.2)

If we let the volume shrink to zero we have lim_{dV→0} (1/dV) ∫∫ a·n dS = ∇·a. (3.23.3)

If a is thought of as a flux, then ∫∫ a·n dS is the net flux out of the volume. A vector field whose divergence vanishes identically is called solenoidal. If the flux field of a certain property is solenoidal there is no generation of that property within the field, for all that flows into an infinitesimal element flows out again.

If a is the gradient of a scalar function ∇φ, its divergence is called the Laplacian of φ: ∇^2 φ = div grad φ = ∂^2φ/∂x1^2 + ∂^2φ/∂x2^2 + ∂^2φ/∂x3^2. (3.23.4)

A function that satisfied Laplace’s equation ∇^2 φ = 0 is called a potential function.

If A is a tensor, the notation div A is sometimes used for the vector (∇·A)_j = ∂A_{ij}/∂x_i, and then div A^T would be (∇·A^T)_j = ∂A_{ji}/∂x_i. We shall see these later.

I generally prefer the index notation for tensors.

Exercise 3.23.1. ∇·(φa) = ∇φ · a + φ∇·a.

Exercise 3.23.2. ∇×(a×b) = (∇×a)×b - a×(∇×b).

Exercise 3.23.3. ∇²f(r) = f''(r) + 2f'(r)/r, r² = x·x.

Exercise 3.23.4. {d_n a} denotes the symmetric tensor of order n+1 [a_i x_j ... x_k], whereas a_{i+1} is the tensor a_i x_j x_k of order n+2. Show that div (a_{i+1}) = {x·∇ a}^i if div a = 0.

Exercise 3.23.5. Interpret ∇²φ physically by thinking of it as ∇·(∇φ).

Exercise 3.23.6. If φ(x) = ψ(x₁, x₂, x₃) is a potential function and r² = x·x, show that ψ(x/r) is also a potential function and that its normal derivative on the sphere r = a vanishes. (Weiss, P. Proc. Camb. Phil. Soc., 40, (1944), 249.)

3.24. The curl of a vector field The symbolic vector or cross product of ∇ and a vector field a is called the curl of the vector field. It is the vector ∇×a = curl a = ε_ij ∂_i a_j, with three components. It is connected, as we shall see, with the rotation of the field and is sometimes written rot a in older texts.* In dyadic notation curl a = (grad a)×.

Consider an elementary rectangle in the plane normal to O₁ with one corner P at (x₁, x₂, x₃) and the diagonally opposite one Q at (x₁ + dx₁, x₂ + dx₂, x₃), as shown in Fig. 3.8. We wish to calculate the line integral around this elementary circuit of a·t ds, where t is the tangent. Now the line through P parallel to O₂ has tangent e(2), and the parallel side through Q has tangent e(2), and each is of length dx₂. Accordingly, they contribute to a·t ds an amount = [a₂(x₁ + dx₁, x₂, x₃) - a₂(x₁, x₂, x₃)] dx₃ + O(dx³). Similarly, from the other two sides, there is a contribution - [a₃(x₁ + dx₁, x₂, x₃) - a₃(x₁, x₂, x₃)] dx₂ + O(dx³). Thus writing dA = dx₂ dx₃, we have ∮a·t ds = (∂a₃/∂x₂ - ∂a₂/∂x₃) dA + O(d⁴) and in the limit lim_{dA→0} (1/dA) ∮a·t ds = (∂a₃/∂x₂ - ∂a₂/∂x₃).

The suffix 1 has been put on the integral sign to show that the line integral is in a plane normal to O₁, and the limit is the first component of the curl. An entirely similar treatment would give the other two components for line integrals around rectangles in planes perpendicular to the O₂ and O₃ axes.

We can treat an infinitesimal triangle (PQR of Fig. 3.9) in a similar way. If the length of PQ is dx₂ = ds cos θ, and the length of PR is dx₃ = ds sin θ, the area is dA = ½ ds² cos θ sin θ. The unit tangents around the triangle are e(2) = (0, -cos θ, sin θ), -e(3). Thus approximating each part of the line integral by the length of side multiplied by a·t evaluated at its midpoint, ∮a·t ds = a₂(x₁, x₂ - ½ dx₂, x₃ + ½ dx₃) dx₂ + { -cos θ a₂(x₁, x₂ + ½ dx₂, x₃) + sin θ a₃(x₁, x₂, x₃ + ½ dx₃) } ds - a₃(x₁, x₂ + ½ dx₂, x₃ - ½ dx₃) dx₃ = {∂a₃/∂x₂ - ∂a₂/∂x₃} ds² cos θ sin θ + O(ds³). Again, as ds and so dA tends to zero, lim_{dA→0} (1/dA) ∮a·t ds = ∂a₃/∂x₂ - ∂a₂/∂x₃, and similar forms hold for triangles in planes normal to O₂ and O₃.

Consider now a fourth point S at (x₁, x₂ + dx₂, x₃ + dx₃) so that QRS is a plane triangle of area dA whose unit normal is n. Thus the areas of the triangles PQR, PRS, PSQ are dA₁ = n₁ dA, dA₂ = n₂ dA, dA₃ = n₃ dA respectively. However, the line integral around QRS can be taken to be the sum of those around PQR, PRS, PSQ since the parts PQ, PR, PS are traversed once in each direction and so cancel (see Fig. 3.10). Thus, if dA is small, ∮_QRS a·t ds = (∇×a)·n dA + O(dA²). Then in the limit lim_{dA→0} (1/dA) ∮_QRS a·t ds = (∇×a)·n.

By working a little harder (Exercise 3.24.9), it can be shown that if any small curve in the plane with normal n shrinks on the point x, the limit of the ∮ a·t ds divided by the area is the projection of curl a on the normal, n.

A vector field a for which ∇×a = curl a = 0 is called irrotational, for evidently the circulation around any infinitesimal curve vanishes.

Exercise 3.24.1. ∇×(∇φ) = 0.

Exercise 3.24.2. ∇·(∇×a) = 0.

Exercise 3.24.3. ∇×(φa) = ∇φ × a + φ∇×a.

Exercise 3.24.4. ∇×(a×b) = a(∇·b) - b(∇·a) + (b·∇)a - (a·∇)b.

Exercise 3.24.5. ∇×(∇×a) = ∇(∇·a)

surface S’. The vector a is continuous in V = V₁ ∪ V₂ and its derivatives are continuous in V₁ and V₂ separately and the normal derivative is continuous across S’. Show that Green’s theorem holds good for any volume V* within V.

3.32. Stokes’ theorem

The previous theorem concerned the relation of an integral over a closed volume and its relation to an integral over the bounding surface. Stokes’ theorem relates the surface integral over a cap to a line integral around the bounding curve. The line integral appearing is that of a·t, that is, the total circulation, and the theorem says that this is equal to the surface integral of the normal component of curl a. We shall again give two demonstrations.

We have shown earlier in Section 3.24 and Ex. 3.24 that for an infinitesimal triangular area the line integral ∫ a·t ds = (∇ ∧ a)·eₙ dS. (3.32.1)

If S is the cap of a closed curve C, we can divide its surface into a large number of small triangles for each of which Eq. (3.32.1) is true. Then in summing the right-hand sides we shall have the surface integral over the whole cap, whereas on the left-hand sides contributions from adjacent sides of triangles will cancel since they will be traversed in opposite directions. The only remaining contributions from the line integrals will thus be those from the bounding curve C and ∫ₙ a·t ds = ∫ₛ (∇ ∧ a)·n dS. (3.32.2)

The convention that the normal to the curve should be right-handed with respect to the direction of traversing the curve C is observed throughout. More precisely stated, Stokes’ theorem says that for any two-sided piecewise smooth surface S spanning the closed curve C and any continuous vector field a whose partial derivatives are continuous, Eq. (3.32.2) holds.

We shall give another proof depending on Green’s theorem. Suppose first that the cap S can be specified by a single function x₃ = f(x₁, x₂) in the region R within the closed curve C’, the projection of C on the plane 012. Consider the terms in a₁, namely,

* It appears that the attribution of this theorem to Stokes is less appropriate than that of the previous one to Green. It is actually due to Kelvin though the usage of Stokes’ name is too entrenched to be changed. See Truesdell, “Kinematics of Vorticity,” footnote, p. 12.

62 Cartesian Vectors and Tensors: Their Calculus §3.32

Now on S, x₃ = f(x₁, x₂) and so ∂a₃/∂x₁ = ∂a₃/∂x₁ + ∂a₃/∂x₃ ∂f/∂x₁.

However, ∂f/∂x₁ = -n₁/n₃ because the direction cosines of the normal are proportional to ∂f/∂x₁, ∂f/∂x₂, and -1, respectively. Hence, by Eq. (3.15.1). However, by putting a₁ = 0, a₃ = g in Ex. 3.31.3 which is a two-dimensional form of Green’s theorem, -∫∫ ∂g/∂x₁ dA = ∫ₙ g ds’ = ∫ₙ g(x₁, x₂, f(x₁, x₂)) ds’, R               C’ where rᵢ and ds’ are the component of the tangent and element of arc C’ respectively. However, τ ds’ = t ds so this last integral is really the line integral around C and the theorem is established for a₁. A similar proof goes through for a₂ and a₃ and for surfaces that can be decomposed into parts which are either 1, 2, or 3-elementary. A further discussion will be found in Kellogg’s book.

Other forms of Stokes’ theorem may be derived by inserting various vectors; in particular the components aᵢ may be a set of components from a tensor, say A_{jk} with j, k fixed. Thus it is convenient to write ∫ₛ A_{jk} F_{k,j} dS = ∫ₙ A_{jk} F_{k} ds*. (3.32.3)

Exercise 3.32.1. Relate the results of Exercises 3.13.1 and 3.14.1 by Stokes’ theorem.

Exercise 3.32.2. Show that the vanishing of the integral of (∇ ∧ a)·n over a closed surface is a consequence both of Green’s and Stokes’ theorems.

Exercise 3.32.3. Show that

Exercise 3.32.4. Show that ∫ₙ (∇ ∧ a)·t ds = ∫ₛ [(∇·a)·n - (n·∇)a] dS.

Exercise 3.32.5. The flux of a through the cap S is ∫ₛ a·n dS. Suppose a = a(x₁, x₂, x₃, t) and S moves in space its velocity being given by a vector field v. Consider the volume bounded by S, the position of S at time τ and S, its position at time t + dt and a bounding surface of vectors v dτ for all points of the boundary C. Then applying Green’s theorem to the volume, show that

Exercise 3.32.6. If ∇ and a are as in Ex. 3.31.5 save that this time it is the tangential derivative that is continuous across S’, show that Stokes’ theorem still holds.

3.41. The classification and representation of vector fields

We have already noted two distinct types of vector field; namely, the solenoidal, for which ∇·a = 0, and the irrotational, for which ∇ ∧ a = 0. Such fields occur physically, and it is of interest to explore their properties a little further. We are particularly interested in relating the three components of a to certain scalar functions of position. For example, if a is the gradient of a scalar function φ, then it is certainly irrotational for ∇ ∧ ∇φ ≡ 0 identically. Thus if a problem calls for an irrotational vector field, it may be possible to turn it into a problem that requires finding only the function φ; certainly an easier matter than finding all three components of a. Before this can be done however it must be proved that all irrotational vector fields can be represented as the gradient of a scalar function, which is slightly more difficult than showing that the gradient of a scalar is irrotational.

To show the value of these representations let us anticipate the results of the next few sections and show that a vector field which is both irrotational and solenoidal is uniquely determined in a volume V if it is specified over S, the surface of V. If a vector field is irrotational we shall show that it can always be written as ∇φ, where φ is determined up to an arbitrary constant.

64 Cartesian Vectors and Tensors: Their Calculus §3.41

If a = ∇φ, and a is solenoidal, ∇·a = ∇²φ = 0; that is, φ is a potential function or solution of Laplace’s equation. Now suppose it were possible for two different functions φ₁ and φ₂ to satisfy ∇²φ = 0 in V and take the same values on S. Then the difference between them ψ = φ₁ - φ₂ would satisfy ∇²ψ = 0 in V but ψ would be identically zero on S. Now put ψ in Eq. (3.31.7) so that ∫ᵥ ∇ψ·∇ψ dV = ∫ₛ ψ (∇ψ·n) dS. (3.41.1)

However, since ∇²ψ = 0 in V and ψ = 0 on S, the first term on the left-hand side and the integral on the right are both identically zero. It follows that ∫ᵥ (∇ψ)² dV = 0. (3.41.2)

However, the integrand is everywhere positive and so the integral could not vanish unless ∇ψ itself were everywhere zero. However, this means that ψ is a constant, and since it is zero on the boundary this constant must be zero everywhere, that is, ψ = φ₁ = φ₂.

Apart from the solenoidal and irrotational, several other types of fields have been named. We will give a brief description of these though we shall not be able to go fully into the representation of them all.

The name lamellar is also applied to an irrotational vector field (∇ ∧ a = 0) and it is a special case of the complex lamellar field for which a·(∇ ∧ a) = 0. The condition for a field to be complex lamellar is evidently that it should be orthogonal to its curl, which is less restrictive than the requirement that the curl should vanish. Another type is the Beltrami field for which the curl is parallel to the original vector, that is, a ∧ (∇ ∧ a) = 0. The relations between these types are best shown in a diagram (Fig. 3.11). Arrows coming together at the same place denote the simultaneous possession of the character of the type from which they come. Thus, if a field is both a complex lamellar and a Beltrami field, it is irrotational (except possibly where a = 0), for curl a is both orthogonal and parallel to a and so must be zero if a ≠ 0. A field which is both solenoidal and irrotational is sometimes called Laplacian since it is the gradient of a potential function. If curl a is not only parallel to a but is proportional to a with a constant that does not vary with position (that is, ∇ ∧ a = ka, ∇k = 0), it is called Trkalian.

§3.42. Irrotational Vector Fields 65

Exercise 3.41.1. Show that if the curl of a Beltrami field is itself a Beltrami field, then the field is Trkalian (Bjørgum).

Exercise 3.41.2. If T = a/|a| is the unit vector tangent to the field a, show that s·(∇ ∧ T) = lim (1/S) ∫ₙ T·t ds where S is a cap of the curve C that shrinks on the point in such a way that the normal to S is T. (t is the unit tangent of the curve C.)

3.42. Irrotational vector fields

We wish to show that if ∇ ∧ a = 0 then there exists a scalar function φ such that a = ∇φ, (3.42.1)

This function φ is often called the potential of a by analogy with force fields for which the force on a particle can be obtained as the gradient of the potential energy.

Since ∇ ∧ a = 0 we know by Stokes’ theorem that the circulation integral round any closed curve vanishes, ∫ₙ a·t ds = 0. (3.42.2)

It follows (see Section 3.13) that the line integral from a fixed point (say the origin) to a point P, (x₁, x₂, x₃), is independent of the path. Let φ(P) = ∫₀ᴾ a·t ds then this is a definite scalar function depending only on the position of P. Consider a nearby point Q, (x₁ + dx₁, x₂, x₃), then φ(Q) - φ(P) = ∫₀ᵠ a·t ds - ∫₀ᴾ a·t ds = ∫ₚᵠ a·t ds since we are at liberty to take the path OQ through P. We may also choose the path from P to Q to be the straight line parallel to the axis 01, and then t = e₁. Thus, φ(x₁ + dx₁, x₂, x₃) - φ(x₁, x₂, x₃) = ∫₀¹ a₁(x₁ + δdx₁, x₂, x₃) dx₁ dδ = dx₁ a₁(x₁ + θdx₁, x₂, x₃)

where 0 ≤ θ ≤ 1. In the limit as dx₁ → 0 we have ∂φ/∂x₁ = a₁(x₁, x₂, x₃). (3.42.4)

This can be repeated with PQ parallel to the other two axes and establishes the representation (3.42.1).

Thus an irrotational vector field a can be characterized by any one of three equivalent properties. They are: (i) curl a = 0, (ii) ∫ₙ a·t ds = 0 for any closed curve C, (iii) a = ∇φ, where φ is a scalar point function.

If the partial derivatives are only piece-wise continuous, the equivalence has to be framed with slightly more care, but for continuously differentiable vector fields it is exact.

可以简明陈述。一些作者将(ii)视为更基本的物理属性，并由此方程定义无旋性。由于∇p₁垂直于一族曲面H(x₁, x₂, x₃) = 常数，向量场的无旋性意味着存在一族处处垂直于该向量场轨迹的曲面。实际上，a = ∇p₁表达了比这更多的信息：若存在函数φ使得φa = ∇q（其中φ不一定为常数），则a的法线方向也指向a。假设a ≠ ∇p₁，但存在函数p使得pa = ∇q。则

∇×(pa) = ∇φ×a + p∇×a = ∇×∇q = 0。 (3.42.5)

由于a·(∇φ×a)恒为零，将a与式(3.42.5)作标量积得

pa·(∇×a) = 0。

因此若p ≠ 0，要存在积分因子φ，必须满足

a·(∇×a) = 0。 (3.42.6)

由此可知，要使这样的曲面族存在，向量场必须是复合层状的。反之可证（见练习3.42），若向量场是复合层状的，则存在积分因子。族φ₁ = 常数称为向量场a的法线汇，而一个向量场为复合层状的充要条件是其拥有法线汇。

§3.43 无散向量场 67

练习 3.42.1. 若 a·∇×a = 0 且 p 为任意函数，则 (pa)·∇×(pa) = 0。

练习 3.42.2. 若 a·∇a ≠ 0，证明积分因子 p（使得 p(a₁dx₁ + a₂dx₂) = dψ）的存在性源于常微分方程 dx₃/dx₁ = -a₃/a₁ 的解的存在性。

练习 3.42.3. 先取 x₂ 为常数，证明存在函数 A(x₁, x₂, x₃) 和积分因子 p，使得 a·dx = dA + Bdx₃，其中 B = pa₃，∂A/∂x₃。进一步证明 (pa·∇)(pa) = (∂/∂x₁, ∂/∂x₂, ∂/∂x₃, ∂/∂x₃) × (A, B) 。

练习 3.42.4. 雅可比行列式 ∂(A, B)/∂(x₁, x₂) 为零意味着 A 与 B 之间存在独立于 x₃ 的关系。结合前述三个练习的结果，证明 a·∇×a = 0 是积分因子 A 存在的充分条件，使得 Aa = ∇q。

## 3.43 无散向量场

无散向量场定义为满足 ∇·a = 0。 (3.43.1)

根据格林定理，这等价于对任意闭曲面 S 有 ∬_S a·n dS = 0。 (3.43.2)

我们将证明 a 可表示为依赖于两个标量函数 ψ 和 χ 的向量场 ψ∇χ 的旋度。

考虑微分方程组 dx₁/a₁(x₁, x₂, x₃) = dx₂/a₂(x₁, x₂, x₃) = dx₃/a₃(x₁, x₂, x₃)。 (3.43.3)

若 aₙ 连续可微，该方程组有两个独立解，可写为 f₁(x₁, x₂, x₃) = c₁ 和 f₂(x₁, x₂, x₃) = c₂。

由于 a 同时与这两个曲面相切，故垂直于它们的法线，因此 a = λ ∇f₁ × ∇f₂。 (3.43.4)

令 f₃(x₁, x₂, x₃) 为第三个函数，使得 (∇f₁ × ∇f₂)·∇f₃ ≠ 0； (3.43.5)

即曲面 f₃ = c₃ 的法线不在前两个法线构成的平面内。则可取 f₁, f₂, f₃ 为点 x 的坐标，根据偏微分法则 ∇f₁ × ∇f₂ = (∂(f₂, f₃)/∂(x₁, x₂), …)。

因此 ∇·(λ ∇f₁ × ∇f₂) = λ ∇·(∇f₁ × ∇f₂) + (∇f₁ × ∇f₂)·∇λ = (∇f₁ × ∇f₂)·∇λ (3.43.6)

因其他项为零。然而，若 ∇·a = 0，与式(3.43.5)比较得 (∇f₁ × ∇f₂)·∇λ = 0，即 λ 仅为 f₁ 和 f₂ 的函数。令 ψ = ∫ λ df₁ （积分时保持 f₂ 不变）， 则 ∇ψ = λ ∇f₁ + (∂ψ/∂f₂) ∇f₂。

且 ∇·(ψ ∇f₂) = ∇ψ·∇f₂ = λ ∇f₁·∇f₂ + (∂ψ/∂f₂) |∇f₂|²。

(3.43.7)

因此，令 χ = f₂，由式(3.43.4)和上式得 a = ∇ψ × ∇χ = ∇×(ψ ∇χ)， (3.43.8)

此即所需表示。注意到 ∇·a = ∇·∇×(ψ ∇χ) = 0， 故该表示也可写为 a = ∇×α， ∇·a = 0， (3.43.9)

其中 α 是位置的向量函数。α 不唯一，因为可加任意无旋向量场 φ（∇×φ = 0），有 ∇×(α+φ) = ∇×α = a。

具体例子有助于理解。假设 a₁ = 0, a₂ = -x₃/r², a₃ = x₂/r²， 其中 r² = x₁² + x₂² + x₃²。

则式(3.43.3)为 dx₁/0 = dx₂/(-x₃/r²) = dx₃/(x₂/r²)。

立即得两个积分 f₁ = x₁, f₂ = ρ = √(x₂² + x₃²)。

于是 ∇f₁ = e₁，∇f₂ = (x₂e₂ + x₃e₃)/ρ， ∇f₁ × ∇f₂ = (-x₃e₂ + x₂e₃)/ρ。

故 λ = ρ/r²，从而 ψ = ∫ (ρ/r²) df₁ = ∫ (ρ/(x₁²+ρ²)) dx₁ = arctan(x₁/ρ)， 且可写 a = ∇×[arctan(x₁/ρ) ∇ρ]。

注意该表示不唯一，因满足式(3.43.10)的另一对函数为 f₁ = x₁, f₂ = r = √(x₁² + x₂² + x₃²)， 此时 ∇f₁ × ∇f₂ = (-x₃e₂ + x₂e₃)/r，故更简单的函数对为 ψ = x₁, χ = r。

连续可微无散向量场具有三个等价特征： (i) ∇·a = 0, (ii) ∬_S a·n dS = 0 对任意闭曲面 S, (iii) a = ∇×α，其中 α 也是无散的。

练习 3.43.1. 证明 f(r)ω×x（ω为常向量，r² = x·x）是无散向量场。构造其 χ∇ψ 和 ∇×α 的表示。

练习 3.43.2. 证明无散场中向量管的强度在所有截面上相同。

70 笛卡尔向量与张量：其微积分 §3.44

## 3.44 亥姆霍兹表示

已获得的无散和无旋向量场表示可结合给出任意连续可微向量场的表示。因此，对任何有限、连续且在无穷远处消失的向量场，总可找到三个标量函数 φ, ψ 和 χ 使得 a = ∇φ + ∇×(ψ ∇χ)。 (3.44.1)

等价地，可找到标量函数 φ 和无散向量场 α 使得 a = ∇φ + ∇×α。 (3.44.2)

于是向量场被分解为无旋和无散两部分。

为证明该定理，需要泊松方程的解公式 ∇²φ = -f(x₁, x₂, x₃)。 (3.44.3)

这由积分 φ(x) = ∫∫∫ f(ξ) dVξ / (4π|x-ξ|) (3.44.4)

给出。积分遍及全空间，若 f 仅定义于某区域，可令其在外部为零；若处处定义，则要求其在无穷远处趋于零。图3.12说明了该积分；r 为点 x 与积分元 ξ 的距离，故 r² = |x-ξ|² = (x-ξ)·(x-ξ)。

考虑 φ 的梯度向量 ∇φ = ∫∫∫ f(ξ) (x-ξ) dVξ / (4π|x-ξ|³)。

将 ∇φ 在有限体积 V 上积分，由格林定理 ∫∫∫_V ∇φ dV = ∬_S φ n dS， 交换积分次序。然而，(x-ξ)/r³ 是指向 PQ 的单位向量 [图3.12b]，故 n·(x-ξ) dS/r³ 是点 P 对面元 Q 所张的立体角。若 P 在 V 外，该立体角积分为零（因 Q 和 Q' 的贡献抵消）；若 P 在 V 内，则积分为总立体角 4π。故 ∫∫_S n·(x-ξ) dS / |x-ξ|³ = { 1, 若 ξ 在 V 内; 0, 若 ξ 在 V 外 }。 (3.44.5)

因此，在全空间 ξ 上的最后一个积分在 V 外被积函数为零，可视为仅在 V 上积分。于是 ∫∫∫_V ∇²φ dV = -∫∫∫_V f dV。

因 V 任意，仅当 ∇²φ = -f 处处成立，此式才成立，可见式(3.44.4)确实给出解。

回到任意向量场 a，若其能写成 ∇φ + ∇×(ψ∇χ) 的形式，则有 ∇·a = ∇²φ。现用刚构造的公式解此方程，得 φ(x) = ∫∫∫ (∇·a)(ξ) dVξ / (4π|x-ξ|)。 (3.44.6)

由于 a - ∇φ 是无散场（因 ∇·(a - ∇φ) = 0），由前述方法可构造函数 ψ, χ 或无散向量 α 使得 a - ∇φ = ∇×(ψ∇χ) = ∇×α， 即得证。

72 笛卡尔向量与张量：其微积分 §3.44

练习 3.44.1. 向量泊松方程指 ∇²a = g，其中每个分量满足泊松方程。考虑 ∇×a，证明式(3.44.2)中的向量 α 为 α(x) = ∫∫∫ (∇×a)(ξ) dVξ / (4π|x-ξ|)， 并完成式(3.44.2)形式的表示。

## 3.45 其他表示

任意向量场也可表示为无旋场与复合层状场的叠加： a = ∇ψ + γ ∇χ。 (3.45.1)

因 ∇×a 必为无散场，故由 §3.43 可表示为 ∇×(ψ∇χ)。然而，∇×(a - ψ∇χ) = 0，故 a - ψ∇χ 是无旋场，可表示为标量 ψ 的梯度。

此处 ψ, γ, χ 称为蒙日势。

a·(∇×a) = (∇ψ + γ∇χ)·(∇γ×∇χ)

= ∇ψ·(∇γ×∇χ)。 (3.45.2)

满足 a·(∇×a) = 0 的场称为贝尔特拉米场。该方程意味着 a 与旋度平行，故 ∇×a = R a， (3.45.3)

其中 R 称为场的次法线性。R = 0 是向量场具有法线汇曲面的条件，此即该术语的由来。若 a 按式(3.45.1)表示且是贝尔特拉米场，则 a·(∇×a) = (∇ψ + γ∇χ)·(∇γ×∇χ) = 0。

若括号内各项非零，则 ∇γ 与 ∇χ 平行，从而 ∇γ×∇χ = ∇×a = 0。

故除 ∇×a = 0 外，必须有 ∇χ·(∇ψ + γ∇χ) = ∇χ·a = 0， ∇γ·(∇ψ + γ∇χ) = ∇γ·a = 0。 (3.45.4)

由第一式得 ψ = -χ (∇χ·∇χ)/2 + 常数， (3.45.5)

故 a = -∇χ (∇χ·∇χ)/2 + γ ∇χ。

由第二式得 ∇γ = - (∇χ)² ∇χ / 2。

若场满足 ψ = k（常数），则称为特里克莱场。此时 a = (∇×a)/k，故 ∇·a = 0，即特里克莱场是无散贝尔特拉米场。但存在非特里克莱的无散贝尔特拉米场。因 ∇×a = k a， ∇×(∇×a) = k ∇×a = k² a。

然而，由练习 3.24.5 及 ∇·a = 0， ∇²a + k² a = 0。 (3.45.6)

故特里克莱向量场满足亥姆霍兹方程。比约尔格姆和戈达尔已证明，若 h 是波动方程 ∇²h + k² h = 0 的解，则 a = k ∇h × e + k² h (e·∇)h， (3.45.7)

其中 e 为任意常单位向量，是特里克莱向量场的表示。

terest in these fields arises from the importance of Beltrami motions in which a is the velocity vector. These have been extensively studied by Truesdell and Bjergum.

Another form of decomposition with some similarity to the Helmholtz theorem has recently been given. Any vector field can be represented as a = (X ∧ ∇)v + (X ∧ ∇) ∧ a + a (3.45.8)

where a is a vector satisfying (X ∧ ∇) a = 0, and (X ∧ ∇) ∧ (X ∧ ∇) a = -(X ∧ ∇) a.

The proof of this is beyond our scope here, but is to be found in the paper by J. S. Lomont and H. E. Moses. (Communications on Pure and Applied Mathematics, 14 (1961), pp. 69-76.)

Exercise 3.45.1. Show that for the Beltrami field (Bjergum)

Exercise 3.45.2. Show that if ∇ ∧ a = k a, then a = (∇ ∧ a) ∧ (∇ ∧ a)

--- (∇ ∧ a)^2 (Truesdell)

Exercise 3.45.3. Show that successive curls of a Trkalian field are Trkalian with the same constant k.

## BIBLIOGRAPHY

3.1. An elementary discussion of space curves such as we have given is common to most books on vectors and tensors. A more extended treatment may be found in Eisenhart, L. P. An introduction to differential geometry. Princeton: Princeton University Press, 1940.

A good introduction to multiple integrals is provided by Ferrar, W. L., Integral calculus. Oxford: Oxford University Press, 1958.

and in the many available advanced calculus texts.

3.2. A valuable elementary discussion of the points that must be examined to give completely rigorous definitions is given in Chapter 4 of Newell, H. E., Jr, Vector analysis. New York: McGraw-Hill, 1955.

3.3. A full discussion of the types of surface for which Green’s and Stokes’ theorem can be established will be found in Chap. IV of Kellogg, O.D., Foundations of potential theory. Berlin: Springer-Verlag, 1929.

3.4. Truesdell, C. A., The kinematics of vorticity. Bloomington: Indiana University Press, 1954 summarises the characterization of vector fields and gives an unusually ample bibliography.

Some general discussion and references, as well as a full treatment of Beltrami fields, are to be found in Bjergum, O., “On Beltrami vector fields and flows. Part I. A comparative study of some basic types of vector fields.” Universitetet i Bergen Arbok (1951). Naturvitenskapelig rekke Nr. 1.

and Bjergum, O. and T. Godal, “On Beltrami vector fields and flows. Part II. The case when k is constant in space.” Universitetet i Bergen Arbok (1952). Naturvitenskapelig rekke Nr. 13.

The Kinematics of Fluid Motion

4.11. Particle paths

Kinematics is the description of motion per se. It takes no account of how the motion is brought about or of the forces involved for these are in the realm of dynamics. Consequently the results of kinematical studies apply to all types of fluid and are the ground work on which the dynamical results are constructed.

The basic mathematical idea of a fluid motion is that it can be described by a point transformation. At some instant we look at the fluid and remark that a certain “particle” is at a position ξ and at a later time the same particle is at position x. Without loss of generality, we can take the first instant to be the time t = 0 and if the later instant is time t we say that x is a function of t and the initial position ξ, x = x(ξ, t) or x_i = x_i(ξ_1, ξ_2, ξ_3, t). (4.11.1)

Of course we have immediately violated the concepts of the kinetic theory of fluids for in this theory the particles are the molecules and these are in random motion. In fact we have replaced the molecular picture by that of a continuum whose velocity at any point is the average velocity of the molecules in a suitable neighborhood of the point. As we have noted in Chapter 1, the definition of average needs some care in this context, but this idealization which endows the elementary portions of the fluid with a permanence denied them by molecular theory is the key to the classical treatment of fluid motion.

The initial coordinates of a particle will be referred to as the material coordinates of the particle and, when convenient, the particle itself may be called the particle ξ. The terms convected and Lagrangian coordinates are also used. The former is a sensible term since the material coordinate system is convected with the fluid; the latter is both a misnomer* and, lacking descriptive quality, is often forgotten or confused by the student. The spatial coordinates x of the particle may be referred to as its position or place. It will be assumed that the motion is continuous, single valued and that Eq. (4.11.1) can be inverted to give the initial position or material coordinates of the particle which is at any position x at time t; that is, ξ = ξ(x, t) or ξ_i = ξ_i(x_1, x_2, x_3, t) (4.11.2)

are also continuous and single valued. Physically this means that a continuous arc of particles does not break up during the motion or that the particles in the neighborhood of a given particle continue in its neighborhood during the motion. The single valuedness of the equations means that a particle cannot split up and occupy two places nor can two distinct particles occupy the same place. Assumptions must also be made about the continuity of derivatives. It is usual (see, for example, Serrin, Handbuch der Physik Bd. VIII/I, p. 129) to assume continuity up to the third order derivatives. Exception to these requirements may be allowed on a finite number of singular surfaces, lines or points, as for example when a fluid divides around an obstacle. It is shown in Appendix B that a necessary and sufficient condition for the inverse functions to exist is that the Jacobian J = ∂(x_1, x_2, x_3)/∂(ξ_1, ξ_2, ξ_3) ≠ 0 (4.11.3)

should not vanish.

The transformation (4.11.1) may be looked at as the parametric equation of a curve in space with t as parameter. The curve goes through the point ξ corresponding to the parameter t = 0, and these curves are called the particle paths. Any property of the fluid may be followed along the particle path. For example, we might be given the density in the neighborhood of a particle as a function ρ(ξ, t), meaning that for any prescribed particle ξ we have the density as a function of time, that is, the density that an observer riding on the particle would see. (Position itself is a “property” in this general sense so that the equations of the particle path are of this form.) This material description of the change of some property, say S(ξ, t), can be changed into a spatial description S(x, t) by Eq. (4.11.2), S(x, t) = S(ξ(x, t), t). (4.11.4)

Physically this says that the value of the property at position x and time t is the value appropriate to the particle which is at x at time t. Conversely, the material description can be derived from the spatial one by Eqs. (4.11.1)

S(ξ, t) = S(x(ξ, t), t), (4.11.5)

meaning that the value as seen by the particle at time t is the value at the position it occupies at that time.

Associated with these two descriptions are two derivatives with respect to time. We shall denote them by ∂/∂t = derivative with respect to time keeping x constant, (4.11.6)

and dS/dt = (dS/dt)_ξ = derivative with respect to time keeping ξ constant. (4.11.7)

Thus ∂S/∂t is the rate of change of S as observed at a fixed point x, whereas dS/dt is the rate of change as observed when moving with the particle. The latter we call the material derivative.* In particular the material derivative of the position of a particle is its velocity. Thus, putting S = x_i, we have dx_i/dt = v_i, (4.11.8)

or d x/dt = v.

This allows us to establish a connection between the two derivatives, for dS/dt = ∂S/∂t + (∂x_j/∂t) ∂S/∂x_j = ∂S/∂t + v_j ∂S/∂x_j = ∂S/∂t + (v · ∇)S. (4.11.9)

It is sometimes convenient to write this as dS/dt = ∂S/∂t + (v · ∇)S. (4.11.10)

* It is also called the convected or convective derivative and often denoted by D/Dt.

Exercise 4.11.1. It is not always necessary to use the initial position as material coordinate. Consider the equations for the particle paths in Gerstner waves x_1 = a (e^{b k} / k) sin k(σ - c t), x_2 = -a (e^{b k} / k) cos k(σ - c t), x_3 = constant.

Relate the constants a and b to the initial position and show that the particle paths are circles. Find the velocity vector and show that d |v| / dt = 0.

Exercise 4.11.2. Show that the Jacobian Eq. (4.11.3) is 1 for the Gerstner wave.

Exercise 4.11.3. Show that f(x, t) = 0 is a surface of the same material particles if and only if ∂f/∂t + v · ∇ f = 0.

Exercise 4.11.4. If f(x, t) is not a material surface but moves with a speed u different from the stream speed v, show that (v - u) · n = - (∂f/∂t) / |∇ f|, where n is the normal to the surface.

4.12. Streamlines

From the material description x(ξ,t) of the flow we have derived a vector field v = dx/dt = v(x_1, x_2, x_3, t). (4.12.1)

The flow is called steady if the velocity components are independent of time. The trajectories of the velocity field are called streamlines; they are the solutions of the three simultaneous equations dx/ds = v or dx_i/ds = v_i(x_1, x_2, x_3, t) (4.12.2)

where s is a parameter along the streamline. This parameter s is not to be confused with the time, for in Eq. (4.12.2) t is held fixed while the equations are integrated, and the resulting curves are the streamlines at the instant t. These may vary from instant to instant and in general will not coincide with the particle paths.

To obtain the particle paths from the velocity field we have to follow the motion of each particle. This means we have to solve the differential equations dx_i/dt = v_i(x_1, x_2, x_3, t)

subject to x_i = ξ_i at t = 0.

If the functions v_i do not depend on t, then the parameter along the streamlines may be taken to be t and clearly the streamlines and particle paths will coincide. Exercise 4.12.1 shows that streamlines and particle paths may coincide for an unsteady motion.

The acceleration or rate of change of velocity is defined as a = dv/dt = (∂v/∂t) + (v·∇)v. (4.12.3) Notice that in steady flow this does not vanish but reduces to a = (v·∇)v. (4.12.4) The higher rates of change are sometimes used and defined by repeated material differentiation; thus the (n - 1)th acceleration is v^{(n)} = d^n v / dt^n. (4.12.5) If C is a closed curve in the region of flow, the streamlines through every point of C generate a surface known as a stream tube. Let S be a surface with C as bounding curve, then ∫ v·n dS is known as the strength of the stream tube at its cross-section S.

Exercise 4.12.1. Show that the streamlines and particle paths coincide for the flow v_i = x_i / (1 + t).

Exercise 4.12.2. Show that if v_i / |v| is independent of t, then streamlines and particle paths will coincide.

Exercise 4.12.3. Find the streamlines and particle paths for v_i = -a_i + x_i / (1 + a_i t) where a_i are positive constants. (There is no summation on i here.) Describe the paths and streamlines if a_1 = 2, a_2 = 1, a_3 = 0.

4.13. Streaklines The name streakline is applied to the curve traced out by a plume of smoke or dye which is continuously injected at a fixed point but does not diffuse. Thus at time t the streakline through a fixed point y is a curve going from y to x(y, t), the position reached by the particle which was at y at time t = 0. A particle is on the streakline if it passed the fixed point y at some time between 0 and t. If this time were s, then the material coordinates of the particle would be given by Eq. (4.11.2) g = g(y, s). However, at time t this particle is at x = x(g, t) so that the equation of the streakline at time t is given by x = x(y, s), 0 ≤ s ≤ t. (4.13.1) If we regard the motion as having been proceeding for all time, then the origin of time is arbitrary and s can take negative values -∞ < s ≤ t.

These concepts may be illustrated by the simple plane flow v1 = x1/(1+t), v2 = x2, v3 = 0. Here the streamlines at time t are the solutions of dx1/ds = x1/(1+t), dx2/ds = x2, dx3/ds = 0. (4.13.2) Thus keeping t constant the streamline through a is x1 = a1 e^{t} / (1+t), x2 = a2 e^{t}, x3 = a3, which is a curve in the plane x3 = a3. (4.13.3) The streamlines are shown for increasing t in Fig. 4.1a.

The particle paths are solutions of dx1/dt = x1/(1+t), dx2/dt = x2, dx3/dt = 0. (4.13.4) These are x1 = ξ1(1+t), x2 = ξ2 e^{t}, x3 = ξ3, or the curves in the plane x3 = ξ3, x2 = ξ2 e^{-ξ1/ξ1 + t}? (4.13.5) They are shown for several initial positions in Fig. 4.1b.

For the inverse relations defining the particle at y, at times we have ξ1 = y1/(1+s), ξ2 = y2 e^{-s}, ξ3 = y3. (4.13.6) Hence, the streakline is given by x1 = y1/(1+s), x2 = y2 e^{-s}, x3 = y3. (4.13.7) This, with some of the particle paths that contribute to it, is shown in Fig. 4.1c. (For other examples of streamlines, streaklines and particle paths see Truesdell and Toupin, Handbuch der Physik III/1, Berlin, Springer-Verlag, 1960, pages 331-336, where further references will be found.)

4.21. Dilatation We have noticed in Section 3.16 that if the coordinate system is changed from coordinates g to coordinates x, then the element of volume changes by the formula dV = J dV0. (4.21.1) A parallelepiped is moved and distorted but because the motion is continuous it cannot break up and so at time t is some neighborhood of the point x = x(g, t). By Eq. (4.21.1), its volume is dV = J dV0 and hence 0 < J < ∞. (4.21.3) We can now ask how the dilatation changes as we follow the motion. To answer this we calculate the material derivative dJ/dt. However, J = det(∂x_i/∂ξ_j). (4.21.4) Now d(∂x_i/∂ξ_j)/dt = ∂/∂ξ_j (dx_i/dt) = ∂v_i/∂ξ_j, (4.21.4) for d/dt is differentiation with ξ constant so that the order can be interchanged. Now if we regard v_i as a function of x1, x2, and x3, ∂v_i/∂ξ_j = ∑_k (∂v_i/∂x_k) (∂x_k/∂ξ_j). (4.21.5) In Appendix A it is shows that

d(ρv)/dt + ∇·(ρv) = 0 (4.3.3)

which is the equation of continuity.

Combining the equation of continuity with Reynolds' transport theorem for a function g = ρF we have

(4.3.4)

since the second term vanishes by (4.3.3).

A fluid for which the density ρ is constant is called incompressible. In this case the equation of continuity becomes

∇·v = 0 (4.3.5)

and the motion is isochoric or the velocity field solenoidal.

Exercise 4.3.1. Show that ρ = ρ₀ if ρ₀ is the distribution of density of the fluid at time t = 0 and ∇·v = 0, then the distribution at time t is ρ = ρ₀.

Exercise 4.3.2. Show that, for the motion of Ex. 4.12.3, ρx₁x₂x₃ = f(t₁t₂t₃).

4.41. Deformation and rate of strain

Consider two nearby points P and Q with material coordinates ξ and ξ + dξ. At time t they are to be found at x(ξ, t) and x(ξ + dξ, t).

(4.41.1)

where O(dξ²) represents terms of order dξ² and higher which will be neglected from this point onwards. Thus the small displacement vector dξ has now become

dx = x(ξ + dξ, t) - x(ξ, t),

where

(4.41.2)

It is clear from the quotient rule (since dξ is arbitrary) that the nine quantities ∂xᵢ/∂ξⱼ are the components of a tensor. It may be called the displacement gradient tensor and is basic to the theory of elasticity. For fluid motion, its material derivative is of more direct application and we will concentrate on this.

If v = dx/dt is the velocity, the relative velocity of two particles ξ and ξ + dξ has components

(4.41.3)

However, by inverting the relation of Eq. (4.41.2), we have

(4.41.4)

expressing the relative velocity in terms of current relative position. Again it is evident that the (∂vᵢ/∂xⱼ) are components of a tensor, the velocity gradient tensor, for which we need to obtain a sound physical feeling.

We first observe that if the motion is a rigid body translation with velocity u,

x = ξ + ut (4.41.5)

and the velocity gradient tensor vanishes identically. Secondly, the velocity gradient tensor can be written as the sum of symmetric and antisymmetric parts,

∂vᵢ/∂xⱼ = eᵢⱼ + ωᵢⱼ (4.41.5)

Now we have seen (Section 2.45) that a relative velocity dvᵢ related to the relative position dxⱼ by an antisymmetric tensor ωᵢⱼ represents a rigid body rotation with angular velocity ω = -vec ω. Therefore dvᵢ = ωᵢⱼ dxⱼ represents a rigid body rotation with angular velocity ω = -vec ω. In this case

(4.41.6)

or ω = ½ curl v.

(Cf. Ex. 3.24.8.) Thus the antisymmetric part of the velocity gradient tensor corresponds to a rigid body rotation, and, if the motion is a rigid one (composed of a translation plus a rotation), the symmetric part of the velocity gradient tensor will vanish. For this reason the tensor eᵢⱼ is called the deformation or rate of strain tensor and its vanishing is necessary and sufficient for the motion to be without deformation, that is, rigid.

Exercise 4.41.1. If eᵢⱼ = 0 show that xᵢ = Ωᵢⱼ ξⱼ + uᵢt, where Ωᵢⱼ and uᵢ are constants.

4.42. Physical interpretation of the deformation tensor

To interpret the tensor eᵢⱼ we shall see how a small element is changing during the motion. The length of the line segment from P to Q is ds, where

(4.42.1)

Now P and Q are the material particles ξ and ξ + dξ so that dξᵢ and dξⱼ do not change during the motion. Thus

by symmetry. However,

Thus

d/dt (ds²) = d/dt (dxᵢ dxᵢ) = 2 dxᵢ dxᵢ/dt = 2 dxᵢ dvᵢ = 2 ∂vᵢ/∂xⱼ dxⱼ dxᵢ = 2 eᵢⱼ dxᵢ dxⱼ (4.42.2)

by symmetry, or

½ d/dt (ds) / ds = eᵢⱼ (dxᵢ/ds) (dxⱼ/ds). (4.42.3)

Now dxᵢ/ds is the i'th component of a unit vector in the direction of the segment PQ, so that this equation says that the rate of change of the length of the segment as a fraction of its length is related to its direction through the deformation tensor.

In particular, if PQ is parallel to the 0₁ coordinate axis, we have dx/ds = δᵢ₁ and

d/dt (ds) / ds = e₁₁. (4.42.4)

Thus e₁₁ is the rate of longitudinal strain of an element parallel to the 0₁ axis. Similar interpretations apply to e₂₂ and e₃₃.

Again consider two segments PQ and PR, where R is the particle ξ + dξ'. If θ is the angle between them and ds' is the length of PR,

ds ds' cos θ = dxᵢ dx'ᵢ.

Differentiating with respect to time we have

d/dt [ds ds' cos θ] = dvᵢ dx'ᵢ + dxᵢ dv'ᵢ

since dvᵢ = (∂vᵢ/∂xⱼ) dxⱼ. The i and j are dummy suffixes so we may interchange them in the first term on the right, then performing the differentiation we have

cos θ d/dt (ds)/ds + cos θ d/dt (ds')/ds' - sin θ dθ/dt = eᵢⱼ (dxᵢ/ds) (dx'ⱼ/ds') + eⱼᵢ (dx'ⱼ/ds') (dxᵢ/ds)

Now suppose that dx' is parallel to the axis 0₁ and dx to the axis 0₂, so that (dx'ᵢ/ds') = δᵢ₁ and (dxⱼ/ds) = δⱼ₂ and e₁₂ = e₂₁. Then

(4.21.5)

Thus e₁₂ is to be interpreted as one-half the rate of decrease of the angle between two segments originally parallel to the 0₁ and 0₂ axes respectively. Similar interpretations are appropriate to e₂₃ and e₃₁.

The fact that the deformation tensor is linear in the velocity field has an important consequence. Since we may superimpose two velocity fields to form a third, it follows that the deformation tensor of this is the sum of the deformation tensors of the fields from which it is composed. Thus a flow with v₁ = A₁x₁, v₂ = v₃ = 0 would have only one nonvanishing component of the rate of strain tensor, e₁₁ = A₁. This represents a pure stretching in the 0₁ direction with no deformation of an element perpendicular. Again, if vᵢ = Aᵢxᵢ (no summation on i), we have a deformation which is the superposition of three stretchings parallel to the three axes. However, if v₁ = f(x₂), v₂ = v₃ = 0 so that the only nonzero component of the deformation tensor is e₁₂ = ½f'(x₂), the motion is one of pure shear in which elements parallel to the coordinate axes are not stretched at all. Note however that in pure stretching an element not parallel or perpendicular to the direction of stretching will suffer rotation. Likewise in pure shear an element not normal to or in the plane of shear will suffer stretching.

Exercise 4.42.1. Follow through the ideas of this section for the plane stagnation flow v₁ = x₁, v₂ = -x₂, v₃ = 0. Show that if θ is the angle between an infinitesimal material segment and the axis 0₁, then the rate of change of log tan θ is constant along a particle path.

Exercise 4.42.2. Find an expression for the rate of change of the angle between a material line segment and a fixed direction and analyse it.

4.43. Principal axes of deformation

The quadratic form (4.42.3) may be written

d/dt ln (ds) = eᵢⱼ lᵢ lⱼ (4.43.1)

where l is a unit vector in the direction PQ. From our knowledge of symmetric second order tensors we know that there are three mutually perpendicular directions along which this expression has stationary values (see Appendix A.12). Moreover we know from Section 2.5 and Appendix A.ll that we can find a rotation of coordinates to a frame 0123 such that the component eᵢⱼ in this frame of reference are zero if i ≠ j. If e⁽¹⁾, e⁽²⁾, e⁽³⁾ are the values of e₁₁, e₂₂, and e₃₃, they are roots of the cubic

det (eᵢⱼ - e δᵢⱼ) = e³ - Θ e² + Ξ e - Δ = 0 (4.43.2)

(cf. Eq. 2.5.4). The three directions 0₁, 0₂, 0₃ are called the principal axes of stretching or rate of strain and e⁽¹⁾, e⁽²⁾, e⁽³⁾ the principal rates of strain.

The three scalars Θ, Ξ, Δ are the invariants of the deformation tensor and the first of them we have already encountered as the dilatation. In fact

Θ = e₁₁ + e₂₂ + e₃₃ = ∂v₁/∂x₁ + ∂v₂/∂x₂ + ∂v₃/∂x₃ = ∇·v

Ξ = e₁₁e₂₂ + e₂₂e₃₃ + e₃₃e₁₁ - e₁₂² - e₂₃² - e₃₁²

Δ = det eᵢⱼ = eᵢⱼeⱼₖeₖᵢ.

We know that Θ is to be interpreted as the fractional rate of change of an infinitesimal volume. Dishington (Physics of Fluids, 3, 1960, p. 482) has given a physical interpretation to the other invariants. He finds that

lim_{V→0} (1/V) d²V/dt² = (∇·a)₀ + 2Ξ

where (∇·a)₀ is the divergence of the acceleration as measured by an observer moving and rotating with the element.* Thus 2Ξ is the part contributed to the fractional acceleration of volume by the steady velocity of the surface. In a similar way 6Δ is found to be the contribution to the limit of (d³V/dt³)/V.

A picture of the deformation may be formed by considering what happens to a small sphere of radius dr during a short interval of time dt. Suppose that we have chosen the coordinate system so that the axes are parallel to the principal axes of stretching at the point x. The particles on a sphere of radius dr and center x are x + l dr, where l is a unit vector and they have material coordinates ξ + l dξ where

l dξ = dr. (4.43.3)

In the interval from t to t + dt the center moves from x(ξ, t) to x(ξ, t + dt). If dy is the position of a particle that was on the surface of the sphere relative to the new position of the center,

dyᵢ = xᵢ(ξ + l dξ, t + dt) - xᵢ(ξ, t + dt)

(4.43.4)

However, here ∂xᵢ/∂t is evaluated at ξ and t + dt, that is,

Substituting this value back into Eq. (4.43.4) and using the relation (4.43.3) in the form

we have

dyᵢ = lⱼ dξⱼ ∂xᵢ/∂ξⱼ + ∂xᵢ/∂t dt - ∂xᵢ/∂t dt

= (∂xᵢ/∂ξⱼ dξⱼ) + lⱼ dξⱼ aᵢⱼ dt

= (δᵢⱼ + eᵢⱼ dt + ωᵢⱼ dt) lⱼ dr = Aᵢⱼ lⱼ dr (4.43.5)

Now since the coordinate axes were chosen parallel to the principal axes of deformation eᵢⱼ = 0 for i ≠ j,

Aᵢⱼ = (1 + eᵢᵢ dt) δᵢⱼ + ωᵢⱼ dt

The offdiagonal terms thus represent the rigid body rotation as before and the remaining terms are purely diagonal giving, in the absence of rotation,

dyᵢ = (1 + eᵢᵢ dt) lᵢ dr (no summation).

Since l is a unit vector,

Σ lᵢ² = 1 = Σ dyᵢ² / [(1 + eᵢᵢ dt) dr]²

and this is an infinitesimal ellipsoid whose axes are coincident with the principal axes of stretching and of lengths (1 + eᵢᵢ dt) dr, i = 1,2,3. Thus in the complete deformation a small sphere is distorted into an ellipsoid and rotated, as shown in Fig. 4.4.

This insight into the character of deformation is expressed by the so-called Cauchy-Stokes decomposition theorem, which Truesdell formulates as follows: an arbitrary instantaneous state of motion is the sum of a pure deformation and a rigid motion.

on may be resolved at each point into a uniform translation, a dilatation along three mutually perpendicular principal axes of deformation, and a rigid rotation of these axes.

Exercise 4.43.1. Show that e_{ij}e_{ij} = θ^2 - 2ω and deduce that θ ≥ 0 for an isochoric motion.

Exercise 4.43.2. The stretching is called spherical if all the principal rates of strain are equal. Show that in this case e_{ij} = (1/3)θ δ_{ij}.

Exercise 4.43.3. If u1 = f(r)(x2/r), u2 = -f(r)(x1/r), u3 = 0, r^2 = x1^2 + x2^2, the motion is a steady one with circular streamlines. Show that the deformation tensor is e_{11} = -e_{22} = F sin 2θ, e_{12} = -F cos 2θ where tan θ = x2/x1 and F = 1/2 {f'(r) - f(r)/r}. Show that the principal rates of strain are equal and opposite and find the principal axes.

4.5. Vorticity, vortex lines, and tubes

We have seen that the antisymmetric part of the rate of strain tensor represents the local rotation, in fact vec Ω = 1/2 curl v. The curl of the velocity is known as the vorticity, ω = ∇ × v. (4.5.1)

For an irrotational flow the vorticity vanishes everywhere. The trajectories of the vortex field are called vortex lines and the surface generated by the vortex lines through a closed curve C is a vortex tube. Since the strength of a vector tube of the field a at its section S has been defined as ∫∫ a · n dS, we see that the strength of a vortex tube equals the circulation round the closed curve C which bounds the cross-section S, for ∫∫(∇ × v) · n dS = ∮_C v · t ds (4.5.2) by Stokes’ theorem.

The kinematics of vorticity has been elegantly and extensively treated by Truesdell in a monograph of that title (Indiana University Press, 1954) and in the appropriate sections of Bd. III/l of the Handbuch der Physik. Here we have no intention of covering or even attempting to survey the full scope of the theory; it will be sufficient if the reader’s buoyancy is increased enough for him to enjoy swimming in these waters. Truesdell collects four interpretations of the vorticity some of which we have already encountered. First, since the curl can be defined in terms of the circulation around an infinitesimal curve, the component of vorticity in a given direction is the circulation around a small circuit in a plane normal to that direction. Second, for a rigid body rotation the angular velocity is 1/2 curl v. Now the principal axes are unchanged by the deformation part of the rate of strain tensor and hence 1/2ω is the angular velocity of the principal axes at a point with respect to a fixed coordinate system. Third, it may be shown that 1/2ω_1 is the mean value of the angular velocity of two line segments through the point parallel to the e_2 and e_3 axes. The fourth interpretation is related to the last and identifies 1/2ω_1 as the mean value of all the rates of rotation about an axis parallel to e_1 of line segments in a plane normal to e_1. The last two interpretations can of course be generalized to relate 1/2 ω_n to the mean rates of rotation of segments in a plane with normal n.

We observe that the strength of a vortex tube at any cross-section is the same, for ω is a solenoidal vector. One characterisation of the solenoidal field is the vanishing of ∫∫ ω · n dS over any closed surface. Take this closed surface to be a stream tube with sections S1 and S2 whose boundary curves are C1 and C2. If n is the outward normal, it will be the positive normal (in the sense of being right-handed for a given circuit of C) for one of S1 and S2 and negative for the other. Since ω · n vanishes identically over the surface of the vortex tube, ∫_{S1} ω · n dS = ∫_{S2} ω · n dS (4.5.3) and the strength is constant.

Taking the curl of the formula (Ex. 4.5.1) for the acceleration ∂v/∂t, we have ∇ × a = ∂ω/∂t + ∇ × (ω × v) = dω/dt - (ω · ∇)v + ω(∇ · v), (4.5.4) where we have made use of Ex. 3.24.4. Thus, using the continuity equation, dω/dt - (ω · ∇)v = 0 for incompressible flow, ∇ × a = 0. (4.5.5) If the acceleration is irrotational this equation may be solved. Setting ω_i = p c_i (∂x_j/∂ξ_k), where the c_j are components of a new vector c, we have ... Since J, the determinant of the coefficients of the dc_i/dt, is not zero, this gives ... (4.5.6) If ω_0 and p_0 are the initial values of ω and p of a particle, (ω/p) = c_0 and hence ... (4.5.7)

If initially an element δl is in a vortex line, δl = ω_0 δu. However, under the motion, this element becomes ... in other words a material element tangent to a vortex line remains tangent to it. It follows that, if ∇ × a = 0 then vortex lines are material lines. It can be shown that this is also true under the broader condition ω · (∇ × a) = 0. We shall return to this subject in Chapter 6, but must now pass on to some dynamical considerations.

Exercise 4.5.1. Show that the acceleration a is given by ...

Exercise 4.5.2. Establish the third interpretation given above.

Exercise 4.5.3. Show that the abnormality of the velocity field is the ratio of the component of vorticity in the direction of motion to the speed. (Abnormality is defined in Section 3.45) (Truesdell).

Exercise 4.5.4. Show that v_{i,j}v_{i,j} = e_{ij}e_{ij} + ω_iω_i and hence that ... ∇e = dΩ/dt + (θ^2 - 2ω)δ - 4 I ω I^2 (Truesdell).

Exercise 4.5.5. Show that the strength of a vortex tube remains constant if ... (Cf. Ex. 4.22.7.)

## BIBLIOGRAPHY

The basic material on kinematics goes back to the seventeenth century. Full references can be found in the works of Truesdell and a valuable survey has been given by him in his introduction to volume (2) I2 of L. Euleri Opera Omnia (Lausannae MCM LIV), “Rational Fluid Mechanics,” 1687-1765.

4.1. The most extensive exposition is to be found in chapter B of Truesdell, C. A., and R. Toupin, The classical field theories, in Handbuch der Physik III/l, Ed. S. Flugge. 1960. The “peculiar and characteristic glory of three-dimensional kinematics” is the subject of an earlier treatise Truesdell, C. A., The kinematics of vorticity. Bloomington, Ind: Indiana University Press, 1954.

The basic material is given in Serrin, J., Mathematical principles of classical fluid mechanics, in Handbuch der Physik VIII/1, Ed. S. Flügge, 1959. We have followed his exposition in treating the vortex line in the last section.

## 5. Stress in Fluids

The object of this chapter is to show the tensorial character of stress and exhibit some of the ways in which it may be related to strain. We have already referred to stress as being a force per unit area and so having two directions (those of the force and the normal to the area) associated with it. This gives reason to suspect that stress can be represented by a tensor, but to establish this we follow a very elegant line of reasoning laid down by Cauchy in 1823. On the principle of the conservation of momentum we can then establish certain properties of the stress tensor. The relation between the stress tensor and the deformation tensor is known as the mechanical constitutive equation for the material and the remainder of the chapter will treat some elementary examples of these defining relations.

5.11. Cauchy's stress principle and the conservation of momentum

The forces acting on an element of a continuous medium may be of two kinds. External or body forces, such as gravitation or electromagnetic forces, can be regarded as reaching into the medium and acting throughout the volume. Internal or contact forces are to be regarded as acting on an element of volume through its bounding surface. If the element of volume has an external bounding surface, the forces there may be specified, as, for example, when a constant pressure is applied over a free surface. If the element is internal, the resultant force is that exerted by the material outside the surface upon that inside. Let n be the unit outward normal at a point of the surface S and t(n) the force per unit area exerted there by the material outside S. Then Cauchy's principle asserts that t(n) is a function of the position x, the time t, and the orientation n of the surface element. Thus the total internal force exerted on the volume V through its bounding surface S is ∫∫ t(n) dS. (5.11.1) If f is the external force per unit mass (for example if e_3 is vertical, gravitation will exert a force -g e_3 per unit mass or -ρg e_3 per unit volume), the total external force will be ∫∫∫ f ρ dV. (5.11.2) The principle of the conservation of linear momentum asserts that the sum of these two forces equals the rate of change of linear momentum of the volume; that is, d/dt ∫∫∫ v ρ dV = ∫∫ t(n) dS + ∫∫∫ f ρ dV. (5.11.3) This is an integral form of the equations of motion which can be changed when we know more about the nature of t(n). If we assume that all torques arise from macroscopic forces, then not only momentum but also its moment are expressible in terms of f and t(n). This is the case with many ordinary fluids, but a fluid with a strongly polar character is capable of transmitting stress torques and being subjected to body torques. We shall consider this briefly in Section 5.13.

From the form of these integral relations we can deduce an important relation. Suppose V is a volume of given shape with characteristic dimension d. Then the volume of V will be proportional to d^3 and the area of S to d^2, with the proportionality constants depending only on the shape. Now let V shrink on a point but preserve its shape, then the first two integrals in Eq. (5.11.3) will decrease as d^3 but the last will be as d^2. It follows that lim_{d→0} (1/d^3) ∫∫ t(n) dS = 0 or, the stresses are locally in equilibrium.

Exercise 5.11.1. Show that t(-n) = -t(n).

Exercise 5.11.2. Establish a result for the moments of the stresses as the volume shrinks on a point.

5.12. The stress tensor

To elucidate the nature of the stress system at a point P we consider a small tetrahedron with three of its faces parallel to the coordinate planes through P and the fourth with normal n (see Fig. 5.1). If dA is the area of the slant face, the areas of the faces perpendicular to the coordinate axis P_i is dA_i = n_i dA. The outward normals to these faces are -e_i.

We may denote the stress vector over these faces by -t(+) (where t(+) denotes the stress vector when +e(,) is the outward normal.) Then applying the principle of local equilibrium to the stress forces when the tetrahedron is very small, we have

t(n) dA - t(1) dA1 - t(2) dA2 - t(3) dA3 = [t(n) - t(1)n1 - t(2)n2 - t(3)n3] dA = 0. (5.12.1)

Now let T_ij denote the component of T and t_i(n) be the i-th component of t(n), so that this equation can be written

t_i = T_ij n_j. (5.12.2)

However, t(n) is a vector and n is a unit vector quite independent of the T_ij, so that by the quotient rule the T_ij are components of a second order tensor T. In dyadic notation we might write

t(n) = n · T. (5.12.3)

This tells us that the system of stresses in a fluid is not so complicated as to demand a whole table of the functions t(x,n) at any given instant, but that it depends rather simply on n through the nine quantities T_ij(x). Moreover, because these are components of a tensor, any equation we derive with them will be true under any rotation of the coordinate axes.

Inserting Eq. (5.12.2) in Eq. (5.11.3) and using Green’s theorem we have

However, since V is an arbitrary volume, this equation is only satisfied if

∇ · T + ρ f = ρ a (5.12.4)

or

ρ a = ρ f + ∇ · T, (5.12.5)

where a = dv/dt is the acceleration. This is Cauchy’s equation of motion. It holds for any continuum no matter how the stress tensor T is connected with the rate of strain.

Exercise 5.12.1. Show that Cauchy’s equation of motion (5.12.4) can be written as

-∂(ρ v_i)/∂t = (T_ij - ρ v_i v_j),j

and interpret this physically.

Exercise 5.12.2. Show that if Φ is any function of position and time, (Theorem of stress means.)

5.13. The symmetry of the stress tensor

If the fluid is such that the torques within it arise only as the moments of direct forces, we shall call it nonpolar. A polar fluid is one that is capable of transmitting stress couples and being subjected to body torques, as in polyatomic and certain non-Newtonian fluids. For the nonpolar fluid we can make the assumption either that angular momentum is conserved or that the stress tensor is symmetric. We will make the first assumption and deduce the symmetry and then discuss the more general situation that obtains for the polar case.

Since v × v = 0, d(x × v)/dt = x × a, applying the transport theorem (4.3.4) to the equation for moment of momentum (5.11.4) we have

∫_V ρ d/dt (x × v) dV = ∫_V ρ (x × f) dV + ∫_S (x × t(n)) dS. (5.13.1)

This last integral has as its i-th component

∫_S ε_ijk x_j T_kl n_l dS = ∫_V (ε_ijk x_j T_kl),l dV

by Green’s theorem. However, this integrand is

ε_ijk (x_j,k T_kl + x_j T_kl,l),

since x_j,k = δ_jk, and this is the i-th component of x × (∇ · T) + T, where T_i = ε_ijk T_jk. Substituting back into Eq. (5.13.1) and rearranging gives

∫_V x × (ρ a - ρ f - ∇ · T) dV = ∫_V T dV. (5.13.3)

However, the left-hand side vanishes identically by Cauchy’s equation (5.12.5), hence the right-hand side vanishes for an arbitrary volume and so

T = 0. (5.13.4)

However, the components of T are (T_23 - T_32), (T_31 - T_13), and (T_12 - T_21), and the vanishing of these implies

T_ij = T_ji. (5.13.5)

so that T is symmetric.

In the case of a polar fluid we must introduce a body torque per unit mass, ρ g, in addition to the body force ρ f, and a couple stress C_ij in addition to the normal stress t(n). Then just as t(n) can be written as n · T so C(n) can be expressed in the form n · C. The angular momentum must also be conceived to consist of two parts, the moment of linear momentum ρ x × v and an intrinsic angular momentum ρ l. Then a balance of total angular momentum gives

d/dt ∫_V ρ (x × v + l) dV = ∫_V ρ (x × f + g) dV + ∫_S [x × t(n) + c(n)] dS.

This is an equation for the total angular momentum which may be written

d/dt ∫_V ρ (x × v + l) dV = ∫_V [ρ (x × f + g) + ∇ · (x × T + C)] dV. (5.13.7)

From the vector product of x and Cauchy's equation we have

ρ x × a = ρ d/dt (x × v) = ρ x × f + x × (∇ · T). (5.13.8)

and subtracting we see that

ρ dl/dt = ρ g + ∇ · C + T. (5.13.9)

Thus the antisymmetric part of the stress tensor contributes to the rate of increase of the internal angular momentum. When the tensor is not symmetric, the external moment of momentum is not conserved in the usual sense for if we integrate the i-th component of (5.13.8) throughout the volume V, we have

In dyadic notation this is

which shows that there is a loss of external angular momentum per unit volume of T_i which shows up as a gain in internal angular momentum in Eq. (5.13.9).

Exercise 5.13.1. Apply the result of Ex. 5.11.2 to an elementary parallelepiped to prove the symmetry of the stress tensor.

Exercise 5.13.2. Show that the symmetry of the stress tensor is equivalent to Cauchy's reciprocal theorem: Each of two stresses at a point has an equal projection on the normal to the surface on which the other acts.

5.14. Hydrostatic pressure

If the stress system is such that an element of area always experiences a stress normal to itself and this stress is independent of the orientation, the stress is called hydrostatic. All fluids at rest exhibit this stress behavior. It implies that n · T is always proportional to n and that the constant of proportionality is independent of n. Let us write this constant -p, then

n_i T_ij = -p n_j (5.14.1)

However, this equation means that any vector is a characteristic vector of T which must therefore be spherical. Thus

T_ij = -p The fluid is isotropic, that is, there is no preferred direction. IV. When there is no deformation (e_{ij} = 0) the stress is hydrostatic, (T_{ij} = -p\delta_{ij}).

The first assumption implies that the relation between stress and rate of strain is independent of the rigid body rotation of an element given by the anti-symmetric kinematical tensor a_{ij}. The thermodynamic variables, for example, pressure and temperature, will be carried along throughout this discussion without specific mention except where it is necessary for emphasis. We are concerned with a homogeneous portion of fluid so we assume in the second place that the stress tensor depends only on position through the variation of e_{ij} and the thermodynamic variables with position. The third assumption is that of isotropy and we shall first show that this implies that the principal directions of the two tensors coincide. To express this as an equation we write T_{ij} = f_{ij}(e_{mn}), then if there is no preferred direction, T_{ij} is the same function f_{ij} of 2 as T_{rs} is of e_{mn}. Thus (5.21.1)

The fourth assumption is that the tensor P_{ij} = T_{ij} + p\delta_{ij} vanishes when there is no motion. P_{ij} is called the viscous stress tensor.

The Stokesian fluid is essentially nonelastic. We shall discuss later (Chapter 8) the case where both viscous and elastic behavior is present.

5.22. Constitutive equations of the Stokesian fluid

If l_{mi} is the set of direction cosines of a rotation of the axes from the system 0123 to 0123, we have, since T_{ij} and e_{ij} are tensors, T'_{ij} = l_{mi} l_{nj} T_{mn}, e'_{ij} = l_{ri} l_{sj} e_{rs}. (5.22.1)

Hence Eq. (5.21.1) becomes l_{mi} l_{nj} f_{mn}(e_{rs}) = f'_{ij}(l_{rp} l_{sq} e_{pq}). (5.22.2)

Now suppose that the coordinate system has been chosen so that it coincides with the principal axes of e_{ij}. Then we can take e_{11} = d_1, e_{22} = d_2, e_{33} = d_3 and e_{rs} = 0, r ≠ s. Then f_{mn} is a function of d_1, d_2, and d_3. If we take the rotation specified by l_{11} = l_{22} = l_{33} = -1, and l_{ij} = 0, i ≠ j, then the d_i = e_{ii} are unchanged. However, f'_{33} = l_{3m} l_{3n} f_{mn} = f_{33} and so both are zero. Similarly, f'_{13} = f'_{31} = 0 and a similar transformation with l_{11} = -1, l_{22} = 1, l_{33} = -1 shows that f'_{12} = f'_{21} = 0. Thus in the principal coordinate system of the deformation tensor, the stress tensor has diagonal form and it therefore has the same principal axes. We may therefore write P_{ii} = p_i, P_{ij} = 0, i ≠ j and p_i = p_i(d_1, d_2, d_3) (5.22.3)

where, by the fourth assumption, the p_i must vanish when the d_i vanish.

We now ask what is the most general form that the p_i can have. Since a permutation of d_1, d_2, d_3 can be effected by an orthogonal transformation, such a permutation must permute the functions p_i in the same way. For example the diagonal tensor (d_1, d_2, d_3) is transformed to (d_3, d_2, d_1) by l_{11} = l_{33} = 1, other l_{ij} = 1, other l's zero. Such a relation is given by p_i = α + β d_i + γ d_i^2, (5.22.4)

where α, β, and γ can be functions of the three invariants Θ, Θ_2, Θ_3 since these are unaffected by a permutation. Moreover we do not need to assume any higher powers than the square of d_i, for these can be expressed as functions of d_i, d_i^2 and the three invariants. For example, d_3^3 = Θ d_3^2 - Θ_2 d_3 + Θ_3, d_3^4 = Θ d_3^3 - Θ_2 d_3^2 + Θ_3 d_3 = (Θ^2 - Θ_2) d_3^2 - (ΘΘ_2 - Θ_3) d_3 + ΘΘ_3, and so on. If the d_i are all different, the three equations (5.22.4) can be solved for α, β, and γ. If two of the d_i are the same, the corresponding p_i will be the same and there will really only be two distinct equations from which α and β may be determined to give a relation p_i = α + β d_i. If all the d_i are the same, then all the p_i are the same and we have p_i = α(Θ, Θ_2, Θ_3).

All cases are thus subsumed under the general formula (5.22.4) which is written for the principal coordinate system. If we transform back to any other system, the functions α, β, and γ must be the same or the requirement of isotropy will not be met. Thus in general p_i depends only on the thermodynamic state but α, β, and γ depend as well on the invariants of the rate of strain tensor. This gives ample scope for the fitting of exceedingly complex relations, but the tensorial character is prescribed by the assumptions.

If the fluid is compressible, the thermodynamic pressure is a well-defined quantity and we should take p equal to this. Then, by the fourth assumption, α = 0 when e_{ij} = 0. If the fluid is incompressible, the thermodynamic pressure is not defined and pressure has to be taken as one of the fundamental dynamical variables. We are at liberty to do this in the simplest possible way so that without losing any generality we can absorb α into the pressure p and write T_{ij} = -p\delta_{ij} + β e_{ij} + γ e_{ik} e_{kj}, (5.22.6)

which insures that T_{ij} reduces to the hydrostatic form when the deformation vanishes.

5.23. The Newtonian fluid

The Newtonian fluid is a linear Stokesian fluid, that is, the stress components depend linearly on the rates of deformation. Moreover, since the viscous stress tensor must vanish with vanishing e_{ij}, we must have p_i = a_{i1} d_1 + a_{i2} d_2 + a_{i3} d_3. (5.23.1)

However, we have observed that the assumption of isotropy implies that any permutation of the d's must effect the same permutation of the p's. Writing out these equations in full gives: p_1 = a_{11} d_1 + a_{12} d_2 + a_{13} d_3, p_2 = a_{21} d_1 + a_{22} d_2 + a_{23} d_3, p_3 = a_{31} d_1 + a_{32} d_2 + a_{33} d_3.

Now permute the d_1, d_2, d_3 to d_3, d_1, d_2 and rearrange to obtain a_{11} d_3 + a_{12} d_1 + a_{13} d_2 = p_1, a_{21} d_3 + a_{22} d_1 + a_{23} d_2 = p_2, a_{31} d_3 + a_{32} d_1 + a_{33} d_2 = p_3.

The right-hand side of each equation has been obtained by making the same permutation on the p's. Now we compare these two sets of equations; for example, a_{11} d_1 + a_{12} d_2 = a_{13} d_3 + a_{11} d_1, gives all = a_{13}, a_{12} = a_{11}, a_{13} = a_{11}. Doing this for all, and for the set we could derive by permuting d_1, d_2, d_3 to d_2, d_3, d_1, we find a_{11} = a_{22} = a_{33} = a, a_{12} = a_{21} = a_{23} = a_{32} = a_{13} = a_{31} = b.

Let the common value of the second row be μ and of the first a + 2μ/3, where these are for the moment numbers whose physical meaning has to be obtained. Then p_i = μ(d_1 + d_2 + d_3) + (a + 2μ/3) d_i = λ Θ δ_{ij} + 2μ e_{ij}. (5.23.2)

Transforming to a general coordinate system P_{ij} = λ Θ δ_{ij} + 2μ e_{ij} (5.23.3)

or T_{ij} = (-p + λ Θ) δ_{ij} + 2μ e_{ij}. (5.23.4)

We have given this proof in extenso since it is a kind of link between the following two demonstrations. In the first of these we observe that the result follows immediately from imposing linearity on the general relation (5.22.6) for this requires that γ = 0, β be a constant, and α be proportional to Θ since it must vanish with Θ. Again, since P_{ij} is to be a linear combination of e_{ij}, it can be expressed as a tensor product P_{ij} = A_{ijmn} e_{mn}.

Now A_{ijmn} must be symmetric in i and j and must be an isotropic fourth order tensor. However, by Section 2.7 we know that the most general form of A is A_{ijmn} = A δ_{ij} δ_{mn} + B(δ_{im} δ_{jn} + δ_{in} δ_{jm}) + C(δ_{im} δ_{jn} - δ_{in} δ_{jm}).

The symmetry requirement is met by putting C = 0 so that P_{ij} = A δ_{ij} e_{kk} + B(e_{ij} + e_{ji}) = A Θ δ_{ij} + 2B e_{ij}.

The first demonstration is a link between the latter two in that the same kind of arguments are used there as were used in establishing the form of the general isotropic tensor. However, since we had already dismissed the antisymmetric part, the argument was distinctly simpler.

5.24. Interpretation of the constants λ and μ

Consider the shear flow given by u_1 = f(x_2), u_2 = u_3 = 0. (5.24.1)

For this we have all the e_{ij} zero except e_{12} = e_{21} = 1/2 f'(x_2). (5.24.2)

Thus T_{12} = T_{21} = μ f'(x_2) (5.24.3)

and all the other viscous stresses are zero. This is shown in Fig. 5.2 and it is evident that μ is the proportionality constant relating the shear stress to the velocity gradient. This is the common definition of the viscosity, or more precisely the coefficient of shear viscosity, of a fluid.

For an incompressible fluid we have seen that the pressure is the mean of the principal stresses since this is -(T_{11} + T_{22} + T_{33})/3 and Θ = 0. For a compressible fluid we should take the pressure p as the thermodynamic pressure to be consistent with our ideas of equilibrium. Thus if we call -p the mean of the principal stresses, p - p = -(λ + 2μ/3) Θ = -(λ + 2μ/3) ∇·v (5.24.4)

Since p, the thermodynamic pressure, is in principle known from the equation of state, p - p is a measurable quantity. Equation (5.24.4) shows that it is proportional to (d ln ρ)/dt and the constant of proportionality is known as the coefficient of bulk viscosity. It is difficult to measure, however, since relatively large rates of change of ρ must be used and the assumption of linearity is then dubious. Stokes assumed that p = p and on this ground claimed that λ + 2μ/3 = 0 (5.24.5)

supporting this from an argument from the kinetic theory of gases. While this assumption seems to be reasonable for monatomic gases, it is certainly not true for polyatomic gases or liquids. However, the precise value of λ becomes unimportant for motions that are nearly isochoric or fluids nearly incompressible. For a fuller discussion see the bibliography at the end of this chapter.

## BIBLIOGRAPHY

5.11. For a fuller analysis of the distinctions of force see Truesdell, C. A. and R. Toupin, The classical field theories, in Handbuch der Physik Bd. III/1, 1960, pp. 536 et seq. and references given there.

5.13. Asymmetric stress tensors arise from the molecular theory of gases, see Dahler, J. S., J. Chem. Phys. 30, (1959), 1447-1475. and Grad, H., Comm. Pure Appl. Math. 5 (1952), 455-494. The matter is treated by Truesdell in the above reference sects. 60-61, 205. See also Dahler, J. S. and L. E. Scriven, Angular momentum of continua, Nature, 192, No. 4797 (Oct. 7, 1961), 36-37.

5.21. Serrin, J., The derivation of stress deformation relations for a Stokesian fluid. also his article in Handbuch der Physik VIII/1, sections 58-65.

5.24. A summary of the history of Stokes relation 3λ + 2μ = 0 is given by Truesdell, C. A., Rat. Mech. and Anal. 1 (1952) pp. 228-231, where many other references are given. The importance of the second viscosity in sound propagation is discussed by Landau, L. D. and E. M. Lifshitz, Fluid mechanics, pp. 304-9, Reading.

我们现在已经掌握了所有材料来组装流体运动方程，对于柯西运动方程(5.12.4)，我们可以加入本构方程(5.23.4)。我们将首先对牛顿流体进行此操作，并得到被称为纳维-斯托克斯方程的方程组。

柯西运动方程是 ρ a_i = ρ f_i + ∂τ_ij/∂x_j，(6.11.1)

其中对称应力张量 τ_ij 与应变率张量的关系为 τ_ij = (-p + λθ)δ_ij + 2μ e_ij。(6.11.2)

从最后一个方程我们显然需要 e_ij = 1/2 (∂u_i/∂x_j + ∂u_j/∂x_i) = 1/2 ∂u_i/∂x_j + 1/2 ∂u_j/∂x_i = -1/2 ∇² u_ij + 1/2 (∇×(∇×u))_ij。

于是有 ∂τ_ij/∂x_j = -∂p/∂x_i + ∂/∂x_i (λθ) + ∂/∂x_j (2μ e_ij)， 将其代入方程(6.11.1)得到 ρ du_i/dt = ρ f_i - ∂p/∂x_i + ∂/∂x_i (λ∇·u) + ∂/∂x_j (2μ e_ij)。(6.11.4)

使用已熟悉的记号，这可以写成多种形式。

方程(6.11.4)是以下方程的第 i 个分量 du/dt = ∂u/∂t + (u·∇)u = f - (1/ρ)∇p + (λ' + ν)∇(∇·u) + ν∇²u，(6.11.5)

其中 ν = μ/ρ，λ' = λ/ρ。ν 被称为运动粘度，若采用斯托克斯关系则有 λ' + 2ν = 0。对于不可压缩流体，我们有 du/dt = f - (1/ρ)∇p + ν∇²u，(6.11.6)

对于不可压缩无粘或理想流体，令 ν = 0 方程即化简。利用恒等式 ∇(∇·u) = ∇×(∇×u) + ∇²u， （参考练习 3.24.5）最后一项有时被改写为 du/dt = f - (1/ρ)∇p + (λ' + 2ν)∇(∇·u) - ν∇×(∇×u)，(6.11.8)

或在不可压缩情况下 du/dt = f - (∇p)/ρ - ν curl ω。(6.11.9)

这揭示了粘度与涡量之间的联系，因为我们看到，对于无旋流动 (ω = 0)，粘性项从方程(6.11.9)中消失，它简化为理想流体的方程。

静力学方程也是一个非常特殊的例子，通过令 u = 0 可得 ρ f = ∇p。(6.11.10)

练习 6.11.1. 证明对于不可压缩流体 d/dt (ρu) = ρf + ∇·(ρuu) - ∇·(μ∇u)。

练习 6.11.2. 如果 f 是无旋的且 p 仅为 ρ 的函数，证明 du/dt = -∇[Ω + P(ρ) - (λ' + 2ν)(∇·u)] - ν∇×ω， 其中 f = -∇Ω 且 P(ρ) = ∫ dp/ρ。

P(ρ) 是应变能。

练习 6.11.3. 如果流动是定常的（即 ∂u/∂t = 0）且 f 和 p 如上题所述，证明 ∇[(1/2)u² + R + P(ρ) + (λ' + 2ν)(u·∇ ln ρ)] = ω×ω - ν∇×ω， 其中 u² = u·u。

练习 6.11.4. 证明对于不可压缩牛顿流体的二维流动，涡量满足扩散方程 dω/dt = ν∇²ω。

对于三维流动获得一个类似的方程。

6.12. 边界条件在通常情况下，假设粘性流体附着在边界上。因此，如果边界以已知速度运动，则流体速度被指定，在静止边界上 u = 0。纳维-斯托克斯方程解的存在性是一个非常深奥的主题，对此我们所知相对较少，一些基本结果现在才刚刚获得。

对于无粘流体，边界上可能有切向速度，但法向速度被指定。高空大气表现出滑移流动，尽管它不应被视为理想流体。斯托克斯本构方程中的高阶项可能变得重要，并且存在其他效应。对于这种状态的流体，已经创造了“麦克斯韦流体”这个名称。

在许多问题中，应力可能在已知或未知边界上被指定。在后一种情况下，我们有一个自由边界问题，其解需要我们找到边界的形式。

练习 6.12.1. 证明对于不可压缩无旋流动，可以找到一个势函数 Ω 使得 u = ∇Ω。推断通过指定封闭边界上的法向速度所给出的流动是唯一的。

6.13. 雷诺数从纳维-斯托克斯方程中出现了一个重要的无量纲数，称为雷诺数。展示这一点的技术是使方程无量纲化。这以最清晰的形式展示了方程所依据的物理原理，因为它们现在摆脱了单位的任意选择。假设流动由某个特征长度 L、速度 U 和密度 ρ₀ 表征。例如，如果我们考虑绕障碍物的定常流动，L 可能是其直径，U 和 ρ₀ 是远离障碍物处的速度和密度。我们可以通过代入 u = U u', x = L x', t = L/U t', ρ = ρ₀ ρ', p = ρ₀ U² p', f = U²/L f' (6.13.1)

使变量无量纲化。

然后，例如， ∂u_i/∂t 成为 U²/L ∂u'_i/∂t'， -∂p/∂x_i 成为 -ρ₀ U²/L ∂p'/∂x'_i，等等。

将这些代入方程(6.11.4)，为简化起见使用斯托克斯关系 λ' + 2ν = 0，我们有 ∂u'_i/∂t' + u'_j ∂u'_i/∂x'_j = -∂p'/∂x'_i + 1/R ∂/∂x'_j (∂u'_i/∂x'_j + ∂u'_j/∂x'_i) + ∂²u'_i/∂x'_j²。(6.13.2)

如果 ∇' 表示无量纲空间变量中的梯度算子，我们可以将其写成 du'/dt' = -∇'p' + 1/R ∇'(∇'·u') + ∇'²u'，(6.13.3)

其中 R = UL/ν。(6.13.4)

R 是一个无量纲数，称为雷诺数，它显然是粘性项重要性的一个度量。因此，如果 R 非常大，忽略方程(6.13.3)右边的项可能是允许的，这时它就简化为理想流体的方程。然而，重要的是要注意，当 R 非常大时方程的性质与 (1/R) = 0 的情况有根本不同。只要 R 是有限的，方程(6.13.3)就是二阶偏微分方程，但当右边设为零时，我们得到一阶方程。

如果我们考虑无体积力的定常不可压缩流动，运动方程可以写为 (ρ u_i u_j),_j - (μ (u_i,j + u_j,i)),_j = 0 或 (6.13.5)

[R (u_i,j u_j + u_i u_j,j) - (u_i,jj + u_j,ii)] = 0。

由此可得 R (u_i u_j + p' δ_ij) - (u_i,j + u_j,i)

沿流线为常数。由于这个原因，雷诺数有时被称为粘性应力与惯性应力之比。然而，必须构建特定的流动系统，这个概念才具有实际意义。

练习 6.13.1. 不可压缩流体充满平面 x₁=0 和 x₁=L 之间的空间，上平面以速度 u₁=U 运动，从而发展出定常流动。证明雷诺数 UL/ν 与 (a) 移动上平面所消耗的单位面积功率与流体中穿过流动的平均动能通量单位面积之比，(b) 任何平面 x₁=常数上的剪应力与该平面上的动量通量之比有关。找出这些关系。

练习 6.13.2. 对于通过圆管的定常流动，找出类似的关系。

练习 6.13.3. 证明对于起源于 u₁=U, u₂=u₃=0 区域的定常不可压缩流动，有 u_i u_i = U², e_ij e_ij = 2 (i≠j)。

6.14. 由粘性力引起的能量耗散法向为 n 的面元上应力在速度方向的分量为 (u_i/u) τ_ij n_j。该应力做功的速率是该应力分量乘以 u dS，因此对于封闭表面 S 的总功率是 ∬ u_i τ_ij n_j dS。

然而，根据应力中值定理（见练习 5.12.2），这是重新整理我们得到用文字表述，这意味着一个物质体积动能的变化率是三个部分之和： (i) 体积力做功的速率， (ii) 内应力做功的速率， (iii) 表面应力做功的速率。

由于 τ_ij 是对称的，第二项可以写为 -τ_ij u_{i,j} = [-p δ_ij + λθ δ_ij + 2μ e_ij] u_{i,j} = -p θ + λθ² + 2μ (e_ij e_ij - 2Φ) (6.14.2)

其中 Φ 是变形张量的第二不变量。因此，由于内应力导致的单位体积动能变化率应分为两部分： (i) 与应变能的可逆交换，-p θ = -(p/ρ)(dρ/dt)， (ii) 粘性力耗散， -[(λ + 2μ)θ² - 4μΦ] (6.14.3)

由于 e_ij e_ij - 2Φ 总是正的，最后一项总是耗散性的。如果使用斯托克斯关系，此项是 -2μ[θ² - 2Φ]；(6.14.4)

对于不可压缩流动，它是 4μΦ。(6.14.5)

如果 τ 不对称，我们可以写 τ = τ_a + τ_s 其中 τ_a = 1/2(τ - τ^T)

τ_s = 1/2(τ + τ^T)。

对于 u_{i,j}，我们已经有一个分解为对称和反对称部分，因此 τ_ij u_{i,j} = (τ^a_ij + τ^s_ij)(e_ij + Ω_ij) = τ^s_ij e_ij + τ^a_ij Ω_ij， 因为其他乘积恒等于零。现在其中其中 T_k 是 T 的第 k 个分量，T 是应力张量反对称部分的矢量。因此 τ_ij Ω_ij = -T_k ε_{ijk} u_k = -u·T。

因此应力张量的反对称部分对涡量做功，就像对称部分对变形做功一样。我们在此不再进一步探讨这些考虑。

* 方程(6.14.3)有时写作 -Φ，其中 Φ 被称为耗散函数。我们为第二不变量保留了符号 Φ，然而对于不可压缩流动，它与耗散函数成正比。T 是后来用于表示方程(6.14.3)的负值的符号。

练习 6.14.1. 考虑练习 6.13.1 和 2 中情况的能量耗散。

练习 6.14.2. 写出平面流动 (v₃=0) 中能量耗散的表达式。

练习 6.14.3. 证明流动 u = (0, 2a² x₁/(x₁² + x₂² + a²)^2, 0)

的单位体积能量耗散是 4μ a⁴ [4 x₁² x₂²]/(x₁² + x₂² + a²)^4， 其中 a² = 2νU。

练习 6.14.4. 对于在固定静止边界内运动且无体积力的不可压缩牛顿流体，证明总动能耗散率是 ∬ 2μ e_ij e_ij dV。

6.2. 斯托克斯流体的方程对于斯托克斯流体，将本构方程代入柯西运动方程将产生一组复杂得多的方程。从方程(5.22.6)我们有 τ_ij,j = (-P α_{i,j} + β_{r,i} ε_{r,j}) ,_j + ...

e_{ij} = α e_{ij} + β e_{ik} e_{kj} + γ e_{ik} e_{kl} e_{lj}.

(6.2.1)

The coefficients α, β, and γ are functions of the invariants I₁, I₂, and I₃ and so, for example, It is not surprising that with equations of this appalling complexity few solutions have been found and that for the special circumstances in which solutions can be obtained, it is best to work more immediately with the stresses themselves.

One point may be worth remarking in connection with the energy dissipation. For the Stokesian fluid we have T_{ij} v_{i,j} = (-p δ_{ij} + α e_{ij} + β e_{ik} e_{kj} + γ e_{ik} e_{kl} e_{lj}) v_{i,j} of which the first two terms are familiar. To calculate the third we observe that e_{ik} e_{kl} e_{lj} is a scalar (in fact the trace of the cube of the symmetric tensor e_{ij}) and so can be evaluated in any coordinate system. In particular, the principal axes form a suitable one for here e_{ik} e_{kl} e_{lj} = λ_i λ_i λ_i.

However, which gives this term in the dissipation function in terms of the invariants of deformation.

Exercise 6.2.1. A first step away from the Newtonian fluid would a quadratic dependence of the form α = μ₀ + μ₁ I₁ + μ₂ I₁², β = λ₀ + λ₁ I₁, γ = 4ν.

(Notation of Serrin, loc. cit. p. 235). Show that the dissipation term is (4ν + 2λ₁ + μ₂) I₃ - (12ν + 4λ₁ - μ₁) I₂ I₁ + 12ν I₂² (2μ₂ + λ₁) I₂ I₁² - 4μ₁ I₁³ or 4(3ν I₂ - μ₁ I₁) in the incompressible case.

Exercise 6.2.2. The name homogeneous Nth power fluid might be applied to the case where α, β, and γ are polynomials in I₁, I₂, and I₃ of weight N, N - 1, and N - 2, respectively. By weight we mean that each term of α is of the form μ_{pqr} I₁^p I₂^q I₃^r and p + 2q + 3r = N. Show that the dissipation term is a polynomial of weight N + 1.

Exercise 6.2.3. Consider the dissipation of energy by viscous forces in the situations of Exs. 5.22.3 and 4.

6.3. The energy equation We shall attempt no sophisticated formulation of the thermodynamics of flow since it brings out comparatively little of the peculiar virtues of tensor analysis. However, we cannot pass by the formulation of the energy equation entirely since up to this point we have rather more unknowns than equations.

In fact we have one continuity equation (involving the density and three velocity components), three equations of motion (involving in addition the pressure and another thermodynamic variable, say the temperature) giving four equations in six unknowns. We have also an equation of state, which in incompressible flow asserts that ρ is constant reducing the number of unknowns to five. In the compressible case it is a relation P = f(ρ, T), (6.3.1)

which increases the number of equations to five. In either case, there remains a gap of one equation which is filled by the energy equation.

The equations of continuity and motion were derived respectively from principles of conservation of mass and momentum. We now assert the first law of thermodynamics in the form that the increase of total energy (we shall consider only kinetic and internal energies) in a material volume is the sum of the heat transferred and the work done on the volume. Let q denote the heat flux vector, then, since n is the outward normal to the surface, -q·n is the heat flux into the volume. Let E denote the specific internal energy, then the balance expressed by the first law of thermodynamics is This may be simplified by subtracting from it the expression we already have in Eq. (6.14.1) for the rate of change of the kinetic energy. Doing this and using the transport theorem (4.3.4) and Green's theorem ∫_V [ρ dE/dt - τ : (∇v) ] dV = 0 where τ : (∇v) is the dyadic notation for τ_{ij} v_{i,j}, the dissipation of energy by internal stress and the reversible interchange with strain energy. Assuming the continuity of the integrand ρ dE/dt = τ : (∇v). (6.3.3)

If we assume Fourier's law for the conduction of heat q = -k ∇T (6.3.4)

is related to the gradient of temperature T. For a Stokesian fluid we can write τ : (∇v) = -p(∇·v) + Φ, (6.3.5)

where Φ is the viscous dissipation, which for a Newtonian fluid is Φ = (λ + 2μ) Θ² - 4μ a. (6.3.6)

Substituting back into Eq. (6.3.3) we have ρ dE/dt = ∇·(k∇T) - p(∇·v) + Φ. (6.3.7)

Physically we see that the internal energy increases with the influx of heat, the compression and the viscous dissipation.

If we write the equation in the form ρ dE/dt - p d(1/ρ)/dt = ∇·(k∇T) + Φ, (6.3.8)

the left-hand side can be transformed by one of the fundamental thermodynamic identities. For if S is the specific entropy, T dS = dE + p d(1/ρ)

= dE - (p/ρ²) dp, so that Eq. (6.3.8) is ρ T dS/dt = ∇·(k∇T) + Φ, (6.3.9)

giving an equation for the rate of change of entropy. Dividing through Eq. (6.3.9) by T and integrating over a volume gives Now the first integral is the heat transferred into the material volume divided by the temperature at which it is transferred, that is, The second law of thermodynamics insists that the rate of increase of entropy should not be less than this transfer, and we see that Eq. (6.3.10) is quite consistent with this for the second term on the right-hand side cannot be negative. Indeed it can only be zero if k or ∇T and Φ are zero. For a perfect fluid with no conductivity or viscosity we see that entropy is conserved, for Eq. (6.3.9) becomes dS/dt = 0. (6.3.11)

Exercise 6.3.1. If H is the specific enthalpy*, show that ρ dH/dt = ∇·(k∇T) + dP/dt + Φ.

Exercise 6.3.2. If the specific heats c_v and c_p and the conductivity k of the fluid are constant and it obeys the ideal gas law p = ρRT, show that ρ c_v dT/dt = k∇²T - p(∇·v) T and Exercise 6.3.3. Without assuming Fourier's law, show that the second law of thermodynamics will be satisfied if T > 0 and q·∇T < 0 and interpret this physically.

Exercise 6.3.4. Modify the energy equation to account for internal sources of heat.

6.41. Résumé of the development of the equations We have now obtained a sufficient number of equations to match the number of unknown quantities in the flow of a fluid. This does not of course mean that we can solve them nor even that the solutions exist, but it is certainly a necessary beginning. It will be well to review, at this point, the principles that have been used and the assumptions that have been made.

The foundation of the study of fluid motion lies in kinematics, the analysis of motion and deformation without reference to the forces that are brought into play. To this is added the concept of mass and the principle of the conservation of mass, which leads immediately to the equation of continuity, dρ/dt + ρ(∇·v) = 0. (6.41.1)

An analysis of the nature of stress allows us to set up a stress tensor, which together with the principle of conservation of linear momentum gives the equations of motion ρ dv/dt = ρf + ∇·T. (6.41.2)

If the conservation of moment of momentum is assumed, it follows that the stress tensor is symmetric, but it is equally permissible to hypothesize the symmetry of the stress tensor and deduce the conservation of moment of momentum. For a certain class of fluids however (here called polar fluids) the stress tensor is not symmetric and there may be an internal angular momentum as well as the external moment of momentum. These may be exchanged subject to the conservation of the total angular momentum.

As yet nothing has been said as to the constitution of the fluid and certain assumptions have to be made as to its behavior. In particular we have noticed the hypotheses of Stokes that lead to the constitutive equation T_{ij} = (-p δ_{ij} + α e_{ij} + β e_{ik} e_{kj} + γ e_{ik} e_{kl} e_{lj}). (6.41.3)

The coefficients in this equation are functions only of the invariants of the deformation tensor and of the thermodynamic state. The latter may be specified by two thermodynamic variables and the nature of the fluid is involved in the equation of state, of which one form is P = f(ρ, T). (6.41.4)

Finally, the principle of the conservation of energy is used to give an energy equation. In this, certain assumptions have to be made as to the energy transfer and we have only considered the conduction of heat, giving ρ dE/dt = ∇·(k∇T) - p(∇·v) + Φ. (6.41.5)

These equations are both too general and too special. They are too general in the sense that they have to be simplified still further before any large body of results can emerge. They are too special in the sense that we have made some rather restrictive assumptions on the way, excluding for example elastic and electromagnetic effects. We shall broaden our view in a later chapter to consider a reacting mixture, but more than this is beyond our present scope. Rather we will consider some of the specializations of the equations and a few results that exhibit the value of vector and tensor analysis.

6.42. Special cases of the equations The full equations may be specialized in several ways, of which we shall consider the following: (i) restrictions on the type of motion, (ii) specializations of the equations of motion, (iii) specializations of the constitutive equation or equation of state.

This classification is not the only one and the classes will be seen to overlap.

We shall give a selection of examples and of the resulting equations, but the list is by no means exhaustive.

Under the first heading we have any of the specializations of the velocity as a vector field. These are essentially kinematic restrictions. We have already met several of these and the following selection is not exhaustive.

(ia) Isochoric motion. The velocity field is solenoidal ∇·v = 0. (6.42.1)

The equation of continuity now gives dρ/dt = 0, (6.42.2)

that is, the density does not change following the motion. This does not mean that it is uniform, though, if the fluid is incompressible so that ρ = constant, the motion is isochoric. The other equations simplify in this case for we have α, β, and γ functions of only I₂ and I₃, in particular for a Newtonian fluid T_{ij} = -p δ_{ij} + 2μ e_{ij}. (6.42.3)

The energy equation is r, pT=V-(kVT)+ (6.42.4)

and for a Newtonian fluid = - 4 p ~ . (6.42.5)

(ib) Irrotational motion. The velocity field is irrotational W=vAV=o. (6.42.6)

It follows that there exists a velocity potential dx, t) from which the velocity can be derived as v = vq, (6.42.7)

and in place of the three components we seek only one scalar function. The continuity equation becomes !f pv2q = 0 (6.42.8)

dt so that for an isochoric motion or an incompressible fluid, p is a potential function, satisfying v29, = 0. (6.42.9)

The Navier-Stokes equations become + + + V R ;(vq)2] = f - -1 vp (A' 2v )V(V2q). (6.42.10)

In the case of an irrotational body force f = - VSt and when p is a function only of p, this has an immediate first integral since every term is a gradient.

Thus, if P(p) = $dp/p, + + + -1i (Vq)' St P(p) - (A' 2v)V2p = g(t) (6.42.11)

at is a function of time only.

(ic) Complex lamellar motions, Beltrami motions, etc. These names can be applied when the velocity field is of this type. Various simplifications are possible by expressing the velocity in terms of scalar fields. We shall not discuss them further here.

(id) Plane flow. Here the motion is restricted to two dimensions which may be taken to be the 012 plane. Then 0, = 0 and x3 does not occur in the equations. If the fluid is incompressible, (6.42.12)

so that we may introduce a stream function w(xl, xz) such that, (6.42.13)

The vorticity has only a single component, that in the 03 direction, which we may write without sumx - -q).

w=- aax02l 2 a 1 x 2 = (6.42.14)

For an incompressible, irrotational motion we therefore have which are the Cauchy-Riemann relations and show that o = 9, iy is an analytic function of z = x1 ix2. The whole resources of the theory of functions of a complex variable are thus available and many solutions are known.

If the fluid is compressible but the flow is steady (that is, no quantity depends on t) the equation of continuity becomes (6.42.16)

A stream function can again be introduced, this time in the form vl=-- 1 aY , v2=---*1 aY (6.42.17)

P 8x2 P 8x1 The vorticity is now given by pw = -V2y (Vy Gp)/p. (6.42.18)

For irrotational, isentropic flow with no body forces this can be developed into an equation for y alone. The velocity of sound c is defined by dpldp and in isentropic flow vp = c2vp.

Since the fluid must be inviscid or entropy would not be conserved Eq.

(6.42.10) can be written vp = -pV(lv2). (6.42.19)

Also we have identically V[&(Vy)2]= V()p2v2) = pv*vp p2V(+v2)

= p(v2 c3Vp (6.42.20)

by the last two equations. Substituting for Vp in Eq. (6.42.18) with w = 0, and expanding p2c2 - (akx, )' 1ax3: = 0. (6.42.21)

This is a partial differentiale quation for w, more complicated than Laplace's but still amenable to analysis.

(ie) Axisymmetric flows. Here the flow is a function only of a coordi- nate along one axis, say t = x,, and the distance from it w = (g + x:)~/*.

If u and u denote the velocity components in the w and z directions the continuity equation is ,ap + a a -((p..u) +-(PO) = 0- (6.42.22)

at am aZ For steady flow a stream function can be introduced as in the case of plane flow and similar but more complicated equations follow.

Under the second type of restriction where simplifications are introduced into the equations of motion, we may mention the following: (iia) Steady flow. Examples of this have already been given and indeed it might have been considered as a restriction of the first class. All partial derivatives with respect to time vanish and the material derivative -d = V.V.

dt In particular, the continuity equation is (pv) = 0 (6.42.23)

so that the mass flux field is solenoidal.

(iib) Hydrostatics. This is the ultimate in steady flows when v itself is set equal to zero, then pf = vp. (6.42.24)

(iic) Creeping flow. It is sometimes justifiable to assume that the velocity is so small that the square of the velocity is negligible by comparison with the velocity itself. This linearizes the equations and allows them to be solved more readily. For example, the Navier-Stokes equations become - av = f - -1 vp + (I' + Y)V(V v) + YV2V. (6.42.25)

at In particular, for a steady incompressible flow with no body forces vp = pv2v. (6.42.26)

However, since the continuity equation is F v = 0, we have vzp = 0 (6.42.27)

or p is a potential function. This is the starting point for Stokes' solution of the creeping flow about a sphere and for its various improvements.

Another specialization of this type arises in stability theory when the basic flow is known but is perturbed by a small amount. Here it is the squares and products of the small perturbations that are regarded as negligible.

(iid) Boundary layers. A circumstance that arises when large gradients of velocity are confined to the neighborhood of a boundary has attracted considerable attention. Here it proves possible to neglect certain terms in the I F * = u ( ~ , equations of motion by comparison with others. The basic case of steady in- compressible flow in two dimensions will be outlined. If a rigid barrier extends along the positive 01 axis the velocity components rl and u2 are both 0 zero there. In the region distant from the Fig. 6.1 axis the flow is rl = U(x,), = 0, and it2 the velocity distribution may be expected to be of the form shown in Fig. 6.1, in which L', differs from CJ and z72 from zero only within a comparatively short distance of the plate. To express this we suppose that L is a typical dimension along the plate and 6 a typical dimension of this boundary layer and that Vl and V2 are typical velocities of the order of magnitude of c1 and c2. We then introduce dimensionless variables which will be of the order of unity. This in effect is a stretching upward of the coordinates so that we can compare orders of magnitude, for now all dimensionless quantities will be of order of magnitude one. It is assumed that 6 L, but the circumstances under which this is valid will only become apparent later. It is also assumed that the functions are reasonably smooth and no vast variations of gradient occur.

The equation of continuity becomes (6.42.29)

which would lose its meaning if one of these terms were completely negligible in comparison with the other. It follows that v2 = 0 (v,;), (6.42.30)

where the symbol 0 means "is of the order of." The Navier-Stokes equations become and v v au V; aU lap 2 (6 - , - a2 u +a$j '.u-+-u-= ---+v111 ax ay pay L 6 62 cax2 In the first of these equations the last term on the right-hand side dominates the Laplacian and a2u/ax2c an be neglected. Dividing through by V:/Lw e see that the other terms will be of the same order of magnitude provided p = O(pV:) and -Lv -- O(1). (6.42.31)

62 v, Inserting these orders of magnitude in the second equation the dominant term is ap/ay so that p is a function of x only. Returning to the original variables we have the equations (6.42.32)

The circumstances under which these simplified equations are valid are given by the second term of Eq. (6.42.31), which can be written (6.42.33)

Since it has been assumed that 6 L this equation shows that this will be the case if v VIL.

Certain of the specializations of the third class have turned up already in the previous cases. We mention here a few important cases.

(iiia) Incompressible fluid. The motion of an incompressible fluid is always isochoric and the considerations of (ia) apply. It should be remembered that for an incompressible medium the pressure is not defined thermodynamically, but is an independent variable of the motion.

(iiib) Perfect fluid. A perfect fluid has no viscosity so that T .= -p6.

11 If and dv + p - = pf -vp (6.42.34)

dt If, in addition, the fluid has zero conductivity the energy equation becomes -dS- -0 (6.42.35)

dt and the flow is isentropic.

(iiic) Ideal gas. An ideal gas is a perfect fluid with the equation of state p = pRT. (6.42.36)

The entropy of an ideal gas is given by s - = scv-d T Rlnp (6.42.37)

which for constant specific heats gives p = es/ccpy, Y = CPlC,. (6.42.38)

(iiid) Piezotropic fluid and barotropic flow. When the pressure and density are directly related, the fluid is said to be piezotropic. If the motion is such that the density and pressure are directly related (for example, for an isen- tropic flow Eq. (6.42.38) givesp = kp‘) the motion is called barotropic. Thus all piezotropic fluids (and this includes incompressible fluids as a special case)

flow barotropically, but other fluids may also do so. The terms piezotropic and barotropic thus stand in the same relationship as incompressible and isochoric. The simple relation between p and p allows us to write I”* 1 v -vp = VP(p) = (6.42.39)

## P - P

and such relations as we have noticed above in Eq. (6.42.1 1) can be obtained from the equations of motion. We shall have occasion to notice these in more detail in the next section.

(iiie) Newtonian fluids. Here the assumption of a linear relation between stress and strain leads to the constitutive equation + + Tjj= (-p AO)6, 2pe,. (6.42.40)

The equations of motion then become the Navier-Stokes equations (6.1 1.5)

or (6.1 1.6).

Exercise 6.42.1. Show that for an incompressible, irrotational flow with velocity potential q, the dissipation function for a Newtonian fluid is = v2(vq)2 = 5 ~ 4 ~ 2 .

Exercise 6.42.2. Obtain an equation similar to Eq. (6.42.21) for the velocity potential of a plane, irrotational, isentropic flow. Show that both can be written (c2 - u;) a - 29, - 2u,u2 -a2v + (c2 - 022 ) 2 a-2P = 0.

ax; ax, ax, 8x2 Exercise 6.42.3. Transform the Navier-Stokes equations in the axisymmetric case (ie).

Exercise 6.42.4. Show that for axisymmetric flow the vorticity where u=- 1 9 u=--- 1 aY, am P am Exercise 6.42.5. The plane parallel 流动 v₁ = u(x), v₂ = 0, p = P(x₁, x₂) 的不可压缩流体满足纳维-斯托克斯方程。它受到一个小扰动，使得 u₁ = u + u₁', v₁ = v₁', p = P + p'。

忽略扰动量的平方和乘积，可证明它们满足方程 ∂v₁'/∂t + u ∂v₁'/∂x₁ + ...

6.51. 伯努利定理考虑具有无旋体力的完美流体的定常正压流动，并设 f = -∇R, P(p) = dp/ρ. (6.51.1)

则运动方程为 (v·∇)v = -∇(R + P(p))

并利用恒等式 (v·∇)v = ∇(½v²) + ω×v, 可写成 ∇(H + P(p) + ½v²) = ω×v. (6.51.2)

令 H 表示该方程左侧梯度的函数。∇H 是一个垂直于 H 等值面的矢量。

然而，ω×v 是一个垂直于 v 和 ω 的矢量，因此这些矢量与该曲面相切。但 v 和 ω 分别与流线和涡线相切，因此它们必须位于一个 H 的等值面上。

由此可知，H 沿流线和涡线是常数。与该流线和涡线网格相交的 H 的等值面被称为兰姆曲面，如图 6.2 所示。

如果流动是无旋的，则 ω = 0，因此能量函数 H = R + P(p) + ½v² (6.51.3)

处处为常数。这代表运动方程的一个完全积分，是一个相当重要的结果。然而，一般情况下，我们只能指出，对于定常正压流动，H 沿任意流线（或者不那么重要地，沿任意涡线）是常数。

该定理（被称为伯努利定理）还有其他形式，可针对不同流动推导。例如，对于非定常无旋流动，可以引入一个时间相关的速度势 φ(x, t)，使得 v = ∇φ。则 ∂H/∂t = f(t) (6.51.4)

只是一个时间的函数。另一种形式在上文方程 (6.42.11) 中给出，适用于牛顿流体的无旋运动。它可以写为 ∂H/∂t + (μ∇² + 2ν)∇²φ = g(t). (6.51.5)

还有其他条件导致此类定理。Serrin (Handbuch der Physik VIII/1, p. 153) 指出，如果涡量而不是流动是定常的，则会得到类似的结果。Bird (Chem. Engng. Sci. 6, (1957), 123.) 得到了他称之为“工程伯努利方程”的、用于存在做功和摩擦损失过程的流动方程。

6.52. 正压流动的进一步性质我们已经看到了涡量的一些一般性质，这些性质源于涡量场是无源场这一事实。例如，涡管的强度恒定以及涡线是物质线，这在前文已经提及。对于定常正压流动，我们还有一个由开尔文证明的定理，该定理表明围绕任意物质闭曲线的环量是常数。因为第二项恒等于零，因为它是绕闭曲线的 ∇v₂ 的积分。对于完美流体的正压流动，f = ∇H，因此 f·dx = dH，并且绕闭回路的积分也必须为零。因此环量保持不变。

如果每个质点都来自一个静止区域，则定常正压流动是无旋的，因为在静止区域中 H = 0，因此对于整个质点路径有 ω×v = 0。然而，这意味着 ω = kv，其中 k 是一个标量变量，并且由于 ∇·ω = 0，有 ∇·(kv) = ρv·∇(k/ρ) = 0，因此 k/ρ 沿流线是常数。然而，如果对于在无穷远处 v = 0 的流线，ω/ρv 是常数，那么在那里 ω = 0，并且由于涡线是物质线，整个流动必须是无旋的。

参考文献 6.12. 关于纳维-斯托克斯方程解的存在性问题，请参考： Serrin, J., Mathematical principles of classical fluid mechanics, in Handbuch der Physik VIII/1, 1959, p. 252.

麦克斯韦流体的讨论见： Truesdell, C., J. Rat. Mech. and Anal. I, (1952), p. 245 et seq.

6.13. 热力学严格发展的要素可以在吉布斯的著作中找到。然而，直到最近，理性流体力学所需的热力学才被建立在一个相当完整和严格的基础上。参见： Noll, W. and Coleman, B. D. On the thermostatics of continuous media. Archiv. for Rational Mechanics 4, (1959), p. 97-128.

## 第7章 张量

7.11. 坐标系与约定让我们暂时回到将一点 P 的笛卡尔坐标写为 (x, y, z) 的方式，并考虑另外两个熟悉的坐标系。x, y 和 z 是点 P 到通过原点 O 的三个坐标平面的垂直距离。然而，它们并不是用来确定 P 位置的唯一坐标，因为我们可以保留 z 作为 P 在 Oxy 平面上的投影 Q 的高度，并取任何其他一对坐标来确定 Q 在平面上的位置。特别是，Q 可以由其到原点的距离 ρ 和 OQ 与固定方向（例如 Ox）所成的角度 φ 来确定。这就给出了一个坐标系 (ρ, φ, z)，称为柱面极坐标。它们通过以下方程与笛卡尔坐标相关： x = ρ cosφ, y = ρ sinφ, ρ = (x² + y²)^{1/2}, φ = tan⁻¹(y/x). (7.11.1)

另一种描述是取 P 到原点的距离 r 作为一个坐标。这使 P 位于一个特定半径的球面上。如果取第二个坐标为 θ，即 OP 与 Oz 之间的夹角，这就将 P 限制在球面上的特定纬度上。在这个纬度圆上，P 的位置可以通过再次取 φ 作为坐标来确定。因此 x = r sinθ cosφ, y = r sinθ sinφ, z = r cosθ, 或者 r = (x² + y² + z²)^{1/2}, θ = tan⁻¹((x² + y²)^{1/2}/z), φ = tan⁻¹(y/x). (7.11.2)

这个系统称为球面极坐标系，是曲线坐标系的另一个例子，与直线的笛卡尔坐标系形成对比。这些名称源于仅有一个坐标变化的线的性质。在笛卡尔坐标系中，这些坐标线是直线且平行于坐标轴。在柱面极坐标系中，ρ、φ 和 z 单独变化的线分别是通过 Oρ 轴的射线、平行于 Oxy 平面的圆以及平行于 Oz 轴的直线。在球面极坐标系中，坐标线是通过原点的射线、包含 Oρ 的平面内的圆以及平行于 Oxy 平面的圆。在后两种情况下，并非所有坐标线都是直线。

坐标曲面是只有一个坐标保持常数的曲面。对于笛卡尔坐标，这些都是平面，但对于其他坐标系，我们会遇到圆柱、圆锥和球面作为坐标曲面。现在，这种曲线坐标系具有重要价值，我们需要能够使用它们并从一种转换到另一种。此外，我们希望以这样的方式表示物理实体：当改变坐标系时，我们的描述会以确保实体本身未改变的方式发生变化。到目前为止，我们考虑的变换仅仅是笛卡尔参考系的旋转，但从现在开始，我们需要能够处理更一般的变换。

在描述这些变换的基本特征之前，我们将引入一些新的约定。我们将有机会区分变换下的两种行为类型，并将它们与上标和下标关联起来。当变换仅涉及笛卡尔坐标系的旋转时，不会出现这种区分。将来，我们将用上标坐标书写坐标。因此，xⁱ，i = 1,2,3，将表示 P 在某个系统中的坐标，以代替迄今为止用于笛卡尔系统的 xᵢ。因此，在柱面极坐标中，我们可能有 x¹ = ρ, x² = φ, x³ = z。如果我们转换到另一个系统，将再次使用上划线表示变换后的坐标。例如，如果变换后的系统是球面极坐标：x̄¹ = r, x̄² = θ, x̄³ = φ，并且定义变换的方程为 x̄¹ = [(x¹)² + (x²)²]^{1/2}, x̄² = tan⁻¹(x³/x¹), x̄³ = x². (7.11.3)

求和约定也将修改如下： 求和约定：在项的乘积中，任何在上标位置重复一次并在下标位置重复一次的索引被称为哑索引，并被认为在其值的范围内求和。在三维空间中，我们将使用拉丁字母作为索引，因此其范围将是 1,2,3。任何未重复的索引称为自由索引，可以取其范围内的任何值。

在使用张量时，有一种非常方便的检查偶然错误的方法，可以称为索引守恒。任何出现的自由索引必须在方程的每一项中以相同位置出现。因此，公式 Aⁱⱼₖ = Bⁱⱼ Cₖˡᵐ Dₘ Eₙˡ Fₙᵏ + Gₙᵖ 将是明显错误的，因为在右侧的第一项中，i 在错误的位置且 k 没有出现；然而第二项是一致的。当然，用于哑索引的字母可以随意更改，但它不能与自由索引相同，以免造成严重混淆。分母中的上标在分子中算作下标，反之亦然。因此，如果我们需要一个表示 ∂/∂xⁱ 的符号，我们会写成 Dᵢ = ∂/∂xⁱ，其索引在下标位置。

练习 7.11.1. 描述以下坐标系的坐标线和坐标面（x, y, z 是笛卡尔坐标）： (i) x¹ = x + y, x² = x - y, x³ = z, (ii) x = (x¹)² - (x²)², y = 2x¹x², z = x³, (iii) x¹ = x²y, x² = x¹x²(1 - (x³)²)^{1/2}, x³ = (x¹)² - (x²)², (iv) x = x³[(x¹)² + (x²)²]{1 - (x²)²}]^{1/2}, y = [(x¹)² + (x²)²]{1 - (x²)²}(1 - (x³)²)]^{1/2}, z = x¹x².

(v) x(x¹ - x²) = ux³((x¹)² - 1)^{1/2} y(x¹ - x²) = u[((x¹)² - 1)(1 - (x³)²)]^{1/2} z(x¹ - x²) = u{ 1 - (x²)²}^{1/2} 7.12. 真实变换 We wish to define the class of transformations that we shall regard as proper or admissible. A transformation of coordinates is not of much value if we cannot get back to the original coordinates by inverting the transformation. For example, the transformation from cylindrical to spherical polars is given above by Eq. (7.11.3), but the inverse transformation is ξ¹ = r sin θ, ξ² = φ, ξ³ = cos θ. (7.12.1)

Both sets of equations are perfectly definite except at the origin where x¹ = x³ = ξ¹ = 0 and the value of the other coordinates is immaterial. It is shown in Appendix B that the transformation yᵢ = fᵢ(x₁, x₂, . . . ,x n), i = 1, . . . ,n, can always be inverted in the neighborhood of a point to give xᵢ = gᵢ(y₁, y₂, . . . ,y n), i = 1, . . . ,n, provided that the Jacobian exists and does not vanish. Translating this into our coordinate notation we see that the transformation ξⁱ = ξⁱ(x¹, x², x³) (7.12.2)

can be inverted to give xʲ = xʲ(ξ¹, ξ², ξ³) (7.12.3)

provided that the Jacobian (7.12.4)

exists and does not vanish. We have already encountered the geometrical meaning of the Jacobian, namely, the ratio of volume elements in the two coordinate systems. Thus, to say that neither J nor its reciprocal is zero, is to say that no infinitesimal region in one coordinate system is collapsed into a single point in the other.

The set of proper transformations forms a group if we define the product of two transformations as the result of applying them successively. A group has the following properties: (i) the identity transformation I belongs to it, (ii) if T₁ and T₂ are two transformations of the group their product T₂T₁ also belongs to it, (iii) if T is a transformation of the group then its inverse T⁻¹ also belongs to it (TT⁻¹ = I), (iv) the product is associative, T₁(T₂T₃) = (T₁T₂)T₃.

The identity transformation ξⁱ = xⁱ is obviously proper and our definition of propriety has ensured the existence of the inverse (iii). What we need to show is that the product or successive application of two proper transformations is still proper. Let T₁ be the transformation from xⁱ to ξⁱ and T₂ that from ξⁱ to ηⁱ. Then we can write symbolically η = T₁x, η = T₂ξ and by the product T₂T₁ we mean the transformation from x to η, that is, η = T₂T₁x. This product will be proper if the Jacobian |∂η/∂x| is not infinite or zero. However, (7.12.5)

so that the matrix [J] whose typical term is ∂ηⁱ/∂xᵏ is the product of the matrices [J₁] and [J₂] whose typical terms are ∂ξⁱ/∂xʲ and ∂ηⁱ/∂ξᵏ respectively. However, the Jacobians of the two transformations and their product are the determinants of these three matrices and the determinant of the product of two matrices is the product of their determinants (see Appendix A9). It follows that (7.12.6)

and since neither J₁ nor J₂ vanishes or is infinite, their product is neither zero nor infinite and the transformation T₂T₁ is proper.

The idea of a group is a very valuable one. Its importance and the geometry to be associated with it were first brought out by Felix Klein in 1872. A subgroup of the group is formed by a subset of the transformations of a group which themselves enjoy the group property. Thus the identity operation must belong to every subgroup; the inverse of any transformation and the product of any two transformations of the subgroup must also belong to it. For example, the group of transformations given by nonsingular constant matrices Aⁱⱼ is a subgroup of the general group of proper transformations, ξⁱ = Aⁱⱼxʲ. (7.12.7)

It is proper since J = det A is not zero. Hence the inverse exists and is given by a nonsingular constant matrix. Also, the product of any two constant matrices is a constant matrix and thus belongs to the subgroup. This subgroup induces all forms of Cartesian coordinates including those with oblique axes when operating on the ordinary rectangular Cartesian coordinates. It is itself a subgroup of the more general transformation ξⁱ = Aⁱⱼxʲ + bⁱ (7.12.8)

which involves a shift of origin as well as distortion of axes. This last subgroup is called the affine group. It has subgroups such as that given by (7.12.7) with bⁱ = 0 and known as the group of linear homogeneous transformations. This in turn has subgroups of equivoluminar linear homogeneous transformations (for which J = ±1), the group of orthogonal homogeneous transformations (for which A is orthogonal and J = ±1), and the group of rotations (for which A is orthogonal and J = 1). It is this last subgroup which is the only group of transformations considered in constructing Cartesian tensors.

Exercise 7.12.1. If J = |∂ξ/∂x|, show that (Here there is summation on p, q, r and s.)

Exercise 7.12.2. Calculate the Jacobians for the transformation from Cartesian coordinates to those of Ex. 7.11.1, (i)-(v).

7.13. General plan of presentation It will be useful at this point to sketch the development we shall follow. At first we shall just be paralleling the development of Cartesian vector and tensor analysis and making use of the maturity that the reader should now have attained to minimize some of the more fussy details. We shall have to distinguish at the outset two types of behavior under transformation, which in the subgroup of rotations are identical, but until we reach differentiation the analogy with Cartesians is very close. We shall find, however, that a new kind of differentiation has to be introduced to preserve the tensorial character that partial differentiation has hitherto enjoyed.

A distinction will also emerge between the curvature of the coordinate system and the curvature of the space it is being used to describe. Thus the cylindrical and spherical polar coordinates are curvilinear systems but they describe the Euclidean space in which the ordinary Cartesian coordinates can be constructed. Since the space of our gross experience is Euclidean it is rather difficult to imagine a curved three-dimensional space. The distinction can however be seen in two dimensions by comparing the plane and the surface of a sphere. The latter has an intrinsic curvature which actually precludes the setting up of a Cartesian system of coordinates. Strictly speaking, Cartesian tensors suffice for Euclidean space and if we wanted equations in curvilinear coordinates we could transform the equations in Cartesians to obtain them. However, they do have certain manipulative advantages and this redundancy gives another useful pedagogical bridge from the familiar to the abstract.

When we come to consider flow in surfaces, then a full tensorial treatment is quite essential as the space is not Euclidean. To prepare the way for this, Chapter 9 is devoted to the study of surfaces in space.

7.21. Contravariant vectors Since the coordinates are in general curved, we cannot expect any linear transformation between the coordinates themselves. However, differentials of the coordinates dξⁱ and dxʲ are connected by the laws of partial differentiation and (7.21.1)

(The affix j in ∂ξⁱ/∂xʲ is in the upper position of the denominator and so counts as a lower affix.) The coefficients ∂ξⁱ/∂xʲ are generally functions of position, but are calculable from the equations of transformation. Consider, for example, the transformation from Cartesians to cylindrical polars, ξ¹ = {(x¹)² + (x²)²}¹/², ξ² = tan⁻¹(x²/x¹), ξ³ = x³.

Here we have dξ¹ = (x¹ dx¹ + x² dx²) / {(x¹)² + (x²)²}¹/² dξ² = (- x² dx¹ + x¹ dx²) / {(x¹)² + (x²)²}¹/² dξ³ = dx³.

We call this behavior under transformation the behavior of a contravariant vector and, as before, define a contravariant vector to be anything that behaves in this way.

More precisely, we say that ξⁱ are the components of a contravariant vector at a certain point in the coordinate system Ox¹x²x³ if under a transformation of coordinates to Oξ¹ξ²ξ³ the components of the contravariant vector become (7.21.2)

Thus a vector is associated with a given point and the coefficients ∂ξⁱ/∂xʲ must be evaluated there.

As before, we have to establish this behavior on the part of any entity we wish to show to be a contravariant vector. If xⁱ(t) is the coordinate of a moving particle with the time t, then vⁱ = dxⁱ / dt (7.21.3)

is its velocity. In the transformed coordinates the velocity has components v'ⁱ = dξⁱ/dt but clearly, (7.21.4)

so that velocity is a contravariant vector. Similarly, the acceleration and all higher derivatives are contravariant vectors.

7.22. Covariant vectors If f(x¹, x², x³) is a scalar function and we transform it to a function of the variables ξ¹, ξ², ξ³, its derivatives transform according to the equation (7.22.1)

We could consistently write (7.22.2)

for the upper affix j in the denominator is equivalent to an affix in the lower position. Then, since f is a scalar or invariant function, ∂f/∂ξⁱ will be the set of quantities ∂ᵢf. Thus Eq. (7.22.1) is (7.22.3)

and this type of behavior under transformation is the behavior of a covariant vector. More precisely, the quantities ∂ᵢf are components of a covariant vector in the coordinate system Ox¹x²x³ if under transformation of Ox¹x²x³ they transform according to Eq. (7.22.3). These two transformation formulae may be recalled readily if the "conservation of indices" is remembered. The index i is associated with the barred component and so must be associated with ξ. Since the index on a coordinate is always in the upper position, the ξ must be in the denominator and the derivative is ∂xⁱ/∂ξʲ. Considerations of the summation convention lead to the same reassurance.

For the rotation transformation let us write and its inverse Thus, ∂ξⁱ/∂xʲ = δⁱⱼ and ∂xʲ/∂ξⁱ = δⁱⱼ. However, δⁱⱼ and δⁱⱼ are both identical with the δ of Chapter 2 being the angle between Oxⁱ and Oξʲ. Hence Eq. (7.21.2) and (7.22.3) are identical and the distinction between covariance and contravariance does not arise for Cartesian tensors.

Let y = (y¹, y², y³) be the Cartesian coordinates of a point.

and x1, x2, x3 its coordinates in some other system. For fixed i, y' = y'(x1, x2, x3) is a scalar function and so the three quantities ∂y'/∂xj for j = 1,2, and 3 are the components of a covariant vector. For fixed j, g_{ij} = ∂y^k/∂x^i ∂y_k/∂x^j (7.22.4) is a Cartesian vector. The three Cartesian vectors g_{i1}, g_{i2}, g_{i3} are called base vectors in the coordinate system x_j, and they are not coplanar if the transformation from Cartesian coordinates is a proper one. Any Cartesian vector can be expressed in terms of a system of base vectors. Thus (7.22.5) where the u_i are the components of a with respect to this base system. Now for another system of coordinates 9 we would have base vectors Hence, (7.22.6) This shows that the u_i are components of a contravariant vector.

7.23. The metric tensor The reader will already have guessed that the tensor is to be defined by an extension of these transformation properties which is entirely analogous to the way Cartesian tensors were developed. Before going on to the general definition, it is convenient to consider a special tensor of fundamental importance. We shall only be able to introduce it in an informal style and will have to come back later to establish its nature. In Euclidean space a Cartesian system of coordinates can always be erected. Let us denote these by y_i to distinguish them from the general curvilinear coordinates x_i. The distance between two points P and Q with coordinates y_i and y_i dy_i is ds, where ds^2 = dy_k dy_k. (7.23.1) Notice that we cannot use the summation convention here since both affixes are at the same level. However, (7.23.2) hence, ds^2 = g_{ij} dx^i dx^j (7.23.3) where g_{ij} = ∂y^k/∂x^i ∂y_k/∂x^j (7.23.4) g_{ij} is called the metric tensor since it relates distance to the infinitesimal coordinate increments.

For example, with the cylindrical polar coordinates x1 = {(y1)^2 + (y2)^2}^{1/2}, x2 = tan^{-1}(y1/y2), x3 = y3 we have g_{11} = 1, g_{22} = (x1)^2, g_{33} = 1, (7.23.5) and all g_{ij} = 0, i ≠ j. For spherical polars g_{11} = 1, g_{22} = (x1)^2, g_{33} = (x1 sin x2)^2 (7.23.6) and the off-diagonal terms are again zero. When only the diagonal terms are nonzero, the coordinates are called orthogonal (for reasons which will appear later) and it is convenient to write g_{ii} = h_i^2 (7.23.7) where the h_i are called scale factors. The name arises from the fact that if we make an infinitesimal displacement only in the direction of the x_i coordinate then ds = h_i dx^i (no summation) so that h_i represents the ratio of distance to coordinate difference. This may be seen in the simplest case with cylindrical polars in Fig. 7.2, where h1 = h3 = 1, h2 = x1. Reverting to the notation ρ, φ, z we see how this comes about; for x1 = ρ and x3 = z are true distances in space, but x2 = φ is an angle and the corresponding distance is ρ dφ and varies with ρ.

Let g denote the determinant of the matrix whose typical element is g_{ij}. Then g is not zero for it is the square of the Jacobian |∂y/∂x| of the transformation to Cartesian coordinates. If g^{ij} denotes the ijth element of the inverse of matrix of g_{ij}, we have g^{ij}g_{jk} = δ_i^k if i = k but zero otherwise. This is the definition of the Kronecker delta which we will now write with one suffix in the upper and one in the lower position, δ_i^j = 1 if i = j, 0 if i ≠ j. (7.23.8) If the coordinates are orthogonal we observe that g^{ii} = h_i^{-2}, g_{ij} = 0, i ≠ j. The notation suggests associating covariance with g_{ij}, and contravariance with g^{ij}, and regarding g as a scalar. We must now proceed to formal definitions and establish the tensorial character of these entities.

Exercise 7.23.1. Calculate the metric tensors of the coordinate systems given in Ex.

the sign alters, it is said to be antisymmetric with respect to them. The metric tensor \( g_{ij} \) is an example of a symmetric tensor.

Associated tensors. If \( A_i \) is a covariant vector, the contravariant vector \( g^{ij} A_j = A^i \) is called its associated vector. This operation is known as raising the index and its inverse is the lowering of the index by an inner product with \( g_{ij} \), for example, \( B_j = g_{ji} B^i \). A tensor obtained by raising or lowering any index is said to be an associated tensor. Since \( g_{ik} g^{kj} = \delta_i^j \), the original tensor is restored when the index is lowered again. \( g^{ij} \) has been defined as the conjugate tensor, that is, the element of the inverse of the matrix of \( g_{ij} \). If \( A_{ij} \) is a covariant second order tensor, the associated tensor \( A^{pq} = g^{pi} g^{qj} A_{ij} \) is not generally the conjugate tensor. The exception to this is when \( A_{ij} \) is a scalar multiple of \( g_{ij} \), for \( g^{ip} g^{jq} a g_{pq} = a g^{ip} \delta_p^q = a g^{ij} \) (7.31.1)

The conjugate of a second order tensor \( A_{ij} \) can, however, be calculated in the same way as for \( g_{ij} \) and exists provided that the determinant of the \( A_{ij} \) does not vanish.

Exercise 7.31.1. Rephrase the definitions for relative tensors.

Exercise 7.31.2. Establish that the tensor character is preserved under addition, contraction or multiplication.

Exercise 7.31.3. Establish the tensorial character of \( g^{ij} \) from the previous exercise and Eq. (7.24.8).

Exercise 7.31.4. If the coordinates are orthogonal and \( g_{ii} = h_i^2 \), show that the associated vector of \( A^i \) has components \( A_i = h_i^2 A^i \), with no summation on the i.

Exercise 7.31.5. Show that \( \epsilon_{ijk} A^i B^j \) and \( \epsilon_{ijk} A^j B^k \) are associated absolute vectors. They are vector products of \( A \) and \( B \).

Exercise 7.31.6. Show that any tensor can be represented as the sum of outer products of vectors. Take as a typical case \( A^i_j \).

7.32. The quotient rule The quotient rule stands exactly as for Cartesian tensors and is most easily exhibited in a simple case, the generalization being evident. If \( A^{(ijk)} \) is a set of 27 quantities, \( B^k \) a contravariant vector independent of \( A \), and it can be shown that the inner product \( A^{(ijk)} B^k = C^{ij} \), a contravariant second order tensor, then the \( A^{(ijk)} \) are the components of a mixed third order tensor, \( A^{ij}_k \). For \( C^{ij} = A^{(pqr)} B^q \) and subtracting, and since \( B \) is independent of \( A \) this can only be satisfied by the vanishing of the bracket. This is the transformation law for \( A^{ij}_k \). The generalizations can be written down by invoking the conservation of indices. The essential point is that \( B \) should be independent of \( A \). It is not possible to establish the tensorial character of \( g^{ij} \) by invoking the quotient rule on the formula \( g^{ij} \delta_j^k = g^{ik} \).

7.33. Length of a vector and angle between vectors For an infinitesimal contravariant vector with components \( dx^i \) we already have a measure of length; namely, \( ds = \{g_{ij} dx^i dx^j\}^{1/2} \). (7.33.1) Any contravariant vector \( A^i \) can be thought of as a large multiple of an infinitesimal vector \( A^i = M dx^i \). The length of \( A \) may thus be taken to be \( M ds = |A| \), and we write \( |A|^2 = g_{ij} A^i A^j \). Since \( A_j \) is the associated covariant vector \( A_j = g_{ji} A^i \), we can also write \( |A|^2 = g_{ij} A^i A^j = A_j A^j = g^{ij} A_i A_j \). (7.33.2) Thus the lengths of a vector and its associate are the same. If \( |A| = 1 \), we say \( A \) is a unit vector.

For example if \( x^i(s) \) is the equation of a curve and \( s \) is the arc length, then \( \tau^i = dx^i/ds \) is a unit tangent vector to the curve. Any vector may be made a unit vector by dividing by its length. The unit contravariant vector tangent to the \( x^1 \) coordinate line is obtained by making the vector \( A^i = \delta^i_1 \) of unit length. Its length is \( \{g_{ij} \delta^i_1 \delta^j_1\}^{1/2} = g_{11}^{1/2} \), so the unit vector is \( e_{(1)} = g^{1/2}_{11} \delta^i_1 \). (7.33.3) The index 1 is not a tensorial index and so has been enclosed in parentheses. \( e_{(2)} \) and \( e_{(3)} \) are similarly defined. If the coordinates are orthogonal, \( e_{(j)}^i = (g_{jj})^{-1/2} \delta^i_j \), (no sum on j). (7.33.4) The associated unit covariant vectors tangent to the coordinate lines are \( e_{(j)i} = \delta_{ik} e_{(k)}^k = g_{ij} e_{(j)}^j = (g_{jj})^{1/2} \delta_{ij} \) (no sum on j). (7.33.5)

The angle \( \theta \) between two unit vectors \( A^i \) and \( B^j \) is \( \cos \theta = g_{ij} A^i B^j = A_i B^i = g^{ij} A_i B_j \). (7.33.6) To prove this we observe that it is a tensor formula identifying a scalar with the twice contracted product of a tensor and two vectors. It is certainly true in Cartesian coordinates where \( g_{ij} = \delta_{ij} \), and hence is true in any coordinate system for we can transform both sides of the equation and the one is a scalar and so stays the same. If \( A \) and \( B \) are not unit vectors then \( \cos \theta = \frac{g_{ij} A^i B^j}{(g_{ij} A^i A^j)^{1/2} (g_{pq} B^p B^q)^{1/2}} \). (7.33.7)

The angle between the coordinate lines at any point is given by \( \cos \theta_{pq} = g_{ij} e_{(p)}^i e_{(q)}^j = g^{1/2}_{pp} g^{1/2}_{qq} g_{pq} \) (no sum on p or q). (7.33.8) Thus, when \( g_{pq} = 0 \) for \( p \neq q \) the angle between the \( x^p \) and \( x^q \) coordinate lines is a right angle. For this reason, the coordinate system is called orthogonal.

The projection of a vector \( A^i \) on the direction tangent to the \( x^j \) coordinate line is \( |A| \cos \theta \) where \( \theta \) is the angle between \( A^i \) and \( e_{(j)} \); \( A^i e_{(j)i} = g_{ij} A^i (g_{jj})^{1/2} \). (7.33.9) In an orthogonal coordinate system this is \( |A| \cos \theta = h_j A^j \) (no sum on j). (7.33.10)

Exercise 7.33.1. For an orthogonal coordinate system, the angle between two unit vectors is given by \( \cos \theta = \frac{A^1 B^1}{h_1^2} + \frac{A^2 B^2}{h_2^2} + \frac{A^3 B^3}{h_3^2} \).

Exercise 7.33.2. Show that the length projection of \( A^i \) on the direction of \( B^i \) is \( \frac{g_{ij} A^i B^j}{(g_{pq} B^p B^q)^{1/2}} \).

Exercise 7.33.3. Show that if the metric is positive definite (that is, \( ds^2 = g_{ij} dx^i dx^j \) is always positive) then the angle between two vectors is always real.

Exercise 7.33.4. Show that \( \frac{d}{ds} (\cos \theta) = \ldots \).

7.34. Principal directions of a symmetric second order tensor The covariant vector \( A_{ij} L^j \) derived from the covariant tensor \( A_{ij} \) and contravariant vector \( L^j \) will have the same direction as the associated vector \( L_i \), if \( A_{ij} L^j = \lambda L_i = \lambda g_{ij} L^j \). (7.34.1) This set of three simultaneous equations has nontrivial solutions only if \( |A_{ij} - \lambda g_{ij}| = 0 \), (7.34.2) which is a cubic equation for \( \lambda \). Its roots are the latent or characteristic values of the tensor and the associated \( L^i \) are the corresponding characteristic vectors. For a real symmetric tensor, it can be shown that the characteristic values are all real and that characteristic vectors associated with distinct values are orthogonal. It follows that there is a rotation of coordinates that makes the transformed tensor \( A_{ij} \) diagonal. These properties are entirely analogous to the Cartesian case.

Exercise 7.34.1. Show that the characteristic values of a tensor are invariant under transformation.

Exercise 7.34.2. Demonstrate the orthogonality of characteristic vectors of a symmetric tensor for distinct latent roots. Construct the transformation to canonical form.

Exercise 7.34.3. Show that if \( A_i^j = \delta_i^j \), \( A_j^k = g_{jl} A^{kl} \), \( A^{ij} = g^{ik} g^{jl} A_{kl} \), the four tensors have the same characteristic values and associated characteristic vectors.

7.35. Covariant and contravariant base vectors In Section 7.22 we defined a set of Cartesian base vectors \( g_{(i)} = \partial y / \partial x^i \), (7.35.1) where \( y \) is the Cartesian position vector of the point \( x \). \( (i) \) is to be regarded as a label on the Cartesian vector but for any given component of the vector, say \( g_{(i)} \), the first three quantities \( g_{1(i)} \), \( g_{2(i)} \), \( g_{3(i)} \) are components of a covariant vector. We have also shown that if a Cartesian vector is expressed in the form \( a = u^i g_{(i)} \), (7.35.2) then the coefficients \( u^i \) are the components of a contravariant vector. They may be called the contravariant components of the vector \( a \) in the given coordinate system.

The length of \( a \) is given by \( |a|^2 = a \cdot a = (u^i g_{(i)}) \cdot (u^j g_{(j)}) = g_{ij} u^i u^j \). However, if \( u^i \) are the components of a contravariant vector its squared length is \( g_{ij} u^i u^j \). So that \( g_{(i)} \cdot g_{(j)} = g_{ij} \), (7.35.3) which is another way of writing Eq. 7.23.4. The basis vectors are not usually of unit length but a basis of unit vectors tangent to the coordinate lines is given by \( e_{(i)} = g_{(i)} / (g_{ii})^{1/2} \). As we have seen the angle between two coordinate lines is \( \cos \theta_{ij} = g_{ij} / (g_{ii} g_{jj})^{1/2} \).

If \( \Gamma \) denotes the matrix whose \( i \)-th row is the set of components of \( g_{(i)} \), the matrix of the \( g_{ij} \) is \( G = \Gamma \Gamma^T \). Hence, the determinant \( \gamma \) of \( \Gamma \) is related to the determinant \( g \) of the metric tensor by \( g = \gamma^2 \). (7.35.4) Since this does not vanish we can construct the reciprocal basis (cf. Section 2.36), \( g^{(k)} = \frac{1}{\gamma} \epsilon_{ijk} g_{(i)} \times g_{(j)} \), (7.35.5) where \( i, j, k \) is an even permutation of \( 1, 2, 3 \). The reciprocal basis is such that \( g^{(i)} \cdot g_{(j)} = \delta^i_j \). (7.35.6)

Let the components of \( a \) with respect to this reciprocal basis be \( a_i \) and \( a = a_k g^{(k)} \). (7.35.7) Then \( a \cdot g_{(j)} = a_k g^{(k)} \cdot g_{(j)} = a_k \delta^k_j = a_j \), but by Eq. 7.35.2 \( a \cdot g_{(j)} = a^i g_{(i)} \cdot g_{(j)} = a^i g_{ij} \), and comparing these two we see that \( a_j = a^i g_{ij} \). (7.35.8) Thus the covariant components of \( a \) are the components with respect to the reciprocal basis and are also the components of the covariant vector associated with the vector of its contravariant components.

We notice that the matrix whose rows consist of the components of the reciprocal base vectors is \( (\Gamma^{-1})^T \). Thus the matrix with components \( g^{ij} = g^{(i)} \cdot g^{(j)} \) is \( (\Gamma^{-1})^T (\Gamma^{-1}) = (\Gamma \Gamma^T)^{-1} = G^{-1} \). However, this is just the definition of the conjugate metric tensor, which is evidently formed from the reciprocal basis in just the same way as was the metric from the original basis; \( g^{ij} = g^{(i)} \cdot g^{(j)} \). (7.35.9)

With curvilinear coordinates the system of basis vectors will depend on the point under consideration. It is this variability, not present in Cartesian coordinates, that makes the construction of a tensor derivative more complicated than a straightforward partial derivative. Light is also thrown on the absence of distinction between covariance and contravariance in Cartesian systems. The basis there is a set of mutually orthogonal unit vectors, whose reciprocal is identical with itself.

7.41. The physical components of a vector in orthogonal coordinate systems Cartesian coordinates all have the physical dimensions of length but in general we cannot expect this of curvilinear coordinates. For example with cylindrical polars \( x^1 = \rho \), \( x^2 = \phi \), \( x^3 = z \), the first and third have the dimensions of length but the second has no dimensions. Thus the contravariant velocity components \( u^i = dx^i/dt \)

would not all have the same physical dimensions and can hardly be what we understand by the physical components of velocity. The associated covariant vectors are in no better position for though in this case u1 = u^1 and u3 = u^3 have the dimensions of velocity, u^2 = h_2^2 (dx^2/dt) has the dimensions of (length)^2/(time). Actually for this system ds^2 = (dx^1)^2 + (x^1 dx^2)^2 + (dx^3)^2, so that we see that dx^1, x^1 dx^2, and dx^3 all have the physical dimensions of length and dx^1/dt, x^1(dx^2/dt), dx^3/dt would therefore have the dimensions of velocity. For a general orthogonal coordinate system ds^2 = (h_1 A^1)^2 + (h_2 A^2)^2 + (h_3 A^3)^2 (7.41.1) so that the h_i A^i have the same physical dimensions as the magnitude of the vector A, which is evidently given by Pythagoras' theorem. This is the sort of behavior we expect of a physical component.

The unit contravariant vectors tangent to the three coordinate lines are e^(i) = (1/h_i) ∂/∂x^i (no sum on i).

If the contravariant vector A' is represented as a linear combination of these base vectors A' = A^(1) e^(1) + A^(2) e^(2) + A^(3) e^(3), (7.41.2)

comparing the three components on each side we see that A^(1) = h_1 A^1, A^(2) = h_2 A^2, A^(3) = h_3 A^3. (7.41.3)

The A^(i) are called the physical components of the contravariant vector A' and, as Eq. (7.41.1) shows, they all have the same physical dimensions as the magnitude of A.

The physical components of the covariant vector A_i can be constructed in the same way by the representation A_i = A^(1) e^(1)_i + A^(2) e^(2)_i + A^(3) e^(3)_i. (7.40.3)

Since e^(i)_j = δ_{ij} h_i (no sum on i), we have A^(i) = h_i A_i (no sum on i). (7.41.4)

However, A_i = h_i A^i, etc., so that both these sets of formulae define the same physical components.

It is worth remarking that the conservation of indices is a great help in keeping these formulae straight, though there is no summation involved. Thus a parenthetic index has no tensorial significance being merely a label. The lower index to h_i has covariant significance since h_i is an element of a covariant second order tensor, and the upper index A^i is contravariant. In the product h_i A^i these cancel one another out and leave the neutrality of a parenthetic index. The same considerations apply when we write (g_{ii})^{1/2} in place of h_i if we regard the square root as reducing two affixes to one.

The physical components do not of course transform as tensors, but their transformation law can be easily deduced. In a new coordinate system A^(i)' = h_i' A^(i') (no sum on i)

so we have A^(i)' = h_i' (∂x^j/∂x^i') A_j (no sum on i but a single summation on j). (7.41.5)

where there is no sum on i but a single summation on j. Consider the angle θ_{ij} between e^(i) in the new coordinate system and e^(j) in the old. We can only calculate this angle by bringing both unit vectors into the same coordinate system. In the new coordinate system e^(j) becomes (1/h_j) (∂x^j/∂x^i') (∂/∂x^i').

However, this is a unit vector since [(1/h_j) (∂x^j/∂x^i')]^2 = (1/h_j^2) g_{jj}' / g_{jj} = (1/h_j^2) (h_j'^2 / h_j^2) = (h_i' / h_j)^2, hence (1/h_j) (∂x^j/∂x^i') = h_i' / h_j. (7.41.6)

Hence the transformation law for physical components can be written A^(i)' = cos θ_{ij} A^(j), (7.41.7)

which is just the familiar sum of the projections of the three components on the new direction. In Cartesian systems the physical, covariant and contravariant components are identical.

Exercise 7.41.1. Show that the physical components are the lengths of projections of the vector on the tangents to the coordinate lines in orthogonal systems.

Exercise 7.41.2. Show that the same law of transformation (7.41.5) is obtained by starting with A^(i) = h_i A^i.

Exercise 7.41.3. Show that Σ_{i=1}^3 |A^(i)| |B^(i)| cos θ = A^(i) B^(i).

7.42. Physical components of vectors in nonorthogonal coordinate systems For nonorthogonal coordinates the definition of the physical components is not quite as simple but we start from the same representation as before. The contravariant unit tangents are e^(i) = (g_{ii})^{1/2} A^i and if we set A^(j) = (g_{jj})^{1/2} A^j (no sum on j) (7.42.1)

we have A^(j) = (g_{jj})^{1/2} A^j (no sum on j) (7.42.2)

which reduces to Eq. (7.41.3) for orthogonal coordinates.

For a covariant vector we first construct the associated contravariant vector and apply Eq. (7.42.2). Thus A^(j) = (g_{jj})^{1/2} g^{jk} A_k (no sum on j). (7.42.3)

Only in the orthogonal case where g_{jj} = 1/h_j^2 and g^{jk} = 0, i ≠ j, does this give A^(j) = A_j / (g_{jj})^{1/2}. However, the relation A = Σ_{j=1}^3 A^(j) e^(j) (7.42.4) is preserved since e^(i)_j = g_{ij} / (g_{jj})^{1/2}.

The transformation law of physical components is A^(i)' = (∂x^j/∂x^i') (g_{jj} / g_{ii}')^{1/2} A^(j) (no sum on j). (7.42.5)

The scalar product of two vectors can be expressed in terms of the physical components, for it is A·B = cos θ_{ij} A^(i) B^(j), (7.42.6)

where θ_{ij} is the angle between the tangents to the x^i and the x^j coordinate lines.

The quantities ε_{ijk} A_j B_k and ε^{ijk} A_j B_k (7.42.7) define a contravariant and a covariant vector respectively, the associated vector products of A and B (cf. Ex. 7.31.5). Denoting these by C' and C, we have C^(i) = (g_{ii})^{1/2} ε^{ijk} A_j B_k. (7.42.8)

This is a cumbersome formula but reduces in the orthogonal case to C^(i) = ε_{ipq} A^(p) B^(q). (7.42.9)

Exercise 7.42.1. Show that the scalar and vector products given by Eqs. (7.42.6 and 8) transform appropriately.

7.43. Physical components of tensors Higher order tensors usually occur in such formulae as that for stress where t_i = p_{ij} n_j and we would like to associate physical components in such a way that t_(i) = p_(ij) n_(j). In orthogonal coordinates we have t_(i) = h_i t^i = h_i p_{ij} n^j = p_{ij} (h_i n^j) = p_{ij} n_(j) / h_j, so that we can write p_(ij) = h_i h_j p^{ij} / h_j = h_i p^{ij}. (7.43.1)

Evidently, we may treat each index exactly as the corresponding covariant or contravariant index of the vector is treated. Thus, for example, p^(ij) = p^{ij} / (h_i h_j) (no sum), (7.43.2)

where none of the indices is summed. In orthogonal coordinate systems, we need not distinguish between the physical components, the tensors p_{ij} and p^{ij} for p_(ij) = p_(ji).

Notice that the diagonal elements of a mixed second order tensor are the same as their physical components p_(i)^i = p_i^i = p^i_i (no sum on i). (7.43.3)

In nonorthogonal systems the relation for a mixed second order tensor t^(i) = p^i_j n^(j) leads to p^(ij) = g_{ii} g^{jk} p_k^i / (g_{jj} g_{ii})^{1/2} (7.43.4)

by analogy with Eq. (7.43.1). To find the physical components of a pure covariant or pure contravariant tensor we should lower or raise an index. Thus p_(ij) = g_{ii} g_{jj} p^{ij} (sum on i,j), where there is summation on m only. With nonorthogonal coordinate systems a distinction must be made between the tensor formulae p_{ij} and p^{ij}. Truesdell writes the physical components of p^i_j as (j)p so that the product would be written n(j) (j)p in physical form. Thus (j)p = (g_{ji} / g_{jj})^{1/2} p^i_j, which for a symmetric tensor is the transpose of p_(ij). In orthogonal coordinate systems this distinction does not arise and we will not pursue it farther; the reader is referred to Truesdell's paper in the bibliography. The method which Truesdell elicits in that paper is as follows: Starting with the tensors of lowest order the tensor components are replaced by the physical components as already defined, the final result showing the proper way of defining the physical components of the higher order tensors.

7.44. An example The discussion of physical components is sufficiently important to warrant an example, which will be made simple to avoid heavy algebraic manipulations. Consider the three coordinate systems: Cartesian x^1, x^2, x^3 or x, y, z Cylindrical polar θ, ρ, z or φ, r, z Elliptical cylinder θ, z, ρ or φ, x, z They are defined and related by x^1 = λ' cos φ = μ' cos θ, x^2 = λ' sin φ = μ' sin θ, x^3 = z^3 = Z^3, (λ' and μ' constants).

R' = constant is a circular cylinder and λ' = constant is an elliptical (λ'^2 / a^2 + μ'^2 / b^2 = 1) cylinder.

The coordinate planes φ = constant and θ = constant are both planes through the x^3 axis, as shown in Fig. 7.3. The first two systems are orthogonal but the third is not.

Since if λ' = μ' = 1 the second and third coordinates are the same we will do the calculations for the more general elliptical cylinder coordinates.

g_{11} = μ'^2 sin^2 θ + λ'^2 cos^2 θ, g_{22} = (λ'^2 μ'^2 / a^2) (λ'^2 sin^2 θ + μ'^2 cos^2 θ), g_{33} = 1, g_{12} = g_{21} = (μ'^2 - λ'^2) sin θ cos θ, g_{13} = g_{31} = g_{23} = g_{32} = 0.

For the orthogonal polars, λ' = μ' = 1, h_1 = 1, h_2 = r, h_3 = 1.

Consider a vector f with no component in the 3-direction and let it be the force on a particle rotating in a circle of radius r and subject to a retardation proportional to its velocity. If we take its mass and angular velocity to be unity, the physical components of the acceleration in cylindrical polars are f_(1) = r, f_(2) = -ar, f_(3) = 0.

In Cartesian coordinates the physical, covariant, and contravariant components are the same and f_1 = f^1 = f^(1) = x^1 + a x^2, f_2 = f^2 = f^(2) = x^2 - a x^1, f_3 = f^3 = f^(3) = 0.

To get the contravariant components in the other systems we must transform tensorially. Thus f^(1') = (∂x^1/∂x^1') f^1 + (∂x^2/∂x^1') f^2 and similarly, f^(2') = (∂x^1/∂x^2') f^1 + (∂x^2/∂x^2') f^2 = -a f^2 i - - -a(-μ'^2 cos^2 θ + λ'^2 sin^2 θ) + μ'^2 sin θ cos θ.

ax' P I For the orthogonal case λ' = μ' = 1, f^(1) = r, f^(2) = -a = -a(x^1)^2.

From these we can extract the physical components in the cylindrical polar coordinates f_(r) = h_1 f^(1) = 1·r = r, f_(θ) = h_2 f^(2) = r·(-a r) = -a r^2, and since R^1 = r these agree with f_(r) and f_(θ). The formulae using the oblique coordinates are more cumbersome.

Exercise 7.44.1. Using the apparatus provided in this section, find f^(1) and f^(2) and interpret them in the light of the geometry of the situation.

7.45. Anholonomic components of a tensor If e^(k), k = 1, 2, 3, are three linearly independent contravariant vectors (e^(k), e^(l), e^(m) not linearly dependent), they can be regarded as a basis. The reciprocal basis of covariant vectors can be constructed, a set e_{(k)} such that e^(i)·e_{(j)} = δ^i_j, e^(i)·e^(j) = δ^{ij}. (7.45.1)

The parenthetic index is a label for the member of the triad and the other index is the component index, but we allow summation convention to apply to both. If A^i_j is a mixed second order tensor, the nine quantities A^k_l = A^i_j e^(k)_i e^j_{(l)}, i, j = 1, 2, 3, are scalars which we may denote by A^{kl}. They are called the anholonomic components of the tensor with respect to the given set of base vectors (J. L. Ericksen, Tensor Fields, Section AIO, p. 801, in Handbuch der Physik III/I, Berlin, Springer 1960). In the case of a vector its anholonomic components (for example, A^k = A_i e^k_i) are clearly the projections ns on the three base vectors. In general, the anholonomic components of a tensor Aij are the scalars (7.45.2)

They are of course as many anholonomic components as tensor components. If the coordinate system is orthogonal and the base vectors are unit vectors tangent to the coordinate lines, they are e1 = (h1, 0, 0), e2 = (0, h2, 0), e3 = (0, 0, h3).

Then the anholonomic components with respect to this system of base vectors of a tensor are T(ij) = * * - * TL.’.j’ . (7.45.3)

where there is no summation on the indices i, j. We recognize these immediately as the physical components.

7.51. Differentials of tensors We have noticed that although af/axt is a covariant vector for any scalar function f the second derivative azflaxaa x’ does not give a covariant second order tensor (cf. Ex. 7.24.3). In this respect our curvilinear coordinate system is not so convenient as the Cartesian system in which the partial derivatives gave higher order tensors, and it is important to try and define a derivative which preserves tensor character. To be acceptable, such a derivative should tie in with what we already have. That is to say that in Cartesian coordinates and when applied to a scalar, it should reduce to the familiar partial derivative. We should also expect the derivative of a sum to be the sum of the derivatives and the derivative of a product to be given by the usual rule. The name covariant differentiation is applied to this operation and the covariant derivative of a tensor A (the suffixes are suppressed) with respect to xf is denoted by A,i. A further property that we should expect would be that the differential dA = A(xz dx’) - A@’) for infinitesimal displacements dx’ should be given by dA = A,i dx‘.

Our method of approach is as follows. We shall first consider what is meant by the parallel displacement of a vector along a curve and obtain a condition for this. Then follows an interlude in which one of the terms in this condition is expressed in terms of the metric tensor. This defines the Christoffel symbols which we express in various forms. To define the covariant derivative of a contravariant vector field we take an arbitrary covariant parallel vector displaced along an arbitrary curve and form the scalar product of the two. This is a scalar and its derivative with respect to a parameter along the curve is perfectly familiar. However, by using the rule for the derivative of a product and the condition for the second vector to be parallel, we are immediately led to an expression with tensor character and such that dA' = Addxj. This definition is then extended to an arbitrary tensor.

7.52. Parallel vector fields In Cartesian coordinates y', a vector field B' with constant components is represented by a field of parallel vectors. If we take any curve f(t) in the region of definition of the field, then we can think of the field along the curve as generated by the parallel propagation of the vector along the curve. The constancy of the components B' is expressed analytically by aB'/ayi = 0 (7.52.1)

and their constancy along the curve is dB'/dt = 0. If the second condition holds for an arbitrary curve it is equivalent to the first.

In curvilinear coordinates the constancy of components does not provide a condition for parallelism. For example, in spherical polar coordinates (1,0,0) is a unit vector always pointing away from the origin. If it is propagated along a curve, say the unit circle in the plane 8 = 7r/2, it is obviously not parallel to itself (see Fig. 7.4). This may be seen by looking at the Cartesian components of the vector, which are (y'lr, r2 = (Y')~ (y*)* (y9)2, and certainly not constant.

Let x' denote the general coordinate system and A' be a contravariant vector field. In Cartesian coordinates y' we will denote the vector by B* so that A' = B* (7.52.3)

If x'(t) and yi(/) are the parametric equations of an arbitrary curve in the two coordinate systems and the vector field is parallel we must have dBi/dt = 0. However, this condition is dB' d ay" - ayPdA5 d ay"

dt dt ax' dt dt ax5 = - a - y Dd A' a2yv dxk - 0. (7.52.4)

dt axj + Aja--;ir- If we multiply by ayp/axia nd sum on p, we have, by definition of the metric tensor, or multiplying through by g'r (7.52.5)

Exercise 7.52.1. Obtain the condition for the parallel propagation of a covariant vector AS. (Hint. Differentiate the scalar AiCzf or arbitrary parallel C.)

7.53. Christoffel symbols Since, by definition, (7.53.1)

it should be possible to express the sum in Eq. (7.52.5) in terms of the derivatives of the gi5. The summation is always from p = 1 to 3 and it is not necessary to write it in full each time. Then we have from which we have (7.53.2)

This expression is written [jk,i ] and is called the Christoffel symbol of the first kind. The factor occurring in Eq. (7.52.5) is g"[jk, i] which is written as rk) and is the second kind of Christoffel symbol. These symbols are not tensors (cf. Ex. 7.53.1) but are most important functions of the metric. The notation used here is standard and shows the nontensorial character; the notation is also commonly used. The definition may be best remembered by first writing the last term in [jk,p], which is negative and has the suffixes in this order; namely, ag,JaxP. The other terms are positive and are permutations of this order. (Since the metric tensor is symmetric, the parity of the permutation does not matter.) The Christoffel symbols and [jk, i] are clearly symmetric in j and k.

The condition (7.52.5) for a contravariant A' to be a parallel field may thus be written (7.53.4)

The analogous condition for a covariant Ai is dAi- ( . j (7.53.5)

dt 1 k Since (d/dr) = (a/axk)(d2/dr) and the curve was arbitrary, these conditions might be written -- (7.53.6)

and aA, (ijk)Aj=o. (7.53.7)

ax* The Christoffel symbols can be interpreted in terms of the variation of the base vectors. The base vector (7.53.8)

where y is the Cartesian coordinate of a point (cf. Eq. 7.35.3) and gij = &i) &j). (7.53.9)

Hence and forming the Christoffel symbol we have (7.53.10)

since ag(,,/ax' = ag(j)/ax*. It follows that (7.53.11)

Thus if m is regarded as a contravariant index, the Christoffel symbols are the components of the rate of change of the jth base vector with respect to the kth coordinate.

Exercise 7.53.2. Show that if the coordinate system is rectilinear (that is, all coordinate lines are straight), then the Christoffel symbols are all zero.

Exercise 7.53.3. Show that

7.54. Christoffel symbols in orthogonal coordinates In an orthogonal system of coordinates g, = 0 if p ≠ q and gii is written as hi". The Christoffel symbols are relatively simple and involve only one term. For example, [12,3] vanishes identically since it is composed of derivatives of g ,, gzs,g , which all vanish. Similarly, and Thus we can see that (7.54.1)

when p = q = r = i = j, with the positive sign, or q = r = i, p = j, with the positive sign, or r = p = i, q = j, with the positive sign, or p = q = i, r = j, with the negative sign, and is zero if p, q, and r are all different.

Since [jk] = [jk,i ] with no sum on i, we have 0 when p, q, r are all different, -1 -ah i u=l when p =q = r = i = j, 'tax5 Or q=r=i, p=j, (7.54.2)

or r = p = i, q = j, - -hi -ah, h2, ax5 when p =q = i, r = j.

In Cartesian coordinates the Christoffel symbols vanish. In cylindrical polars the only nonvanishing symbols are [12,2] = [21,2] = XI, ( ] [22,1] = = -2, 2 2 (7.54.3) (1 2) = (22 1) = In spherical polars we have [21, 23] = [12,2] = -[22,1] = 2, [31,3] = [13,3] = -[33,1] = x1 sin22 , [32,3] = [23,3] = -[33,2] = (x')'sin x2 cos x2, l3 3) = -x1 sin2 x2, (7.54.4)

Exercise 7.54.1. Show that Exercise 7.54.2. Calculate the Christoffel symbols for one or more of the coordinate systems given in Ex. 7.11.1.

7.55. Covariant differentiation A comparison of the conditions for parallelism in Cartesian and general coordinates (see Eqs. 7.52.1 and 7.53.6) suggests that may be the generalization of partial differentiation that we are looking for. It certainly satisfies the requirements we have laid down and we could proceed to show that it is a tensor by direct transformation. We shall, however, proceed more slowly and use the quotient rule to establish the tensor character.

Let A*b e any contravariant vector field and x'(t) a curve within its region of definition. If Bi is an arbitrary parallel covariant vector defined along this curve, then A'Bi and its derivative dAiBi/dt are both scalars. However, - - + - d (AiBi) = dA' Bi A' d Bi dt dt dt = dAiBi + A'[.' )B1d*L dt I k dt by Eq. (7.53.5) since Bi is a parallel vector. Changing the dummy suffix in the first terms from i to j we can write this [- d( A'Bi) = dA' (iik)Ai-d]xBk j. (7.55.1)

dt dt dt Since the left-hand side is a scalar and B, an arbitrary covariant vector the quotient rule implies that the term in the bracket is a contravariant vector. It is called the intrinsic derivative and written kk 6 ~-' d ~+' i k)Ai (7.55.2) 6t dt dt Moreover dA' aA' dxk -=-- dt axk dt so that (7.55.3)

The curve was taken to be arbitrary so d.x+/dt is a contravariant vector quite independent of the quantity in brackets. Since the left-hand side is a contravariant vector, the quotient rule asserts that the quantity in the brackets is a mixed second order tensor. We write it (7.55.4)

Notice that the same rule applied to a scalar gives the conventional partial derivative since there is no index on which to sum the second term. Also, in Cartesian coordinates the Christoffel symbols vanish identically so that the partial derivative is again recovered.

To find the covariant derivative of a covariant tensor we proceed in the same The way as before with an arbitrary curve and parallel contravariant vector. We then arrive at the formula (7.55.5) and dA^i/dt = A^i_{,k} dx^k/dt (7.55.6).

The general rule may be easily discerned from the case of a mixed second order tensor A^{ij}. Let X^k(t) be an arbitrary curve and B_i and C_j arbitrary parallel vectors. Then A^{ij}B_iC_j = E is a scalar and dE/dt = 0. Substituting for the derivatives -dE/dt = dA^{ij}/dt B_i C_j + A^{ij} dB_i/dt C_j + A^{ij} B_i dC_j/dt, and -dB_i/dt = Γ^i_{pq} B_p dx^q/dt, -dC_j/dt = Γ^j_{rs} C_r dx^s/dt, we have dA^{ij}/dt B_i C_j - A^{ij} Γ^i_{pq} B_p C_j dx^q/dt - A^{ij} B_i Γ^j_{rs} C_r dx^s/dt = 0. To get B and C always with the same suffix we now interchange the dummy suffixes i and p in the second term and j and q in the third to give [dA^{pq}/dt - A^{ir} Γ^p_{ri} dx^q/dt - A^{rq} Γ^q_{rj} dx^p/dt] B_p C_q = 0. Since the left-hand side is a scalar and the vectors B_p, C_q and dx^q/dt are all independent of the bracket, the quotient rule asserts that (7.55.7) is a mixed third order tensor. It is evident therefore that a form that is much more easily perceived than written down.

A delightfully simple and elegant example of the power of tensor methods is the proof that the metric tensor acts as a constant with respect to covariant differentiation, g_{ij,k} = 0. (7.55.9). This is a tensor equation asserting that a certain third order tensor equals the zero tensor. If the equation is true in one coordinate system, it is therefore true in all since we may transform both sides of the equation. However, it is obvious in Cartesian coordinates and so always true. This is known as Ricci's lemma. The same method can also be used to show that the rules of differentiation of sums and products hold for covariant differentiation.

The additional terms that arise in the covariant derivative are due to the variation of the base vectors. To see this let us consider the case of a contravariant vector, which may be written a = a^i g_i. The derivative of a with respect to x^k is ∂a/∂x^k = (∂a^i/∂x^k) g_i + a^i (∂g_i/∂x^k). However, by Eq. (7.53.11) this can be written as ∂a^i/∂x^k g_i + a^i Γ^j_{ik} g_j = (∂a^j/∂x^k + a^i Γ^j_{ik}) g_j. Hence a^j_{;k} = ∂a^j/∂x^k + a^i Γ^j_{ik}. By interchange of the dummy suffixes i and j, we have a^i_{;k} = ∂a^i/∂x^k + a^j Γ^i_{jk}. From Ex. 7.53.3 it is evident that a covariant vector would give (7.55.10).

These expressions in the brackets are just the appropriate covariant derivative and show that the Christoffel symbol comes in with the variability of the base vectors.

Exercise 7.55.1. Show by direct transformation that a^i_{;j} is a mixed second order tensor.

Exercise 7.55.2. Show from the definition that g_{ij,k} is zero.

Exercise 7.55.3. Show that the covariant derivatives of g^{ij}, g_{ij}, ε^{ijk}, and ε_{ijk} all vanish.

Exercise 7.55.4. Calculate the components in spherical polar coordinates of the covariant derivatives of the three contravariant tangent vectors to the coordinate lines of that system.

Exercise 7.55.5. Show that a^i_{;j} - a^i_{;j} is antisymmetric. (Hint. Use g_{ij} = 0 and the result of Ex. 7.54.1.)

Exercise 7.55.6. x^i(t) is a curve in space satisfying d^2x^i/dt^2 + Γ^i_{jk} (dx^j/dt)(dx^k/dt) = 0. Show that it is a straight line.

7.56. The Laplacian, Divergence, and Curl

The covariant derivative of a scalar φ, which reduces to the partial derivative, is a covariant vector φ_{,i}, the gradient of φ. We can raise the index to give a contravariant form of the gradient g^{ij}φ_{,j}, and both of these are the vector ∇φ in Cartesian coordinates. If we take the covariant derivative of this vector with respect to x^i and sum on i, this is again a scalar, the Laplacian of φ, ∇²φ = g^{ij}φ_{,ji}. (7.56.1). Writing this in full we have ∇²φ = ∂/∂x^i (g^{ij} ∂φ/∂x^j) - Γ^i_{ip} g^{pj} ∂φ/∂x^j. However, by Ex. 7.54.1 and switching of dummy indices, ∇²φ = g^{ij} ∂²φ/∂x^i∂x^j - g^{ij} Γ^p_{ij} ∂φ/∂x^p. So that ∇²φ = g^{ij} φ_{,ij} - g^{ij} Γ^p_{ij} φ_{,p} = g^{ij} φ_{,ij} (7.56.2). In orthogonal coordinates this takes the form ∇²φ = Σ_{i=1}^3 (1/h_i) ∂/∂x^i (∂φ/∂x^i / h_i).

The covariant derivative with respect to x^i of a contravariant vector A^j summed on j is called the divergence of the vector A, div A = A^j_{,j} (7.56.4). If A_i is a covariant vector, the suffix must first be raised to give div A = g^{ij} A_{i,j} (7.56.5). By the same methods as before we can write these as div A = (1/√g) ∂(√g A^j)/∂x^j (7.56.6). These are scalars and so are identical with their physical components but we can express them in terms of the physical component of A by using the relation A^{(i)} = (g^{ii})^{-1/2} A^i and A_{(i)} = (g_{ii})^{-1/2} A_i, both become div A = (1/h_1 h_2 h_3) [ ∂(h_2 h_3 A^{(1)})/∂x^1 + ∂(h_1 h_3 A^{(2)})/∂x^2 + ∂(h_1 h_2 A^{(3)})/∂x^3 ] (7.56.8) in orthogonal coordinates.

The expression ε^{ijk} A_{k,j} is an absolute contravariant vector which reduces in Cartesian coordinates to the familiar expression for the curl of the vector. We therefore define curl A = ε^{ijk} A_{k,j} or ε^{ijk} g_{kl} A^l_{,j} (7.56.9). To obtain the physical components of the curl we need first the physical components of A_{k,j}. In an orthogonal system A_{k,j} = ∂A_k/∂x^j - Γ^p_{kj} A_p. We only need this for k ≠ j so that the two Christoffel symbols that appear are with p = j or p = k. However, these are Γ^j_{kj} = (1/h_j) ∂h_j/∂x^k and Γ^k_{kj} = 0, Γ^j_{jk} = (1/h_j) ∂h_j/∂x^k and Γ^k_{jk} = (1/h_k) ∂h_k/∂x^j. Then A_{(k,j)} = (1/h_j) ∂A_{(k)}/∂x^j + A_{(k)} (1/h_j h_k) ∂h_k/∂x^j - A_{(j)} (1/h_j h_k) ∂h_k/∂x^j (since Γ^j_{kj} A_j = A_{(j)} (1/h_k) ∂h_k/∂x^j? Wait, need to check. Actually, A_{k,j} = ∂A_k/∂x^j - Γ^p_{kj} A_p. For p=j term: -Γ^j_{kj} A_j = - (1/h_j) ∂h_j/∂x^k A_j. For p=k term: -Γ^k_{kj} A_k = - (1/h_k) ∂h_k/∂x^j A_k. So A_{k,j} = ∂A_k/∂x^j - A_j (1/h_j) ∂h_j/∂x^k - A_k (1/h_k) ∂h_k/∂x^j. Then in physical components: A_{(k)} = h_k A^k? Actually, A_k = h_k A^{(k)}? Usually A^{(k)} = A^k / (g^{kk})^{1/2} = A^k / (1/h_k^2)^{1/2}? In orthogonal, g^{ii} = 1/h_i^2, so (g^{ii})^{1/2} = 1/h_i, so A^{(i)} = A^i / (1/h_i) = h_i A^i. And A_i = g_{ii} A^i = h_i^2 A^i = h_i A^{(i)}. So A_k = h_k A^{(k)}. Then ∂A_k/∂x^j = ∂(h_k A^{(k)})/∂x^j = h_k ∂A^{(k)}/∂x^j + A^{(k)} ∂h_k/∂x^j. Then A_{k,j} = h_k ∂A^{(k)}/∂x^j + A^{(k)} ∂h_k/∂x^j - A_j (1/h_j) ∂h_j/∂x^k - A_k (1/h_k) ∂h_k/∂x^j = h_k ∂A^{(k)}/∂x^j + A^{(k)} ∂h_k/∂x^j - (h_j A^{(j)}) (1/h_j) ∂h_j/∂x^k - (h_k A^{(k)}) (1/h_k) ∂h_k/∂x^j = h_k ∂A^{(k)}/∂x^j + A^{(k)} ∂h_k/∂x^j - A^{(j)} ∂h_j/∂x^k - A^{(k)} ∂h_k/∂x^j = h_k ∂A^{(k)}/∂x^j - A^{(j)} ∂h_j/∂x^k. So A_{(k,j)} = (1/h_k) A_{k,j} = ∂A^{(k)}/∂x^j - (1/h_k) A^{(j)} ∂h_j/∂x^k. That's the physical covariant derivative? Actually, the physical component of a tensor of rank (0,2) is different. But here A_{k,j} is a component of a covariant vector derivative, which is a (0,2) tensor. The physical component is usually defined with appropriate scale factors. For a vector derivative, the physical component for the j derivative is (1/h_j) times the partial derivative plus connection terms. But from above, A_{k,j} in orthogonal coordinates is: A_{k,j} = h_k ∂A^{(k)}/∂x^j - A^{(j)} ∂h_j/∂x^k. Then the physical component for the j-th derivative (for fixed k) is (1/h_j) A_{k,j}? That would give A_{(k,j)} = (1/h_j) [h_k ∂A^{(k)}/∂x^j - A^{(j)} ∂h_j/∂x^k]. That is not symmetric. Actually, the physical components of the covariant derivative of a vector are defined as (∇_j A)_{(k)} = (1/h_j) (∂A_{(k)}/∂x^j + connection terms). Let's derive properly: The covariant derivative A_{i;j} = ∂A_i/∂x^j - Γ^p_{ij} A_p. In orthogonal, Γ^p_{ij} = 0 for p≠i,j; Γ^i_{ii} = (1/h_i) ∂h_i/∂x^i; Γ^i_{ij} = (1/h_i) ∂h_i/∂x^j; Γ^j_{ii} = - (1/h_j) ∂h_j/∂x^i. So for fixed k and j: A_{k;j} = ∂A_k/∂x^j - Γ^p_{kj} A_p. Only p=k and p=j terms matter: Γ^k_{kj} = (1/h_k) ∂h_k/∂x^j, Γ^j_{kj} = (1/h_j) ∂h_j/∂x^k? Actually, Γ^j_{kj} = (1/2) g^{jj} (∂g_{kj}/∂x^j + ∂g_{jj}/∂x^k - ∂g_{kj}/∂x^j) = (1/2) g^{jj} (∂g_{jj}/∂x^k) = (1/2) (1/h_j^2) (2 h_j ∂h_j/∂x^k) = (1/h_j) ∂h_j/∂x^k. Yes. So A_{k;j} = ∂A_k/∂x^j - A_k Γ^k_{kj} - A_j Γ^j_{kj} = ∂(h_k A^{(k)})/∂x^j - (h_k A^{(k)}) (1/h_k) ∂h_k/∂x^j - (h_j A^{(j)}) (1/h_j) ∂h_j/∂x^k = h_k ∂A^{(k)}/∂x^j + A^{(k)} ∂h_k/∂x^j - A^{(k)} ∂h_k/∂x^j - A^{(j)} ∂h_j/∂x^k = h_k ∂A^{(k)}/∂x^j - A^{(j)} ∂h_j/∂x^k. So A_{k;j} = h_k ∂A^{(k)}/∂x^j - A^{(j)} ∂h_j/∂x^k. Then the physical component for the j derivative (keeping k) is A_{(k;j)} = (1/h_j) A_{k;j} = (h_k/h_j) ∂A^{(k)}/∂x^j - (1/h_j) A^{(j)} ∂h_j/∂x^k. That is what I have. For the curl, we need A_{(k,j)} - A_{(j,k)} for k and j. So A_{(k,j)} = (h_k/h_j) ∂A^{(k)}/∂x^j - (1/h_j) A^{(j)} ∂h_j/∂x^k, and A_{(j,k)} = (h_j/h_k) ∂A^{(j)}/∂x^k - (1/h_k) A^{(k)} ∂h_k/∂x^j. Then A_{(k,j)} - A_{(j,k)} = (h_k/h_j) ∂A^{(k)}/∂x^j - (1/h_j) A^{(j)} ∂h_j/∂x^k - (h_j/h_k) ∂A^{(j)}/∂x^k + (1/h_k) A^{(k)} ∂h_k/∂x^j. That is the expression for the physical component of the curl. But the standard formula for curl in orthogonal coordinates is: (curl A)^{(1)} = (1/(h_2 h_3)) [ ∂(h_3 A^{(3)})/∂x^2 - ∂(h_2 A^{(2)})/∂x^3 ], etc. And indeed, for i=1 (so k=2, j=3), we have (curl A)^{(1)} = (1/h_1 h
