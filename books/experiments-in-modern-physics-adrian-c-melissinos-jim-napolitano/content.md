# Experiments in modern physics Adrian C Melissinos Jim Napolitano

EXPERIMENTS IN MODERN PHYSICS Second Edition Adrian C. Melissinos UNIVERSITY OF ROCJI.DSTER Jim Napolita,io ~@ ACADEMIC PRESS An imprint of Elsevier Science Amsterdam Boston. London Ne:wYork Oxford Paris SaoDiego San Frandsco Singapore Sydney . Tokyo Senior Publishing &liter Jeremy Hayhurst Senior Project Main1F Ju,i.oEspcros Editorial Cootdinator Noa Donaghy Product M.anaga- Anne O'Ma.ra Covcr Des.ig.n Dick HannlL~ CopyeditoT Cl'Ull'les LautktT Jt.

Cnl)1posltion Ceptu1 Imaging P,rt. Ltd.

ftintc:r l11e M~pl~V ail Book Manufacturing Gruup 112;s book is printed lU:id-f~ paper.

All rights ~trved.

No pnrt of lhis publication may be n=ptoduccd « transmitted in any form or by any means.

electronic or m~hrutlcal. ineludmg phoLOCOpy. . m.:ordirJg, or any w.fonnution storag~ nnd rettleval sy;.tem, without penni:;.~ion io writing from the publ..i~het'- Rcqu.c-.,;ts ror ~ission IO l'Wlke copie~ of any part of the work mould be mailed to: s~ Permis.sions Department. H,.rcourt. Jnc,., 6277 Harbor Dri~e.. OrJMdo, Florida 32S87-6777.

## 4. L The Principle of Laser Operation

4.2. Properties of Laser Bea.ms 156 4.3. The HeNe La.~er 159 4.4. Measurement of tbe Trnnisverse Beam Profile 164 4.5. The Michelson Interferometer 167 4.6. The Fabry-Perot Interferometer 172 Optics Experiments 179 5.1. Jn trodu.ction 179 5.2. Diffr41cuon from a SUt !80 5. 3. Calculation of the DiffrJ.Ction Pattern 185 5.4_ Diffraction from a Circular Aperture 188 5.5. The Diflnicrion Grating 192 5 .6. Fourier Optics 198 5.7. The Faraday Effect 201 5.8. Berry"s Phase 210 5 .9. References 214 6 High-Resolution Spectroscopy 6-1. Introdu clion 215 6.2. The Zeeman Effect 218 6. 3. Hyperfine Strucrure 228 6.4. The Line Width 236 6.S. The Zeerrum Effect of the Green Line of 198Hg 238 6.6. Saturation Abs.orption Spectro~copy of Rubidium 243 6.1. References 250 7 Magnetic Resonance Experiments

## 7. I. Introduction

7 .2. The Rate for Magnetic-Dipole Transitions 255 7.3. Absorption of Energy by the Nuclear Moments 262 7 .4. Experimenlal Obsef'\•ation of the Nuclear ~.fagneric Resona.nee of Protons 273 7 .5. Electron Spin Resonance 283 7.6. References 293 8 Particle Detectors and Radioactive Decay 295

## 8. I. General Considerations

8.2. Jnlcractions uf Charged P..inicles und Pholons with Mauer 298 8,3. Gaseous Ionization D~tcctors; the Geiger Counter 320 8.4. The Sciotilh1tion Counter 333 8.5. Solid-Stale Detectors 344 8.6. Nuclear Half-Life Measurement~ 354 8.7. Rc:fcrcnccs 364 9 Scattering and Coincidence Experlrnents 367 9.1. Introduction 367 9.2. Compton Scattering 369 9 .J. ~1<\~hah~r EffecL 3~5 9.4. Detection of C~mi~ R.).ys 399 9.5. y-y Angular Correfotion Measurements 409 10 Elements from the 17ieory of Statistics 423 IO. I. Definitions 42., 10.2. Frequency Functions of One Variable 431 10.3. Estimation of Parameters and Fitting of Dilta 445 10.4. Errors and Their Propagation 454 t 0.5. The Statistics of Nuclear Counting 465 I 0.6. References 473 Appendiees A Students 475 B A Short Guide to MATLAB 477 BJ. AfvlATLAB Review 478 B.2, Making Fancy Plots ao MATI..AB ~I X Contents C Laser Safety D Radioactivity and Radiation Safety 485 E Optical Derection Techniques 489 E. l . Photographic Film 489 E.2. Photomultiplier Tubes 490 E.3. Photo diodes 496 F CoJLrtants 499 G Exercises Preface In the forty years since the first edition of this book was published.

De!-<'lfly the fuodament.al concepts are of cc.-i~c unchanged while many of the detaiJs are radicnlly diffcrcnL This new edition a.u.e.mpt~ 10 maintain the emph~is on the fu nda.menral importance of experimental physics and lnb oratory rechniqu~ while updating lbe equipment and tools used to set up the experiments and lo acquire and analyze the data.

As much as possible'\ this revision is in keeping with the style of the original text. The importance of exp erimentd investig-~lion and 80und Ia b· oratory technique, as a way for &1utl~ts to connect ad v.aoccd physics 1opics to measurements carried out with their own hand. is emphasized. If any thing~ this .-ppTooch is even more importa11t than it was fony years ago.

Curricula have r o ct1sed more and ino re oo "interactive" tedmiques in the introductory sciences, and the advnnced laboratory ii; a primary way to eKlen.d this approach co upper Ieve1 courses.

\Ve have incorporated many of the changes that have occuned in experi mental techniques. Clrnpter 3 collects topi~s in basic faboratory electronics {including some simpJe e~perimenl.8 wilh elementary circuits). as weJJ a~ the somewhat more advanced topics of OpAmps. lock.in ampHfiers. and computer in terfac~~-Chapter 4 focu.se.~ on lasers and optical iostrumeOls.

Data analysis and presentation is generally carried out with the program MA1'LAB; analysis program.s are avnilable from the authors. Throughout the booi4 we make use of computers and computer-controlled hartlware, as well as various commerciaJ sofuvare packages., as illustrative options for building such experiments. Also.. n col lcction of exercises suitabl~ for homework or examinations is in~tu.Jed in Appendix G •ii Pref ace New experiments have been added and the material has been reor ganized. A number of new experiments in condensed matte1 have been introduced in Chapter 2, including measurements of the resistivity of met als using eddy curren18t the Hall effect in bismuth, electrical, and therrnnl properties ofd iodes., and high T('. superconductors. Chapter 3 includes new ~ pe.riments on Johnson noise. and chaos. Chapters 4 and 5 arc completely new and several eApcriments involving lasers are discus~ed. These include classical experiments on diffraction and inlerferometty as well as a mea ~urernent of the Faraday effect and ofBeny>s pha.~e. Chapters 6 nnd 7 have been updated and an experiment on saturation absorption spectroscopy ha~ been introduced. The material on nucle~ physics and nuclear techniques has been reorganized into Chapters 8 aml 9 and some oew measurement.st including cosmic ray expcritnent.li and muon decay have been ildded.

Space limitations have forced us to drop sevenll experiments, and other material, from the first editioo. We have eliminated experiments on the pho toelectric eff ~ thenw onlc emissiont the Hall effect in semicondueton;, Rutherford scattering, and velocity and particle identific.ition measun> ment~. Some detailed discussions of experimental techniques, such as the prism spectrograph and vacuum purnpiog, have also been removed.

This revision is built on advanced laboratory courges at the Uni ve.rsity of Rochester and at Rensselaer Polytechnic Institut~ as well as labora· tory compooents of upper level lecture courses. Our stodents take part in intemctive courses at the inlroductory level, and they extend this exposure with this advanced laborntory mate.rial as they continue their education.

Io many cm.cs~ the cxperin1ents are developed.. built, and debugged by student~ who have already gone through a dedi~ted advanced laboratory co~e. In most cases .. the data presented were acquired by students. These students are listed colloctively in Appendix A We are grateful to many of our colleagues for their help nod support. [n particular, A.C.M. lhanks Todd Blalock, Glen Ha!lit.. and Craig Spencer.

who were in ch.1Tgc of the "senior Iab" in reeeol years. He .llao thanks Judy Mack ror chee:rfuJ and efficient rypiog of early vef8ions of the mantL~cripL J.N-1.hank.s Toh,MiogLuforhissuppon of this COU!$C, Peter Persans forWs ctTon.s to teach and extend the taborntory an<l for contributing h.is notes on using 1v1ATLAB, and Tom Shaooon fur his ma.intemwce of the equipment.

A.C.rvt., J.N.

Rochester. New York Troy. New York ~~­ Preface from the First Edition . ' . .

..

.'.

.' ft is generally accepced th~t training in the sciences, especfally at the undergraduate level, is nor complete wilhout n fair oroount of laboratory e.xperi.ence. This is parucularl;• true io physics where the basic freshman and sophomore courses are supplemented by concurrent laboratory exercises.

At the junior and senior level, however, laboratory training becomes more important and forms the subject of an independent c.ourse. Rather than simple labomtory exercises. the students now pcrfonn oomplete experimenlS and one coul<l li1>l the aims of Ibo cou.rse as fol?ows: (a) To teach the srudcnt the. melhuc.Js and procedures of experimental physics at mt advanced level; a-od 10 give him confidence in his own ability to me.asure physkal entities and relotinnships between them.

(b) To familiarize the student wich modern rc:;carch equipment and it.'i u.c;c; also lo make him aware of I.be most basic t.cchniques presently used in widely varying fields of physics.' {c) To convince the student that the matecial he studied a.nd covered .in bis Iecrure courre~ can iodeetl be tested experimentally; and co give him the s.itisfactioo of doing so himself.

On the other hand the real pl'()fessional training for students who will become experimental physicists takes pk.ice in gr.1duate school during their thesis work; this is a period of intensive involvcm1..-nt in research bucwilhin a highly specialized field. It therefore appears that the best opportunily for a broad look st the general experimental methods of physics still remains in 1he junior and senior laborntory courses.

xvi Preface from the First Edition The present text is-:an outgrowth of such a laboratory course giveo by the author at the University of Roche$;ter between 1959 and 1963. le consisted of a one-year course with two 3-hour meetings in the laboratory and two 1-hour lecture meetings weekly; the students had access to the laboratory at all times and. .in gcner4.l1, worked during hours of their own choice well in exce~ of the. scheduled peciods. The srudents w,uked in pairs? which in most cnses provides a highly Inotivating and succcssfuJ relationship.

The material included in this course was selected from d1ose experiments in atonuc and nuclear physics that have laid the foundation and provided the evidence for modern quanrum theory. The experiments were set up in such a fa.won that they could be completed ina two· to four-week period of normal work taking into accouot the otber demands oo the srudenl's time.

A frequent tendency of ~tudents {especially the more enthusiastic ones) is to become involved in experiments that are '-aJmost original"'' 01' in setting up new experiments; th.is, however? requires constructioo of their own equipment and can result io oonsidembJe "'gadgcteering', as wen as leadini; to extended involvement, which a ,senior cannot afford. We found this to be a com.II1on trap eventually leadiog to frustration and discouragement with a student having only a &'progres~ report" or a marginal resuh to show for one term of work.

For these reasons we used, whenever possible. commtrcial equipment, and all experiments were carefully tested before being handed over to the student. The emphasis wa~ oo the "physics" of the experiment and the interpretation of the results obtained; clearly, to obtain correct result~ the student had to properly adjus~ useT and understand hi~ equipment. Further more, a time limit ~ould he set so that eight to ten c.lifferent e.xperimenL~ could be completed in one academic year. This variety not only brings the student in contact with a broader segment of physfos and of tech11iques. ir also gives him the opportunity of a ·'fresh starr several times throughout the course; and. most in1portant, it keeps lhe student continuously inter e~ted in spite ofa ny setback or difficult}· he may enoount.er in one or more experiments.

The experiments described in the first four chapters ot this text are, in general, e~icr than d1e ones discussed later; each can usually be completed in a one-week period, and at the University of Rochester are perfomtcd io the second term of the junior year.. This leaves then the two teans of the senior year for the more advanced experiments described in the later chapters. The various experiments have been grouped according to the basic physicat principle rather than the special technjgue. For each experiment ..

. .

the w,derlyiog theoretical ideas are first iotroducciJ. then the experimen rnl apparatus is dc.c;cribed io coosiderable detail and, finnlly, the rcsolt5 oblnined by lht !itudenrs are given nod discusrod. Tn this respect we believe that tl:us text is not o "loboratory IDanual"; _instead we have aimed at a fairly coherent presentation of cxpcrimcnLa1 physics in spite of the limited and occasionally random selection of the ~xperimems. We feel tbaL our opproach is similar to lhat G P. Hamwell and J. J. Livingood in their 1)f classic rext ''E.,perim~tal Atomic "Physics," which appt.ru-cd'originally in 193:3.

The render may occasionally be surprised by the veat delnil with which we describe apparatus or special procedure$ for analysis of data. We have done so lo a.-.sisl those who mny wish to sel up a sunilar laboratory and .. because these are the details the :ihnlenl ha.~ l l<;ually 10 find out by himself: but we believe that onJy through such dem.il cnn one acx.iuire 1he real • . • . .

tla vor of e.xperimentu physics. \Ve have placed special emphasis on numer ' .

' • ical results and on simple calculations, emphasizing the use of cbe cor.rccr .' • ' ' . units.

' Contrary to accepted practice we have includeJonly a minimum number ofreferen~-~; ins1ead, we have given a sclce!Cd bibliography lO each subject through which the interested ce.tder may find all pertinent infoIT0.3tion. lt is. howcvu , expec1ed thnt lhe ::iiw1cnL is famjJiar or is concurrently taking a course on modern physics. The usual mathematical level of culcului- is considered as a prerequisite and is freely used throughout.

As meotiooed before, modcnl commercial equipment is used whenever practicable: this is I.he same rype of equipm~t ~ used in present-day research and frequently is the basis for a succ~. .. ful c.eaching laboratory.

ll true. however, thnr similar equipmcnl can be obmined from several LS manufacturers and thru special apparatus is preferably built in one's own ::shop. \Ve do have on file the prinL-t of all such special equipment and wc will be glad to supply them oo rcqucs1.

The list of experimcnLS in this rexr is not complete. For cx3mr,le, we bave not included a discu.~~ion of ''cohereol scau.cring" (diffraction) exper iments. of ..e lectromagnetic spectrometers." and of "visual techniques"· (bubble chamber. spark chamber, and nuclear emulsion) in spice of 1heir succe&sfol performance by sever.Ii :ilu,J,..·nu. \Ve bope to be able to remedy these omic;sions in a future edition. We also realize lhnt io some c~~ u bcue.r, or more educational. technique might be avaifoble for the experi ments presented here. \Ve would be grateful co our readers if they wish to indicate to us these alternatives.

,n,n; Pref ace from the First Edition rn line with oor original ill teotion all the data and ro.~ults pl'esentcd in this book were obtained by students of the "Senior Ulhoratory" of the University of Rochester and the approprfatc credit js given in the lext. The resu1ts presented here could not have been achieved without the suppon of the Physics Dcpartm~nt of the University af Rochester; also major equlp- tnent was purchased tJuough a grant from the Unired States Atomic Energy Commission and a matching funds giant from the National Science Foun dation4A s is a! ways the case. whatever success this !aborJtory did enjoy is· due to the oombined effo ns of many individuals. a large pan of which wa.~ supplied by the pMticipating srudenl~-It is a special pleasure to thank from ht--re the gradua(e assi~tants during lhe 1959-1963 period. On;, E.. Griffin, J. Robbins, J. Mocheli and J. Reed, fortbeircontributions to the laboratory.

More than to anyone else 1.he laboratory is indebted to Mr. F. L Reynolds.

who has been in charge of aU technical mauen, and hes.~ kept the equipment io operating condition; 1 wish to expre..~s to him my personal gratituuc for his friendship nrul for many heJpfu l suggestions connected with this text I alM<> wish lo acknowledge discussions with many of my c;oJleagues in Rochester and, in panicular, Dr. W. P. Alford. Dr. M. . F. Kap!on., and Dr. R. E. Mars;hak.

In the preparation of the manuscript [ benefited from the an work of Mcs6rs. Yu-Chang Lee. W. Stinson, and J. Pinero; most of the manuscript was typed by Mrs. B. M. ~1anh. . and to all of lhem r express my appreci ation for their excellent work. [ am al oo indebted to the folJowing of rn y coUeagues for reading early parts oft he manuscript and making many valu able suggestions and corrections: Dr. P. Baumeister on Chapter 2; Dr. T.

Castner oo Chapter 3; Dr. D. Cline on Chapter 5; Dr. R Ellsworth OD Ch.ipter 6; De. L. Bradley oo Chapter 7; lvlr. C. Cook on Chapter 8; &ad Dr. J. Reed OD Chapter 9. Still, howevc:rt the respon'sibHity for all crron; is mine and I would appredate it if the readers could indicate thern to me.

Finally, l would like to dutnk my wife, Joyce, for her encouragement and a5j;istance during the course of this w'Ork.

A.C.M.

Rochestet; New York . , ,, . , . . . . . . . . .. . . . . . . . . . ..

" .

... .' . . . 4 . . . . • . . .• . . • CHAPTER 1 .... .

.. .

...

..' .. .

. Experiments on .. . .

. ..

Quantization .. .

. .. . . . . ' .. ' ..

Ll. INTRODUCTION A defining characteristic of prostnl-day physjcs is that many of the quat1- tilic~ ured to describe physical pbenomeoa are quantized. That i~) such I ' quantities cannot take any one of a L'Ontinuum of values.. but are rc~tricted to a .set (perhaps ao infinite set) of discrete value~. Common ex.antples ore the intensity of radiation of the electromagnetic field. the energy of atomic systems, or the electric chafEe. Strong evidence for such quantization is obtained from e>tptriments that will be ~,;cribed in this chapter: (a) Millilam's experiment by which the chnrge on iodh·idu.al oil dropleL~ is measured. The experiment shows that the charge is always an integer multi pie of lhe smallest charge ob served; this is identified with the charge of lhe electron.

(b) The Frank-Hertz experiment on the e~citation by electron born~ bardment of atomic vapors. It is found that only for discrete bombarding 2 1 Experiments an nuantizat~on energies is such excitation possible. and the first excited state of the mercury (Hg) atom is thus measured.

(c) A n1easoremeot of spectral lines in the visibJe. In particular the Balmerseriesofthehydrogenatom. as well as the more complicated spectra of sodium and mercury wi11 be discussed.

PASCO Scientific also markets a ~'Precision Student Spectrometer"1 Model SP-9268, which is fuUy equivalent to the s~trometer used to obtain the data described in Sections LS aud L.6. Of oourse such an .apparatus c.in also be built in-house, and we shall describe the apparatus and data-takif\g procedures in sufficient detail.

1.2. THE MILLIKAN OIL DROP EXPERIMENT 1.2. . 1. General In 1909t R. Millikan reported a reliable method for measuring ionic charges.

It consists of obscrviog lhe motion of 8TtUill oil droplets under the influence of an elecUic 6¢ld. Usu.a.lly the drops acquire a few electron charges and thus conventioJ1al fields impart to them velocities that pennit isolation of a drop and continuous observatioo for a considerable length of time; further.

the mass of the oil droplet remains alm~r constant (there is very slight evaporation) daring these long observation time~.

In principle, if we measure the force due to the electric field Et F, =qE = neE~ (I. I)

we can obtain ne; repeating this measurement for several (or the same)

drops but with different values of the integer n., we can extract the charge of the electron e.

The electric fOl"C-e cao be measured either by a oulJ method-that is .. by balancing the drop ngainst the gravitatioruil fon::e-or, as will be described ..

. . .

.. a .. l . .. . . a .• . • . .I I. .• ,.. • .

. " . ".

. e .

. A .I • ' . ' . 1.2. The Millikan Oil Drop Experim&nt 3 -.. .

I 411 • • ~ . ..

• 4 4 I •I : ·4 : ·• : ·t :h ere, by observing the motion of the drop under the influence of both forces.

: I : 6 : ' : • : : :I : O il urop!ets in air) acted on by a constant force F. soon reach a terminal :.~.:.: :: .. velocity givr.:.n by Stokes' law, .. ". .. .' . . ' .

. . • . . . . . . • . . . . . f . • F = 6;ra17v. (l.2)

. .

•: .· : ·: · where a i~ the radius of the ( assumed spheri~l) droplet. '1 the viscosity of :::::: the air. and v the terminal velocity. To obtain the t8dhls of the drop (needed :..: : : : · in Eq. (1.2)) we observe the free fall of the drop; the gravitational force is ..

.. . ' ' .. . ' 4 . .. . .. ' . Fg = -rra 3 (p - <1)g (1.3)

' 3 .. . ' . . .. ' ' with p rut<! u lhc density of air nnd oil and g the acceleration of gr.1Vily.

. .. . . . . . . . ' ' . Schematic.ally, 3$shown in Fig. I. I, the apparatus consists of lwo parallel . . .' .

. . .. . . . . . ' . ' plntes that can be altern.ntively charged to a coo&tant potential + V, - V.

. . or 0. The drop is then observed (wilh ~ t.eleiscope)~ ;md the Lime t il takes .. . to travel through a disranc:e d is measurer.I. Let F + dt-'1lote the foree on a oegstively charged drop with elcchic field up (time t+. electric force aiding . .

.. . . . . . . . . ' gravjty) and F_ the force with electric fie1d down (time L. electric force . . . . ' . ' opposing gravity). Then . .

. ' ' = I/it>)

~ ' = F± ±nt?(V/ s) - :ira·~(p - o)g 6naryd ( (1.4)

= - 4 3 = Fo 3 rrtJ (p - o)g 6'~at1d(l/to).

where the sign conventions hqld if t is considered >0 when the drop moves up, and 1 < 0 when it is moving down (recall thot e is negative.).

• J • +V ..

FlGURE l .1 Fcm::cs on ~ ,~o il drop between tbe pJates of a 1\1iHik::an 1p,pa.ratus, 4 1 Experiments on OuantizaUoo A convenient method of analysis is to write Eq. (1.4) as I Ve (n) ±An - B A== --- 6.nraqd t±_ (1.5)

B ~a2(p-u)g -=-B to 9 11d so that A and B can be ea.c;ily detennined.

Indeed a plot of 1/ rf) against n reveals I.be linear relationship and the fact U1at only integervmues ofn appear. . proving that the drop has acquired one. twoJ three) or more electric cluugcs of value e. and never a fraction of that value. Thus we have clear evidence thnl the ionic charge picked up by the oil drops is quanrized. Furthermore, the absolute value of this minimal electric charge is in good agreement with inferred measurement.~ of the charge carried by the atomic electrons. 1 and therefore is accepted as the most aocurate va!ue of the charge of the electron.

1.2.2. The Experiment The apparatus used in this labomtory (Fig. t .2) consi~ts of two para1 lel brass plates l/4 in. rhiclc and approximate))' 2 in. in diametc½ placed in a lucite cylinder he.Id apart by three ceramic spacers 4.7 mm long. This assembly is in tum enclosed in a cylindrical brass housing with provisions for electrical connection~ and containing two windows, one for illumina tion of the drops and one for observation. The top plate has a small hole in its center for Ute admission of the oil drops,. which are produced by spraying oil with a regular atomizer.

To charge the plates) a 500-V DC power supply and a reversing switch ure used) the plates are shunted by a 50-MQ resistor to prevent them from remaining charged when tl1eswitcb is open~ For observations a lO·cm focal.

length microscope is used (Cenco 72925) .. while illumination is provided by a Mazda 1017-W lnrnp and coodcnsing lens. To avoid convection currents inside the apparatus, n heatrabsorbing filter (Corning infrared-absorbing)

is placed in the illuminating beam.

The plates should be mad~ pcrpendicublr to the graviLatiorutl field by means of the three leveling screws at the base of the apparatus and a le,el ru, in c / m experiments., shot noise IUC1lSUremc,us. ~lC.

. . - . . . .

~--."

.. . ..

. . • I . .' . .. 4 . . . .•• . •. . · • . 1.2 The Millikan 011 Drop Experiment 5 I .. ...... . " . • .....

. .

. ..

I • .t . • .... .

. .I Il l. . .. .. - • . . " • . • . . . . . . . . . . . ' ' ff~~ H IN . l t . -~ .---- ir- . o . f _ ilte r$ + . .... ..

. . .. . .. . . . . . . . ' .. . . ' Burgess~20 soov .. .. (approx.> . .. . . ..

. . .. . .. . . . . . . . . . . 6V ...

. .

..

. ' 0 . . Pofarity switch ... .

. .

.. . . . .

. . . Miaoscops .. . • . .. 1 . \ \ . Oil op&nin,g . .

.. ' . 110V . . . .. ac . . . . . ..

FIGURE 1.2 Mil.li.k.aa oil drop cl.pcrimcnt ~hcm~t.lc: of the app::i..ratill..

. .

. .

placed on the top plate. Being n cosine error. the deviution introdu~d hy an ..

. .

. . angular displacement of the gravi~tional component from perpendicular ..

. . . .. by 8\) is l %. A value for tbe plate spacing s may be obtained by using the sts.ge micrometer. The micrometer should be focused oo a wire inserted in t.he oil hole in the center of the lop p1 a te~ and the cross hnir of the micrometer should bemove<l i.11ong lhc lcnglh of the wire. Several measurements should be taken and their resultS averaged.

The velocitie~ are determined by measuring \,·ith a stopwatch lhc Lime required for tl1e droplet lo cover a specified number of divisions of lhe micr<i~cope scsle. Cnre musr be taken to avoid drart.s and v-ihrations in the vic1ni1y of the apparatus: for that re~imn and because of Browaian motion, lhe drop may wander or be displaced out of the field of the microscope. It tn2.y dten be oecessa1y to reposition the microscope between measurements on a single drop. :t\loreover. lhe drop should be kept in focus to avoid parallax errors.

Both tbe micros.cope and the ligbt source may be adjuslctl by viewing a ~ I I, 0 :,man wire inserted 1n rhe oil hole. The light should. be .ldjusltd so that the I • focal point is somewhatahend or behind the wirennd the wire is moreorles.s 1 • 1 • \",.. evenly illuminated. To light the scale. a $mall light~ pJaced next to the slit ll,1 o \'II, I jll"'l ah~d of the eyepiece of the microscope. The acruaJ distnnce to which ...

I • ( .. a scale division correspond& may be found by usiag a microscope slide (' ..

{' f:: ..

i l Exp erimenu on Quantization on which a subdivided mil limetcr scale has boon scratched. 2 The eyepiece focus of the microscope shouJd not be changed during a run. since moving the eyepiece chaogcs the effective distance of the scale. (To bring the drop back into focus the entire micro~ope should be n1oved.)

Itis irnportanU.obe:.tparing in the amounto fo il sprayed into the chamber~ In addition to gumming up the interior more quickly, ]arge quantities create so many particle.~ in the mic;.oscope field that \vithout excessive eyestrain it is virtually impossible to single out and follow a single droplet.

Under the influenoe of gravity, droplets will fall nt various limiting speeds. If the plates an.'l charged~ some of the drops ,vill move tlowo more rapidly~ whereas others wUl reverse their direction of motion si nee in the process of spraying some drops become posi lively chm:gcd and others nega tively charged. By conceotrnting 011 one drop chat can be controlled by the field, nod manipulatio g the sign of lhe electric field so that this particufaT drop is retainedt it is possible to remove all other drops from the fickl The iicniling velocity is n;ached very quickly and the measurement should be started near the top or bottom of the plate. Measurement should be completed before the drop has reached a point in its travel where appU cstioo of the reverse potential is insufficient to save the drop from beiog ugobbic:d up.,,.

3 3 The deosily in air oft he oil used was 0.883±0.003 g/cm . It is desirable to talce mca~urements in the shortest possible time $ince, as previously mentiom!d. the mass of the drop changes through evaporation.

It is al~o important to make measurements on as many different charge.-c; on the same or diflercnt drops as possible. Thus after four or five measure t!;l, ments of t~). and tc, have been taken. lhechnrge on the drop must be changed~ this is accompUsbed by bringing cJose to one of the windows a 60 4 radioactive source (10 to 100 µCi ofCo will do). The droplet should be brought c]ose to d1e top plate and allowed to fa)) with the field off; oo its way down it will sweep up a few ions created by tho source. This can be checked by occasionaUy luming the field on to sec whether the charge has changed; rarely will a clmp pick op any charge when the field is 011.

The power supply voltage should be checked with a 1% digital multi~ meter (D~); micf'05cope cnlibration should be ch.edred before and after 1 Notelhat the focal lea.gth of the micmscope must not be coangcd, bu1 instead the slide shmild be brough~ irito the focal plane.

3Thts may be found hy n simple m~uremcnt.

4Ci =Curie:::: 3.7 x tom disintegrations per second.

....

....

I. . ,_ . • . • j. ..-..•. • I. -.., .

I. .1". .t . , 1.2 The Millikan Oil Drop ExperimEJnt 7 I. .•. ., .

I • ' I. .•. . ' I • ' 1.92 I • • I • • I • • 1.9 I • I • • I 68 6i"' 1.ee ci1 1,8,t .:, -I .._. I.a;?

,=- J.8 ..

I J. 78 1.78 to 15 ~ ~ 30 TPmp913ture ("C} . .

FIGURE 1.3 VisOOdiity of d.ty ll,jr a.c. a foncJ{<m M tc:rnpcrahlrc. The data poinlS are 1aken c.

from D. Pnuc:li and Gutfingi:r. Fluid Me.cllJllliC!, Cambridge Univ. Press. Cl.mbridse.

.. . tJK. 1992. Thbk H--l.1lai:sic points are fittecl to a second-Order polyl'lomial 10 intc:rpulal<= I()

tile te:mpe.mrure in the laboratory.

..

. . lhe mea5urements. The same holds true for air tempernture and pr~surc, which arc needed for a correction to Stokes~ law.

Indee~ when lhc di~mctcr of tbe drop is comparable to the mean free path in air. the viscosity 11 in Eq. (l.2) s.houIJ be replaced by5 ]-I = b ~(T) '1o(T) [ 1 a P (1.6)

where tJo(T) is the visco~ity nf air as a function of T (Fig. 1.3), b

## 6.17 x

o -6 , P is the air pressure in centimerers of mercury, and a is the radius of the drop ia mete.rs (oo lbe order of 10-6 m). In analyzing the data it is convenient to calculate ao by lening 1J = 11o(T) fo the "a:ond of 5 This fonnu.la. aiteJnatively parameterized with b/ P = Al, whi:~ l. is the mean-free ~th of th~ nit molecuk:i;, w21.:> the ~ubjecl ofmuc:h resurrh by Mil.lik:m and many others.

Sc~. for cumpk~ R. A. Millik.in. PFrys. Rt'l'. Z~ l ( 1923). Our v:ilile fot b js wen fl'On\ Y.

Loqtlda, Pity!. Re-.,. 21, 550 {1 923), Table I.

8 1 Experiments on Quantization Eqs. (l.5); ao is then inserted in Eq. (1.6) to obtain 1J(T} and thus a more accurate value for a.

1.2.3, Analysis of the Data Thble 1~ l is a sample of data obtained by a sturJem. Two drops were w,ed and ~cvernl charges were messure.d; for each charge six measurements were perfoirned and averaged, with the results shown in Fig_ 1.4. The drop radiu.~ a v,ras determined frotn the average values of 1 / ro. The viscosity rJ ~e.,; the correction from Eq. ( 1.6). Values of n that give consistent values for A== 1(1/t+) - {1/t-))/2n were identified The pertinent parameters for these data were Pist an« of fall ti; 7.63 X 10-4 m ~CW'e T - '2..'>°C Press~ P 76.01 ~m Hg ~ity p' ~ p-a 8&2 ksfm3 Polcslli3J V == :500 V Plate scpal1Uio11 = 4.71 x 10-3 m TABLE 1.1 Data fmm th~ MHlikan Oil Drop &pcrimcnt ;(1t} 0/r+) - (! /1_)

to + "

2n Drop 1 -27.9 +&.69 -.5.65 J -O.l46 -29.6 +1.36 -1.18 !i -0.158 -28.2 +3.66 -3.00 z -0.152 -29.3 +O.iS -0.716 'il -O,l5l -29A +2.35 -1.97 3 -0.155 => a == 4.66 x 10-7 m t'/ 1.58 X 10-5 N•slm2 Drop 2 -24.22 +3.9H -3.071 2 -0.144 -25.75 +9.TI -5.6.5 1 -0.140 -2S.4 +2.5 -2.12 3 -0.145 -25.22 +9.67 -5.42 l -0.144 -25.22 +4.1 -3.07 2 -0.143 -24.4 +1.73 -t.73 4 -0.l44 -24.4 +9.95 -6.02 l -0.133 ~ 0 =.5.04 X lO-? m 11 ~ 1.60 x 10-5 N · slm 2 I I . • • . . . • ' ' I, . • . ' I , . . • . ' 1.2 The Millikan Oil Drop Experiment .9 I • ' I .A ' • I • ' • I . • 1~~------------------- I • ' .I .• . I . • Drop 1 .' ..

. '

## 0.5 Fie la Op~ <3ravfty

.. - . . ~e &,~~-------------- . - ..

' ~ Field Aiding Gravity . •.

- I ..

. ' .. -1.5 '------'------L------'-----~ ' -10 -5 0 5 10 s, (Number of aleclron cllargas)

.. ll.8 -~~-------..----------- 0,6 . . . . Cl.4 ..

-(12 . ...

. 1 ..a 0 ...

..

-0.2 I • -0.6 -o.a ~---------..___ ________ __,, -s 0 5 n (Nl.lJ'f1ber ol ASactron charge£)

FIGURE l.4 Plots of 1/i+ and l/t_ ,rersu~ 11 wbc('(;?n is an inu:gc.r. Negative YiU\lcs of n we us.ctl u-. ~~t the data '1lken \vith the-electric field pointing downward (i.e .. I+). The.

d.lta art from 'Thblc J. 1.

10 1 EX pt! r•m ants 011 Ouanttzation Averaging the appropriate columos in Table LI (See Eq. (1.5)) we find that = = A1 -0.1526 ± 0.0046 s-• B1 0.0346 ± 0.0009 s-1 lef ::: (1.52 ± 0.05) x 10-19 C Ai= -0.1419 ±0.0042 s-l B2 = 0.0401 ± 0.0(UO s- 1 le.! == (1.55 ± 0.05) x 10-19 C, where the values of ~ are calculated using the value of A and the drop radius as obtained from the value of B. They .ire in good agreemenr6 with 1.he a~epred value Jet 1.602 x 10-•9 C, Errors on A and B are simply taken to he the standard deviation of the set of me~~urements. (See Chapter 10.) The dnta are plotted in Fig. 1.4 along with the straight line!i predicted hy F.q. (l .5) using Lhe ,-alues of A and 8 derived above.

The realization that the elemental)' (hodronic) particles nre composites of qaarh that have electric charge of½ or~ of the electron's charge led to a revival of the Millikan experi menL Automated versions of the e."<periment have been built nod ro.n for a long time withoutr evealiJ1g any such fr.tctional charges.

1.3. THE FRANK-HERTZ EXPERI1\1ENT 1.3.l.. General From the early spectroscopic work it was clear that atoms emined radiation at discrete frequcnci-es; from Bohr's mode1 the frequency of the radiatioo v is related to the change in energy levels through A E hi,. Further experiments demoos.trated that the absorption of radiation by atomic vapors also occurred only for discrete frequencies.

6 1t is see.n thAt in thh ~pecial case {pQ.nJy ~LLi.e of th(: low voltage), the diam~of th~ drop1 is s,> small &hat tho correcrioo to the Sto~s e')llalioo, i.e., Eq_( J .6), i5 considerable (about 7%)_ 7 See.. fOT eumplc. N. Mar ttJ aL, Phys. R~ D 53, 6017 (1996).

r,.-.......

t;i:,····· ... .

:---~:-:-: ..

~--= ...

. ~ ·:· :-:- 1.3 The fra nk41ertz Experiment 11 ,..4- .. ..

~:~~ ~ ~ ~ ~: 11 is Lhen to be expected that the transfer of energy to atomic electrons by ~::: .'_a,ny mechanism should always be in discrete amcmnt41 8 and related to the ~::::: .'~mic spect.l'Um through the equa.li-oo given above. One such mcchru1i:sm ~:::: :0·f energy trMsfer is by the inelastic scauering of electrons from the entire ;.:::::-'.atom. Uthe is atom that bomba.rded does not beoome ionized, and since :=::::~·little energy is needed for momentum balance, almost the entire kinetic :::: : : ~ :~ergy of the bombarding electron c-an be rraru;ferred to the atomic system.

::::::::::.J.

Frank: and G Hertz in 1914 set out to verily these considerations, ....

:::::::-fuimely that (a) it is possible to excite titoms by low-energy electron born- ~::::: ~i:rdment, (b) that the energy transferred from the electrons to the atoms •:·:·:··always had Jiscrote values, and {c) lhat the -value::; soobt.aincd for the energy ::::::: ievels were in agreement with the spect.ros.copic rcsuhs.

::::::::: The necessary appar:arus consists of an clcctron-cmini ng fl lament and ::::::: 'an adequate strucrure for accelerating the electron.~ to a desired (variable)

:::::::.potential. The nccelerated electrons are aJJowed to bombard the atomic ::::::: .vapor under investigation, and the ex.citation of the atoms is studied as a.

:::: : : : function of accelerating potential.

:::::::: For detecting the ~'\Citation of the atoms in the vapor it is possible to ::: : : : : observe, for example. the .ra<li ation emiue<l when the atoms return to the or ::::::: ·gi:ound tit.rue. the change in .absorption a given spcctrot tine. or some other :=:::::'¢lated phenomenon; however. a much more sensitive technique consists :::::'.:·of obsen'ing lhe e]ectron beam it41e1f. Indeed> if the electrons have been ::::: '.: accelerated to a potential just equal to the energy of the firsL excited 1evel :.:.:.::.:: some of them will excite atoms of the vnpor filld as a consequence wiH ::::::: Jose almost all their energy; if n small retarding potential exists before the ::::::: collector region, eleclrons that have scattered inelasticaJly will be unable ·=·=.:.

I • • • to overcome 1 • t and thus ,vi• ll not re~ch the anode.

::::::: The~e conditions are c~ted in tile experimental arrJngement by using ::::::: two grids between the cathode an<l ietlllcctor. When lhc potentials are dis :=::::: tributed as in Fig. l .5~ the beam ;s accelerated between the cathode and ::::::: grid l~ then ii is allowed to drifl in che interaction region belween I.he lWO ::::::: grids and finally tnust overcome the retarding potentia.l between grid 2 and ::::::: ·the anode. When the threshold for exciting the first level is renched, a sharp ::::: '.: decrease in electron current is observedJ proportional to the number of col~ :~::::: lisions thaibaveoccurred (product of the atomic density and cross section).

:::::'.:_When the threshold of the next level is reached. a further drp in the collector ... .

:::: : : : current wilJ be observed. The~ currenl decroas~ {dips) are Huperimposed -.,, ---- .I- ~_-. .... • • • : .. : :.:: '.. : 8 Whc:n they ~main b<l11nc.l ~ft.er the collision .

... . .

I..• ... . .•. .

... .' I.• • . .

I Al- • • I I . . ~. • . . .. - . • • ' ' • I_.- • .' • I ,. • ' 12 1 Experiments on QuanOzation Grid 1 Grid 2 Calhode' Anode I I v~ {a)

_______________ .._...____.

(b)

v~ {c)

1-,1~=:::;;;..J~------'--~---, v~ -----~--~-~----~-- FlGURE 1.5 DifTerenr ~unligufllti1lD3 of me p(llentiiJ in a Ftaak-Re:rtz ammgcmerrt: (Q) For ()bservatio.o of a s.l.ngl~ exci~ (b} for oh.11uvalion of a nml,iple e~dtation, attcl (c) for m(:llSurlng the ionization potenll.al on a monotonically rising curve; indeed the number of electrons reaching the anode depends on Va s:c~ i nasmoch as it reduces space charge effects .and elastic scaneriPg in the dense vapor. In addition, the dips are not perfectly sharp because of the distribution of velocitie.~ oft he thenniooi ca.Uy emitted electrons. and the en crgy dependence of the excitation cros~ section.

An alternate distribution of potentials is shown in Fig, l..5bt whc:re Vacc is opplied at grid 2 so that an electron can gain further energy aft.er a col lision io the space b elw een the two grid~. In this case when Vi,oc reaches the first excitation pot~ntial. inelastic collisioos are again possible and the· decrease in electron current is observed at the nnodc; whcnt howevery Va ce reaches a value twice that of the first excitation potential. it is possible for an electron to excite an atom ha1fway between the grids, lose all its energy, and then gain anew enough energy to excite a second atom i.!nd reach grid 2 with practically zero energy. Thus it is not able to overcome the retarding poteotial to reach the anode, giving rise to a second dip io the current.

w__. . -:-:-: • »~·.·.·.· .

:=:: .·,.·.·. ..

n, : := :9 -1 , : . : : . ::: . : . : : 1 .3 a Frank-Heru E.xpe riment 13 :»--:~ :.·:.-.:..:..

:=::.:::::: .rtie-advantAge of this ~lup iB that the current dips are much more pro- ~::: :~:o~oc~, ~nd it is easy to obtain favcfold ?r. even l~ger ~ultipli~ity in.

:.=•:·:·.i.he ~:::::A~ec.rxvCe1 tat1on of the first level. However. 1t ts practtcally 1mposs1ble to the exdratlon of higher levels. As before, a slight retarding poten ~:::: ·,µa_l is applied between grid 2 and the anod~ and an acceJerating potentfal .~·::-::: :· ::_-:b~,-t~;rw·toe cn-the cathode and grid 1. sufficient to overcome space cbarge effects pro1.iidc adequate cl~tron current. It is evident that the densicy of the ~:::::.:~f~ic vapor through wh1ch tho electron beam pt\S&es greatfy affects the ~::::::~rveo re~ullh£ Low densilie~ re~uh in large electron currents but very :=:::::· -~~ dips; in conr..rast, high density has a~ a consequence weaker ~urrents ::=::::: ~~t proportionally Jnrger dips. \Vheu mercury vapo..-is used. adju.stnlcnt of ~:::: 'ui,e_tube lemperarure provides control of the denshy.

~:::::::. _Another important point is that in principle tbe experiment mll'it be : :: - = :- : : : · :: : ~ · i ~ ~ formed with a monatomic gas; si nee if a molecu]ar vapor is bombarded.

is possible for the electrons to transfer energy to the moleculnr energy ;:.::: '. :(~y~s which fonn almost a continuum. Some of the preferred elements for ~=:::: .~e Frank-Hertz experiment are mercury. neon. and argon.

-:-:•: ·: .. The same apparatu.s ~a.n be lL~ed for a.he m~'\urement of the ionization ::.::: : :potcntfoJ-that is, the energy required to remove an dccu-on complcte]y :=-::::."f~m the ntom. In this case. instead of observing tl1c bombarding clcc ~::: :~n beam, it is easier to detect the ions that are fonned. The da.$;tributillo ''"" : . :: . :: . . 'o f potentials is as shown in Fig. 1.5c, where the anode is made slightly '":•:-: negative with re~pect to the ~lhrn.Je; no electrons can then rench the ~:::: :ano~c. which becomes an ion coUcctor. The accelerating potential is '":•:·'. .. increased until a. ~harp rise in the ion current measured at the anode is 1'""·.··-,.··..··o.b d ~.-.,,,·.. serve .

,, ~:::::: In both types of measurements the val nes oht3inoo Io r the accelerating ~--:·potential have to be corrected for the contact potential difference (cpd)

:=::::: .)?et ween cathode and anode. 9 If in the excitalioo experiment the same folic!

:::::::~~as been observed two or more times. bowever, the potential differenet: :=::::::~tween n<ljac:enl peaks is an exact measure of the excitation energy, since ~::::)he cont.act potentiul difference shifts the whole voJta.ge scale. Once the :-::::: 'excitation energy has been found th¢ contact poteotiul difference is glven '~"·:·:·: :: ·by the difference between this true value and the first peak: in tum the ..

...... - .,,,A.,1.(, •, /.'~..... · ~ -"·.-' --- ~:::: '.' M efiy this is be.cause. the ';VOtlc fMcli on'' fat the me~ of which the anode is rm.di: is :=::::'.-.usually hig~t thru1 that of lh~ ~lhode. The \VOrk function _is a measure of the .. i.orumtion ,•:•:-:.potentilll'" uFthc mcral, that i.s, of the cmc.,gy aeeded to e.,tracta.n electron from it :I:":.:·.- .. :• .· ..

»:::: .. ·.

..

: - .~ ~ ,.: :. . ~. : . : -r- .-.·~.·- .... · 14 1 Exp1Himants on Quantiut~on contact potential difference. so found can be u~ to correct the ionization potential measurement..

1.3.2. The Experiment In this Jaborntory a mercucy~fillcd tube made by the Leyhold Company (55580} was used. . the electrode contigurntion is shown in Fig. l.6i and the circuit diagrams for the measurement of e~citation and of ionization potential are given in Figs. 1. 7a and 1.7 b, respectively.

As seen in the circuit uiagram, grid I i ~ operated in the neighborhood v.

of 1.5 and the retarding potenM! is of the mmc order. The anode ~lll' orocr rents are on the of 1o -9 A and are rne.a.~ured either with a Keithley 610B elec.t.romcter or with a higb·input impedance digital multimeter1 for instance, Hewlett-Packard 3440) A; adequate Mie1ding of the leads is required to eliminate AC pickup and iuduced voltages. The diagnun of Fig. L7a uses the distribulioo of potentials shown in Fig. L5b, and tile accelerating volt.age can be mea.~ured with a DMM in steps of 0.1 V.

The Fmnk-Henz tube is placed in a small oven. which is heated by Ji~ voltage through a v3riac~ it should be operated io the vicinity of 2(){)°C for the excitation curve and between I 00 and 150°C for the ionization curve.

To measure the temperature a coppe.r-constantan thermocouple should be FIGURE l .6 Skdeh of a cylindrical Fran'k-Hcnz tuht=.

.-.-.·.·.

. . · . . .....· .... ..·.. .· '.. .

W ~ ·..A ·. . a . . • . ' ... .... i .3 The Frank-Hertz Experiment 15 .. · . . . . . . '' ' . ' ' :--~········ ;-;-:~·: :::::~~:'''·ca·} .. -·. . ·. . ·. . ·'' . . . ' ....· .·.·.·.·.· .

0 . ..- . . . - . . . . . . . . . . . . . .' .

:~:::.. . . .. . · .. . . · . . . ·.· . . . ·. ' ' . · ' ' ' ·.·.·.·.·, :.: .... .

' . 300 Z ~ ..·. •. . . . · . . . . . . . . . · .a . .e ·. a . 'O .· .. . .t . ' I . I .' ' \ 10W 1½V Ory call •.. .. .. .. .,.'.. L{+ Z ... .. ' :~: - :: : : •. . . . . . . . .. . · . . . . . . · a . . . · . • . . . · ' I . ' ' · . I ' . . • $!1 6 )r V :IS ,0 i . •~ .I . i . . - : . . · . . . . A . . . . . • · . . . a . . . . a . . . a ' ' ' I . ' 0 t. ' I . ' I I . ' I 0 t . batte~ r.- _. ' :;: ...I .I .

·~... _.. t .I.

.. 41 . 1 . . • .- . .• • .a . • 4 .I .I I .• . .

~. . .

...

...

. .

.I .

·.

. • .. ·' .a: .l. . .•: . -• : . -I . : .

(h)

. ~ r . . . , .. . .. . . • .... .•.. · . .. . . ·. . I ...__. ..... ___. ....j, ~ --= A ~ . s .. : . . . . , .. o . _ - _ -, . . T e o kl c K ir o o ll m hl e y t 6r r~ · . . . . . .' . gl l'2 ... .

i~i: -······ •J11:.-:-~ <•I ·~· .• . ·.a ·.

·.

: X -:• ... . · . . · . ,· .· ~:--..:·.. .. ·• .·.I ..·I .· .. • . . • . . . ·.· . . 6V SV .Z... .

I ... • I I Storage .i . i. . :. • . .• . . .I . I .. . I . ' • ' ' battery . . .. . . . . . . . . . .. . . I .' ' • .. . . .. ' ' .' : X =: • :.. ... :• t . • /fl~URB 1.1 Wiring djagrarn for the Fmnk-lknz i::x~rimcnt (a) for observation of .. .

~:.-.:. .•. : ~. Jcita.ti~ and (b) for observation of ionization .

:.:. . .. . ... .. ' '.

~ ' ~:~: :ijjserted through the small hoie of the futrtace. The junction should be :=:::: or :positioned on the side the ,ubc near the electrodes. The other junccion is ~:::: ~immersed in a thermos of ice and water bruh. The potentlaJ deveJoped across .... <\ • ~::: :we lherrnocoupJe is measured with a D~lNI; Fig. 1.8 gives a caJibration :curve i':•:· for the copper-constnntllil thermooou plel ~~.,-.. :.... :J .•·• The ~:::i~ resolution and definition ofboth the excitation and ionization curves a function of ntom density (temperature) and electron beam density (fila :,.::::~~ent and grid I vo]tage) aod the e.~perimenter must find the optimum :-:=::~¢~ndi1ions.. However, for fo.rgc beam densities a discharge occurs. which.

::;::::?.~iously.

$houkl be avoided.

:~:·:=::·::: :··A suggc.4ttcd adjustment procedure is to set grid 2 at 30 V and then . :~vance grid I until the discharge sets in. as evidenced by the immediate ..

.,· ..- • ' ....

')"• »• ..... . t .

.~. J"..·· .• ..

....

,...

~,I".·.·.

-..--;.~.. .... - JI.

16 1 Experiments on Quantization 12 12 ~ 11 11 ~ 10 f>olenli0m8'er jg i~ ;8 ; 5 5 ~ 4 4 3 3 g ~ 2 ~ 1 1 O015--1.--..&o..........__ ______ ._,.L--.I___,......_ __~ .,,.___._..___.__.___,___.__~...____, 0 20 40 60 80 100 120 140 160 180 200 220 Junciion temperature (0C} FIGU~£ l .S Calib-ration of wppe:ryco:astan~ thermocouple using ice stuldard.

build-up of the anodecunent. Grid 2 should men be quickly rcrumcd to OV aod grid 1 ~et :,lightly below the discharge voltage; a reasonable filament voltage is between 4 and 6 V. To determine whether the tube is overheated it can be taken out of the oven for about 30 s; the collector cwrent will then increase and maxima may appear if such is the case. l f the tube is too cool, the emission current will be large~ and the maxima.. particularly those of higher order, will be washed ouL It is pos~ible to use an oscilloscope for a simultaneous cJisplay of the .

electron or ion current against accelerating potential. The sweep generator (~awtomb) output is fed to 1ht OC(:elerJting grid. while it synchronously drives rhe horizontal sweep; the ourput of lhe clectr001etcr is fed to the vertical input. An excitation curve and an ionization curve obtained by a.

student in this fashion are shown in Figy 1.9. Alternately a ::.implc ramp circuit can be built to drive the accelerating grid ruid the digitized output of the electrometer read directly into a computer.

l.3.3. Analysis of the Data Two sets of data obtained by a student for the excitation potenli al are shown.

in Fig. l .10~ both curves were obtained al a temperature of 195~c and with I V on grid l. The filament voltage wa~ 2.5 V fur curve C and 1.85 V for ~····-·.· m~. . :-:.:.

m=:=:>: ~ij__,.;::::::: 1 .3 The Frank-H ert2 Experiment 11 :--...:.. ..

f.:§=::::··' · .. . .

ij)

~::l: itii: [::I: 0:,. .... ' i=:::=: f::::: .· A«ete..,ng PotenOB1 _. ..,,,..,..,.9 l'OtentJaJ-+ ij?\ Ca) lbl ~::)iGµRE

## 1.9 Oscilloscope display of a Fro.nJc-Henz experiment: (a) Beam current \'i

::3:::: ~leraring '(JOti:nLial. (b) Jon cuttent v~ acce.Jeratin~ potc:ntfal.

:::=:. .: •:':.

~ f.. ~ -. · . . . - .. , . ..... ·,· ("~~===~:::: ,.~.-.·,·.· t~. . • • Data G (2.5V)

4 I tr. ...... ...• · ,·. 9 r,..-~•_O_ata_ D _x_l_O. .__.85___.._____.

4 I f~ ,,_. • • :,a- • :• 4- :I I . a ...

(",~·"' "11;'.

.'..r.. ... • ... e .. • •. . I I I .s. 7 r.•:•:•:4~1 :-=,.·. .. -.·.·.

'I:.. ....... ,' I ~ J9 .- :•: a • : I • I :- I I• r .. ... ..

r...· . . ·.·,·.· t ..• .. · .. .· .· ,. ' .rr.:..~•.. -....: .- •: I-:I - .·~-- I t..·. ..· .. · ... . . I. I :("p, -:-:-~ ' '· . . · . 2 f •. :.-.: < .I - I ~ l -..

(;-"• : .. •- .

. .... .

.l ..

I ·.• o~ ---~~--~--~-~~-~--~ tI .. i ..

-.

·.

..

-.

., ..

a· _, ..

· .I · 0 1D ts 20 25 ..

•.J". . .. . ... .... .. . G~ Accelerating {V)

:::.,..::.:. f)..G URE l. IO Piot af be.arn current versus nttel.er.lting vol ta~ in Franl:-Heru expcri- :•:•:-:-(n~nL Daw for C\Jf1,'C C (~p<Jinls) 1m:: ubUlin~ wilta th~ nlam~t 5et~l 2.5 V wruk data • I . :. . • . . . :. . . • . .: - • · . · 't • . f · l ! ' i;u,vc D (lCW\,;-cr points) are olJtaincd with filament ~t 1.85 V.

~ ... .. . .

tI '•.r• ••.• ' I ::=:::: ~urve D with the consequent decrease cf die elecr.ron current by a whole :.;:::::~e.cade.

::::::::~::Re~dings are taken for 1-V changes on grid 2 with srruiller sreps io the :.::.::.::. ~v ~d nity of the peak. A significant decrease in electron (collector) current .. ...

I. ..... .• 1 I.

..,JJ.JJj • I I I I I . . . . • • . . . . . • • . . .. . . . • a . ..,. . I I I . . .

·~.,JJ·JJ/J ..·a. ·• .

..: :-:.

~ ...

18 l Experiments on Quantization is noticed every time the potential on grid 2 is increased by approximately 5 V, thereby indicating that energy is transfem<l from the beam ,n bundles {'~quant1f') of 5 e V only. Indeed, a prominent line in the spectrum of mercury exists at 253.7 nm? corresponding to 1237.8/253.7 4.86 eV. arising from lhe transition of the 6s6p 3 P, excited state to the 6s6s lSo ground state.

Our interpretation is that the electrons in the beam excite the mercu,:y atom from the ground state 10 the 3 P1 ~tale, thereby losing 4 .86 e V in the process.

The location of the peaks is indicated in Fig. J .10 and wa.~ measured 1~ this case with a DMM. The average value obtained for the spacing between peaks~

## 5.02 ±0.t V

lo be oompared with the accepted ~pectmscopic value fur the energy level difference {as iureacly mentioned) of4 .86 eV.

Using the vaalue found for the spacing bct\1;1een peaks and the locatiot1 of the first peak, we obta;n the contact potential (6.65 ± 0.15} - (5r02 ±0.1) = 1.63 ± 0.18 V.

As discussed in Section l .3.1, with the configurntion of potentinls osed (Fig. 1.5b) it is more probable that the same energy level will be excited twice rather than that several different levels will be ~'lcited; indeed, this is the way in which the data Fig. 1.1D have boen ioteq>rcted. This is .

not surprising if one considers the excitation probabilities for the energy levels lying closest to the ground state of mercury. It i~ possible, howe;rcr, by using different grid and voltage configurstions (for example. Fig. ! .5a)

and improved resolution. to observe thee~citations to other levels, namely;, 63 P,.. fr I'o. and 61 Pi.

For the ionization potential, data obtained by a student arc shown in or Fig. J• l 1. A word of caution is to be added to the interpretation such ionization curves, which seetn strongly dependent on filament voltage and.

vapor pressure; indeed, the very sharp increase observed in ion current is due lO an nvaland1e (regenerative effect) of the ejected electrons ionizing more atoms, the thus-ejecled electrons ionizing still more atorns1 and so on, This avalanche does not necessarily occur as soon as the ionization threshold is crossed. II the vapor is too dense? the ions recombine before reaching the anod~ thus masking the effecl until complete breakdown sets in.

s~c The curve shown was ttikeo at a temperature of 15 with a filament v: voltage of2.6 V. If. then. the onset of ion current is taken to be .-t 11.4±0.2 ...... .

,._,.-_16". .- •.•• •• .-A":-:-:,: .-~. .- .....

, ~ = '£4 - • : • -:- • · 1.3 The Fraok-Hertz Experiment 19 :?.:==::::: r,:~~ ... -.·.·, ,z .--------------,.- -----.

~::::;.-.

·.=.;.~..- ..~ -:. -··-.··. .· ...

, r . .- : .- .: ~ - . : . - , ,, · · . .. · . . , . . . tD ~-=:::::,·, :-.h.-.~ /. :-: .·. < .

8 • ~~,,,. .. T ~/.-:-:-.. .

::::=-~.:-: . .~....

~:-:-:-·.· I .

~ !• • • :=:::::::: -.. . 8 •..

I' ... • . .

.~.- ~/:. j ' • " = - - ~ " . . . ..- .- . . • • ' . • . .

r,,.r• ..

~::::::: 2 _, ~~ -".

,-~. .-.-:-.:... :.

. .

5 10 t5 .:x ..:.:.:.. :::-.

,.,,, . ... .. G G Aoe&lerellng M ·._ . ... 1 2 i~:-:= . .: : = ·:I ~ -1 ~ .0 M UR E 1. J L Ivnc11~ m1 1crs~ s.r:oc:kr.111ng ,•oh.age-in the Fr:mk- Hcmexpcrimcnt. The ot 8 V 1s due to che phoroel.e..--uic effect.

;x. .: . :-: :X~:~~d usiog the value for the contract potential previousJy delerntined (fron1 :J'.-:.; t he ex.citation curvt). l .63 ± 0. J 8 V. the ioniMttiun potealial is obt.iioed os "'"'~· ·· •.:a, ... .

± ± = ± :~:~:'.:'.:' (ll.4 0.2} - (1.63 0.18) 9.77 0.25 eV [.::,,=:. .-~ ',:,,-~• ••~ t.y in fair ~ment with the accepted value of 10.39 eV.

:~:?::=:::-: ;~.At.n additional feature of the curve Fig. J. 11 is a "knee·· in tbe ion cur set.ling in at appro){imatcly 8 V: 1hc observation of this ''knee" as well ~:::.t~~1rongly dcpcn<lcnLo n l.h~ inmpcrawro and current den~ily. but can be ~ :: "t;t>nsis1cntJy reprodu~ d over a consjderab1e range of LhC$C paramctcfl>. ln i~ :::: cµdcr co undcrstnnd Lhjs behavior we remember I.hat the arrival of ions at ·qie anode is equivnlenc to the departure of electrons; indeed, the ob.,.erved ~ :;~~bavior is due to a photoe]ectric effect prodllced al the anode, by short- 0::::s¥/1velength light quil?lta (the electrons are furtheJ' accelerated by grid 2).

~ :: ~hen lbc electron beam re~bes 8 V. it can excite the 6 P1 level (lying at ~::-~:7 eV above the ground state. pJus 1.63 V for contact potential difference), ~:~-~I? !he mercury 3.lOm~ radia1c the ultraviolet line at 184.9 nm when muming ,-:=::;-.<:7,tne very grouud state. TI1esc quanta are efficient in ejecting pholoeiec- :x:}!Ons from the anode, and the cyliodrical geometry of the anode jg most :x:: ~vorable for this process.

:x:-:-· :-: ....

~:-:~- : ;--.-: ~-.-·-·1·- :.-.. :.: ::::: .. ..•. .... ··..

-·~=-=-:- 20 1 Experiments on Quantization 1.4. THE HYDROGEN SPECTRUM The hydro gen atom is the simplest quantum-mechanical system. It consists of an electron bound, due to the Coulomb force, to a proton. It is character istic of bound quantum-mechanical systems that their total energy cannot have any value, but that the system is found in one of a discrete set of energy levels, or states. Transitions of the system between these states may occur. Such transitions must satisfy the basic conservation laws of electric charge, energy, momentum, angular momentum, and the other relevant symmetries of nature.

Transition from a higher energy state to a state with less energy can occur for an isolated system, and the larger the probability for this transition, .

the shorter the "lifetime', of that excited state. During such spontaneous .~: transitions of a quantum-mechanical system to a lower energy state, a quantum of radiation, or one or more particles, can be emitted, which will carry away the energy lostb y the system ( after recoil effects have been taken into account). In the presence of a radiation field the quantum-mechanical system can either gain energy from the field and change into a state with higher energy, or lose energy to the field and revert to a lower energy state.

For all quantum-mechanical systems there exists a lowest energy state, called the ground state.

By observing the quanta of radiation, or the particles emitted during such transitions, we gain information on the energy levels involved. The typical example is optical spectroscopy, which consists of the accurate determination of the energy of the light quanta emitted by atoms. Infrared spectroscopy deals mainly with the quanta emitted by_m olecules, nuclear spectroscopy with the quanta emitted in nuclear transitions, and so on. In nuclei, however, the separation between energy levels is much larger, so that the emitted quanta of electromagnetic radiation lie in the gamma ray region; thus different techniques are employed for detection and measure ment of their energy. It is also very common for nuclei to decay from one energy state to another by the emission of an electron and neutrino (beta decay} and for certain heavier nuclei by the emission of a helium nucleus (alpha particle). Similar processes take place in the interactions or decay of the elementary particles.

The idea of energy levels and their structure for the hydrogen atom was first introduced by Niels Bohr in 1913. However, a complete theoretical interpretation had to wait until the introduction of the Scbrodinger equation in 1926. Even then, for theory to agree with observation it is necessary to --~ilf l lllif

## 1.4 The Hydrogen Spectrum

~ {j;~cl~d~ ~dditio~al small effect~ such as the fine a_nd hyperfine suuc~e, ~ {:(elauv,sbc motJon. and other higher order corrections. These correctJons ~{)~,re derived using the theory of quantum electrodynamics (QED) so that ~}Joday we can theoretically calculate the energy levels of the hydrogen atom ij~}jo the amazing aceuracy of I part in L0 .

~If/ V-:~ We use _the Bohr theory t~ p~icl the. hydrogen energy levels, i~fJ1ecause ,t 1s so simple. even though 11 assigns the mcorrccL anguJar momen ~Jfif tiun to the states. The postulates of the Bohr theory are (a) that the electron is ~:t.::ftiouod in a circular orbit around the nucleus such that the angular momeo :::tg~um is quantized in integral units of Planck's constant (divided by 2,r); = = jj{}amely, pr= mvr n(h/2n) n!i; and (b) that the electron in this orbit i~f\\oes not radiate energy, unless a transition to a different orbit occurs. We ~~t{¢,4n then calculate the radii of these orbits and the total energy of the system, ~fjf »otential plus k:ineLic energy of the electron. The at.tractive force between f,I'. $-:-);·.h·• • '~ ele~tron (charge -e) and the ?ro!on (charge +e) or a nu~leus (of charge ~:f f ~e) 1s the Coulomb force, which 1s set equal to the centnpetal force.

f.~t}/ I i. The toL al mechanical energy of the electron is E=T+V ~fl} ze2 1 1 ~::::::-:: = ? (1.7)

2mir- 41Teo _r_· I::~::::::::.

~~rJt}+ij~zree m, v, and -e are the electron's mass, velodty, and electric charge, is the Charge OD the nucleus, and r is the "orbjtaJ radius" of the ~tfj~Jectr~n. w The potential energy, of course. is just the attractive Coulo~b ~{\yotential between the electron and the nucleus. We can relate the velOCJty t ~ :f 1 :: { ) : 1 ~ , dl o the other variables by using F ma, wbere F is the CouJomb force a is the centripetal acceleration. That is t=::::::::; ?f::;:;:;:• 1 2 2 ::cJ.::::::·::· ----2 e - = v m-, ;!'¼:-:·:-.

~=:=:?=:- 4,r eo r r ~rt fft.f ~ch implies thac «i~tr· :;C,?.rr-:::::: fif\. 2 l l Ze 2 0:~";:::::-;'. 1J = - m4 - rre - o - r - (l .8)

;,z,l:;:;-::;::. . -.

;-. i=··-·.·.·.· :-;?'~f{.

i..-·=~z~. ......-. - -- ff/f;· 10 we assume that the nuclcw is infinitely heavy.

,..~::;:::::.

tii~~~r ;q;--3:fz:::·: {'~...at:::; :e;,~::: ::· i/~1},?::~ tl&i:::;:.

22 1 Experiments on Quantization If we introduce this result into Eq. ( 1. 7) we obtain 1 1 Ze2 1 Ze2 I 1 Ze2 l E = - - - - - - = ....::.. ___ = -- IVI.

241reo r 4n.so r 24neo r 2 At this point we can impose the Bohr quantization condition Ii r=n to eliminate v in Eq. (1.8). Here n is the principal quantum number. We obtain 1 1 Ze2 m2r2 m 4n so-,-.

or !_~_l_ze2 r - n2 2 4neo · Inserting this result in Eq. (1.9) we find for the total energy 2 4 mZ e ] 1 En= - [ 2(4nco)2n2 n2.

For the hydrogen atom where Z 1~ the expression in brackets in Eq. (1.12) equals 13.6 eV. This is the energy required to take an electron in the ground state (n 1) and separate it from the nucleus completely (E 0). We refer to it as the binding energy of the hydrogen atom. It is customary to introduce the Rydberg constant (wave number) through En= -hcRoo 2 t where Roo = 10973731.534m- 1 and thus E1 -13.6057 eV.

Furthermore, from Eq. (1.11) we can write for the radius of the orbits in hydrogen ~l;l

## 1.4 The Hydrogen Spectrum Zl

-~llli},:.

OeV-.-----------n-.~ ~t}t ..

1=~-------n=S ~i:f:/ :-· _:::::::· 1----------n=3 i------------n=2 I;:=;;%::t::· ~.--··:·:· ~{%:::::-.

t~f\;- 1'.

- 13.6 eV..__ ________ n,:1 0}:(~~GURE I. 12 Energy-level diagram of lhe hydrogen atom according 10 1he simple Bohr &/it!7eory.

~¾·:::::- ~fl:· 'th ~-z-:,:,Wl = 4 = ~~~\\} . a /i, rrfo 0.5291772 x 10-10 m, fi/.. 00 m e2 ~:::::/ cal.Jed the Bohr radius ?-;::::::: .

/i/ ,: The energy levels of the hydrogen atom that we derived can be rcp- l\(reseoted by Fig. 1.12. However, tbe lines observed in the spectrum {}/60.iTespond co transitions between these levels; this is shown in Fig. 1.13, }(}where arrows have been drawn for all possible transitioos. The energy of //:~ :line is given by fa\} I : Mu - hcRoo ( .} - .'.,), (1.14)

fa/ where the subscripts i and f stand for initial and final state, respectively.

f f Since the frequency of the radiation is connected to the energy of each 1/.··-·.

~::::?quantum through i,•~.r.·l.·t.r · E=hv ::S:::one ... finds that I;,: - 1 -- -V --- E A C he 9.:::: ~···· ?ii~:~ r~~)

..· .

;:,, ¼:(: 24 1 Experiments on Quantization .

1 ~ii Pa 0 ' .. " . Ba 11)

,- X . 4 r-- .C.l '.)

t:.p ' , ', ' , . ' . .. "

FIGURE 1.13 Transitions between the energy levels of a hydrogen atom. The lines La, L13, etc., belong to the Lyman series, BC%, Bp, etc., to the Balmer series, and Pa, P13, etc., to the Paschen series, and so forth.

and n'.2) · (1.15)

A'.J = Roo (:} - Indeed, the simple expression of Eq. (1.15) is verified by experiment to a high degree of accuracy.

From Eq. (1.14) (or from Fig. 1.13) we note that the spectral lines of hydrogen will form groups depending on the final state of the transition, and that within these groups many common regularities will exist; for example, in the notation of Fig. 1.13 v(Lp) - v(La) == v(B~).

If n f 1, then nl )

Ail = 91.1 ( nm n· > 2 n?- - 1 i - and all lines fall in the far ultraviolet; they form the (so-called) Lyman series. Correspondingly if n f 2, then A;2 = 364.4 n? 1 - ) nm n· > 3 ( n.2 -4 i - ~~tif ~Ir

## 1.5 Experiment on the Hydrogen Spectrum

£:::::: •;::=::: in part ~}\fuld all lines fall the v_isi~le of the spectnun, fonni~g th~ Balmer ~~}=/series. For n I 3 the sene s is named after Pasch en and fal Is in the infrared.

l~m~:":t·-·:.--.:f·-:.-· ~-:-:-:-: 1.5. EXPERIMENT ON THE HYDROGEN SPECTRUM ~/f:.

.f .\ J.5.1.

General )fl::)? ,.

f f To measure the frequency of the radiation emitted by atoms one can use .~ ?>either a grating or a prism to disperse the different wavelengths. When ·tl>using a prism. ooe exploits the variation, with wavelength. of the refractive '?t iodex of certain media. Prism spectrometers are limited to wavelength ~[f~gions for which they are able to transmit the radiation: for example, ~f:)n the infrared, special fluoride or sodium chloride prisms and lenses are Jt\.used. In the ultraviolet, the optical elements are made of quartz. Also, the ~t}se11sitivity of the detectors varies with wavelength, so that different types .~iftMt used in each case (thermopile, photographic emulsion, phototube, etc.).

i4trr rn this laboratory a small constant-deviation prism spectrograph and a ~jf f2-in. reflection grating spectrometer were ~sed. We ~U co~sider in detail a W.~f / tneasurement of the hydrogen spectrum with the gratmg, smce an absolute ~f}:v.~ue ~or the_ wav~le~gths can be obtain~d ~d v~sual d~tection is used. A ~::!\{brief d1scuss10n of pnsm spectrographs 1s giveo rn SecL1on 1.5.4.

}/f·.

From Fig. 1.14, it is evident that the path difference between rays l and ~f\ ·i after reflection is ~!It .0;:~-:-:-.,·.

BD -AC = CB sin Or - CB sine,.

;{}:where CB is the grating spacing d. The angles 0i and 0r are both taken as it)

positive when they lie on opposite sides of the normal. Since for coostruc ~fl·tive interference the path difference musl be a multiple of the wavelength, ~rt we obtain the condition i~/-t;.:-r:- nl=d(sin8,-sio0;). (l.16)

~--·.·. .

~f{ It can be sbown11 that the resolution of ~he grating is given by ,:u.·.····.

~:~~:-:-· ~ff: .!:_ - n N ~.~;ii?::· b.)... - • ~¼-":.-:-:, ~[}"here n is_ the o~der of diffraction and_ N_ the tot~! number of rulings. The ~Jf } ame cons1derat1ons apply to a trans!Illss10n grating.

Wffi····· ~f:\{:: ~·.······ ll Sec Chapter 5, Sect.ion 5.5.

!~~,,.,,, ....

~ti ~I~-::·\: ~~f - 26 l Experiments on Ouantization FIGURE 1.14 Schematic diagram of a reflection grating. A parallel. beam of radiation is incident along the rays 1 through 4 at an angle ei, with respect to the normal; the reflected radiation is observed at an angle 0r. The spacing between the grooves of the grating is d.

Grating Focusing lens Collimator lens Telescope position 2 FIGURE 1.15 Diagrammatic arrangement of a grating spectrometer.

The grating is mounted on a goniometer table in the general arrangement shown in Fig. 1.15. A slit and collimating lens are used to form a beam of parallel light from the source, and a telescope mounted on a rotating arm is used for viewing the diffracted lines. It is obviously necessary to ensure ½:-:-:•:• ·~::::::: .Ill!!

## 1.5 Experiment on the Hydrogen Spectrum

t }~lelism of the incident aod reflected beams, normality of the grating, x:\~~d :so on. A suggested alignment procedure is as follows: ~~f}({a) is The viewing telescope focused for parallel rays (on some distant -=········s··· t)

.-fj~ .~ec .

·}// ·.(b) Then with the grating removed, the slit is viewed with the telescope ~1rt~ posi~on 2) to as~~in that the slit is aligned and in focus; in this way ::=:::the collimator lens adJusted.

tS '!> tf/\ .(c) The source and source lens are placed in position and the align ~}Jnent and focusing are again checked The cross hairs are aligned with the ~~r~l.it.

/ /~\. . (.d) This position of the telescope is carefully noted since it represents •;.•. . ·-·.·.· ..t }tlie 0° position. The readings on the scale should be made to one minute of ~f }ij.:degree by using the vernier and a flashlight.

:t\:.: (e) From now on one may have to work in dark, or by draping the .-....

:t)~pparatus with a black cloth .

••4 .r.·.·.·.

~:t:/: (f) The grating is placed in position and aligned for normal incidence .......

{ft(' r = 0). This can be done by "autocollimation"; a strong light is focused J { &hto the slit and a cardboard mask with a narrow slit is placed on the { f }ollimator lens. The grating is then adjusted until the reflected image of the \ ?/cardboard slit coincides with the slit itself.

If{: With any reasonable grating it is possible to observe the visible lines of }{)he spectrum in severa] orders; thus we expect the measurements for ). / d (jo be self-consistent, since -ttt . . ). J.. ).

.. - - · :: : : : : : : : : : : : : : : : : :: sm0m+l - sm0m = (m + 1) d - m d = d (1.17)

:r::::::::::: ;::::::::::: :r:-:-:-:-:-: ~=::::::::: ;.f)mdependently of angle of incidence ei, or order.12 The grating spacing f\/4 is usually stated by the manufacturer; for example. the grating in th.is .-.·.·.·.·.' ~ti/laboratory had rulings on the order of 7000 to the inch (d 3.629 x ~~J)o-6 m). However, d can be obtained by using one or more standard lines .,,,_;..·.·.· ..

::i:~{:};ff known wavelength .

..· ;ii( .-:=~:::::,_-:, -- -~-:-:-:, :f{:::, 12 Provided that both 8m and Bm+l are taken on the same side of the normal.

,:~l;~::l::::· ~ :::::-:-· 28 1 Experiments on Quantization The following data were obtained by a student using the grating spec trometer. The source was a low-pressure hydrogen discharge tube (Cenco type 87210) operated at a few thousand volts; a5-kV transformer and variac were used to provide the variable voltage. The useful life of these discharge tubes is limited because of the appearance of strong molecular bands after some hours of operation.

1.5.2. Determination of d To obtain the grating spacing d, sodiwn (Na) was used as a standard, and measurement on three lines (for the shorter wavelength of the doublet) gave the results shown in Table 1.2. Since for all the above measurements 0i is the same, it follows that + = and a least-squares fit to the linear relation fJx a y can be made; we have I N L(nkAk sin 0k) - I::Csin 0k) 2)nkAk)

-=--------------- (1.18)

d N L(nkAk)2 - [I)nkAk)]

TABLE 1.2 Diffraction Angles from a Sodium Source ).. in nm Ordern 0n oi = 19°12'

## 615.43 1 29°42'

2 41 °27' 3 55°581

## 589.00 1 29°14'

2 40°21' 3 53°49' 4 75° 15'

## 568.27 2 39°32'

3 52°12' 4 70°48'

## 1.5 Exp&riment on the Hydrogen Spectrum

where the sums are over k. k I, 2, .. . , N and N is the total number of measurements. From the data of Table 1.2 we obtain13 ~ = ± 5

## 2.7085 0.009 X }0 ID-I (1.19)

in good agreement with the manufacturer's specification.

Some care must be exercised when comparing wavelengths, since they do depend on the refractive index, n, of the medium in which they are measured, , c(vacuurn)

C = --- hence , 1(vacuum).

The wavelengths listed in most tables are given for dry air at a pressure of 760 mm mercury. However, any theoretical calculation, such as in Eq. (1.15) predicts the vacuum wavelengths. The refractive index of air at stp is n(air} 1.00029. (1.20)

1.5.3. The Balmer Series ~~// Measurements on the first four members of the Balmer series, which lie in the visible region, can be made with the spectrometer described above.

The data obtained by a student and their reduction are given in Table 1.3.

We observe that the obtained values for the wavelengths of the Bahner series are in agreement with the accepted values at the level of 1/1000. We can now test Eq. (1.15) and obtain the Rydberg wave number. We note that :i):.

~ = RH [~ - _J ] .

i~?: A 4 n2 ·:-:-··.

:,.:-:-: ~:::::· So that from a least-squares fit ..· -_·._.·.

=~:::: z::: " 2 :~::::. RH= L.., pi )

: ... = .· . : · : . : · : )..iPi :=:=::, :::::: .:: - : .. : · : . : · 13 In reaching this result we have constrained ~ = 19° 12'.

·~=~:::.

1(·: :~:::: :::::: 1.•.:..-.:.·- : ~::: .... r.· • :;·.

'' 30 l Experiments on Quantization TABLE 1.3 Data on the Balmer Series of Hydrogen as Obcained with a Grating Spectrometer Calculated ' Accepted Balmer series Color 0n sin 0n - sin Bi Order ).. ). identification Violet 33°121 0.22199 2 410.75 ±6 410.17 Hs ni = 6 41°15' 0.33378 3 Blue 26°16' 0.11698 1 34°06' 0.23483 2 433.82 ±8 434.05 Hy = 5 1li ' ' 42°42' 0.35259 3 Green 27°10' 0.13001 1 36°04' 0.26316 2 485.75 ± IO 486.13 Hp 1J,i 4 "

46°09' 0.39559 3 Red 30° 11' 0.17720 1 42°57' 0.35579 2 657.94 ± 14 656.28 Ha ni = 3 .

59°29' 0.53532 3 Note. All wavelengths are in nm. T.hese measurements used d = 3692.1 ± 30 nm as determined by the previous measurements on the sodium standard lines, and siu 0i 0.32557.

where 4nf Pi 2 4, n. - . .

grvmg ± 7 RH= (1.09601 0.003) X 10 m-l in good agreement with the accepted value M = 7 -1 RH= - - R .1.096776 x 10 m .

M+m 00 Here M is the mass of the proton and m the mass of the electron.

1.5.4. The Prism Spectrog-raph Long before gratings became widely available, prisms were used as the dispersive element in spectrographs. Prism spectrographs are handy for viewing a large span of the spectn1m and come in various ingenious optical 14 The difference between RH and R is due to the motion of the electron about the center of mass rather than about the proton.

,i ~ ::;:

## 1.5 Experiment on the Hydrogen Spectrum

~l.l: ~ ~::·: ~Ji· ~~-:-:: ~:-·-:- ~@\ m:/ ~:-:-:- &:{:: ..

~:::: ~ } ~\:.

~::~-:.

,"/..,"

~:~:::, ~*;:;:, if\ .

FIGURE 1.16 Diffraction of a ray at minimum deviation throogh a prism ofapex angle A.

~ifif ~ {: ·~gemen~s- The dispersion of a prism is a function of ~e refractive ~\t mdex; thus 1t cannot be used for absolute measurements without careful ~fr calibration.

(f!f?: In tbe case of a simple prism at roioimnm deviation (see Fig. 1.16) the ,.-z-...... .

~;.:::::::: ::diffraction angle () is gi veu by ~})ii sin~ ~:=:?::.;::: - = n 28r = A ~ {{{ sin 0, ~ ::::::::::thus ~:::::f ~=~i:;:;' = . (A +0) . A ;?:::::::: s10 = nsto , (1.21)

if\ 2 ~;-:,;., Ii.Ii_:!.:.: where 81 and 0r are the angles of incidence a.od refraction, respectively, ~= and A is the apex of the prism. In Fig. L.17 the refractive index of flint ~J{ glass as a function of wavelength is given. We note that in the deteonioa it\ tion of wavelength from the diffraction angle the relation is by no means .~~/::.:·:.:-?.·, linear and is in general of serious complexity. Further, most modern prism ~-=·-·.·.· ~?\ spectrographs do not consist of a single dispersive element, but of some f:1?

combination of prisms. The instrument used in this laboratory was of the ~\( "constant-deviation" type. and Fig. 1. I 8 gives the optical paths for an inci j f f ·clentray. It may be seen that the angle of incidence and the angle of exit can ~ff =remain fixed for all wavcleogrhs by an appropriate rotation of the prism; [~{?

this has obvious advantages for positioning and alignment of source and ;:-··· d ~~::::::: etector.

if}.-: The rotation of the prism is calibrated to give rough wavelength lnd.i- ff}·· cations. but measurements are made on the exposed photographic plate ~It ~:;:;: ~\: ~j;;;=;:; ~ ::::: "'~··=·:-; Yz--· -:,:~:.:-: 32 1 Experiments on Quantization 2.2 2.0 'O .s 1.8 §!

.:; ~ Flint glass ~ 1.6 a: Crown glass 1.4 2000 4000 6000 Wavelength (A)

FIGURE 1.17 Refractive index of various materials as a function of wavelength.

FIGURE 1.18 A constant-deviation prism and the diffraction of a ray passing through it.

or film. A known spectrum is superimposed on the spectrum that is to be investigated, and an interpolation between the known lines is used.

The general arrangement of the spectrograph is shown in Fig. 1.19.

Source, lens, and slit should be aligned and the sol;lrce focused on the slit.

By viewing through the eyepiece and varying the prism position, one can get a feeling for the dispersion and the range of the instrument. To obtain photographs of a spectrum, the telescope is replaced by the camera assem bly. Several exposures can be bad on the same plate; to distinguish different spectra superimposed at the same location on the plate, the "fishtail," which controls the length of the sli~ can be used.

## 1.6 The Spectra ot Sodium and Mercury

I Constant-deviation prism Fo cus l ng lens o-------0-- ---------I- ------ SourcG SIii ' ..

Camera lens:?, Bellows ! l !

: I I c...l•m-o Plate holder C . ' F FLGURE l .19 Schematic arrangement of \he cons1am-deviation spectrograph.

...

,._ I :c -,._ /::;::'. FIGURE 1.20 A spe.ctrugram of the first four lines of the Balmer series of hydrogen as :~;:;:;:;. obtained with the constant-deviation spectrograph.

!!lilt ~?> Figure 1.20 sbows the first four lioes of the Balmer series of hydrogen t{::; obtained with the "constant-deviation'' spec1rograpb. A composite expo t?{ sure cootaining l1yd.rogen, sodium, and mercury lines is shown in Fig. 1.25.

~l]l!Jt :~:~::::: L6. THE SPECTRA OF SODIUM AND MERCURY ~;:}f/ ~===~::::.

x::::=:=:: 1.6.1. General iirt ~f:f Mention has been made in the previous section of the spectrum of sodium faf{ (Na) and mercury (Hg); a brief analysis will be given here, since both ?~~===: :Xz.-.·.

34 1 Experiments on Quantization elements have been investigated in detail and are repre·sentative of the one electron spectrum (Na) and two-electron spectrum (Hg) correspondingly.

= = Sodium has 11 electrons, so that the n 1 and n 2 shells are com pletely filled and one electron (n 3) is found outside closed shells. In this respect the sodium spectrum should be equivalent to that of hydrogen except for the central charge that the free electron sees. Indeed, since the = = nucleus with Z 11 is ''screened', by 10 negative charges (then 1 and n 2 electrons) the free electron sees a potential -e/ r when far from the nucleus and a potential ( - Ze) / r C when close to it, where C is the potential generated at the nucleus by the other electrons. However, whereas in hydrogen only one energy level was found for each value of 11, a more con1plex situation arises in sodium, with several levels corre sponding to the same n. This splitting is to be attributed to the fact that the time-independent Scbrodinger equation for the hydrogen-like atom, 2m 'v 2 1/1 + ,if( E - V)l/1 = 0, admits solutions with a principal quantum number n, and angular momen tum quantum number l, sucb·that n. > . t-+··1; when the potential that the electron sees is exactly of the Couiomb type as in the case of hydrogen, where V (-Ze 2 )/r the energy eigenvalues 2 4 mZ e ] 1 = - (1.22)

En [ 2(4irc:o)21i2 n2 are independent 15 of l, and agree with the Bohr theory. However, the screened potential that the free electron sees is no longer of the simple Coulomb typet and the energy of the level depends on both n and l. Orbits with smaller values of l are expected to come closer to the nucleus and thus be bound with greater strength; as a consequence their energy will be lower (more negative).

The energy level diagram of sodium is shown in Fig. 1.21> where the to levels have been grouped according their l value. The customary notation = = = is used, namely, l 0 --+ S state, l 1 --+ P state, l 2 --+ D state, l 3 --+ F state, and so on, alphabetically. The last colun111 in Fig. 1.21 gives the position of the levels of a hydrogen-like atom.

15This is the so-caJled Coulomb degeneracy: a peculiar coincidence for the Coulomb potential when used in the Schrodinger equation.

## 1.6 The Spectra of Sodium and Mercury

I== o Sstate I== 1 Pslate /=2 Dstate I"' 3 Fstata 25 ~p 20 2F H drO{leo 0 ,--- = -- =- - -=c - =-----"-- s= 6- 6- 6- 5- 5- s- s- s- !!..::...i 4- 4- 5- ~ 4- n=3 iE ~ 20 > a, .·. ~ ? 2 .·, .·.• .·.· .·•· .·. 40 ;-'..:• . 0 -:·· FIGURE 1.21 The energy-level diagram of sodium, grouped according to the orbital oogular momentum. The last column give.~ Lhe corresponding position of the levels of hydrogen. The left-hand scale ii; in 10 5 m- 1 , referred to O for the singly ionized. sodium arom; the right-band scale is in electron volts referred to Oa l the ground state of the sodium atom.

We note that the higher.the value of l, the smaller the departures from the hydrogen-like levels (as suggested qualitatively previously), and that for given 1 the energy levels for different n's follow the same ordering as the hydrogen-like atom, but with an effective charge Z*, which for sodium z• "' is as follows: S stares 11/9.6; P states Z* "' 11/10.1; D states {!

z• "' 1; F states Z* ...., 1.

1.6.2. Selection Rules / :. Thet spt ectral lines lbat we obsen:e arealdu~ to trthansitionstr fromfoned~nergyt sta e o a 1ower one; 11owever, m an yzmg e spec um o so mm, 1 iii{ ~::::: :(}.

:.,-,·,· 36 1 Experiments on Quantization becomes immediately evident that not all possible transitions occur. Thus certain "selection rules" for atomic transitions must be operative, and it is found that for all spectral lines ~l ±1. (1.23)

This selection rule is readily explained by the quantum-mechanical theory of radiation; it then means that only "electric dipole'' transitions occur.

Indeed, the transition probability for electric dipole is larger by a factor of (c/v)2 (c, velocity of light) from the next order. while under no conditions do transitions occur in which the angular momentum does not change at all (fl.I == 0). By applying the selection rule of Eq. (1.23) to the energy-level diagram of Fig. 1.21, we obtain Fig. 1.22, which gives the principal lines of the sodium spectrum; since l must change by one unit, transitions will always occur between adjacent columns and never within the same one.

Figure 1.23 is a reproduction of the visible part of the above spectium obtained by a student with the constant-deviation spectrograph. Beginning from the top (long wavelengths) we recognize the following lines (where the wavelength is given in nanometers)

(a) Red 615.43-616.07 nm (b) Yellow 589.00-589.59 (famous Na D lines)

(c) Green 568.27-568.82 (d) 514.91-515.36 (e) 497 .86-49&.29 (f) Blue 474.80-475.19 (g) 466.49-466.86 (h) Blue-Violet 449.43--449. 77 1.6.3. Fine Structure The data in Table l .4 on the red, yellow. and green lines of sodium, viewed with the grating, were obtained by a student simultaneously with the data used for the determination of the grating spacing d of Eq. (1.19). In the above data two wavelengths were given for each sodium line. Indeed, by viewing through the constant deviation or the grating spectrometer it is easy to resolve into a doublet each of the lines that appear in Fig. 1.23; the spacing is on the order of several tenths of a nanometer.

16Exceptions (such as quadrupole transitions) are found in steller spectra.

## 1.6 The Spectra of Sodium and Mercury

2F-,rz.

5/2

## E

'.&..

:);'.: Bl n-3--J f \: · FIGURE 1.22 The "allowed" transitions between the energy levels of sodium. The wave /\ leoglhs in angstroms ( 10 A I run) of some of the principal lines are indicated. Note I.hat f { the P states have now been shown in two columns. one referred 10 as Pt/2 the other as ;.:;:;\ /'312; the small difference between their energy levels is the "fine structure."

l]f :;:::.;.:, ' ' 5?:~{: :~){ ::,;;:;:: Iii 38 1 Experiments on Quantization 616.1......___ "-4...•_._,. •• ,, _. .,,.,,..~..,,"""-"· -~ 615.4--- :--. --·-· ...; ..· _·rrr.· ..... -..- .-.

589.a---········· ·· · ···· 56688.98.010,· 568.3 515.4--?

54194.89.3/ 1 497.9 :::~~ 446666..95/j/// 449.8/ 449.4 FIGURE 1.23 Photograph of the visible spectrum (in run) of sodium as obtained with a consrant-deviation spectrogrnph.

TABLE 1.4 Data on the Fine Structure of Sodium as Obtained with a Grating Spectrometer Line Order 01 8i .6.0 (radians)

Red 2 41°271 41 °291 5.8 X 10-4 3 55°58' 56°001 5.8 Yellow 2 40°211 400231 5.8 3 53°49' 53°52' 8.7 4 75°15' 75°23' 23.2 Green 2 39°32' 39°33' 2.9 4 70°48' 70°56' 23.2 ;::::::: [fi II 1.6 The Spectra of Sodium and Mercury 39 To reduce ilie dam we note iliat angle :~den:e~s::: - lllll/li: where 0i is the of sin~).

{t = + 02 0( D.0 ![if ~ ~ .J3Y letting sin tJ.0k a0k, cos 6.0k l, ··4····· ·.

fj)· nk!!.>.. =dcos0ktJ.01t.. ~ (1.24)

~f/ Using d 3,692.1 nm and averaging over orders within each line, namely f f "writing ff: .

I: :?:;?: cos Bk A0k = Lnk , ~(( • f:!.).. d-- (1.25)

If:~):( : ;:r-••4 ?::::}{w.e obtain for ~)..: ;;:w nm) ;;;i,mu,,"""

i@\= Green 0.59 0.555 if:(·The experimental data are thus in ,..._, 10% agreement with the exact values.

f{/· ,· Thls splitting of spectral lines was named "fine structure" and must f{{'teflect a spLitting of the energy levels of sodium; if we express the wave- "· ....

:)1/:Jengths of the sodium lines i.n wave numbers (ii = 1/'A = v/c, i.e., ~}{{in a scale proponional to energy since b.E he!:!. v), it becomes evi t\}~¢nt that the spacing in all doublets is exactly the same and equal to )f{(&v = l.73 x 103 m- 1 • Indeed, the doublet structure of all the above ,-!·.·.·.· . ·•· = = t?Jines is due to the splitting of only the 3P (n 3, l l) level as can be {{!;'een by referring back to Fig. 1.22. The splitting of the 3 P level is due r_ ..• ••••• ••• •• tf)Jo the effect of the electron "spin" and its coupling to the orbital angular f:/jnomentum (designated by l). According to the Dirac theory, the electron lf\possesses an additional degree of freedom, called "spin," which has the z........:..:..:.· \.:·.· ·,•, . = properties of angular momeorum of magnitudes h/2 (and therefore two [J(:fpossible to axis, +½ -½)

= = orientations with respect any ms or ms j~//Ibe spin s can then be coupled to I according to the quantum-mecbanical ·.········ ~~.#/. . )}Jtles of addition for angular momenta; this will result in a total angular j~:j{)r.~omentum of magnitude j = l + ½o r j = l - ½, and tbe energy of the @"{]tate will depend on j. Jn the case of sodium, the 3 P level splits into two ij{Je:yels, with j = ½a nd j = ~ designated as 3P1;2 and 3P312 separated by ~ ~-~ ir : - { ·· : . . · ;iii= l.73x 103 m-1 • W'if( w·::;;:-:-· ~!f~t:· ~?=::::: ~,_.::;:::::::: :: .-'h/h.Z•:•:- c-"//.,.•,•.•.•.

40 1 Experiments on Quantization 1.6.4. Electron-Electron Coupling; the Mercury Spectrum The mercury atom (Z 80) has 80 electrons. These fill the shells n == 1, = = n 2, n 3, and n 4 completely (60 electrons}, and in additio~ from = = the 11 5 shell, the l 0, 1, 2 subshells account for another 18 electrons.

= = The remaining two electrons instead of occupying the l 3 and l 4 = = subshells are in the n 6 shell with l 0, giving rise to a configuration equivalent to that of the helium atom.

We thus have an atom with two electrons outside closed shells in contrast to the one-electron systems of the hydrogen and sodium type. In the two electron system, we can hardly speak of then number of the atom, since each electron may be in a different shell; however we can still assign a total angular momentum J to the system, which will be the resultant of the values of each of the two electrons, and (as we saw in the previous section) of their additional degree of freedom, their spin. The addition of these four angular momenta, l 1, h, s1, s2, to obtain the resultant J can be done in several ways. For the helium or mercury ato~ the Russell Saunders coupling scheme holds, in which l 1 and 12 are coupled into a resultant orbital angular momentum L and s1 and s2 into a resultant spin S; finally Land Sare coupled 17 to give the total angular momentwn of the ½, system J. Since s1 and s2 have necessarily. magnitude the resultant S has magnitude S = 0 or S = 1. It is customary to call the states with = = S 0 singlets, those with S == 1 triplets, since when S 0 for any = + = value of L, only a single state can result, with J L S L; when = = + S 1, however, three states can result with J L S, L, L - S, namely J = L + 1, L, L - l (provided L f= 0). In systems where energy states have total angular momentum 1, the selection rules for optical transitions are different, namely ~L =±1 (1.26)

= = ~J 0,±1 but not J == 0-+ J 0, and in principle no transitions between triplet and singlet states occur.

17In the ensuing discussion the quantum-mechanical rules of addition of angular momen tum are used. Even if the reader is not familiar with them, he can infer them from following the development of the argument.

;~!!~::'..

## 1.6 The Spectra of Sodium and Mercury

~~!l\1\} t \ With these remarks in mind we consider the energy-level diagram of ~f: ( mercury. Since there are two electrons outside a closed shell, in the ground = = t ( state they will both be in then 6, l 0 orbit, and hence (due to the Pauli ;,:\[J:~rinciplc) must have opposite orientations of their spin. leading to S O; i f jjjh~ 1 spectroscopic notation is So. For the excited states one should expect ~t{~otb a family of singlet states and a family of triplet states; the singlets.

~tf:··~= = 0 wil I be ~-.... ,,,"1 ..

ilr ; ! !

~~; ~ !: :: ::::~: Le ..

~~~=:::.

~t~::::.:- '}i}Note tbe spectroscopic notation, where the upper left index is 2S l, )f)ndicating the total spin of the state; the capital Jetter indicates the total L tt/ofthe atom (according to tbe convention); and tbe lower right index stands ;.({=for J . For the triplets, S l. and the states are .-~;;:::=:=: ~,.::~:=:=:~ 3 So for L = 0, J = 1 tl\!\!;:· = = 3 Po.1,2 for L l, J 0, L, 2 -: ~ ;: - :: - : - : · : . : · : . : · : -· : 3 D 1.2.3 for L = 2, J = 1. 2, 3 etc.

f.UJ· i t( The energy levels for mercury are sbown in Fig. 1.24 with some of the @\{strongest lines of the spectrum. It is seen that the selection rules on AL {f\~d AJ always hold, but that transitions with AS -:j::. 0 do occur. It is also ?f\to 3 be noted that the fine st:ructU1e, lhat is, the splitting of the 6s6p P itrJ~vel.

is of considerable magnitude: Aii<3Po - 'Pi) = 1.9 x 10 4 m-1; ~tf).\v(3 P1 - 3 P2) = 4.6 x 10'1 m- 1 . Figure 1.25 is a reproduction ofthesuper ff}Jmposed spectra of hydrogen (longest lines). mercury (medium length).

{f{~d sodium (shortest lines) obtaioed by a student with the prism spectro iifwapb. Beginning with long wavelengths (from the left) one identifies the lttJollowing lines of mercury: :.,Z,,·,I', ••• ' iJ~:~:i:: tit?

(a) Red 690.75nm ~-:-:-:-:-:- Z:~:::/:::' (b) Yellow doublet 578.97-576.96 ~t:::::::: ~~1{:-. ( c ) Green 546.07 ~ff.

(d) Blue triplet 435.84 :X'l:!'}:•:•: ~ ff (e) Violet 404.66.

~~:::::: ~~:~:::::, ~fl m:-:;:::== ~{,:-:,: ~::;~;~:::::.

:,.,:.:,: '"~ ~ f:--;: ..: ·:•:· ~\ft I 15o 1p1 1~ 1F, I 351 3p2 3p 1 3po 30:3 3Di 3p, 3F4.3,2 10 I- ~ II --;;,-- <-j f;)'\.

'c,Oj I ,.. .., \\ II -~ ~,.,/' ~., /.,., (.)

c.'.l .

60 I ,- e;,'bo'!,)

-'1,: 15o Sfis A)

FIGURE 1.24 Energy.level diagram and the principal lines (in in the spectrum of the mercury atom.

~i=:~::: :-: ::c. -: ·. -.- .· . ·. .: · . -:· .: :· . .. ': .· ,· . -:-..• ,. . -::::.- :-:-: << · : -:-:-.• ;. .· . .: . .: : :: -:~.. ~ -:-:-:-: >= <· :-:-:-:-.< ·.- :-:. :-:: : -:• :-: :::::: :: ::::::=:-:::::-:::::::: : ;: : : ::::::.:-:::::::::-:::-:::::::::::: :::::~ :::.:::::-~:~~~~::~:: _~:: =:-~=~-:: :::::~::~..:. .: : :::::~::: ..: ~:.::: ~~~~~~~ :;:;:,:::: : ::::::::::::::::: : :: :::'.::::::::.:::::.:::> :-: ::: :: ;;:::;_-: ~ :'. :::::: :::: : ::::, ~~tf\ ij:::::::::_ ti;• ::;:;:;:::: ~ '· 1.6 The Spectra of Sodium and Mercury 43 IJ/:.· ~ z!t i ~-:- ~!

w=t ~l :<~~~::;:, ~: ~(0---.· .'/..

. -· ~~=i=~~t~ ~~ :te-H\i::: :,:.

~:~::::g fff:<P IJ)trGURE

## 1.25 Photograph ~f the superi~posed spectra of hydrogen (long slit), mercury

r.t~fJJllcdium slit length), and sodium (short sht).

IJii\ . . .

~,-:·.·.·.·.

~f fi: ttt·. .

ltfi.: wlfl ~~f}:· ~¾~~:r::::::-: ~r;:;::. .

~f:;::: f~·:•:•: ~:::=JJ/ !<~: •...• .•. .• ~:f\.

i=:=:?

## CHAPTER

:-:::::::::. Electrons in Solids ~·.'.

·,~::::::· ~t:: ~--·.•,• f.//: .,._._._ ·.' .· Ii -itl· ~::i) i.1. SOLID MATERIALS AND BAND STRUCTURE /.;:-:,:-:.

WJtJ~~ fundamenraJ_d istincti~n is that the f~rmer type of particles must have ~jft{~mpletely anasymmetnc wave function, whereas tbe lat1er ones must ~-;,:,:.;.· wit<: :-:::=::::::::::::::: 45 -~:-·!-~"·:<•:•:.

~~~~;;;:;::::· it.tit 46 2 Electrons in Solids have a symmetric wave function. This leads to a different distribution function for the probability that a particle will occupy a certain cell in phase space.

The experiments in this chapter are primarily concerned with the elec tronic properties of solids. Since these properties are determined by the behavior of their electrons, it is Fermi statistics that are relevant.

Most solid-state materials have a crystalline structure; that is, the atoms form a periodic lattice. Advantage can be taken of this periodicity so ·:: that the macroscopic behavior of the crystal is predicted from the gen-~:: eral parameters of the lattice and the atoms that form it. It is found ·: that the free electrons, instead of occupying distinct energy levels-as ··: they do in atoms and molecules-are contained in ce11ain energy bands .. : Knowledge of the "band structure" is necessary in most considerations < of the solid state and specifically in the understanding of the behavior J of semiconductors. The motion of the free electrons or holes (contained :: in the valence band) through the lattice can be studied in tenns of a ::· single-particle approach. Such phenomena as scattering and the absorp- ::: tion or emission of vibrational quanta (phonons) are invoked and are .: useful in explaining further details in the macroscopic behavior of the ··: sample. · 2.1.1. The Fermi-Dirac Distribution Let us consider a large ensemble of free Fermi particles (such as electrons); the assumption is made that in phase space1 there exist many states that these electrons can occupy. Each "cell" has a phase-space volume of h3 (where his again Planck's constant), so that the number of available cells for a differential volume of phase space is (2.1)

According to the exclusion principle, however, each cell can be occupied by two electrons (o ne with spin up and one with spin down), so that tht number of available electron states is 2n~I f we integrate over the spacf 1 Phase space is a space spanned by the momentum and position vectors of a particle Thus, a particle moving in ordinary three-dimensional space will have six components j phase space.

## 2.1 Solid Materials and Band Structure

~f ?coordinates and divide by the volume, we obtain the number of states n' ...

~ -'· ff/per unit volume per differential element in momentum space: 11[ ( ijf\ ~t{\ = -2 = 2 )

n I dn 3 dpxdpydp 1.

~t/: Vo x y z h ,}}!further, we can obtain the number of states per unit volume per unit energy I[ ?i;~}Jnterval d w; , W····.·. ·.

d:, = = d~; :,4np[dp; n; ::~f :kd since for nonrelativjstic velocities im)t = -PT dw,· = 2p,dp; I.r;:;:-:i-:·:·:< · ' w· ~;~/:: : r 2m 2m = ~: /2n, d:~:;) 3 (2.2)

=n1 w1 :ff\ Equation (2.2), which was obtained from very simple considerations, ~§f::~resents the number of states per unit volume per unit energy interval (at ½f)a:given energy) and is called the "energy density of slates." We note that it}f9.r a si:r,nple ensemble of free Penni particles (a) all energies are permissi ~{:}61e (since d N(w)/dw is a continuous and not singular function), namely, .ff}Lbe energy is not quantized; aud (b) the nwnber of states increases with ~~ffliicreasing energy.

:. .: . .• z.:.:-:-; ef:f}t Proceeding further to specify our system, we would like to know which it):¢:these in.finitely many states are occupied, or in a statistical fashion.. what :-({ds the probability that a state i of given energy w; will be occupied. This is $.f)he I Fermi-Dirac dis:trib ution and is given by ir' =[exp('"';/·)+ (2.3)

~?:;~J#,here k is the Boltzmann constant, T is the temperature of the system, it.f~'d wp is a characteristic energy, called the Penni energy or Fermi-level l,~;.;;t.:.--.:·t.--:..-.\e ·-·n.: [.eI rtgy .....0 .-::.-:-:-.-.-.· ·. • is interesting to note the properties of th.is function, graphed in Fig. 2.1: lfJ{(a)

It is properly bounded, so that it can represent a probability ~':;:;:::::::::·:··· ~~:::/;:;. 0 < N; /2n < 1.

~fff ~~~~:).

~:it).

~@-:::;::::· %:=~::::::.

,~~:::~:::::.· ·,::--::. ~.j ,:-:--:.

::::.:: 48 2 Electrons in Solids -:·=~ :-:-:- .~ =::j.

·.·.·. .· ,·.-.,..· ' .,·•..··. .· . : : · : . : ·. ~ .· : .·.·•· ·,.:·,.:.· .Jj :::::; T=O · · . . · ·. . · • . . 1 ; ,::::;j ·.·.·•• ......

·.-...J ·:,:'.:":'~J ::::~ :::J T2> T1 ;}~ ' yr >0 1 j)~ y ..

\.

<@ fl ,:.:,:~ FIGURE 2.1 Probability of occupancy of a state of energy w1 as de1ived from Femti-Dirac statistics. ::::ij=·~ -:·.-•:J ,'..

·:;:;.~ ,'.:::j \\j (b) For large values of wi it assumes the form of the Boltzmann }ij distribution :,•::.·.:i,.: ::::t Const x exp(-wi / kT).

'::;.~ .......

= j~j (c ) For T 0 it is a step function, with ·.·.·.:,,: = :;~~ Ni/2n 1 W; < WF ::::.::: :::::~ ::::::~ N,/2n 0 ::::;~ <•,··=.··=~~ = ½, :::;:~ ( d) For T -:j= 0, WF has the property that N ( wp) and as many states · , . : · :: . : · : z :;: ::::;* above wp are occupied, that many states below WF are empty.

:•:-~ (e) In solids and for average T #, 0, the distribution function is only J::::ja: slightly modified from its shape at T 0 (for solids wp is on the order of a few electron volts, while 1 / kT 40 e v-1 at T 300 K).

::::::: :~)

Con1bining the Penni-Dirac disttibution (Eq. (2.3)) with the energy density of states (Eq. (2.2)) it is possible to obtain any desired distribution.

?~ For example, the number ofe lectrons per unit volume (d ensity) at an energy /Ii win the interval dw is given by 'ii:~~ (2.4) ;.;.:: ......

,, ,:)§ If we express Eq. (2.4) in terms of the Cartesian coordinates of the velocity, )f.

Vx, Vy, and Vz~ and integrate over lJx and Vy, we obtain the number of /i electrons per unit volume with a given velocity in the z direction, (in the .

Vz JI ffJ Z•:•:•: .r.,;.:-:-:-:. 2.1 Solid Materials and Band Structure 4S '??::::;:::.

~f: ~tr N(w} N(v,)

::;:::: ~:=: f·~·· T=O i l!ll T=O ;JI!

~w~::r::: \ ·i ,\ {~} WF W 2(: ~)

1{ FIGURE 2.2 (a) Number of electrons with an energy w in the interval dw. (b) Number ~:~t-:-:-:·: ofelcccrons with z component of velocity llz in the interval dvz.

v.:::::::.

~(}\ IJ \ f)wte rval tivz). The result of this integration is2 I l !~ m':T N(v,)dv, In 1 +exp ( WF-k;v:/ ) dv, (2.5)

i./1/ (\?The two distributions given by Eqs. (2.4) and (2.5) are shown in Fig. 2.2.

0fj} Even though the majority of the electrons in a solid are not free (as we 0?{-i:>riginally assumed), Fermi-Dirac statistics are applicable, especially to )}{ metals. ln metals at least one eleclroo per atom has several states available ~{}(is in Lhe conduction band), so that it can be considered free; since there iJ(will be 6 x 1023 free electrons per gram mole, statistical methods are well ~f?Justi ficd_ 0?\ ~f:=::::=:.

i:=\\ 2.1.2. Elements from the Band Theory of Solids ~0·:l:t::}::.q- p to now, n~ account bas been taken of the interatornic or intramolec_ular i·:fJorces that might act on the free electrons. Indeed, we expect (from previous l \ ~perience) that the consideration of some potential in the region where ·[@}he electrons move will result in the appearance of energy levels; however, ~::fa 9ecause of the periodic structure of this potential, instead of energy levels, ;;f ~ne7ID1 bands appear, and only the states contained in these bands can be :r1t::::·.

---- ..

:-:,;;:;:·_~ [ ({ A. Sommerfeld. ThermodyMmics and Statistical Mechanics, p. 285, Academlc Press, ~jf ~ew York, 1956.

~it ,_,~~:~'.- ~ /.'.:;.

j} 3I 50 2 Electrons in So I ids •,•.·.· :){ :::;:; -Vo .'.".J •.•.4.J L :::;:: ......J ·:.·J ·.-..... J :::::1 .·.·n . :::::~j F1GURE 2.3 A periodic potential that may be considered as an ideaJization to the actual · ,·]~ potential of a crystal lattice. · ·j ~ :]

}~ occupied (with any significant probability). In the following paragraphs .:::::~ .:::~:~ we will sketch two approaches toward the understanding of the physical )j origin of the energy bands. < · ) ·'- 1 ?.

Consider first the one-dimensional problem3 of an electron moving in .-:·:-~~ }:?~ a potential consisting of an infinite sequence of "square" wells of depth ...... ,~ ::::~~ Vo and width b and spaced at a di.stance l from one another (Fig. 2.3) . -;.;,.~ .J ~ The solution of th~ Schrodinger equation for such a potential gives for the :-:,:-, :}j electron wave function ·.:·::-:.~...=: -~!

'Vk = Uk ( X)e i kx (2.6) /jj .•.·.•J = (~~ with k = 2rr /). p / 1i the wave vector of the electron. Tiris wave function .··..··..•·,,11 \:~ consists of the plane wave part ei kx, and Uk (x), which must have the :'.:=:~ ± = periodicity of the lattice, namely, uk(X l) uk(x). If there are N lattice -:::;~ }j sites, the length of the crystal is NZ and we impose the periodic boundary .·.·-:-: + = = }:::a condition Wk(X Nl) Wk(X). Tiris leads to eikNl l, or · ::;::* "::;;~ ;::;~ = ll kNl n2rr .·.-~ :::~ k = n2rc/Nl n = 0, ±1, ±21 . ...

(2.7)

Equation (2.7) determines the allowed values of k, which fonn almost :-:-9. )1i a continuum because of the very large integer value of N. Note that for N 1 one obtains the familiar "particle in a box" energy levels, with .\~ ?~!

p2 k2J-;,2 n21i2 ::::::=: -:-:~:=:: E=-=-=-. :::.:~ 2m 2m 2m[2 .·.. ; ,z :::::?.

-:-:,:-: :;:::~ 3 -:;::::=: E. Merz.bacher. Quantum Mechanics, third ed., Wiley, New York. 1998. ·.·,·~ ::-~ ::::j .:::::~ . .;:;~-* :::::~ <;:~ ::::::::= :::;~ ··=-~ ~l}l it= 2.1 Solid Materials and Band Structure 51 ~]:! :.~~:;:~:f: ~;~:?:~:: p;::i~:l::~lve:::,c~O~:g:: it is where l-/ is the one-dimensional Hamiltonian operator ••• fi2 d2 = ---- + H V(x)

2mdx2 j{.:,·.

and V (x) is now the potential of Fig. 2.3.

}:? The solution of Eq. (2.8) is given in graphical form in Fig. 2.4. We note ~f the following: i > = (a) Even though all values of k are allowed, discontinuities arise at k ,.ff.

nn / l (note that for lb.is particular electron wavelength, Bragg reflection ';i,4.t?.·.\· from the lattice will occur with a half-angle 0 = 90°; n>.. = 2Z sin 0, hence ) ?: = = >,. 2l/n, and since A= 2rr/ k, it follows that k nrr/ l).

({j{ : (b) Not all values of the energy are allowed, but only certain "bands"; ~\ other bands of energy are fo rbi<lden.

fi> (c) The relation between E and p (or k) is no longer the familiar ..• .·. ·. .

f~ f::. parabolic p2 k21i2 E=-=- (2.9)

2m 2m ?.i:····· p2 6=-1 E 2m Allowed energy bands ~J/.

l e ~;,;::::.: i:-:-z-..

-r -r 7 : - ; ~- ~- ~:{/ :: (a) (b)

e~f:f,f:-J:-1:-I.-GURE

## 2.4 Results of the solution of the simplified one-dimensional lattice problem

~:fJ-a)·Plot of energy_ E versus wave number k = p /Iif or an electroo in a crystal lattice. (b)The · ~::::::~owed and forbidden energy bands.

~fi -~-:-: -~~~½J:~:::t: .

0-,. .. ·.·· 52 2 Electrons in Solids lnteratomic spacing FIGURE 2.5 Energy levels of a system of six similar atoms placed in a linear array.

The same formalism is carried over into three dimensions, but now the bands are replaced by allowed (Brillouin) surfaces and the axes of symmetry of the crystal must be taken into account.

A different approach is to start with a molecular wave function and study its behavior as the number of identical atoms is increased. In Fig. 2.5 are plotted the energy levels against interatomic distance for the ls and 2s states of a linear array of six atoms (after Shockley). If, then, in the limit the (almost infinite) array of the crystal is considered, the energy levels coalesce into bands. This is shown in the left-hand side of Figs. 2.6 and 2.7, where the energy bands plotted against interatomic spacing are given for diamond which is an insulator (after Kimball), and for sodium (after Slater), which is a conductor. If the lattice spacing for the particular crystal is known (from experiment), it is possible to read off from the graphs the limits of the energy bands. This is done diagrammatically on the right-hand side of Figs. 2.6 and 2.7; also indicated is the position (in electron volts)

of the Fermi level (as it can be calculated, for example, from Eq. (2.4) and the electron density within each band).

## 2.1 Solid Materials -and Bend Structure

.•:•:•;.

Diamond C (1 s)i(2s)2{2p)2 .Jilli:: Energy E ~=ft ?,:::::,, ~::::::.

I~~/ ..,. ..: :::: -~~? 4 states ~i? per atom ·.·· Observed lattice spacing :~(i. ..

:?.::::::•. Latt\ce spacing Diagrammatic sketch tf:: FIGURE 2.6 The energy bnnd saucture of diamond (insulator) as a function of lJ!rtice ·l/ : spacing. The observed lattice spacing is also indicated.

x~·:::::· ?;;:::: ;.:::::: ~:~(~~ Sodium ~-:-:•:• ~?

E E :::::::::: :?~::: j~l{ l\l'li~?,"7'?7?7'?-,.45 3p ~~lf 3s ~-.·,·.

~~i:r:::::: ~r Valence band tr::: Latlice spacing Diagrammatic sketch tf::.: FIGURE 2.7 The eaergy band structure of sodium (conductor) as a function of lattice ~J::::· ~/.('.:'.' ~pacing. The observed lattice spaciog and position of the Fenni level are also indicated.

~t> ,:::::i:::::: ~f\ From these considerations it is possible to u.uderstand the difference ijf between conductors, insul~tors, and semicondu~tors. For diamond, for W::::/.example, the valence bahd 1s completely tilled (this fact follows also from ij\{ the atomic structure of carbon and the deformation of the energy levels).

1tr ¾X:> ~Ii\: ..•·~ >=· 54 2 Electrons in Solids it {f The next available states are approximately 5.4 eV higher and hence can- ::\ not be reached by the electrons, with a consequent inhibition of their :·!:·:::~-:_!!_·:.

mobility; diamond therefore behaves as. an insulator. For sodiu~ in con- - \J trast, the Fermi level lies in the middle of an energy band, so that many ·r; states are available for the (3s) electron, which can move in the crys- tal freely; sodium behaves as a conductor. Pure semiconductors, such <<· as gennanium, have a configuration such that the valence band is com- )] )j pletely filled, but the conduction band lies fairly closely to it (0.80 eV) ..

At high enough temperatures (that is, on the order of a few thousands ')]

iJ of degrees), the electrons in the valence band acquire enough energy to ...- ~ :J cross the gap and occupy a state in the conduction band; when this hap- pens the material that was previously an insulator becomes intrinsically · ·,·.·1 conducting. :{{ Both the electric and thermal conductivity of a solid depend ori the .}J density and mobility of the free electrons. Completely analogous to the )] )j motion of electrons is the motion of "holes"; holes can be thought of either as "vacancies" in an almost-filled band, or as electrons with negative \]

effective mass.4 Due to their thennal energy, the carriers have a random /j motion characterized by (3/2)kT E == m*v2 /2. When an electric field . }j .·.-.•:-: is applied, a drift velocity is superimposed on the random motion of the )){ carriers, resulting in a steady-state cmTent flow. \{ \]

:::::: ::::;: 2.2. EXPERRv.lENT ON THE RESISTIVITY ·...·...· . .

?~i~ OFMETALS '·.·.· .:::::: .·.·.• ):~{ In this experiment we will explore the physics behind electrical resistance -::::: ,::::: in metals. What~ s more, we will do it with a novel technique that measures ::::: .·.· ...

the resistivity of the meULL a property only of the type of material and :\ independent of the size or shape of the conductor. This technique, in fact, }!

\·.·.i· can make measurements of the sample without actually touching i~ and bas fow1d a lot of use in modem applications. It is based on the paper :\ C. P. Bean, R. W. DeBlois, and L. B. Nesbitt, Eddy current method for ):ii measuring the resistivity of metals, J. Appl. Phys. 30, 1976 (1959). ))

First, we make the connection between resistance and resistivity. We .:::: ::_::: assume that Ohm's law is valid, that is, V := IR, where R is independent :::: .{ 4This can be seen from Eq. (2.10) and the negative curvature of some parts of the E (k)

curve of Fig. 2.4a.

'!

## 2.2 Experiment on the Resistivity of Metals

Area A FIGURE 2.8 An idealized resistor.

of voltage or current. Consider the idealized resistor pictured in Fig. 2.8.

The resistor has a length L and a cross-sectional area A. A voltage V is applied across the endc; of the resistor. A current I of electrons flows from one end to the other, against a resistance R, which is due to the electrons interacting somehow with the atoms of the material.

Consider Ohm's law on a cnicroscopic level The magnitude of the elec tric .field setup across the ends of the resistor is just E V / L. The electrons that cacry the current will be spread out over the area A. so at any point within the resistor the current density is (magrutude) j I/ A. Therefore Ohm's law becomes E jp, (2.11)

where R=p A and p is the "resistivity," a property of the material that is independent of the dimeosions of the resistor. Equatioo (2.11) can be derived from the theory of electrons in metals. Tbe resistivity arises from collisions between the electrons and the atoms of the material. In a metal, the electrons are essentially free, so without any collisions they would continually accelerate under the applied field with an acceleration a e E / m, where e and m are the electron charge and mass. However, the collisions cause the electrons to stop and then start op again, until the next collision. lf the time between collisions is called r. then tbe "drift" velocity vd is just eEr = = -.

Vd ar (2.12)

Now if there are n electrons per unit volume in the resistor, then a total = = charge q (nAL)e passes through the resistor in a time t L/vd.

·r~~~ •••. ..J . /:!

56 2 Electrons in Solids :::::;; ;:::::~ TABLE 2.1 Electrical and Thermal Properties of Metals ::::::::: ::::::~ t]

Electrical Temperature Thermal resistivity coefficient conductivity ~~ 'ii@ Name z A (µ.Q · cm) 00-3 /K) (cm,l:,s)

;:::;:~ :.:.:.:•::•:.= , Al 13 26.98 2.65 4.29 0.53 395 { ;~ tJ Fe 26 55.85 9.71 6.51 0.18 420 .-:·:·=~ Cu 29 63.55 1.67 6.80 0.94 333 }::!:a Zn 30 65.38 5.92 4.19 0.27 300 ))~ Sn 50 118.69 11.50 4.70 0.16 :; Iii Pb 82 207.19 20.65 3.36 0.083 83 208.98 106.80 0.020 \\!!

:-:-r ··.-.n ,:::4:i•' .}Jj Therefore, the current density is .-:;:;.½ .:-:~z ·-:j:8 . I 1 q 1 nALe •·:;.~ = = t = = (2.13) -:;:;:~ J A A A LI v d nevd' :-:~~ :::·«~ . :': .'·; .".;r. :.. ~ " ~-"'' ' ' ·::::~i and therefore, :::::=* ···-~ m 1 -:-:w p=- (2.14) :::::.{.j ne2 r · .;:;:;.~ ,;:::~ tii Often the "conductivity" o- ::::: 1 / p is used instead of the resistivity.

Electrical resistivities are listed5 for various metals at room temperature in Table 2.1. Also included are some thermal properties, which are closely 1/ll related to the resistivity through the underlying physics.6 One of these is the temperature coefficient of resistivity, defined as (1/ p)dp/dT. This ·: .. : . : . :z .« :: . .

·{@ quantity is in fact temperature dependent as we shall see, and the quoted .;::::f~ numbers should be valid near room temperature. .{J :=:::~ Clearly, the fundamental physics of resistivity lies in the values for the ::::!~ collision tirne -r. The interaction of the quantun1-mechanical electron waves -:-:-X f1 and the quantized lattice of the metal crystal accounts for the collision time ,•:•:~ _:!f!iI~ 5Values for Z. A, resistivity, and thermal conductivity are taken from L. Montanet -:-:-~ \l et al Review of particle properties, Phys. Rev. D 50, 1241-1242 (1994). The temperature )i~ coefficient of resistivity, and all data for Zn and Bi, is from D. R. Lide, CRC Handbook of_ •)j Chemistry and Physics, 56th ed., p. F-166, CRC Press, Boca Raton, FL, 1975. The Debye temperature is from E. U. Condon and H. Oclishaw (Eds.), Handbook of Physics, 2nd ed.. : :::t{ )Jf Pan 4, Tables 6.1 and 6.3, McGraw-Hill, New York. 1967.

6 A n interesting exercise is to plot the electrical conductivity 1/ p against the thermal · -;:::;* conductivity (see Exercise 30 in Appendix G). )) } ' :-:~h JI '·.•.,.,.

~::::

## 2.2 Experiment on the Resistivity of Metals

~;:~~7~17·n!b~::t;e~~~::· men me scatrering will 1111 ::~:': '!CRYSTAL tJMPURITY The scattering from the crystal depends crucially on the vibrational energy ll1 stored in the crystal lattice, and therefore on temperature. The impurity :::::· "' c::::· scattering is essentially independent of temperature.

t~:::::: The technique we use measures resistivity directly. The idea is based on t::::::.

~::::-.

Faraday's law, which gives the Eiv1F (i.e., voltage) induced in a coil that t> :~::-:: surrounds a magnetic field that changes with time. That is, we measure (( a signal V(t) that is proportional to some dB/dt. The magnetic field B ,"'.r.·.· } \ is generated by the "eddy currents" left in a metallic sample when the W)· sample is immersed in a constant magnetic field that is rapidly switched fa/· off. Figure 2.9 shows how this is done. In Fig. 2.9a, a cylindrical metallic ?{ bar is placed in a constant magnetic field whose direction is along the axis {/ of the cylinder. We assume the bar is not ferromagnetic, so the magnetic !/ \.: field inside is essentially the same as it is outside. Remember that the bar { \ : is filled with electrons that are essentially free to move within the metal.

( ( . Now we shut the field off abruptly. By Faraday's law, the electrons in the }\ metal will move and generate a current that tries to oppose the change in }( the external magnetic field. These so-called eddy currents are loops in the [ \ . plane perpendicular to the axis of the sample, and they generate a magnetic ~ft :=:::::: ..-- .. . · ·- .· · ..

·.·--... ·..·... ·· ... ~ if/ ~:::::: ~=:::::·: ·~~=:-:·:.:·: :.

r:·:-:-:- ~:/: :;::::::: r. .- .·.· r. .· .·.·- ~t( ~::::::.' ~?> t~{ • (a) Field on (b) Field shut off ~::::::: tt\ FIGURE 2.9 The eddy current technique for measuring resistivity. (a) A magnetic field ft.·· tf\ Bo permeates a cylindrical metal sample. (b) Eddy currents set up when the field is shut off generate a field B of their o~n .. ~e eddy currents, and therefore B. decrease with time at ~ :::::- a rate that depends on the res1stiV1.ty.

~:-:-:-: f :=:• ~-:-:-: ~(\ :=x--:-:- ti·=~:?: •·.· . .

." ",•.· 58 2 Electrons in Solids field of their own. See Fig. 2.9b. However, as soon as the external field is gone, there is nothing left to drive these eddy currents, and they start to decay away because of the finite resistivity of the metal. The time it takes for the currents to decay away is directly related to the resistivity, as -:Ne shall see.

We again use Faraday's law to detect the decaying eddy currents. The magnetic field set up by the eddy currents also decays away with the same time dependence as the currents. Therefore, if we wrap a coil around the sample, Faraday's law says that an induced EMF shows up as a voltage drop across this coil. This voltage drop is the signal, and the rate at which it decays to zero is a measure of the resisitivity of the metal sample.

In order to determine the voltage signal as a function of time, one needs to solve Maxwell's equations in the presence of the metal. The derivation is complicated, but outlined in Bean et aL (1959), where a series solution is obtained by expanding in exponentials. For a cylindrical rod, this series takes the form ex Lexp(- >.;o:t), V(t)

i=l where ct is proportional to p and the 'A are roots of the zeroporder Bessel = = = function, i.e., )~1 2.405, A.2 5.520, >..3 8.654, and so on. Since the A increase with each term, for long enough times, only the first tenn is significant because all the rest die away much faster. That is, the falloff of V (t) with time will look like a single exponential if one waits long enough, but will be more complicated at shorter times.

For a cylindrical metal sample where the external magnetic field points along the axis of the cylinder, the result is V(t) Voe-tltE, (2.15)

where 9[Q·s]r2 tE 2.17 X 10- - - , (2.16)

cm p Vo === lONp Bo, (2.17)

and t 0 is the time when the external field is switched off. In this equation, r is the radius of the cylinder, expressed in centimeters, and p is the resistivity of the metal, expressed in ohms-centimeters. Also, N is

## 2.2 Experiment on the Resistivity of Metals

the number of turns in the detector or "pickup'' coil and Bo µ,oi n (in SI units) gives the magnetic field Bo set up by a solenoid carrying a current i through n turns. This equation is only valid for times ton the order of IE or larger. At earlier times, there are transient terms left over that cause V (t)

to fall off more rapidly than given by Eq. (2.15).

2.2.1. Measurements The lifetime tE given by Eq. (2.16) is on the order of tenths of milli seconds. Therefore, the magnetic field must be switched off considerably more rapidly than that This is bard to do mechanically, so we will resort to an electrical switch, using a transistor.7 The circuit that produces the switching magnetic field is shown in Fig. 2.10. A garden variety 6-V/ 2-A power supply puts current through the solenoid, creating the magnetic field Bo. However, after passing through the solenoid, the current encoun ters a transistor (321/TIP 122) instead of passing directly back to ground.

The lead out of the solenoid is connected to the collector of the tran sistor, and the emitter is connected to ground. The base is connected through a 1-kQ resistor to the 600-Q output of the HP 331 l A wave fonn generator. The waveform generator is set to produce a square wave, oscillating between around -10 V and +10 V with a period of a few milliseconds.

Consider the current through the solenoid. First, the DC power supply is connected so that the solenoid is always positive with respect to ground, thus the collector voltage is always above the emitter voltage. Second, the base-emitter acts like a conducting diode, so there will be a voltage drop across it of around 0.6 V when it conducts. Also. if there is no current through the base, then the base-collector junction is reversed biased and no current flows through the transistor, or therefore through the solenoid.

That is, the switch is off. Now when the waveform generator i.s at 10 V, the current through the base is iB ~ 10 V/1 kQ lOmA. This turns the switch on and lets the current flow through the solenoid pretty much as << = if the transistor wasn't there, so long as le fJIB 10 A. You might want to measure the resistance in the solenoid coi] to make sure it does not 7This transistor is actually a "Darlington pair," which effectively gives a single transistor withagainparameterhFE = /J = lOOOorso. VcE = 6Vdoesnotexceedtbespecifications.

For srudents with minimal experience in laboratory electronics, Sections 3.1. 3.2, and

## 3.3 should be consulted

;:;:?, 60 2 Electrons in Solids :1 /Iii Lo HP3311A Coax to scope channel 1 }j Hi 600 Ohm :::::: :}~~~ .: -.:.~...

Solenoid )i{ ... ~""

·::·:::;~ lo R=1K ':-:-t..-: ·:::~?.

6V 2A Hi · . . . . . . . . ., .. . . ~ ..~..

·.·.·-;; ,:::;:~ Ground at .

HP3311A :);~ Testpoint / .;:::::~ :-::;;:; (Probe to scope channel 2) ·.~:::;;~ FIGURE 2.10 Switching circuit for turning the magnetic field on and off. It is a good idea ••• J ....~ iii!!

to cl•eck the current through the solenoid by measuring the voltage at the testpoint. timed against the HP33 l 1A square wave generator.

:::;i~ ·)~~-~~~~ draw a lot of current, but since you are using a 2-A power supply, it is a }::~ good bet that you are in the clear. So, when the square wave generator is :/~ at+ 10 V, the solenoid conducts. However, when the generator switches to ::::::~ -10 V (or presumably anything less than around 0.6 V), the solenoid and }]

\J the magnetic field shut off. This is, t 0 in Eq. (2.15).

/J The pickup coil is wound on a separate tube, which can be inserted inside /J the solenoid. One can then introduce and remove different metal samples }l from inside the pickup coil. By connecting the terminals of the pickup coil to a digital oscilloscope, we record values of V (t) corresponding to !{{ ff Eq. (2.15). There is one complication. The magnetic field shuts off so fast ?{ that the instantaneous induced voltage in the pickup coil is very large. That i\ is, b..t is so small that dB/d t ~ b..B / b..t and therefore also V are very large.hAndoscakilloscope would typicaldly have cirthcuitry that protectsfii~ thibut :!:::~_--.\.{_~ ones ou1 t e some care to avoid amaging e equipment. To x ·s ;.::.

probl e~ the simple circuit shown in Fig. 2.11 is used to connect the pickup · ·_:::·:=-~·::_:__;-__::__: :·:.::_: coil tenninals to the oscilloscope input. The two diodes are arranged so that · . _ }@ any current is taken to ground, so long as the voltage is bigger than +0.6 V or smaller than -0.6 V, for diodes with VF 0.6 V. That is, the circuit ·-· .,.

"clamps" the input to the oscilloscope so that it never gets more negative, :::_:/:_;:f::)_i,_!__:, ...f:~ : but still big enough to make the measurement. :.

## 2.2 Experiment on the Resistivity of Metals

In (from pickup coil) Out (to scope)

FIGURE 2.11 Clamping circuit for the oscilloscope input Sometimes we see the signal "ring" just as the switch shuts off. That is, we see the decaying exponential but a rapid oscillation9 is superimposed on it, and this gets in the way of measuring the decay time. If the ringing goes away while the signal is still decaying exponentially, just use the data past the point where the ringing is gone. Otherwise, a resistor should be attached in parallel with the scope input. It is best if you can get a variable resistor, and play with the values so that the exponential decay is unaffected but the ringing is thoroughly damped out.

Before measuring the resistivity, one should know what the solenoid circuit is doing. Connect a probe to the junction between the solenoid and the transistor collector. View this on the other channel of the oscilloscope, and confirm that you see what you expect. That is, when the square wave is high, the so]enoid is conducting and the voltage at this point should be around +1.2 V,i.e., the sumofthetwoforward voltage drops for the CB and BE diode equivalents for the transistOT. On the other hand, when the square wave is low, the solenoid should not be conducting and there is no voltage drop across it~ so the voltage at this junction should be around +6 V, i.e., the voltage of the DC power supply. This probe should now be removed since the oscilloscope channel i~ needed to make the resistivity measurements.

Next, connect the pickup coil to the clamping circuit and plug it into the second channel of the scope. Do not put any metal sample in just yet. You should see a voltage spike, alternatively positive and negative, when tbe magnetic field switches on and off, clipped by the diode clamping circuit.

Now insert a sample into the pickup coil. Watch the pickup coil signal on the scope as you do this. The effect of the decaying eddy currents 9Toe circuit has lots of ''loops,,, each of which is essentially an inductor. Any capacitance somewhere will cause oscillations, but the exact source can be hard to pin down. One should take care to wind the pickup coil in a way that minimizes the inherent capacitMce. A good way to do this is to crisscross the windings of each layer.

-:-:-:- ·· =·:":' .:::::~ :-:-:4'.

62 2 Electrons in Solids . · · .; .· . - ;. · . . ; : .=:::;~ :-:-:-: ·.·.·--..

,•:-:•: ..

: .

·- :.

.; . ,,, ·.•·•.•·•. ..:• ".J; ,::::::~ .·.·.".; .·.·.·; .·.-.....· .::::;:: ;:::;:;: ;:}~ ._._. ._ ,.

·.-.......

:-:-:-j .; ',: ··:.. :·-. ;·.

.".

.., J/ ,::;:::~ . .; . : . : . : .. : .. : . ~ ..- 0 0.2 0.4 0.6 0.8 ......., , Time (ms) -:-:-.-~ FIGURE 2.12 Resistivity data taken with a high purity aluminum rod as the sample. The decay is dearly not described by a single exponential at the earlier times.

/~:?

should be clear. You may see some transient oscillations of the signal \?( :,:-:. .: -:• right after the field shuts off, but there should be plenty of time left ~r :::::::::: these oscillations die away for you to get a smooth curve. Figure 1 2 0 . 12 - < :, . - · : < : . , - - : · : . - • / . ; . : . : . . . - ; - .. . : . : . .

shows data acquired with a ½-in. diameter high-purity aluminum rod at -~(~~~~ room temperature as a sample. The data points are the output of a digital ,:-:-::-: ::::::::: oscilloscope displayed using MATLAB. Note that at the earliest times, there :;:;::::: )it are higher order contributions to the signal ( as described by Bean et al.), and ,·.·.- ......

.: ::::::: one n1ust choose a suitable range over which the data are indeed described ,:::::::::~~:=: by a single exponential.

::::;::: = :-:-;-;. .

The fit shown in Fig. 2.12 yields a decay time tE 3.051 x 10-4 s. :::::::: .• :-:-:•: Then, from Eq. (2.16) we find for the resistivity . : _ : · ._ . : · : ._ . : . - : . . ; _ .. . : . .

,:.:,:-:.

·:::::~

## 2.17 10-9

X -:::~:~ p = ( x r 2 (cm 2 ) = 2.87 x 10- 6 Q · cm, \ ,· \ . ~ ·.. i - § ...

tE s)

I!

·-:::;:; ':;::::: ·-:-:.1: . - · :- .· :- . : - ..

. :-:.>; .:::::;~ )ffiff

## 2.3 Experiment on the Hall Effect

:::: The main source of systematic uncertainty is likely to come from the / times over which the decaying voltage signal is fitted. At short times, the decay is not a pure exponential because the transient terms have not all died away, so we want to exclude these times when we fit. At long times, :::. there may be some left over voltage level that is a constant added to the ( exponential, and again, a pure exponential fit will be wrong. Varying the /. upper and lower fit limits until we get a set that gives the same answer as /:· a set that is a little bit Jarger on both ends is one approach. One~ should be (-convinced that the results are consistent. For example, use aluminum alloy / rods of the same composition but different radii, and check to make sure ( that the decay lifetimes tE scale like r . This should certainly be the case \ to within the estimated experimental uncertainty.

\ Having learned how to take and analyze data on resistivity, we can now \ investigate the temperature dependence. It is best to start simply by com ½-in.

} paring the two samples of dian1eter alurrrinum rods, one an alloy and _::. the other a (relatively) pure metal. Vary the temperature by immersing the } samples in baths of ice water, dry ice and aJcohol. and liquid nitrogen.

( Boiling water or hot oil can also be used. These measurements are tricky.

( One must remove the sample from the bath and measure the eddy current ( decay before the temperature changes very much. Probably the best way to ( do this is to take a single trace right after inserting the sample, stop the oscil :: losoope, and store the trace. Then one analyzes the trace offline to get the ( decay constant One might also try to estimate bow fast the bar warms up by !: ma.king additional measurements after waiting several seconds, e.g., after !: saving the trace. This would best be done with a sample whose resistivity, \ · and therefore t E, can be expected to change a lot with temperature. Pure :! aluminum is a good choice. Remember that the temperature dependence / will be much different for the pure metal than for the alloy. Try to estimate { the contribution to the mean free path of the electrons due to the impurities.

i:: 2.3. EXPERIMENT ON THE HALL EFFECT \ In Section 2.2 we saw how collisions of electrons with the crystal lattice \:: lead to an electrical resistance, when those electrons are forced to move { under an electric field. If one also applies a magnetic field, in a direction / perpendicular to the electric field, then the electrons (and other current { carriers) will be deflected sideways. As a result an electric field appears in ii: this direction, and therefore also a potential difference. This phenomenon 64 2 Electrons in Solids is called the Hall effect, and has important applications both in identifying :.•./.: the current carriers in a material and for practical use as a technique for measuring magnetic fields.

Let us rewrite the microscopic formula for Ohm's faw~ but this time <:: taking care to indicate current density and electric fields as vectors, and j!j to also note the negative sign of the charge on the electron. Following :::: Bqs. (2.12) and (2.13) we write :'{ ·, )j (2.18)

'::~ or mvd ii -=-eE. (2.19)

::::; It is clear that in Eq. (2.19) we have made an approximation, replacing \ : the time rate of change of momentum, i.e., dp/dt == mdv/dt, with an :::: expression that uses the average ac~eleration vd/r. This is how we have \} )j taken into account collisions with the crystal lattice.

i} It is straightforward to modify Eq. (2.19) to take into account the effect \j of a magnetic field B. We have .·.· ::::: :~:tic I fie::i: :: ff we assume iliat fue :eB:~ITOCtion, and define ilie cyclotron frequency We es e B / m, ilien we can rewrite this equation as :/// er --Ex - Vd m Wc"!Vd X y = eT + --Ey (2.20)

Vd (J)c'&Vdx er --Ez.

Vdx Consider now a long rectangular section of a conductor, as shown in Fig. 2.13. A longitudinal electric field Ex is applied, leading to a current density flowing in the x direction. As this electric field is initially turned ·.

on, the magnetic field deflects electrons along the y direction. This leads to a buildup of charge on the faces parallel to the xz plane, and therefore an electric field Ey within the conductor. In the steady state, this electric field cancels the force due to the magnetic field, and the current density is strictly .

:?--:-:-: 2.3 Experiment on the Hall Effect 65 ~-::::::: ~:-:-:- t?.

r:===:::· ~z - .:::::::: Magnetic field 8 tit·· t t t t t if~(: 111 : t'.·.·.·.· ~:;::::::.: t'.·.·.· .· (a)

ii .

i'::-:-:-:· Section ~·:::-:-:-: . .

~::::;:;:: perpendrcular ~:::::=::: to z axis; ix t'.·.·.·.·.. .

~ f -:-: f -: -:-:- drift velocity hu$t starting up.

::!:::~::::: (b)

~}!/ ____...E'/( % ~= .. : ~ . :: : : - : : : - : : · - :. Section + + + + + + + + ~{\ :perpendicular ~:::::::::::· -·to z axis; :~? . . ~- :~: . : . : : : - : : : ,· : :-. c;lr . i ft veloci . t y 8::::::::::iri steady s,ate.

8'.::::::::::-: ~::::::::,: (c)

~==:=::::::- f { \ ,. .- ..· .·.·. FIGURE 2.13 The standard geometry for discussing the Hall effect (after Kittel).

~::::::::::-.

~=:=:::?

ix, t i)~e quantities Ey, and Bare all straightforward to measure, and in our ~f{j~ple approximation for electrons in conductors we have (from Eq. (2.18))

: 'r - !. : ~ · ~1 :- - :- } · J · x = ne 2 -r Ex/ m; therefore, ~ 1/. ...

t ~=:::=::"

~it eB-r:Ex/m 1 RH=----- (2.22)

(ne21: Ex/ m) B ne f =~:::::· t}~< if=:= fit> ~I> ~ -'.-:-: .-.- ...- ~ /~~~ /]

66 2 Electrons in Solids -:-:.:~ ::::=:: ,•.·.,.· }J That is, the Hall coefficient is the inverse of the carrier charge density. In fact, the Hall effect is a useful way to measure the concentration of charge }@ carriers in a conductor. It is also convenient to define the Hall resistivity as /j i\ the ratio of the transverse electric field to the longitudinal current density, jj that is, ' PH= Ey/jx BRH, (2.23) \{ which depends (in our approximation) only on the material and the applie~·f magnetic field. ) )

}]

:)~: 2.3.1. Measurements )~~~; )]

In order to measure the Hall effect, one needs a sample of a conductor,·-:tt iJ but not an especially good conductor. This is because one also needs a \Ji relatively low carrier density ne in order to get a sizable effect; this of ....

.·.- course leads to a relatively high resistivity. As seen in Table 2.1, bismuth\\ is a good candidate metal, and we describe such an experiment here.11 :\ } .......

The setup uses a bismuth sample with rectangular cross section, mounted }:~: .....

on a probe with attached leads for measuring current and voltage. A ther-<:J mocouple is also attached to the sample so that temperature measurements \]

can be carried out The magnetic field is provided by an electr01nagnet )} capable of delivering a field up to ~5 kG over a volume roughly I cm3 • )j \J The bismuth sample probe is shown in Fig. 2.14. The width of the bismuth sample is w 6.5 mm and its thickness, measured with a micrometer 1 \ / = 4 is t 1.65 x 10- m. The effective length of the sample is the distance) @ i}!

between the leads used to measure the current ("white" and "brown." as.

shown in Fig. 2.14). In our case~ this distance is f. 7 mm. Current is /} supplied by a DC power supply, connected to the sample through the "red'~ }} {@ and '~black" leads. Toe Hall voltage is measured with a digital multimeter~ }J using the "green" lead and the output of a potentiometer used to balance /j the voltage on the "white" and "brown" leads. A separate bundle of wires are connected to leads that carry current to the heating resistor, and to a)/ ·.·.~· -iJ thermocouple that measures the temperature of the bismuth sample. )J Begin by determining the Hall coefficient at room temperature and for a to}J relatively high magnetic field. Turn on the electromagnet power supply :}:~ ·.·.·,' · Semiconductors also make good candidates, with a very low carrier density compared) } to a metal. For a description of such a setup, see A. Melissinos, Experiments in Modem)]

/t Physics, First ed. • Academic Press, New York, 1966.

:::~:: \\ ._._.. ., \::1- ::::;:~ :}~~ ·:::;~ ;-;/~~> .

1\\itl; 2.3 Experiment on the Hall Effect 67 ff: {f_j\\} ...

:_w_hl_te-------------~ Thermocouple u.·.·.· Brown s ,l 'X . ~ .. . . : . .: . - . : : , : • : : : • : - . :. . Cll- I ;-~(::'. /\ J While I I ~ ..: r.:- <· Browri I \ ·- ' . t - · . 1 -~~·:r::: ~ : -. , B . o ord Black 0 Bl : • I I. • • ,. --, - ,,: . Green ' 1 I Cu ,.'1/,I'.·.: ::· Red ~ ~;,:.

..1 -:fi 1 ,;'~·,,-. I ::.:?;:;:; AJ Al - - - I - . I Reststor • 0::::::: ~=:~~: Black ··%::::::: ..: :::?::· .-\t\FIGURE 2. l4 Schematic of the probe used to make mC11.Surements of the Hall effect ::~t:'.:.fo bismuth. Electrical connections are made to the bismuth sample using copper leads, A ff: tfiermocoople, as weU as a resistor which acts as a beat source, is also amicbed to the sample.

}?\ rwo separate bundles of wires emerge from lhe probe, one of wruch is used exclusively for if)1eating the sample and for measuring its temperature.

,;;;:•.•,•,• lli!lf .

~{):around 4 kG. It wilt likely need an hour or so to stabilize. In the meantime, lf (with the sarnfle probe removed fr~m th~ magne~c field, ruo about 3 A %:::Jhrough the bismuth sample, and adJUst the poteot:Joroeter so that the Hall jf/voltage is zero. Return the current through the sample to zero. The sample %,(fc:an get quite hot while it is conducting so much current. Be careful not to i{)ouch it, or to touch it to anything else.

~f) · Wben the electromagnet is stabilized, measure and record the magnetic tlfneld using a gauss meter, or by some other lechni,que. Now, place the sample ~{)>robe in the center of the magnetic field. Quickly raise the CUJT~nt I through ~:;::::tbe sample to 3.0 A, and re<:ord the Hall voltage VH. Then, qu1ckly, reduce '.t'• . J' • • ~:~)be current by 0.25 A, and record the Hall voltage again. You should carry l()his series of measurements out rather rapidly to avoid leaving the bismuth ~fj]:sample at high temperature for any extended period of time. When you f.:({bave reduced the current to near zero, and recorded the final value of the ~:;:::: .-%-~: ,:~;·~-;.: :/}!

}/ll 68 2 Electrons in Solids ·.

.:.::.:.:.:.:.:.:.=....:.:.

tit 4 .-------.------,---~--,-----,-------,----T, ·:.·::::~==== ·.::::~=:::

## 3.5 :::::::::j

·. . · . . .·· . .. · ·. . . . · · • .· · - .•: · ,:::::;::::: 3 Slope=>1.23 mV/A --:;:;::.::~ :;::::::::: .··..··..-·. ................. .

E 2.5 :::::::::::~ .__.. .·· :-:-: ..; -:-: .1:::::: ro 1.s :c 0.5 :1 c;..__ ___...._ __ ___.__ __________ ~---- .·.·-:::::..-, 0 5 25 3 o. C~rrent lh::ugh sam:le (A) .

FIGURE 2.15 Sample of Hall effect data, taken at room temperature and with a magnetic \::?.~:=:: field B == 4.42 kG }:~~:::: ··\ fifiI Hall voltage, remove the probe and recheck the value of the magnetic- \{/ field. }:::;::::: = )}{ A sample of data taken in this way, at room temperature and with B \/?

## 4.42 kG, is shown in Fig. 2.15. A free linear straight line fit gives a slope

of 1.23 mV/A, with an intercept very close to zero. In terms of quantities \{{ {ff related to our measurement~ the Hall coefficient (Eq. (2.21)) is expressed by .

..· .·.·.-....

6 4 ni)

3 = 7 3 RH= (1.23 x 10- :) (1. ~:~; 4.59 X 10- m /C = /}J This is quite close to an accepted room temperature value of RH 5.4 x 7 3 th~.:j)j 10- m /C for pure bismuth metal. The uncertainties in measuring dimensions of the sample can easily account for the discrepancy. · )}~ Of course, this sample and this setup can be used to determine the·{:}~: ·.·.·.·.i"r resistivity of bismuth. Outside of the magnetic fl.el~ measure the·voltag~:\ )§ .: : ::::;;:; ... : · . : - : .: : ·-: :. • .~ = ., 4 . ~ ~. J Ail ~?i~~:~

## 2.3 Experiment on the Hall Effect

TABLE2.2 Sample data, taken by a srodent.. for the resistivity p of bismuth as a function of temperature, using the Hall effect apparatus T (OC) T (K) p (µf2-cm)

-80 193 70 -60 213 85 -40 233 96 -20 253 110 0 273 121 20 293 134 ':.

40 313 150 60 333 163 drop along the length .e. of the bismuth sample, as a function of the applied current, and determine the resistivity p from the ratio Ex dVx wt e· = i-r = p dl The temperature dependence of each of these quantities can be detennined by heating (and cooling) the probe, and recording values as a function of temperature using readings from the thermocouple.

Table 2.2 lists some results for the resistivity p in (µ.,Q-cm) as a function of temperature. To examine the temperature dependence it is best to make a log-log plot of the data vs T since we expect a power law dependence.

This is shown in Fig. 2.16 and when fitted gives p C< yl.52_ Note that at room temperature (T 25°C)

p = 1.4 x 10- 4 Q-cm in reasonable agreement with the data of Table 2. L 3 2 lndee~ one expects a T 1 dependence of the resistivity on the temper ature because of the following argument. From Eq. (2.14) the resistivity is · -inversely proportional to the mean time between collisions, as long as the carrier density remains constant. Now the mean time between collisions is given by r: ).../v, }:::=¾ :-:-:·:--/.

:;::::J 70 2 Electrons in Solids .:::::;=x ,:-;-:.:-:--: :..::..:.::.: =:=: _.. ......

:::::::::~ :::::::::~~ ,::::::::::3 -:-:-:•:. .: ~ ::::::::::~ ::::::::::=: ·:::::::::::: I}i~ i t .· : . :: · t . : - : . : . : .l : .. : .. : .. : · ; 102 )fl :~ tn "iii Q) poc T1,52 a: p (25°C) =139 {µQ-cm)

## 102.4 102..,.;

,·,·.·-~·.,-.

<::::~==~ Temperature T(K)

:::::;;=;;:~ J!all)/f FIGURE 2.16 The resistivity ofb ismuth as a function of temperature, taken with the effect apparatus (data from Table 2.2.) The data are fitted to a power law form. · <}{~~ .Uif ··..··..··..t•.·Jr". .r 4 _ where ).., is the mean free path for scattering, and v the therm.al velocity of'}/{ the electrons. For v we can use \ :}} -:-:.:.:--:, ~mv2 ~kT J3kT / ~(~{: ~~e Ill!

The mean free p!tll, A, de!reases co~lision cross~~tion lllcreases, that:{)} namely as the lattice vibrations increase with temperarure. lt is found ).., is inversely proportional to the ten1perature, and therefore .){} 312 j:{\ t ex 1/ T <:::::::: .:-:-:-:-: or using Eq. (2.14), :\(~~~ .·.·.·.·.

·.·.·.·.·.

We can also exantlne the te~;r:· dependence of tlle Hall coeffi- l!i!J The}/\ cient. In this case it is best to plot RH on a semi-log plot vs 1/T.

reason is that the Hall coefficient (see Eq. (2.22)) is directly inversely pro-))\ portional to the carrier density, and we expect the carrier density to depend})/ shown\\/ on the temperature by an exponential factor, such as for instance in Eq. (2.28). The data are plotted in this way in Fig. 2.17, and we recog-:<{{ nize two distinct slopes. As expected, RH falls with increasing temperature){{ 2. 4 Se mi con d u ct o rs 71 2 2.5 3 3.5 4 4.5 5 1/T (K) X 10--3 FIGURE 2.17 Measurements of the Hall coefficient as a function of temperature.

b~ause the carrier density increases. By fitting the data to the form n cxexp(-E/2kT), we find for the two regions low T, E 0.029 eV high T, E 0.120 eV.

Such energy differences are typical of the excitation of impurities. It is also relevant to note that the carrier density at room temperature is n = 1/eRH = 1.35 x 10L 9 cm- 3 .

This is quite high and typical of a conductor.

2.4. SEMICONDUCTORS 2.4.1. General Properties of Semiconductors We have seen in the first section how a free-electron gas behaves, and what ;an be expected for the band structure of a_c rystalline solid. In the second )]

n /?

2 Electrons in Solids thei[[ii!

section we applied the model of a free-electron gas to the behavior of resistivity of metals. ht the present section we will study some propertie~)J of semiconductors that can be verified easily in the laboratory, where we<( will make use both of the free electron gas model and of the band structure/\ of the material. As mentioned before, a semiconductor is a crystalline\} solid in which the conduction band lies close to the valence band, but is)} not populated at low temperatures; semiconductors are unlike most metals\)

in that both electrons and holes are responsible for the properties of the( ]

semiconductor. If the semiconductor is a pure crystal, the number of holes}~ (positive carriers, p) is equal to the number of free electrons (negative\ :~ carriers, n )t since for each electron raised to the conduction band, a hole/} is created in the valence band: these are called the intrinsic earners. AU~):n]

practically important semiconductor materials, however, have in them certain amount of impurities that are capable either of donating electrons<} to the conduction band (making an n-type crystal) or of accepting electrons.{} from the valence band, thus creating holes in it (making a p-type crystal).)]

<J These impurities are called extrinsic carriers and in such crystals n -::j:. p.

it(/ Let us then first look at the energy-band picture of a semiconductor as is shown in Fig. 2.18; the impurities are all concentrated at a single energy/ } level usually lying close to, but below, the conduction band. The density(/ anc(:J of states must be different from that of a free-electron gas (Eq. (2.4)

Fig. 2.2a) since, for example, in the forbidden gaps it must be O; close to;:)

]II .' ·.· ~· . ,:::::: ..

::::~ ··.,··..··,~.· ·,-.·~ .·,·.·,1 ::::;:- ,:::::: ·.•.•4• •-:,::.":4::' ·-::::;:: FIGURE 2.18 Energy band structure of a semiconductor without impurities. On the left/ j the~/:: hand side the Fermi distribution for a free-electron gas is shown~ on the right-hand side actual density of states D(E) is shown. .)/ /~} . ·.. ...

·.·.·• ·,·.·,· :::::~: · ...' .·<...·· .,i -::::~ -:::::: •:•:": .:.-.:-..~ ., .,.:-:-: ;,I1'.·.1·.

## 2.4 Semiconductors

ff/ .,.~~/ pn the other han~ the Femti distribution functiont Eq, (2.3), remains the ~f)sa.me. The only parameter in this function is the Fermi energy, which can be \ \ Jpund by integrating the number of occupied states (Fermi function times ff {density of states) and setting it equal to the electron density. It is clear, ~{J1owever, that if we are to have as many empty states in the valence band as ~(} occupied ones in the conduction band, the Fermi level must lie exactly in ~{\ the middle of the forbidden gap 12 (because of the symmetry o.f the trailing ~/ :~ge of the distribution). In Fig. 2.18, the density of states is shown to ~\:the right and the Fermi distribution function to the left. We measure the Wf },position of the Fermi level.from the conduction band and define it by Ep; ij})he exact value of EF is ~r--·.·.

*)3/4 ~ .~:: ? :::. · ·- E g ( mb ·;t(·: EF=-- +kTln m* (2.24)

-:-:-:: e ~f t ..-t\. Since the Fermi level lies below the conduction band, EF is a negative mt m; ~ (( quantity, Eg is the energy gap always taken to be positive, and and ?f I!

~~~{·.are the effective masse~ holes and electr~ns. respectively. we and WF I l { r -- ~tand for the actual pos1a.on of the conduction band and Femu level above the zero point energy, then t~r---· t::::· tr fl( To find the density of electrons in the conduction band (or boles in the }?

.valence band) we simply substituteEq. (2.24) for wp into Eq. (2.4), multiply i{\ by the density of states, and integrate over w from w we to +oo. When, t:?

rt·h owever, the exponent ;x?-:--::--·. Eg + >> {? -(WF-W) ~ 2 E kT, (2.25)

~~/: . . : . : . :· :.· J\ the Fermi distribution degenerates to a Boltzmann distribution. (Here E f \\ is the energy of the electrons as measured from the top of the conduction f?.

band; obviously it can take either positive or negative values.) With this ~/ : _assumption the integration is easy, yielding ~~ . .:..:..:..:. .

:-:::::: · · n (2rrmekT) 3/2 (2rrmekT) 3/2 J\: = ~ eEF/kT e-Eg/2kT. (2.26)

~::::-· h2 h2 , ~=:::· ~-··· ~ { 12lf the effective masses of p- and n-type carriers are the same.

...: =:::: P.,:..':·-·: -· ::;::;:: ~::::· 1/.::: z::::: z·-·.· { \:: ,::::::::!

:::::::~1 ·.·.·.·-·,J /J@ 74 2 Electrons in Solids } }:~ .::::::~ similarly, ".·}.·.i-.....j.• .J cJt:tT) (2Jt:;kT)

3/2 · 3/2 :::::::~ = ~ p e-<E,+Ee)/kT e-E,/2kT, (l.l?)- ~j~ , .;::::::~ It is interesting that the product np is independent of the position of the/}~ • 13 · · {.-.\-.,.t·,: Fernu level --especially 1f we take me == m1z · · . ·.-.-.....z = = n?- np 2.31 x l031T3 e-Eg/kT_ ) ] ~ ' . . . :)j~ From the analysis we expect that as the temperature is raised, the density-:/~:~ of the intrinsic carriers in a semiconductor will increase at an exponentia(Ji rate characterized by Eg/2kT. Thls temperature is usually very high since)J ~ .·.-... ,.,:.: Eg ~ 0.7 V (see Eqs. (2.29)). \}~ We have already mentioned that impurities determine the properties o(}j a semiconductor, especially at low temperatures where very few intrin~)Jf sic carriers are populating the conduction band. These impurities, when( )~ are in their ground state, usually concentrated in a single energy level)}~ 6.if {J lying very close to the conduction band (if they are donor impurities)

•· ·,·.·.<_'.•; very close to the valence band (if they are acceptors). As for the inµinsic(j ~ ~6:!Ji]

carriers, the Fenni level for the impurity carries lies halfway between conduction (valence) band and the impurity level; this situation is shown it(}~:~ Figs. 2.19a and 2.19b. If we make again the low temperature approximation(/~ \t~ of Eq. (2.25), the electron density in the conduction band is given by ::::::::t 2n m 3/2 . - · :; .- : . : - = . : - ; ~ ~ n Nd kT) e-E4f 2 kT, (2.28~}:~a: ( h 2 "· ) . i .. i . ,,.

where Nd is the donor density and Ed the separation of the donor-energy\/~ level from the conduction band. In writing Eq. (2.28), however, care must}:~ be exercised because the conditions of Eq. (2.25) are valid only for very(@ low t.emperatures. Note, for example, that for germanium }\ ·.-..•.. ,.

= = .· :::::=~ Eg 0.7 eV, and for kT -:- 0.7 eV, T 8000K .·· ..· -.

-. :.-- .: ..........

whereas }!if = = and for kT 0.01 eV, T 120K. (2. 2 9f~ ,~,.:_:~.~,~,.,~.

. ....•.. ,.

Thus at temperatures T ~ 120 K most of the donor impurities will be in th~/~ conduction band and instead of Eq. (2.28) we will haven ~ Nd; namely)J -::-:::: ~·r>:·1:~ l 3 This result is very general and holds even without the approximation that led }!:~: Eqs. (2.26) and (2.27). ){;; ·.·.-,.

}fit /j

## 2.4 Semiconductors

II :=:· ;~~ ~ ~ •:.:, ::::: ::::· :::: ::::· :=::: (a) (b)

:f FIGURE 2.19 Sarne as described in the legend to Fig. 2.18 but with Lhe addition of f.

impurities. (a) The impurities are of the donor type and lie at an energy slightly below :::::: the conduction band. (b) TI,e impurities are of the ncceptor type and lie slightly above the ti: :valence band. Note the shift of the Fermi level as indicated by the dotted line.

~~~~~: II the density of impurity caniers becomes saturated. Once saturation has !!~I \:been reached the impurity carriers in the conduction band behave like the free electrons of a me~!.

I( 2.4.2. Sketch of p-n Semiconductor Junction Theory !I.

Semiconductor materials with high impurity concentration, when properly f \ combined, form a transistor. Junction transistors consist of two junctions of {dissimilar-type semiconductors, one p type-and one n type; the intermediate ~~/region, the base. is usually made very thin. We will briefly sketch the {}behavior of such a p-n junction and then see how the combination of [ (two junctions can provide power amplification; for this we will use our Itknowledge of the band structure of semiconductors and the position of ( )j,e Fermi level, as developed previously (Figs. 2.18 and 2.19). When two b)naterials with dissimilar band structure are joined, it is important to know ~?~.i what relative energy level one band diagram lies with respect to the ~:}~ther: the answer is that the Fenni levels of both materials must be at the Y.·.· ...

~f~4me energy position when no external fields. are applied; this is shown ~ r = - : . : -: J -·· n F. 1 g. . ? .. . ? .... 0 .

...- ... · f~: f \ ..

From the energy diagram of Fig. 2.20, it follows that only electrons with i~/8e > b. We will be able to cross the junction from the n material into the p ef jegion and only holes with Eh > b. Wh fyom the p region into then region.

.~~ ~:~:- ..

f:.- ~~11 ;.::~:::·· \ff: -:·:-:-:-i . -:-:-:-:~i 16 2 Electrons in Solids \)1 -:-:-:-:~ ::::}i ! :::::::~ Increasing 1 :o wnhlU ··;:/~ potential -·.:·..=...· *· C/) ~ -eC ·oQ) \)~ .c. . -:-:-:-:-:~ .... 0 if :;:::;:~ LL <D . .;::::::~ Preierred Increasing j '' direction of potential motion J (downhilO \Ji ......

p-ty~;:J:~tJ FIGURE 2.20 Structure of the energy bands al the junction of an n-type and a :):ij semiconductor. :· •.:}~~ ::::~~ Minority ·:<j~ Reverse bias Forward bias carriers .·}@~ (a) (b} ··:::===~m :Yi@ .•,·.-..., m -:: ;: : : :: : : : : :~ 1 . . i ~?

by the amount of the bias, as shown m Fig. 2.21a. We see that the bamerrJt ·-:::::;;ij The result of such diffusion is the buildup of a local charge density, which preven~u~ furthe: di~ion. Throughout the present analysis, however, we will neglect the local effecttJ~ at the Juncuon. ::::;:X: ,:::;{;[ . -:-:·.~ ?¾.

::::~i :::=~»· :::::i® .. :::;:,* :-:·:"Y/.

;?::;::.

@} :,.:. . :-:- 2.4 Semiconductors 77 ~=:?

?::/· [}A We and 13.. Wh are increased by almost the full voltage, making any motion t/of minority carriers across the junction very improbable. Figure 2.21 b, on fr ..

....

(the other hand, shows the situation when forward bias is applied (favoring (\the motion of minority carriers). The Penni levels are now displaced in the ( \ opposite direction so that the barriers are lowered. However, the full bias ~\/voltage does not appear as a difference between the Fermi levels because /~ynamic equilibrium prevails. There is a continuous flow of minority car ~:~{riers in the direction of the electric field (ho]es obviously moving in ·the f(~pposite direction from electrons) and as a result a potential gradient exists f(aiong the material; thus the entire bias voltage does not necessarily appear .~.r.·.· :f \~t the junction itself.

§?\.

We will now consider two junctions put together; in Fig. 2.22a, p-type, [\n-type, and again p-type material are joined. When no bias is applie~ we ~~(~pect the Fermi levels to be at the same position, with the resulting config- ,_._._.

~t)ilration shown in the diagram; in agreement with our previous conclusions )rom lhe consideration of a simple junction, we see that barriers exist for f/the motion of holes from the p regions into the n region, and also for the ~t(,notion of electrons from the n region into either of the p regions.

~i/ Figure 2.22b shows the double junction under operating biases; note M(that one junction is biasedfo,ward, the other is biased in the reverse direc f!)ion. The n-type material common to both junctions is called the base, ~:::::: ...

;,:-:-:-:-· ~:::::.

r.:·.·.·.·.

,, , . . . . - · - . .. · ·· . .. · ·· . .· . .

, , . . . . -· ..--..··..·· No bias Operating bias ~=<< (a) (b} ,:-:-:-:-.

, ..- .·.·.·.

, , rr . .

. .. .

.• - · · ..

.. · ·· •.

.. .· •· · .. . · .' ,r.. .-· ..-·..•·..

r ~t:.=•.

:. •::. e:•-.·• ·..

to-or Battery ,, . ..

.· ...

,t:.=.,:,:.,:·: .

. .

[{( ~:-:-:-:-.·. -V #:\Li: 5 )i1 ~:: 1~ to O of ~f{ Battery a Q ~:~:::::-:: +V ~{k aURE if 2.22 Structure of the energy bands for a p-n- p junction transistor: (a) with no ~~·as applied, and (b) with operating biases. Note that the eminer is forwardwbiased. whereas ~l:µie·colJector is reverse-biased.

r ~==:< { ~{' It\ ......... · ::::::: :-.;,•~.:·:,:·: =~~::;: -::::::::~ '::::;::;~ :-:-:-:-~ 78 2 Electrons in Solids ::::::::i )i@~ :)\J~ while the p type of the forward-biased junction- is the emitter; the p-type )}m material of the reverse junction is the collector. A completely symmet~ ric device consisting of n-p-n materials will perform similarly when·.) )~ the biases are reversed. From the energy diagrain of Fig. 2.22b we can /}~~ • • t •f.,i.

:\)@ -:,:-/~ ::J?tl .·.·. .~ ~

## 2.4 Semiconductors

}( •.·,• .....· ::::: FIGURE 2.23 Photograph of the setup used to measure the properties of a diode .

~·..•-..·• {\ \::: :are repeated for different currents through the power resistor, giving the r:: setup time to come to thermal equilibrium.

{::: To analyze the data we must appreciate that the diode does not obey the { \ ideal diode equation (2.30) but operates in the recombination regime, fi lwbere :=:::::·,· ff/: 1 Io(eeVe/2.kT - 1) :::: IoeeVn/2.kT' (2.31)

r:::::t:: and tbe last approximation is justified because the term exp(e Va/2k T) L {{ Therefore, we present the V- 1 curves for VB > 0, on a senti-log plot in [( Fig. 2.24a. From the fit we find the slopes I~~ :~~ ~~: = = T 24°C e/2kT ::: [\.= ;Note the onset of saturation for bia<;es VB 0.5 V and also the different if(: .µitercepts at V 0.

ff: .

We observe that the measured slopes do indeed scale with temperature f{/ as expected and if we average the three results we obtain e/2k=(6.28±0.19) x 10 K/V.

G W. Neu dock, The p·n Junction Diode, Addison-Wesley, Reading, MA, I 983.

..; :::·-:-:, l~ if~~t :-:-:-:--.a:; .::::::;:~ II 80 2 Electrons in Solids (a)

• T=69°C • o T=37°C • ij Iii • T:::24°C • :I 102 0• 0• :: : : : : : ::~-=~ ?ili :./ii~ 10-1 ..

·\}~ 10-2 . .·.·.···x., :::::::~~ -:-:-:-:J..- :/~::::;:~ 10-J ..__ ___ _. ____ _._ ___. ......_ ___ ····x· .L..._ __. .,___ __, .___, . tlef~ 0 0,1 0.2 0.3 0.4 o.s 0.6 .. :. : .. ..: ::•:i' ·::::;~:? xj.

FIGURE 2.24 Measurements of the current through a diode as a function of bias voltage, / ::;:~: )jf~ for different temperatures. (a) is for positive bias, plotted on a semilogarithmic scale, }!l§~ Exponential fits are indicated. (b) is for negative bias voltaget plotted on a linear scale. · }ii :<~==i \Jj ?ti :: :- ,:

## 2.5 High Tc Superconductors

Thus, using the value of the Boltzman constant k 1.38 x I 0-23 J /K we find that e = (l.73 ± 0.05) x 10- 19 C io good agreement with the value of the electron charge.

The different intercepts are an indication of the variation of lo with = = temperature. (Of course at Vs 0, I 0 but th.is point cannot be reached by on the Jogarithm.ic plot.) A better way of determining lo is applying negative bias. From the negative bias dat.a (Fig. 2.24b) we find that :•,' 1" = 297K lo= 3.9 pA 303K =4.4 pA 310K 6.7 pA .. = 319 K l 1.6 pA.

:-· The reverse current is proportional to the minority carrier density. As the := ' : temperature increases, the population density increases as ;:: •.• n ex e -E:/2kT, :'•, ::· :- ,: where Eg is the energy gap between the valence and conduction bands.

} From the data we find thal !: = Eg 0.84eV.

:~ :- :: This is in reasonable agreement with the energy gap in silicon ( l. l e V at Ii room temperature). Systematic error can come from a number of sources, ::: including contact potential differences and the extent to which the negative bias data of Fig. 2.24b has reached its asymptotic value.

:: 2.5. fflGH Tc SUPERCONDUCTORS ·.

=·· •'.• ::: 2.5.1. Introduction :•.

-: In 1911 it was discovered that certain metals completely lose their electrical =· ·.· ::: resistance wben cooled to very low terupcrarures, typically less than 10 K.

The loss of resistiviry sets in sharply when the critical temperaJu.re Tc is } crossed. This is analogous to a phase transition between different states !!; of matter, as for instance from ice to water. The phase diagram for the ·.• :I ::: ~= ;-: r.

.·.·.·-~-:;s, :!itW~ml 82 2 Electrons in Solids ·.:::;:;:~ -:;:) ij ::::;:;:~ ··::::::~ .·.·--·@ H .·-:.:;:-::\-;-f::l::: ·::::::~ ·.·.···P% :: : : : : ~,,;.;·.

·.·.·.·q.-: ;,:-:-·,m .-:-:-:-~ •.-:;:;:~~~ ·::::::~ .·.:-:-:~~ -=·=·=-=~ .·,·.·.-~ ···:::===m -:;:;:~~ -:-:-:~~ :::::~==~ ,-::::-:.;f~ .·.·.·~ ./fai ·}.·.·:.:~-w1=/~.l,~; : . -: · ;t: · :i:.z . ,& ~.

microscopic theory of superconductivity proposed in 1957.

.-:-:-~:-1- )·<··~~ .·:·:~ ))~~ ',:::::~~ >:-:~¾S: :: ::::~

## 2.5 High Tc Superconductors

Room temperature (a)

(e)

Cooled '> (b)

Low !t)\::· tsmpera1ure ?.=}:/· %~~/\~::.

l!I (c) (f)

' ' 8 -0 it}~{/( (d) (g)

.·,·r.·.·.·.·,· t,I'. :.· ~t·~?·.·.·f,·l,·: •O• URE 2.26 Behavior of a superconductor when placed in a magnetic field. (a--0) The ,.,.

.t./..'J..) .~ d is swir.cbed on after the sample is cooled below Tc. (e,f) The field is applied before ~::??tooling the sample. l.n either case the flux is expeUed from the superconductor and ao field ,,,..,.·.·.········· ;:::~===::is trapped in its interior.

~ff/)

f(\$e = external field inside the conductor. In a superconductor, however, B 0 ff(.fu the interior region, irrespective of whether the field is applied before or .,.,. .• .·.·.

,• ?:f\~r the superconductor is cooled below Tc. This is shown in Fig. 2.26.

./'1 •••••• !

ff\/\.The exclusion of the magnetic field (flux) from the interior of a super- ~{/ ¢9~ductor is called rhe Meissner effect and can be easily demonstrated by f?}~vitating a small pennanent magnet above the swface of a superconduc ijf)or: This is shown in Fig. 2.27 where the solid lines are the magnetic field :>... . .

/{:/1.ines of the the permanent magnet. Since the superconductor must expel [ }iJux from its i~terior, the induced surface currents produ~ the fi~ld s~own Wf ~y.-the dotted Imes. They exactly cancel the external field m the mtenor of ~ (te super~nductor. Ho~ever, outside the superconductor there now ex.is~s ..~ f:wmaguet.Jc field opposite to that of the permanent magnet. Thus there 1s ffA force pushing the smaU magnet away from the superconductor. As the ...

~j , i ,., l ·,· · ~r.-::::::<; ~ :-:•:•:•:- ~l\· 84 2 Electrons in Solids Permanent magnet .. :-· ~f;: 0:r= ·.·.· ..

~llF 2.5 High Tc Superconductors 85 ·.,t-.,,.~f ... : Superconductors are widely used for the construction of high-field rnag- :::::iets. They are also extensively used in some of the mo~t sensitive scientific ,,, ..

•. ' :;f/instrumenls; finally, they display fascinating quantun1-mech.anical effects ~·t\o a 17 macroscopic system.

0.::;:;".· ll}i.s.2.

?bservation of the Superconducting Transition [~;@- .: ::::::-. in YBCO .:-;-:,:- ~!.~::!Lo 1986 Bednorz and MillJer reported superconductivity at temperatures ~.l\ }n excess of 40 K in certain samples_ of La-Ba--Cu-0. It was i;~o_n dis f#J:covered that the YBa2Cu3O7 ceram1c (YBCO) undergoes trans1bon to f.j{}t,he superconducting state above 90 K. Pellets of YBCO can be manu fl)iactured in the laboratory by mixing the chemicals in powder form and .-x-...- :-.·.· ~=lff¢ompressing them in a steel die using a hydraulic press (to approximately :tJ~.000 psi). The pellets are then heated in a furnace to about 900°C in an ~~);;:,cygen atmosphere and allowed to cool. However, it is by far more conve l~?iit~nt to order 1-in.-diameter disks of YBCO from a commercial supplier.

. :f:Areliable source is Colorado Superconductor, P.O. Box 8223, Fort Collins, .;.-".. · ..· ····· ,;:=::;;:;:£0 80526.

» ·.·.·.·.

~}(Pata can be taken as the sample cools or, as was done for the data presented if Jere, by first cooling the sample for 2 min. and then removing it from the .BfJi:quid N2 bath. Temperature and resistivity are recorded as the sample .{)~1,arms through lhe superconducting transition.

~~{? The four connections (see Fig. 2.29) are spaced equidistantly, separated d:{~y a distance s, typically ""'1 mm. A high-impedance source supplies a ~r:~9.nstant current to the outer terminals, l and 4, and the voltage across << ~=}~als 2 and 3 is measured. For a flat sample of thickness t s, as if~- the present case, current rings emanate from the outer tips, so that the :«--=--.·.···· . • .

.: ~::::::~tance between temuoals 2 and 3 ts ,..:,-.,;~-:-:-.' ;t:.-;.~-:-:,· :&.}(:· 1 dX p 12.s p = X3 = - = - R p-- In x ln 2.

x 2rcxt 2rrt s 2rrt ~{{t %··· .j(J7see R. P. Feynman, The Feynman Lectures, VoL W, Lecture 2l.

~l\f8 Toe commercial pellets can be obtained with all the leads auachcd .

•: ..4:,f::::: ··*.·:-: :~;:~;;:: .

.:-:?:=:::, ~~% I~~:: :,";::::.

.· .·. .......· ,:)}~~ ·):):~ 86 2 Electrons in Solids ,:::::::;::: :::::::::j .;::::::;:: . ::::::::::: Constant (:~:~{~ current . -:-:-:.:-: :;:;:::;;~ rce ::::::::;~: .' .·.·.·.- ·- :-:-=·~·: ·:-:-:-:•: ,:::::::::: . ·:}J .·.·.• ..· J ::::::=:~ <I YBCO pellet !!I ·tti :->:-:•:..:-: ·:!i\li -:-:-:,:-:'.~ .· .<·:.:·:.·:-:--·:::i-: -1 }\::~ Ice water bath <:?~:~ ·.·.·.-.-~ measuring){!

FIGURE 2.29 Schematic of the connectioos to the four-way probe and of the apparatus. -:-:-:-:~ .·:-:-:-:~ ::;:};~ }/\~]

Furthermore, due to the presence of two outer tips, V23 2/ R, so that fof)Jj a thin sample \ ::::/~ · !l!I (V)

nt = T · (2.32).:::::::.::.: : P 102 .· ).· .l·.·.-i.,,.

Note that the probe spacing s does not enter Eq. (2.32). .{}J In these measurements, the constant current source provided / ~/~]

500 mA to terminals 1 and 4. Typically, in the normal conducting stat~:J ~ below of}?i V23 :::::: 1 m V, whereas the transition, V23 is at the noise limit !o: the HP ~4:401A meter ~sed ~he measurement (V23 '.::::'. 10 µ V). Sintche~,f:~fJif the trans1t10n occurs rapidly 1t 1s important to use a computer to record data. In the present case data were recorded every 0.33 s. The HP meter was}i*.

.·.·.-.-~ connected to the computer through an RS232 serial port, the thermocoupl~{j voltage and source current through an ADC card. })]

/I It!

=~:~:~ .•:-:• .

i •·= i .•·=.··= i . / 2.5 High Tc Superconductors B7 ,~imt /:;::: 1 ...

___.. ...: e:' • • ~:~~~:~ ....:.

...

... -::::::::·. ~~ f f ~!~ •i• • 0,8 I.'· .

~:r: :;:{(:: > 0,6 • : • ~:=::::.- g • :ff~:!::, f • ~t:::.

0.4' • • ,it -: ~l(·

## 0.2 ::

~{jitiJGURE 2.30 Plot of V2.3 vs T. Below lhe uansitioo ut T 98°K the voltage on the i f:'j)robe terminals is compatible with ze,o. The transition width 6T < t°K.

*::::;:: ~l1l~}- ff Results obtained by a student are shown io Fig. 2.30, which is a plot of f}V23 vs T. It is clear that a phase transition occurs at T 98 K. The width ,.(/of the transition is J)..T < 1 K. Note that the voltage V23 below Tc is too .....

.,..

:~/ \small to measure.

-~}} For T > Tc the resistance across rerminals 2 and 3 of the probe is of ~f]>rder :i%-:-:--.

·.•.•.•.• ~f:::"

:;,;:;:;::: R23 = Vn/21 ~ 7 x 10-4 V /1 A= 0.7 mn.

:~-:::-:::~-: ~:;:;: :_ = · \:Jhen, from Eq. {2.32), using r I mm we obtain :;,;:::;:::: .

-~li~f p = 3.15 x 10-4 Q-cm.

,.=: t = ;.::.. .

..,_ =;t~lrus is two orders of magnitude h.igber than the resistivity of metals (~ee ?/able 2.1) but is to be expected for a ceramic material. The gradual increase J~~ the resistivity with temperature for T > Tc is also expected since cbe if~ormal" electrons scatter from the lattice thermal vibrations as discussed ~\'.. Section 2.2.

::a=:::· ~;: ~-~~:·J·.

:::::::=~~ .:::::::::~ -::::::;:~~ 88 2 Electrons in Solids .

. :1:1; ··.·.·.-J 2.6. REFERENCES {!)~ For the material covered on semiconductors, the reader may also consu~(/{i the following texts: \J~ - ·;:::::;1 W. C. Dunlap, Ir.,An Introduction to Semicontluctors, Wiley, New York, 1957. Bricfbut clear treatment~:/;::.:~.

R. A. Dunlap, Experimental Physics: Modem Methods, Oxford Univ. Press, New York, 1988. Detailed.(..} ,.

discussion of semiconductors, their physics, and device applications. · ·:::::~:_;:~ C. Kittel, Jnt~duction to Solid State Physics, 7th ed., Wiley, New York, 1996. Amore general treatmen(Jij \:::if of the solid state.

W. Shockley, Electrons a,1d Holes, Van Nostrand. New York, 1950. A thorough presentation of the\ }::~ ~~ .:~ .;,;.;;:-.~ ,,:.:,.,.;:,:3 i{Jj The lecture on superconductivity in the Feynman lectures, Vol. III-21 <}*?- highly recommended. Also highly recommended is the text -::::i:m:::1 ~f A. C. Rose-Innes and E. H. Rhoderick, Introduction to Superconductivity, Pergamon, Ehnsford, ,:::Ji 1%9.

::::;:;:~ .·>:·:;@ qn§i}l For a practical account including information on high Tc materials can consult · .::::::~ Summidl D. Prochnow, Supe,conductivity: Experimenting in New Technology, Tab Books, Blue Ridge {tw, PA. 1989.

:.

-~ 'f 1:' ,::::~=-~ ,:::::i~ ::;:::;:~ -:;:;:;;~ .·.-.-.-~ :\:::=~ ......: ;; ·::::::::~ .:::::::~ :::::~~ ··::::::::~ :::::::-%=; . ·:.:':.:·:.·:=-~-~~ :-:-:-m1/b.

·-:-:.:- ., <·:-:- .:,. ::: .-:-:-:~~=--- •,·.·-·///.

,-::-::::-:::·~··~ •,·.-.·.~ .::::::.~.;.'.J X ·.·.- .:;:;:·zw·a.

/ttwm ......

.·/:~;.z~; ··-~ )(;~ ....1.. ..

:ti · fiit;_1l :?;;:-..

....

<:::-·~ '":::::::- ~~{/

## CHAPTER

~=.=.=.

~ti 1;;: Electronics and Data Acquisition ~?

Ill · i·~:~::}::\{::-- ~ -:-:-·-: {}\ ~=--··· f¾{\t··· ~lit 0;~:::::: ::::.:-.:-:::.

·={{{ 1t\.: III: 0}}/ ~}pp to this point, we have described measurements that require only ~}fudimentary laboratory equipment. Before continuing, however, we will J".?. ... ·.·, ·· :)µscuss a broader range of topics in electronics and data acquisition.

~ii:: ~t~;l· ELEM:ENTS OF cmcurr THEORY i}~e&rly _ e~ecy measureme?t _~ ade in a physics laboratory c?mes down to 0.:Jetenmrung a voltage, so tt 1s llllportant to have at least a basic understand- 0~~hiJ~ of electronic circuits. It is not important to be able to design crrcuits1 or ~jyen to completely understand a circuit given to you, but you do need to ~;~ow enough to get some idea of how the measuring apparatus affects your :}~-ult. This section introduces the basics of elementary, passive electronic 1®twts.

You should be familiar with the concepts of electric voltage and ~=~ent before you begin, but something on the level of an introductory Ji :~:::·:· \\:-: ~t>- )?

90 3 Electronics and Data Acquisition ·.

physics course should be sufficient. It is helpful to have already learned·;;:; something about resistors, capacitors, and inductors as well, but we will )

review them briefly. ): 3.1.1. Voltage, Resistance, and Current Figure 3.la shows a DC current loop. It is just a battery that provides the } electromotive force V, which drives a current I through the resistor R. ).

This is a cumbersome way to write things, however, so we will use the·} shorthand shown in Fig. 3. 1 b. All that ever matters is the relative voltage·/ between two points, so we specify everything relative to the "common"·.?

\j or "ground.'' There is no need to connect the circuit loop with a line; it is understood that the current returns from the common point back to the:\ terminals of the battery. \ The concept of electric potential is based on the idea of electric potential } energy, and energy is conserved~ This means that the total change in electric. )

potential going aroW1d the loop in Fig. 3.la must be zero. In terins of j Fig. 3 .1 b, the "voltage drop" across the resistor R must equal V. For ideal.)

resistors, V IR; that is, they obey Ohm's law. The SI unit of resistance·)

is volts/amperes, also known as the ohm (Q). / == Electric current is just the flow of electric charge (/ dq /dt, to be } precise), and electric charge is conserved. This means that when there is a )

"junction" in a circuit, like that shown in Fig. 3.2, the sum of the currents !i flowing into the junction must equal the sum of the currents flowing out.

/i In the case of Fig. 3 .2, this rule just implies that I 1 = h + h. It does not !

(a) (b) +V V - FIGURE 3.1 The simple current loop (a) showing the entire loop, and (b) in shorthand.

,•'

## 3.1 Elements of Circuit Theory

I; ~f :::; ~~::\ %f?

,;-:.:•:•:- If!. • FIGURE 3.2 A simple three-wire circuit junction.

ff\:cE!)

(b)

[f t: lil\l(.

R, ½·.;:·:·. R, ~ Bl liI\ R, FIGURE 3.3 Resistors connected (a) in series and (b) in parallel.

~tr matter whether you specify the current flowing in or out, so long as you arc ~ff consistent with this rule. Remember that current can be negaci ve as well as ::::-:-:-:• . .

f::=:=:= pos11l ve.

?:fl These rules and definitions allow us to detemtine the resistance when ff/ resistors are connected in series, as in Fig. 3.3a, or in parallel, as in Fig. 3.3b.

~--·.··· ?=:=::: In either case, the voltage drop across the pair must be/ R, where I is the [ {: current flowing through them. For two resistors R1 and R2 connected in ff: series, lhe curreol is the same lhrougb both.. so the voltage drops across !:/ ( them are l R and f R2, respectively. Since the voltage drop across the pair tf· = + must equal the sum of the voltage drops, then / R I R1 I R2, or ~~~?~~ :::::::. R = R1 + R2 Resistors in series.

i~i~~( ~/:: :lf R 1 and R2 are connected in parallel, then the voltage drops across each rJ = are the same, but the current through them is different Therefore IR ~1/ = = + /1R 1 JiR2. Since I Ii !2, we bave ::::::=:. 1 1 l :~ti R = Ri + R2 Resistors in parallel.

?::::::.

f\ Remember that whenever a resistoI is present in a circuit, it may as well rt be some combination of resistors that give the right value of resistance.

Iii 92 3 Electronics and Data Acquisition :11 ::~:::::~~ A very simple, and very useful, configuration of resistors is shown ~ )]

Fig. 3.4. This is called a "voltage divider" because of the simple relationship(::::~ and + ancf .·.·- ] ·.·.J ",, between the voltages labeled Vout ½n, Clearly Vin= I (R1 R2)

Vout I (R2), where I is the current through the resistor string. Therefore,:}~;~ \]i _ . R2 Yout - Yin-+- - . (3.lJ:-:-:-, R1 R2 :.::::::~ ' ·.·.·.·.·.1 ,-:-:-:-:-~ That is, this simple circuit divides the "input" voltage into a fraction deter{ f ~ tru'~!Jft, mined by the relative resistor values. We will see lots of examples of sort o f t hin g m . t h e I a b oratory. . . } .. ) . : ~ ~ Do not get confused by the way circuits are drawn. It does not mattef )~ Jj which _directions lines go in. Jus~ remember that a l_in~ means that all point_f along 1t are at the same potential. For example, 1t 1s common to draw ~i{~~ voltage divider as shown in Fig. 3.5. Trus way of looking at it is in fact ru{\~ .){W easier way to think about an "input" voltage and an "output" voltage.

\ }:~ ;:[/l~ <:;::::t )@~ [ii :.:-:-:~ : :-:.:. .; -: ::::::::~!

., ::::::;:: .·.·.·--., ·-:-:-:•:• :-:.:-:•:~ ::::::::~ FIGURE 3.4 The basic voltage divider. ~:):~~ '· · . .· ·. .· -. . . . .- ... ,.

.: ;:::::: -:-:-:•:• :1 Vout }Ill )iii!!

FlGURB 3.5 An alternate way to draw a voltage divider. :-:-:-:• :1 .::::::~; ·.·.-.....

i(~i~ t:§fi{ ~-:-:-:.

:::::::::=: 3.1 Elements of Circuit Theory 93 ~?} \ii:::=:·· :i-fah·.2.

Capacitors and AC Circuits ;:~~{}: ~-{A·.~apacitor stores charge, but does not allow the charge carriers (i.e., ffieatrons) to pass through it. It is simplest to visualize a capacitor as a JP',I'.·t.·\.·p.·.·~ of conducting plates, parallel to each other and separated only by a tf~mall amount. If a capacitor has a potential difference V across its leads ~}!ithd bas stored a charge q on either side, then we define the capacitance Jft.:-: a q / V. It is easy to show that for a parallel plate capacitor, C is a ·. .~ jfonstant value independent of the voltage. In general. it is possible, but not ~{i.asy, co calculate C from the geometry of the conducting surfaces. The SI zffa:fujt of capacitance is CouJombsNolts, also known as the Farad (F). As it ~/.,.~·-·.

· i::;tQtns out, one Farad is an enormous capacitance, and laboratory capaci- ~tJ~}'.S-typically have values between a few rnicrofarads (µF) down to a few ?:titlndred m.icrontlcrofarads (µ.µ.F). 1 Jifl{ It is pretty easy to figure out what the effective capacitance is if capacitors JJ.f~e connecled in series and in parallel, just using the above definitions and ..

:-:··· -:xfJhe rule about the total voltage drop. The answers are I!!

= ~ + ~' Capacitors in series jl}~d ~:::=::::· f/ ·= C = C1 + C2 Capacitors in parallel, ·~:;::::=:=~·.

~f(~'.at is, just the opposite from resistors.

-:f-If' .(..:. ... tun' lf the voltage chang~ with time, we refer to tbe system as an AC circuiL il\¥, the voltage is constant, we call it a DC circuit Now go back to the i-:\~:fl~ltage divider with a capacitor, pictured in Fig. 3.6, and let the input J}J-!\-:i_:- --- .· ·:~)i:,. 1 = 11111F I pF (picofarad).

I':,':::/ ~tv ~ti t ::: ~/.

·:})

?~~i~~~ 94 3 Electronics and Data Acquisition .·.·.·.·. .· Ji/!

·::::::::~ .-:,:-:-:•J ;jf@ :--J:-I:-:-\;.. : ·.·.·.·.·. .

.. ::::::::: .-::::::::.

. ,<:::::::: ::::::::::: .·.·.·.·•· .·.·.·.·•· ··\(~;f;~ FIGURE 3.6 A voltage divider with a capacitor in it.

voltage change with time in a very simple way. That is~t ake . ;~::~~= Vin(t) 0 fort < 0 (3.2)))

•"·%• == V fort> 0 (3 3~:jj .. i-.:::~~ ·.·.·,J and assume that there is no charge q on the capacitor at t

## 0. Then

for,!'?.'.~""./ = ,·.·-·J t > 0, the charge q(t) produces a voltage drop V u1 (t) q(t)/C across\\ the capacitor. The current I (t) = dq /dt through the divider string also.{:~ gives a voltage drop IR across the resistor, and the sum of the two voltage}} drops 1nust equal V. In other words .\ } ·.·.·."' dq dVout }} V = Vout +IR :::: Vout + R-d = Vout + RC-- (3.4){~ t dt .·.-.·.

:~:~; = '.

and Vout (0) 0. This differential equation has a simple solution. It is ······ You1(t) V[l - e-t/RC). (3.S)ii ·-:-:-: is{]

Now it should be clear what is going on. As soon as the input voltage switched on, current flows through the resistor and the charge carriers pile/ )

up on the input side of the capacitor. There is induced charge on the output:} side of the capacitor, and that is what completes the circuit to ground.)

However, as the capacitor charges up, it gets harder and harder to pu(\ more charge on i~ and as t -:), oo, the current does not flow anymore and{ Vout -> V. This is just the DC case, where this circuit is not interesting-:_!;_:::!

anymore.

,Y.-::::: : ~r: .::::::: 3.1 Elements of Circuit Theory 95 ·.·.·.·.•.

·.·••.·.· ;.mr ~// 'fhe value RC is called the "capacitive time constant." and it is the only Jfihne scale we b.ave in this circuit. That is, statements like "t --+ O" and << >> 11;{f(-+ oo" actually mean "t RC" and "t RC." The behavior of the -Jcitcuit will always depend on the time as measured in units of RC. So now /l"w.e are to see what is interesting about capacitors_ They sensitive currents -ftbat are changing with time in a way that is quite different from resistors.

:Jf:p.atis a very useful property that we wilJ study some more, and use in lots ::i.f&f experiments_ ~ ~[{/ The time dependence of any function can always be expressed in terms of {fiif~e and cosine functions using a Fourier transfonn_ It is therefore common ?::~j~ work with sinusoidally varying functions for voltage and so forth, just ~-t.....i...J.. ,·. ~ ·.·: i zing that we can add them up with the right coefficients to get whatever ::lf~e dependence we want in the end. It is very convenient to use the i-fftomplex number notation ~mJJ~~lll::: : = 1 V (t) Voiw (3_6)

if¥~~ time--varying (i.e., AC) voltages, where it is understood that the voltage Uf½1e measure in the laboratory is just _the real part of this _function. The ;:::t;l{:8::?Sular frequency w = 2.nv, where v 1s the frequency, that 1.S, the number i(fofoscillations per second. This expression for V (t) is easy to differentiate ~):iliJd integrate when solving equations. It is also a neat way ofk eeping track ~[}~Jall the pbase changes signals undergo when they pass through capacitors ~\)µid other "reactive" components_Y ou will see and appreciate this better /}i~ we go along.

~If Now is a convenient time to define impedance. This is just a general ~f:f \zation of resistance for AC circuits_ Impedance, usually denoted by Z, is ~------.·.

includ¢//i}i We can easily generalize our concept of the voltage divider to AC circuits and reactive (i.e., frequency dependent) components lik~·\ j ~ capacitors. We will learn about another reactive component, the induc-?J f this{Jfj tor, shortly. The generalized voltage divider is shown in Fig. 3.7. In ::t case we have \ , ' = Z2 = i~ Vout(W, t) Vin(W, t)--- Vin(W, t)ge , (3.8).;::::::,~ Z 1 Z2 :::::::1: .·.·.·.·-~ where w~ have expressed the itnpedance ratio Z1/(Z1 Z2), a complex}}~ number, 111 terms of two real numbers g and (/J. We refer to g I Yout I/ I½ n I \Ij~ V;.

.<·:·'.·* ;:::::::=: ·.·.·.·-~ ;:;:~::: :::::).: }Ji ·.·.~~J' ·.-.........

.< <~> -:-:-;..,.

,:.:,:~:: ':;:::.:-:: :-;::::~~ FIGURE 3. 7 The generalized voltage divider.

· ~}1i JJ q,.tt ~-:-:-:• ?.:::::-. 3.1 Elements of Circuit Theory 97 -t} J~ the "gain" of the circuit, and ef> is the phase shift of the output signal f=teiative to the input signal. For the simple resistive voltage divider shown :}Jn = + = Figs. 3.4 and 3.5, we have g R1 /(R1 R2) and <I> 0. That is, J-; . . J - e output signal is in phase with the input signal, and the amplitude is ,_iJu!it reduced by the relative resistor values. Th.is holds at au frequencies • ..., I di DC '.::)llC U ng .

.r :=:,: ·The relative phase is an important quantity, so let's take a moment to . .

'/.·.··· Jlook at it a little more pbysicaUy. lf we write Vin Voe'rot, then according ·f=ij-Eq. = (3.8) we can write Vout g Voefo,r+I/>. Since the measured voltage is J\jjtist the real pru1 of these complex expressions. we have ?~:~:::.' ~:=:;:: ViD Vo cos(wt)

~ft = + Yout g Vo cos(wt ¢)

"~······ )::;::::,: ?'.nJesc functions are plotted together in Pig. 3.8. The output voltage crests :i:t):r a ti.me different than the input voltage, and this time is proportional to i[:«ie phase. To be exact, relative to the tune at whicb Via is a maximum, J:~::::::: ~ i· ;~·...-.-.. T" f . '-' = - - ~ T = - - ~ , --~~:::;;:-· ame o maximum v out If' x If' ;,{:::~:=:- 2,r Cl)

~jf ~bere T 2,r/ w is the period of the driving voltage.

~~l\1il- ~~:::.t:-;>,: ~~If: O.B 0.6 ~~~~t\: r~itr 0.4 - QI 0.2 if{ 0 .---+--t----;--,,-----+----1---1---1 > -0.2 0.:::::. .

~lilt.

-0.4 1 -0.6 -0.8 .J~:;::.

~tilt· 0 10 20 30 40 50 60 70 eo nme ..z ...

~( AGURE 3.8 Input and output voltages for lhe generalized voltBge divider.

~---.·.· -X/ ~::::·· .·,:-:-:.-: ::::::;~ -:-:•:•:• ::;:::;;: 9B 3 -Electronics and Data Acquisition <<·>:-: ·?::::~ ··..··..-·: ..

..

:::::::~ Now consider the voltage divider in Fig. 3.6. Using Eq. (3.8) we find ..:::::::=~ :::::::~ :-::~~==:::: 1 . , · ', . · ·. .· ·. . · ·. • · · >::::::;:: iwC 1 ,::~::::::: = + __!_ = + .·.·.·.·. .· Vout Vin R Vinl iwRC .. :,::;::::!

:-:-:-:. .: '-:-:-:-:- iwC :)/~;3 ·.·.•.•4 The gain g of this voltage divider is just (1 + w 2 R 2 C 2 )- 1 l 2 and you call:}@ see that for w 0 (i.e., DC operation) the gain is unity. For very larg{}j 0)/~ frequencies,. th~ugh, the_ gain goes to 0. The gain change~ from ~ity to \t~ for frequencies m the neighborhood of 1/ RC. We have said all this before, _}@ but in a less general language. . .

However, our new language tells us something new and unportant.:(i about Vout, namely the phase relative to \'in, Any complex number z c~/J J be written as ·::::::;:~ ··::;J/i!

and z* lzle-iip, (3. 9):-:-:-1,,• .\}~ ·-:-: ...

where ~ _))!/]~ tan-1[I m(z)]

<P (3.10))}~ Re(z) tJ is called the ~\)base" of z. Therefore. we find that )]

·:::::~~= \J 1 _ 1 - iwRC _ I eif/J 1 + iwRC - l + w2 R2C2 - (1 + w2 R2C2 ) 1 / 2 \ { In other words, the output voltage is phase shifted relative to the input/]

= - 1 = voltage by an amount ef> tan- (wRC). For w 0 there is no phase}} )j shift, as you should expect, but at very high frequencies the phase is shifted JI by - 90°.

:,:-:.-; :::::::: ........

3.1.3. Inductors .·.-....

..· · . . · ·. . · •. • . ))

Just as a capacitor stores energy in an electric field, an inductor stores/ J energy in a magnetic field. An inductor is essentially a wire wound into(]~~ the shape of a solenoid. The symbol for an inductor is . The key is iir})

the magnetic field that is set up inside the coil, and what happens when the){ current changes. So, just as with a capacitor, inductors are important when\ :!{ the voltage and current change with time, and the response depends on the\]

{j frequency. .

:;::~~ :,:,:.- ::::; ':::::: -:-:-;, !ill ]lj 3. 1 Elements of Ci re u it Theory 99 =11111\The of ac ircuit is to be inductance L element defined ½I:-I:-:>-:-:- N¢ L - I- , lf Where N is the number of turns in the solenoid and <t> is the magnetic flux {Jn.

the solenoid generated by the current I. The SI unit of inductance is the J/fe~la · m /Ampere, or the Henry (H).

/(\.Now if the current I through the inductor coil is changing, then the \ {.~gnetic flux is changing and this sets up a voltage in the coil that opposes J }rhe:cb.ange in the currenL The magnitude of this voltage drop is ..?::?/:.

~{ff\ = = V d(N4>) L di.

~.){{\ dt dt ~f jf = we w_rite V I Z: where Z is the impedance of the inductor, and fi.:~}l:.= loercut, then V = uuLI or Jit •:•:-:-:-··· Z iwL. (3.11)

xf::J,/;e can use this impedance to calculate, for example, Vout for the gener ~~~f#lhed voltage divider of Fig. 3.7 if one or more of the components is an {}~ductor.

"\}\ ·· You can now see that the inductor is, to a large extent, the opposite of }\r(capacitor. The inductor behaves as a short (that is, just the wire it is) at ~{Jo.w frequencies, whereas a capacitor is open in the DC limit. On the other =( )rand, an inductor behaves as if the wire were cut (an open circuit) at high }}ftequencies. but the capacitor is a short in this lim.it.

t{/ One particularly interesting combination is the series LC R circuit, com {}b.ining one of each in series. The impedance of such a string displays the ~}{phenomenon of ''resonance." That is, in complete analogy with mechanical )\resonance, the voltage drop across one of the elements is a maximwn for =-=f )a certain value of w. Also, as the frequency passes through this value, the ) f }elative phase of the output voltages passes through 90°. If the resistance :,/{\~· is very small, then the output voltage can be enormous, in principle.

.- :•:-:-:-:, ~- ~=-:-:·.· ..: :::::::: . · .:%:::::-· ..· f= ~~1.4. Diodes and Transistors :•':".;.i~'".I:":."::. : ,z._·-·.·.· .

· t)ksistors, capacitors, and inductors are "linear" devices. That is, we write f {Y I Z, where Z is some (complex) number, which may be a function \ (~ffrequency. The point is, though, that if you increase V by some factor, ~~::::::- ·-·.·-·.·.

~=~:~:::: ::~::::: ":..:: ::: ,.·.· :if·: :,-;::::: .·.·.·.-J ·.·.·.·.,...J .;::::::::: ·.·.·.·.·.1 :::::::::;: 100 3 Electronics and Data Acquisition ::::::::::: .}}~ .·.-...- ., .-:.:-:-~ then you increase I by the same factor. Diodes and trc:l.Ilsistors are exam-/ \\ }jg ples of "nonlinear" devices. Instead of talking about some impedance Z~ ----~ we instead consider the relationship between V and I as some nonlinear\ }~~ function. What is more, a transistor is an "active" device, unlike resistors}\]

transistor)Jll capacitors, inductors, and diodes, which are "passive." That is, a takes in power from some voltage or current source, and gives an output:{J to that c01nbines that input power with the signal input get a response: It/){ many tubes}l1 used to be that of these functions were possible with vacuum of various kinds. These have been almost completely replaced by solid·,</!]

state devices based on semiconductors. The physics of semiconductors and\:::?~ .)}j semiconductor devices was discussed in Sections 2.1 and 2.4.

The symbol for a diode is ...i where the arrow shows the nominal direc?}~.~..

.·.·:.- tion of current flow. An ideal diode conducts in one direction only. Toa()~~ is, its V -I curve would give zero current / for V < 0 and infinite I fo1/i]~ V > 0. (Of course, in practice, the current I is limited by some resistot\J } in series with the diode.) This is shown in Fig. 3.9a. A real diode, how?\~j ever, has a more complicated curve, as shown in Fig. 3.9b. The current{}!

/ changes approximately exponentially with Vt and becomes very largt(}@ for voltages above some forward voltage drop Vp. For most cases, a goocf J~ ........... ., approximation is that the current is zero for V < Vp and unlimited for/ }~ V > Vp. Typical values of Vp are between 0.5 and 0.8 V. \ / ~~ Diodes are pn junctions. These are the simp]est solid-state devices~m ade{}Jj fill.}]]

of a semiconductor, usually silicon. The electrons in a semiconductor :}.@ --an~1e.cgyi.1Y&i~h·:n·uLn'lfm.allv...9~tJllOY.e. thIOllidi,tbe bulk materi~ s_o I ~ I .l '::?

:..

V=O V V FIGURE 3.9 CWTent / versus voltage V for (a) the ideal diode and (b) a real diode.

.. ..

- - - .- .. ·.·.

\( 3.1 Elements of Circuit Theory 101 ~t\ .r:•:-:- /)¢nergy ban<L which is normally empty. then they can conduct electricity.

\)nus can happen if, for example, electrons are thermally excited across the ~{f ~~ergy gap between the bands. For silicon, the band gap is 1.1 eV , but the =·{/ mean thermal energy of electrons at room temperature is '"'"'k T 1/ 40 e V.

/):;rherefore, silicon is essentially an insulator under normal conditions, and )}ti:ot particularly useful.

})\ . That is where the p and n come in. By adding a small amount (around .. \/10 parts per million) of specific- impurities, lots of current '"carriers can f(b~- added to the material. These impurities (called dopants) can precisely ·}(~ontrol how current is carried in the semiconductor. Some dopants, like \/iatsenic, give electrons as carriers, and the doped semiconductor is called )j~type, since the carriers are negative. Other dopants, like boron, bind :-::f\ it, extra electrons, and current is carried by "boles" created in the other ~:/\ yise filled band. These holes act like positive charge carriers, so we call ?/Uie semiconductor p-type. In either case, the conductivity increases by a rfiactor of r.JIOOO at room temperature, and this makes some nifty things }possible. .

~t<:.

So now back to the diode, or pn junction. This is a piece of silicon, (/~oped p¥type on one side and n-type on the other. Electrons can only flow ;})from p to n. That is, a current is carried only in one direction. A detailed ~{/analysis gives the 1-V curve shown in Fig. 3.9b. See Dunlap (1988~ full { ( ¢iting in Section 3.10) for more details. If you put voltage across the diode {)rt the direction opposite to the direction of possible current flow, that is }\called a ureverse bias." A small "leakage" current flows as shown in Fig.

}{$.9b. If you put too much of a reverse bias on the diode, i.e., V < - V J ;fu, 0 v;w ((it will break down and start to conduct. Typical values of are 100 V ~/}~r less.

if\ if Transistors are considerably more complicated than diodes, 2 and we will (9R1Y scratch the surface here. The following summary closely follows the %}/introduction to transistors in The Art o:f Electronics (full citing in Section ~f \~~ 10). For details on the underlying theory, see Dunlap ( 1988). A transis if ) or has .three terminals,_ called the collector, base, and emi~er. There are j f)YvO mam types of transistors, namely npn and pnp, and therr symbols are Wf)~own i.n Fig. 3.~0-1:he name~ ai:e based on ~e dopants used in th~ se~ ittonductor matenals. fhe properties of a transistor may be surnmanzed m mt{/ ·.-.·.•, :?::;-:-.- ___ }}: · lThe invention of the transistor was worth a Nobel Prize in Physics in 1956.

·4·.·.

t>: •:.-:•:-:-: .~~:::::: :~:::::-.

,·.·.·.· ;f/ :of/: ·.·.·-::% -:;::::::~ .;:;:::l~ 102 3 Electronics and Data Acquisition :/1~ -:::::::::-:: .ij//l~ Collector C :;:::::::~ 111: Base B -::::::::j::: JIii -:-:-:-::,~ ' { j ~ ._;JJ~ Emitter E ,:;:::::. .' l, npn pnp ::::::::~t ·.·.·.·,),t,...-...

}}i~ FIGURE 3.10 Symbols for npn and pnp transistors. ))~ just!/::m the following simple rules .for npn transistors. (For pnp transistors, reverse all the polarities.) \ }\~ \ :;:;:~~

## 1. The collector must be more positive than the emitter. :\\~

-:-:-:-:·~

## 2. The base- emitter and base-collector circuits behave like diodes

·:-:-:-~~ Nonnally the base-emitter diode is conducting and the · _ > ;:: : : : :: : : : ~ 'l~' -~ ··;::J~ base-collector diode is reverse-biased. ·,·.-,;:.. ...

.: :::=~~~~

## 3. Any given transistor has maximum values of le, 1B, and VcE i_t_~r..~

·:.t.:-:.. !.· .;_ _ that cannot be exceeded without ruining the transistor. If you are .....

{/~j using a transistor in the design of some circuit, check the specifications to see what these limiting values are. · .::;:::~:j .-.·:-:-:-.9.

## 4. When rules 1-3 are obeyed, le is roughly proportional to 1 and -:-:::::::~

can be written as / c = h FE I B. The parameter h FE, also called \ {}~ )}Ji {J, is typically around 100, but it varies a lot among a sample of ··\Jt nominally identical transistors.

/;:::~ Obviously, rule 4 is what gives a transistor its punch. It means that a._:}j~ ·-~ transistor can "amplify" some input signal. It can also do a lot of other·}{~ ·.·.·.---..

things, and we will see them in action later on. -}}~ ·::::::::~ -:,:-:-:•::~ .}fl 3.1.5. Frequency Filters /}Ji Simple combinations of passive elements can be used to remove "noise":/J J from a voltage signal. If the noise that is bothering you is in some specific.)i ~ range of frequencies, and you can make your measurement in some other\ J j range, then a frequency filter can do a lot for you. Frequency filters are:\Jt usually simple circuits (or perhaps their mechanical analogs) that allow\ j ~ then)i@~ only a specific frequency range to pass from the input to the output. You :){iij :~ ..........= -: ·: m::::: ~t( .. 3.1 Elements of Circuit Theory 103 J ll\ make your measurement with the output. Of course, you need to be careful ~f {of any noise introduced by the filter itself. The circuit shown in Fig. 3.6 is ~{\ a '1ow-pass)t filter. It exploits the frequency dependence of the capacitor ~\/ impedance Zc = 1/ iwC to short frequencies much larger than 1/ RC to [t/ ground, and to allow much smaller frequencies to pass. As we showed ~rf earlier, the ratio of the output to input voltage as a function of frequency ~?\ v = w/2x is (1 +w2 R2C2 )- 112 . You can also use inductors in these simple ~f \ circuits. Remember that whereas a capacitor is open at low,frequencies ~{ \ ai:id a short at high frequenci~s, an ind~ctor behave~ just the. opposite.

~{ ( Figure 3 .11 shows all permutations of resistors, capacitors, and rnductors, ~\ ) and whether they are high- or low-pas~ filters. . . _ fk< Suppose you only want to deal with frequencies m a specific range.

i { /Then, you want a "bandpass" filter, which cuts off at both low and high ~f {~equencies, but l~ts ~ome intermediate bandwidth P_'!SS through. Consider ~} \ the circuit shown 1n Fig. 3.12. The output voltage tap is connected to ground [::::::· ~ z::- ~:-:-:-.

r~:~.;::::::- ___ C_ircu_i_t ____Ty p_e ___ Circuit Type ~f:- T ~--::::- ?t::: : ~ /"«/'._ -- ;. : . - ··. : .· · ·.. . ·· · · . Low pass High pass :~?:/ :u--=·.·.· rrnt .:f-.·.·.

ij:?i Low pass Hl9h pass ~?> f ::::: .

v.:::::: ~ -:-:- ~=:::: Low pass High pass ~ :-:-:- !=> FlGURE3.ll Simple passive frequency filters.

[ .·.·.· ~:}· ::::::·-·.· ?:f::::.

~=::- ~:;:::;: &f:>: ~~:.::<:::-:. ::.

1~/ i =:f:.: ~l C L ::=:::.

...~ :::· ..· .:::-.

·:-:-: ;~:=:·: .- .·.·. RGURE 3.12 A simple bandpass file.er .

J':·> ~'.:'.- _,.:;-:-: )}j ... : - { :-:- : :- @ :. . : , 104 3 Electronics and 'Data Acquisition · ;:;:;:;:;;: .\(J through either a capacitor or an inductor. Therefore, the output will be zero at both low and high frequencies. Analyzing this filter circuit is simple · {j .· .·.·~·J })J -Vout = -- Z - ic - , ·::::::::; ))1 ½n ZR+ ZLc · where ZR R and ZLc = (zz1 + Zc 1 )- with ZL 1/iwL and·..

\i]

:;, 3.2. BASIC ELECTRONIC EQUIPMENT ·.·.-.-~ :~::::::: ·-::::::~ :::::~=~ 3.2.1. Wire and Cable .::::::=~ =::~:=:=:=:=~~ Connections between components are made with wires. We tend to neglect / ( the importance of choosing the right wire for the job, but in some cases /)~ it can make a big difference. The simplest wire is just a strand of some })

conductor, most often a metal such as copper or aluminum. Usually the wire ) } {J is coated with an insulator so that it will not short out to its surroundings, or to another part of the wire itself. If the wire is supposed to carry some {} {t small signal, then it will likely need to be ''shielded," that is, covered with another conductor (outside the insulator) so that the external environment \{ :!{~ does not add noise somehow. One popular type of shielded wire is the.

"coaxial cable," which is also used to propagate ''pulses." \ } Do not forget about Ohm's law when choosing the proper wire. That. )} = ./ii is, the voluige drop across a section of wire is still V IR, and )ii you want this voltage drop to be small compared to the "rear' voltages · involved. The resistance R p x L / A, where L is the length of the./\ .\!

wire, A is its cross-sectional area, and p is the resistivity of the metal.

Therefore, to get the smallest possible R, you keep the length Las short }\ j!

:-:• it=:- ~!{ 3. 2 8 e sic Electronic Equipment 105 ~::::: ~~ ::::. ~~:::e :O!::c!~~· ;~~ ~o~;;~~ ::c~~1Ad;o~:i Ji.!: :~~ti::. ait~: 1 t: low resistivity (p = 1.69 x I o -8 0-cm) and is easy co fonn into wire ~\} of various thicknesses aod shapes. Other common choices are aluminum if (p 2.75 x 10-8 n-cm), which can be significantly cheaper in large ~ ( quantities, or silver (p 1.62 x 10- 8 n-~m), which is a slightly better [ ) conductor,_a ~~ou~h not usua~ly worth the mcreased_expense~ _ rrt== The res1sbV1ty 10creases with temperarure, and tb1s can leaa to a partic ~ } ularly insidious failure if the wire must carry a large current. The power ~l- dissipated in the wire is P = 12 R, and this tends to heat it up. If there is ijfa.

not enough cooling by convection or other means, then R will increase and ~( cthoem w.miroeo w ill get hotter antod holler until it does serious damage. Th.is is most ~l!

{-·:::::. Fig. 3. L3. CoaxjaJ cable is used in place of simple wire when the signals are i~--f-·:. : very small and are ~ely to be obscured by some ~ort of electr~nj~ noise ~:::;"· in the room. The outside conductor (called the "shield") makes 1t difficult ~){ for external electromagnetic fields to penetrate to the wire, aod minimizes [I{ the noise. This outside conductor is usually connected to ground.

~f: A second, and very important, use of coaxial cable is for "pulse traus ~f: mission." The wire and shield, separated by the dielectric insulator, act as Jt a waveguide and allow short pulses of current to be transmitted with little rt distortion from dispersion. Short pulses can be very common in the labo [ \ ratory, in such applications as digital signal transmission and in radiation t\i detectors. You must be aware of the "characteristic impedance" of the cable [ \. when you use it in th.is way.

i~:f:/ Coaxial cable bas a characteristic impedance because it transmits the .signal as a tra.io of electric and magnetic flucruations, and the cable itself has ijf • characteristic capacitance and inductance. The capacitance and inductance if of a cylindrical geometry like this are typically solved in elementary physics ~ :: ~;-:?

r~.~~:-:-;·: ~ { 3 Wire diameter is usul!lly specified by the "gage number," The smaller lbe wire gage, &r the thicker che wire, and the larger the cross-sectional area.

~t [ f ~ :-:, Ill: ·::::/½ .·,:,:-:-:* ::::::::~~ ·:::::::::~ 106 3 Electronics and Data Acquisition :\ }:~ ::::::::~~ . iii ··::::::J~ ,·.·.·.-~ FIGURE 3.13 Cutaway view of coaxial cable.

texts on electricity and magnetism. The solutions are ln~;a)

= = ~ C X i and L 111 (:) x £, where a and b are the radii of the wire and shield respectively, € and µ are\ /{]

:/Jj the permittivity and permeability of the dielectric, and l is the length of the cable. Itis very interesting to derive and solve the equations thatdetennine)J~ p~e propagation in a co~al cable: but we will not do that here. ~ne;}J?J which:\/]

thing you learn, however, 1s that the unpedance seen by the pulse ( /Jl is dominated by high frequencies) is very nearly real and independent of frequency, and equal to }]~ b) . . ·.·.·.-.::,,,...: :::}'.~:~ Zc = {L = 2_ {ii ln ( (3 12)

Ve 2](v-; . \',',}',?'U3.~L ·:.·.·"% :::::::::;~ /If.: This ''characteristic impedance' is always in a limited range, typically ...• 1/.

50 ~ Zc < 200 n, owing to nanu-al values of E and µ,, and to the slow }}{ {Jl variation of the logarithm.

You must be careful when making connections with coaxial cable, so }(j )\t that the characteristic impedance Zc of the cable is "matched" to the ·tti load impedance Z L. The transmission equations are used to show that r, {/i the "reflection coefficient" defined as the ratio of the current reflected ·(J~ from the end of the cable to the current incident on the encL is given by · z z :·\.·.·t.·~.:,, = )\t f L - c.

ZL Zc <.:/.f.:..~..

. <::~:;; )JJ.

That is~ if a pulse is transmitted along a cable and the end of the cable is not = r = connected to anything (ZL oo), then 1 and the pulse is immediately<::@~ reflected back. On the other hand, if the end shorts the conductor to the )j ~ = r = ..· .. :.i:•:• shield (Zi 0), then -1 and the pulse is inverted and then sent.\;::;~ .·.·.·r ..• back. The ideal case is when the load has the same impedance as the cable. :}f In this case, there is no loss at the end of the cable and the full signal )j~ is transmitted through. You should take care in the lab to use cable and/ !@ \J .·.-........

## 3.2 Basic Electronic Equipment

~f)

~r --.·.· \,lectronics that have matched impedances. Common impedance standards t/ are 50 and 90 Q.

·{( Of course, you will need to connect your wire to the apparatus somehow, t{/ and this is done in a wide variety of ways. For permanent connections, ...} / especially inside electronic devices, solder is usually the preferred solution.

?/)t is harder than you might think to make a good solder joint, and if you ) / are going to do some of this, you should have someone show you who [ \.has a decent amount of experience. Another type of permanent:.connection, }} called "crimping," squeezes the conductors together using a special tool ~\r)e. th at ensures a good contact that does not release. This is particularly useful ,if you cannot apply the type of heat necessary to make a good solder :=f::;:;: joinL .. / \ Less permanent connections can be made us.mg terminal screws or bind ~{{ ing posts. These work by ta.king a piece of wire and inserting it between two ~f} surfaces that are then forced together by tightening a screw. You may need ( (-to twist the end of the wire into a hook or loop to do this best, or you may i/ use wire with some sort of attachment that has been so]dered or crimped ~f.

on the end. If you keep tightening or untightening screws, especially onto ·(\ wires with handmade hooks or loops, then the wire is likely to break at tr some point. Therefore, for temporary connections, it is best to use alliga t : tor clips or banana plugs, or something similar. Again, you will usually t ( use wires with thls kind of connector previously soldered or crimped on tr the end.

i~_~l-~: Coaxial cable connections are made with one of several special types of ~:=:> connectors. Probably most common is the "bayonet N-connector," or BNC, f / standard, including male cable end connectors, female device connectors, f?

and union and T-connectors for joining cables. In this system, a pin is ~'\: r=::: soldered or crimped to the inner conductor of the cable, and the shield is f ( connected to an outer metal holder. Connections are made by twisting the ~{: holder over the mating connector, with the pin inserting itself on the inner [ \ part. Another common connector standard, called "safe high voltage" or t?· i}· S HV, works sintilarly to BNC, but is designed for use with high DC voltages by making it difficult to contact the central pin unless you attach it to the ~V.:?-:•:: correc ma e.

~f} For low-level measurement you must be aware of the thermal elec t::-.

wt tric potential difference between two dissimilar conductors at different temperatures. These "thermoelectric coefficients" are typically around i~~j~.{':.: · 1 µ V /°C, but between copper and copper-oxide (which can easily happen if: if a wire or terminal is oxidized) it is around 1 m V /°C.

~---·.

I••···· -~:::.

·~=::.

:•"~4:· .-~- .......

·.:..:.:.

·.·. ·.·.--· ·.·.·.·.4.J ::::::::;; ·.-::::::~;: 108 3 Electronics and Data Acquisition · \ }:~ ::::::::;: ·.·.-... _.

::::::::: ·.·.·.-.- 3.2.2. DC Power Suppli~ .· :/} . ,•:-:-:.-:, '.·.·.•.,.• ':::::::;: )if Laboratory equipment needs to be "powered" in one way or another. Unlike the typical 1O OMV , 60-Hz AC line you get out of the wall socket, though, ·this ) )~ equipment usually requires some constant DC level to operate. One way } ]

to provide this constant DC level is to use a battery, but if the equipment ·-:-:-:-: draws much current the battery will quickly run down. Instead we use DC :( } /J "power supplies", the power supply in turn gets its power from the wall :-:::?:-::~~ socket. · · .·}.-.?"~.J Power supplies come in lots of shapes, sizes, and varieties, but there '}Ji~ are two general classes. These are '~oltage" supplies or "'currenf' supplies, )J§ and the difference is based on how the output is regulated. Since the inner workings of the power supply have some effective resistance, when the _:{@ }{@ power supply must give some current, there will be a voltage drop across that internal resistance, which will affect how the power supply works. In (~§. )Ji a '"Voltage-regulated" supply~ the circuitry is designed to keep the output voltage constant (to within some tolerance), regardless of how much current :/~;j '·.·.-::·.1 is drawn. (Typically, there will pe some maximum current at which the !\~~ regulation starts to fail. That is, there is a maximum power that can be ))1 \J~ supplied.) Most electronic devices and detector systems prefer to have )jJ a specific voltage they can count o~ so they are usually connected to voltage-regulated supplies. }j A ~'current-regulated" supply is completely analogous, but here the cir- }]

cuitry is designed to give a constant output current in the face of some ( / {j load on the supply. Such supplies are most often used to power magnets, since the magnetic field only cares about how much current flows through })

the coils. This is in fact quite important for establishing precise magnetic )} fields, since the coils tend to get hot and change their resistance. In this {{ case, V == IR and R is changing with time, so the power supply must \} know to keep/ constant by varying V accordingly. In many cases, a sim- ))

}J ple modification (usually done without opening up the box) can convert a power supply from voltage regulation to current regulation. \ ~ \J The output terminals on most power supplies are "floating.,, That is, they are not tied to any external potential, in particular not to ground. One output . )J \J (sometimes colored in red) is positive with respect to the other (black). You will usually connect one of the outputs to some external point at known } potential~ like a common ground. )/ You should be aware of some numbers. The size and price of a power :\ supply depends largely on how much power it can supply. If it provides a )( ~::::: /: .!!!

·,:.

I;;:

## 3.2 Basic Electronic Equipment

1!!!!\,oltage V while sourcing a current/, then the power output is P = JV.

~f/ A very common supply you will find aro~nd ~he lab will put out sev~ral ft/ volts and a coup]e of amperes, so something like IO W or so. Depending ~f ::tm things like control knobs and settings to computer interfacing, they can ~}.{).mst anywhere from $50 up to a few hundred. So-called ''high-voltage"

if ( Power supplies will give several h~ndred up to several thousand volts, and if {¢an source anywhere from a few microamperes up to l 00 mA, -:.and keep the iffyoltage con~tant ~o a level of better ~an 100 _mV. Still, the power output ~f/9f such devices 1s not enormously high, typically under a few hundred (f/watts. run The cost will into thousands of dollars. Magnet power supplies, [f }though, may be asked to run something like 50 A through a coil that has a n.

[{\ resistance of, say, 2 In this case, the output power is 5 kW.

[rt:· !~?}:::f:::. .

~.2.3. Waveform ~nerators ij::f\: [~L/ ~aveform generators" produce an output voltage signal V (t) that varies if):O..tiroe. The function V(t) can be anything from a simple sine wave to an ~f()irbitrary function you program into the device, but increased flexibility can ~~f \~pst a lot of money. Most waveform generators, though, do have at least [ =?i))ne waves. square waves, or triangle waves, and can vary the frequency ~j}gyer a wi_de range. Low frequencies are pr~tty easy to get, but for very high ~\\Jrequenc1es (above a megahertz or so) things get much harder because of ~/\#ray capacitance giving effective shorts. You can also vary the amplitude ~~f\?.J1d offse~ of t~e output voltage over several volts. .

~f)) . Sometu~es. instead of a "wave" ?utput,_ one n~eds a "puls~"-that 1~, a !f~r JJgnal that lS high for some short penod of time, Wlth the next stgnaJ commg ij~\/after a much longer time. Most waveform generators can accomodate your ~f /)vishes either by providing .an explicit "pulse" output, or by allowing you ff/Jo change_ the symmetry of the wavefo ~ so that the "O to :re,, po~on of i~I)!he wave JS stretched or compressed relative to the "rr to 2rr" port.100.

~:::-:,:,:.·.

!l:3::f· .r.· .·.

{.3~2.4. Meters ~:::::::::: ..

~~{~ow that you know trow to obtain some voltages, including time-varying ~o~ i~\:i~~es, and how to connect these voltages usi~g wire and cable. m~st ~/~ about how to measure the voltage. The .sunplest way to do this 1s wtth ~}\~··meter, partic~~arly if the v~ltage is f?C. (Most ~eters do provide you ~}}¥th AC capabtlity, but we will not g~ mto the details here.) An excellent @/::\\.· ~::::: · ~.f?f::;.·.

meters to measure voltage, current, or resistance, respectively. These days,)/} although you still might want to buy one of these specialized instruments/ /@ to get down to very low levels, most measurements are done with .. digita(/i multi.meters," or DMMs for short. (In fact, some DMMs are available now//} that can effectively take the place of the most sensitive specialized meters.}!/]

in{i]

Voltage and resistance measurements are made by connecting the meter \J parallel to the portion of the circuit you are interested in. To measure current, the meter must be in series. } j over/@ Realize that DMMs work by averaging the voltage measurement some period of time, and then displaying the result. This means that if\)~ the voltage is fluctuating on some time scale, these fluctuations will not))~ )it be observed if the averaging time is greater than the typical period of the fluctuations. Of course the shorter the averaging time a meter has (the\@ )@ higher the "bandwidth" it has), the fancier it is and the more it costs.

Meters have some effective input impedance, so they will (at some level}:/ :~ ·:.t·.·#;'.J change the voltage you are trying to measure. For this reason, voltmeters and ohmn1eters are designed to have very large input impedances (many / { megaohms to as high as several gigaohms), while ammeters "shunt'' the ::}~ }J current through a very low resistance and tum the job into measuring the )j (perhaps very low) voltage drop across that resistor.

::;::: .::::: •:-:- 3.3. OSCILLOSCOPES AND DIGITIZERS ·:::: .·.· 3.3.l. Oscilloscopes An oscilloscope measures and displays voltage as a function of time. That \ is, it plots for you the quantity V (t) on a cathode ray tube (CRT) screen / as it c01nes in. This is a very useful thing, and you will use oscilloscopes :i in nearly all the experiments you do. A good reference is The XYZ's of !; Oscilloscopes, published by Tektronix, Inc. You can download a copy )

scope works. The voltage you want to measure serves two purposes. First, ..; after being amplified, it is applied to the vertical deflection plates of the · .•....

-- ---

## 3.3 Oscilloscopes and Digitizers

Vertical System L:J _... ver11ca1 ~ - Ampllio< :z:;:-:-:•:··· ,---:;;;:::::. .

~~r::: Tr1gger ~;: Syslem --- Horizontal System ..._------+.i Swoop Horirontal Genera1or Amplifler /Iv /vI 41I Ramp Time Baao ~!lit ..-:-;-:.: - ~"-'··· FIGURE 3.14 Block diagram of an oscillo11eope.

irr CRT. This means thal Lhc vertical position of the trace on the CRT cor~ ~({:. responds linearly to the input volt.age, which is just what you want. The ;,;-Ji vertical scale on the CRT has a grid pattern that lets you know what the ?:}(: input voltage is.

'J.·.·.

~t) Tbe horizontal pos.ition of the trace is controlled by a "sweep generator"

1/ whose speed you can control. However, for repetiLivc signal shapes, you A\ want the signal to "start" at the same time for every sweep, and this is ,t?

determined by the "trigger'' system. The place on the screen where the ~({ trace starts is controlled by a "horizonlal position" knob on the front panel.

,if One kind of trigger is to just have the scope sweep at the line (i.e., 60 Hz)

}/ frequency, but this will not be useful 1f the signals you are interested in f f do not come at that frequency. Another kind of simple trigger is to have .f .: the trace sweep once whenever the voltage rises or falls past some level, t \i i.e., a "leacliog edge" trigger. There is usually a light on the front panel that j \ flashes when the scope is triggered.

~~f Oscilloscopes almost always have at least two input channels, and it is v.f( possible to trigger on one channel and look at the other. This can be very Ir: useful for studying coincident signals or for measuring the relative phase ~ff of two wavefonns. In any case, the trigger "mode'' can either be "nonnal,"

~:} in which case there is a swe.ep only if tbe trigger condition is met, or "auto"

~;.::::.

t?.t i[: [ft :,.:.:_ . .: .·.

_.?Jr .· , -:-:·: ..: i?t 112 3 Electronics and Data Acquisition \It/2 in\@~~ where th~ scope. will trigger itsel~ if th~ trigger condi~on is not met search-\/li some penod of trme. Auto mode is particularly useful if you are ing for some weak signal and do not want the trace to keep disappearing/:::=:@· ··.·.·.·.-~ :{t~ on you.

"coup1mg" can be set to either AC, DC, or ground. In AC mode, there 1s \t~@ a c_apacitor between the input connector an~ the vertical system circuit.

This keeps any constant DC level from entenng the scope, and all you see :}}~f .<Jm~ is the time-varying (i.e. • AC) part. If you put the scope on DC, then the ::)]~;il constant voltage level also shows up. If the input coupling is grounded, ·yJ~~ the then you force the input level to 0, and this shows you where 0 is on }@~~ screen. (Make sure that the scope is on "auto" trigger if you ground the . t th . ill t tr I) .·.·.···@ mpu; o erw1se, you w no see a ace. :::::\/: :}t~ Sometimes, you also get to choose the input impedance for each channel. · {JI§ Choosing the "high" input impedance (usually 1 MQ) is best if you want ·/]%: to measure voltage levels and not have the oscilloscope interact with the ·:)\!~1~ circuit. However, the oscilloscope will get a lot of use looking at fast pulsed )..f.. ~h •l• signals transmitted down coaxial cable, and you do not want an uimpedance \ti mismatch" to cause the signal to be reflected back. (See Section 3.2.1.)

Cables with 50-Q characteristic impedances are very common in this work, ·}}~f ))Jt so you may find a 50-Q input impedance option on the scope. If not, you should use a "tee" connector on the input to put a 50-Q load in parallel <}{{ with the input \\:~:=:= By flipping switches on the front, you can look at -either input channel's · :\\/ trace separately, or both at the same time. There is obviously a problem, :}// )jf though, with viewing both simultaneously since the vertical trace can only· .

the chopping action will be obvious. .}J( " '1/."

·:}{ : JI ~-··· ~l/

## 3.3 Oscilloscopes and Digitizers

~:::::- ~::::: f }: You should realize by now thai high-frequency operation gets bard, and }{ the oscilloscope get.s more complicated and expeosi ve. Probably the single {(most important specification for an oscilloscope is its "bandwidth," and {j you will see that number printed on the front face tight near the screen.

\\{ The number tells you the frequency at which a sine wave would appear ( only 71 % as large as it should be. You cannot rrust the scope at frequencies ( . approaching or exceeding the bandwidth. Most of the scopes in the lab have { 20- or 60-MHz bandwidths. A "fasL" oscilloscope will have a bandwidth ( of a few hundred megahertz. or more. You will find that you can vary the ::· sweep speed over a large range. but never much more than (bandwidth.)-1 • .. Toe "vertical sensitivity" can be set independently of the sweep spee<l, but :: :: scopes in general cannot go below around 2 mV/division.

On most oscilloscopes, if you turn the sweep speed down to the lowest value, one more notch puts the scope in the X Y display mode. Now, the trace displays channel one (X) on the horizontal ax.is and channel two (Y)

on the vertical. For periodic siguals. the trace is a Lissajous pattern from which you can determine the relative phase of the two inputs. Oscilloscopes are also used in this way as displays for various pieces of equipment which have X Y output options. Thus, the oscilloscope can be used as a plotting device in some cases.

3.3.2. Digitizers In order to measure a voltage and deal with the result in a computer, the voltage must be digitized. The generic device that does this is the analog-to iligital converter or ADC. ADCs come in approximately an infinite number of varieties and connect to computers in lots of different ways. We will cover the particulars when we discuss the individual experiments, but for now we wi II review some of the basics.

Probably the most important specification for an ADC is its resolution.

We specify tbe resolution in tenns of the number of binary digits ("bits")

that the ADC spreads out over its measuring range. The actual measuring range can be varied externally by some circuit, so the number of bits tells you how finely you can chop that range up. Obviously. the larger the number of bits, the closer you can get to knowing exactly what the input voltage was before it was digitized. A "low-resolution" ADC wi11 have 8 bits or less. That is, it divides the input voltage up into 256 pieces and gives the computer a number between O and 255, which represents the voltage.

A "high-resolution" ADC has 16 bits or more.

·::::::::::.r.

.( (j 114 3 Electronics and Data Acquisition . ·::::::::::.~ :: : ::::/:~!:~: li/f High resolution does uot come for ~ee. In the first _place, it can mean lot more data to handle. For example, 1f you want to histogram the voltag¢.i\ J~ ~ing measured with ~n 8-bit ADC, then you need 256 ch~els for eacij( f~ histogram. However, 1f you want to make full use of a 16-bitADC. every}(:~~ affects(\\)

histogram would have to consume 65,536 channels. Resolution also tak~~{J1 the speed a~ which a. v~~tage can be d.igitized. Generally speakin~, it much less time to digitize a voltage mto a smaller number of bits than 1~:;:::~:~ ::;:)?;j does for a large number of bits. ·.

There are three general classes of ADCs, referred to as flash, peak{!}~ voltage sensing, and charge integrating ADCs. A flash ADC, or "wave{j~ form recorder," simply reads the voltage level at its input and convert~f fj that voltage level into a number. They are typically low resolution/ f f but run very fast. Today you can easily get an 8-bit flash ADC th~)~@ digitizes at 100 _:MHz (i.e., one _measure1:1ent _every 10 ns). This is fas~/ ®~ td{jgf enough so that JUSt about any trm~varymg s1~al can be converte?

~(Ji numbers so that a true representation of the signal can be stored m ·:?:::m computer.

To get better resolution, you need to decide what it is about the signal(Jij you are really interested in. For example, if you only care about the maxi~}iff the}ff mum voltage value, you can use a peak-sensing ADC, which digitizes maxilnum voltage observed during some specified time. Sometimes, you.})~ is:}{i are interested instead in the area underneath some voltage signal. This the case, for example, in elementary particle detectors where the net charge}}]

... ·::1 delivered is a measure of the particle's energy. For applications like this,.}}~ you can use an integrating ADC, which digitizes the net charge absorbed.) )]

fr: at\}%, over some time period, i.e., (1/ R) 2 V (t) dt, where R is the resistance )?i the input. For either of these types, you can buy commercial ADCs that digitize into 12 or 13 bits in 5 µ,s or longer, but remember that faster and )}f more bits costs more money. ):}~{ ,·.·~---,,1 The opposite of an ADC is a DAC, or digital-to-analog Converter. Here/ /:} \)j the co1nputer feeds the DAC a number depending on the number of bits·, )JJ and the DAC puts out an analog voltage proportional to that number. The.

simplest DAC has just one bit, and its output is either "on" or "off." In this ....

~ ·•~ ~ case, we refer to the device as an "output register.,, These devices are a way ))t ~ IJt of controling exten1al equip1nent in an essentially computer-independent ·.·.·.t.l.

fashion. ::::::~:~ ,·,:-:-:.-:-: }J In many cases, you want to digitize a time interval instead of a voltage.

level. This can be done with a "time-to-analog converter" (TAC), followed.\ Jt by an ADC. However, both of these functions are now available packaged / j~ ·-:-:;:-,;- ::::~~== Ii.

;f\ =:::::- 3.3 OsciJloscopes and Digitizers 115 =~~:: }}~--a single device called a TDC. The rules and ranges are very simi]ar as -{:for ADCs.

Jf}· J?evices lrnow~ ~ . "latches,, or ~'input r~gister~" will take an external [ / J~gtc level, and digittze the result mto a smgle bu. These are useful for ~f } elling whether some device is on or off, or perhaps if something bas ij~:}happened that the. computer should know about.

I\/· When a device is busy digitizing, it cannot deal with mor~ input. We i ffefer to the cumulative time a device is busy as "dead time." Suppose r it(#.

the time needed to digitize an input pulse, and Ro is the (presumably W!\ tandom) rate at which puJses are delivered to the digitizer. If Rm is the ~{\ ~easured rate, then in a time T the number of digitized pulses is Rm T.

@(The dead ti~e incurred in time T is therefore (Rm T)r, so ~e number of ~~\pulses lost 1s [(RmT)r]Ro. The total number of pulses delivered (RoT)

~:~:::' fuust equal the number digitized plus the number lost, so ~:::;:'.:: ;:?-·.·.·.·.

:~?-:r:::e:: = + RoT RmT RmTrRo, :=:::=:::::and therefore ?::::::::.·- :,:·,·.·.· Ro ...: :::::.

1/.i;::: Rm =- + -- (3.13)

..

..

..

..

·.

..

·· 1 rRo -:•:-:-: ~?\ or z:::::: .·. . ·.·.·.

~~~~\; Ro= Rm (3.14)

~=~:~-. 1- rRm :,.:-:-: {\. The "normal" way to operate a digitizer is so that it can keep up with the f{ rate at which pulses come in. In other words, the rate at which it digitizes ......

f/ (1 /r) should be much greater than the rate at which pulses are delivered, << \/ that is, r Ro 1. Equation (3.13) shows that in this case, Rm ~ Ro; that f ( is, the measured rate is very close to the true rate, which is just what you fr want. Futhennore, an accurate correction to the measured rate is given by = + {/ Eq. (3.14), which can be written as Ro Rm(l r Rm) under normal {/ operation.

>> {/ On the other hand, if r Ro 1, then Rm ~ 1/r:. That is, the digitizier {\. measures a pulse and before it can catch its breat~ another pulse comes fa\ along. The device is ''always dead," and the measured rate is just one per r.·.·.

t / digitizing time unit Essentially all information on the true rate is lost, t/ because the denominator of Eq. (3.14) is close to 0. You would have to ]{.· know the value of r very precise]y in order to make a correction that gives ( : you the true rate.

:=::: ·•~:•· :• ..

..:' .-/.

.: , -· · .

•:•:-.

~:=:- ..:•:-: ~~:~· .......

·.;,;.;.:-:,;,; }j}J 116 3 Electronics and Data Acquisition \\\~~~ :):);~:?

:)\~:}~~-- 3.3.3. Digital Oscilloscopes . -:-:-:.:-:•:. ..

-::})t thf j f The digital oscilloscope is a wonderful device. Instead of taking citj;\Jf input voltage and feeding it directly onto the deflection plates of a (Fig. 3.14), a digital oscilloscope first digitizes the input signal using::tf\.

.h~)tl=; flash ADC, stores the waveform in some internal memory, and then CR'tf{ / other circuitry to read that memory and display the output on the i~fJ.

We then have the voltage stored as numbers, and the internal computer the digital oscilloscope can do just about anything with the numbers. Eve~)~~ though it works very differently from analo~ oscilloscopes, digital sc~p~*rt~ Jj have controls ~at make _them look as _much like analog sc~pes as poss1bl~f The same temunology 1s used, and Just about any function found o~ ~}~~ \)!JI analog scope will also be found on a digital one. ·· .<?::::=?!

\ttl 3.4. SIMPLE MEASUREl\lIENTS \?}:; We now outline some simple measurements of elementary circuits. Circui¼i!I are most easily put together on a "breadboard." This is a flat, multilayeretf}~ij surface with holes in which you stick the leads of wires, resistors, capaciS//J .....

]~j tors, and so on. The holes are connected internally across on the compone~~f pads, and downward on the power pads. <:::::::::]

Connect two 1-kQ resistors in series on the breadboard, and then connecf Jj ..•..., ,r, the terminals of the power supply to each end of this two-resistor string{ f~j tb~/j~~ Measure the voltage across the output of the terminals. Also, measure current through the string. Now connect two more 1-kQ resistors in serie~{/J with the others. Move the connections from the power supply so that onc~/{j again it is connected to each end of the string. Repeat your voltage and(({~ current measurements. Now measure the voltage drop across each of the((/~ four resistors. Compare the result to what you expect based on the voltag~}{J off!/~ divider relation. Use your data and Ohm's law to measure the resistance you the(?f~ each of the resistors. Compare the resistance values measure with ··:\J; nominal value.

Re1nove the DC power supply and replace it with a waveform generator(\)~ th~(Jj Set the waveform to a sine wave. Use an oscilloscope to compare voltage (as a function of time) across the resistor string from the wavefonnfJfj generator with the voltage across one of the resistors. Put each of thesef{I!

into the two channels of the oscilloscope, and trigger the scope on thef \]~~ bo~.•(. •,•!.•}.•,;t,; channel corresponding to the waveform generator output. Look at -:-:-:·,·=~ ::::::~~ /]J ·.:::::::~ . . ,-::,: -:::::~~ ..: /::~:~ \ {.

··-·.·. .

/:-:-:•.

·:::::: .. 3.4 Simple Measurements 117 ;,-::::::.

~r·=·· {\~aces simnltaneously ( on either chop or alternate) and compare the relative ½)frnplitudes of the ''input" sine wave across the string, and the "output" sine :::. . ·. .

.· ;::wave across the smgle resistor.

j f( Now connect a resistor and capacitor in series. Choose a resistance R ?{MJd capacitance C so that the inverse lime constant 1/ RC is well within the ..,{frequency range of the waveform generator and the oscilloscope. Just as ~\you did for the resistor string, measure the amplitude of the voltage across th~ither the resistor or capacitor, relative to the wavefonn generator signal {ipplied across the front and back of the pair. {You sbouJd take care to set 1//.·.·. • • / {0:ie DC offset of the waveform generator to O usmg the osc1 lloscope to ::l »..Jeasure the offset relative to ground.) Do this as a function of frequency, ;:ij panning well on either side of l /RC. Also measure the phase of the output ~}s.we wave, relative to the input sine wave. Figure 3.15 shows how to make Jf~ese measurements on the oscilloscope CRT, using the circuit shown.

"t:Refer to Fig. 3.8 for interpreting the input and output waveforms in·te.nns ;,:.-.-.·.·. .

~;~;~f-ga.in and phase. It would be a good idea lo select your frequency values J ) ogarithm.icaUy instead of linearly. That is, use vo, 2vo, 4vo, ... , Vmax wbere @.)11o is your starting low frequency. Make a clear table of your measurements ...

,./ ij{~d plot the gain (i.e., the relative amplitudes) and the relative phase as a .-ih~tion of frequency. Do not forget that you measure frequency v, but most -~Jr z{{ ~;:::::: ~:}=:· ;;:::::::.

~{\ ·••.·.·.

_.,:rur 1 µF 1 kn ::;:::;:.

~~:~)

•.·.·.· ,:::::> ···.···.···.

~:::::: ,. .; a z::::~.

~Li: ;:::::;:;:;.

...

~y ....; -i;i /,· i i ' 1~~:: FIGURE 3.15 Measuring gain and relative phose on an oscilloscope.

:~} 1/ :;;,,,;:;: 118 3 Electronics and Data Acquisition 10-1 .

(!)

10-2 10-3 102 104 105 108 107 Angular Frequency (Hz)

90 • :R .C....l..

a. 30 1!1

## 3.5 Operational Amplifiers

=;}(Finally, use the waveform generator as a pulse generator and srudy the :~~;~_tput using your RC voltage divider circuit. Compare the input and output :]&se shapes as a function of the width ~t of the pulse. What happens if ,illtl » « RC? What about M RC?

~]&· OPERATIONAL AMPLIFIERS ,.

i~¼.:oise can get in the way of your measurements by causing things to change }w,hen you do not want it. These changes can happen as a function of time, ~]t~uency, temperature, etc. To fight this, you want your apparatus to be t~table against time, frequency, temperature, etc. The most common way to ::f~¢hieve this is using negative feedback. The idea behind negative feedback · f1f~at you take a part of the "output" and subtract it away from the "input,"

}~irising it to "feed back" to the output and discourage it from changing.

}/) Consider a generic amplifier, like that shown in Fig. 3.17, which ampli- {ij:~ the difference voltage between its inputs to give an output voltage. Let /\the gain of the amplifier be a. That is, for the circuit in Fig. 3. 17 we have =·(:Vout = a Vin. We apply negative feedback by taking some of the output ~/j~ltage and subtracting it from the input. This is shown in Fig. 3.18. A \~.esistor voltage divider is used to take a fraction /3 = R2/(R1 + R2) of ~}iµe output voltage Vout and subtract it from the input. The amplifier now ~f ~es not amplify Vin directly, but instead amplifies Vd if "'in - f; Vout.

::3:· "Th .

:::::=:=: ·: at ts, ~::::::· ~::::::.

= = ~:::\·.. V m aVdif aVm - a,BVout, ~:-:-· .· 0 ~f ~d the net gain g is [-:-:-:- tt\ .

Vout a g=-= . (3.15)

Vin 1 + a/3 t - Gain=« FIGURE 3 .17 A generic amplifier.

. }\jj 120 3 Electronics and Data Acquisition .·:·:-:-~ :11~ Gain=c:x ·.·.·-"',.X .:?JI -:-:-:·=~~ -:-:-:-.·,x :)}ij <:::::::x: :;:::::~ -:;}:~i FIGURE 3.18 A generic amplifier with negative feedback.

.}Ji _}:i~ Now's here the key point. The generic amplifier is designed s~ it. h~i ~ enormous gain. That is, a is very, very large. So large, in fact, that a/J >> ~{j {J~ no matter how small f3 is. That means that the gain is .

,._.,.,..,./.

1 R1 -.:\j~ g = - =I+ - for a/3 >> 1. (3.16ff~ /f} /3 R2 The gain oft he system only depends on the ratio ofa pair ofr esistor value.sf\ } l,•.•.•.•J'_ and not on the gain oft he generic amplifier. It is hard to get resistor value~}~]

Ji to change, so this amplifier circuit is very stable. The generic amplifief with gain a, however, is likely to depend a lot on frequency, temperaturef Jj :-:-:-:-~ and so on. :::::=:=~ As you might imagine, commercial versions of the generic amplifie~(~]

shown in Fig. 3.17 are available in lots of flavors. They are called operq,f}~ tional amplifiers or opamps for short. Instead of a box, they are represente~{j an4}~~ by a triangle, as shown in Fig. 3.19. The two inputs are labeled"+'' .. _,, for phase considerations. The+ V and -V terminals are where yoij}~~ apply a voltage source to power the opamp. It is common to leave thes~)]

th~1@j off of schematic circuit diagrams. Opamps are cheap. Most cost less $1, although you can pay a lot if you want special properties. All have ve~Jj )ij large gain, i.e., a upward of 10 4 or more, up to some frequency. (Reme~f becometiri ber that capacitance kills circuits at high frequency because it wide~tJj a short.) An old, popular opamp is the model 741, which is still used today. A version of the 741 in standard use today (the LF411) h~·~{J gain of at least 88 dB (i.e., a > 2.5 x 104 ) and can be used up to fre{}@ quencies of tens of kilohertz or more, depending on the feedback circui!~t~~ ·yJ~ .\ti .....

::::::~*~ ·::;J~ ~trr ~::;:::: ~:=::::: 3.5 Operational Amplifiers 121 ~::::::; tf.:::::-: ii\!)

+v ~-:-:-· ~_~j·~::::[::.

Out JI!/ + _ _ -I ::,,:«:-:-:- =~ -v i ....... ~.;. FIGURE 3.19 Opamp notation.

;;fa\:.

":r::: .

-1~1i( II >--.---- v·oul -~l\t 1 kn 1ft ~;:::::::: {\/· -~r:- -~ :-:•:• 100 ff:::::= w=::>.

wtt FIGURE 3.20 An amplifier circuit with gain of 100.

~f~?> W:•.·.· ..

~~;:;:; l!(l~orowitz ~d Hill ( 1989; see Section 3.1 ~) tabul~te the properties of your $Jf/tarden vancty opamps. They also tell the mterestmg story of how opamps ~f:}were developed, and why the 741 is such a mainstay. A common use ~@?f opamps, of course, ~s j~st as a oegative f~dback amplifier. You pick >> ~;::==\ Rt R2 so that the gam given by Eq. (3.16) 1s g ~ Rif R2. For example.

~\'.)!-'> build a stable amplifier with a gain of,._, 100 up to a kilohertz or so, you -~finight build the circuit shown io Fig. 3.20 .

.k i( Aoother application of opamps connects to our discussion of passive =(/filters. (See Section 3.1.5.) The effective input impedance of an oparnp in ~/·)::{:ifeg ative feedback is huge. Thal is because even though you apply a voltage = = ;.:~f(Vin, the input to the oparnp is Vdif Vin - ,8V u ~ Vin - l3(V; /f3) 0 0~~·r··= 0 1 0 ~,.-.

..

::: ;r: :::: :-:· )/Ji . ·,·.·.·.·-~ 122 3 Electronics and Data Acquisition \11n ··.:?)@ Jill FIGURE 3.21 A high-pass filter with input load buffeling. :::::::~)

_{j~ ) }::~ so it draws no current. This makes the opamp ideal for "load buffering/(~~ ~f {~ That is, you can use it to make the input to _some ~evice (like a fil~er perhaps a meter) large enough SO that you can ignore Its effect on the ClI~t~m i~(?i that feeds it. For instance, you might build a high pass filter as shown fi = ¥})

Fig. 3.21. All the output of the opamp is fed back to the input thus = = and g I. However, Zin oo (effectively) because of the opamp, sq.J ij Iikf ij@ all this c~cuit does, is cut off the output of the source for w < 1 /RC a good high-pass filter should. If the opamp were not there, you wo~1?~]

= + need to add in the filter input impedance Zfilter R 1/ i wC to th¢.}]

source circuit. See Dunlap (1988) for further clever variations on activf{j .r.1t .·.·.·.·-:::: .t1 ers. -:::::::::% 3.6. MEASUREMENTS OF .JOHNSON NOIBE 111 In this experimen4 we will 1neasure a very fundamental source of noise .. I(}:~~ ,·.·.·.·.·?.

has to do with the motion of electrons in a conductor and the heat energy\{{~: (random motion) associated with them. This is called "Johnson noi~fj} because it was originally measured by J.B. Johnson. Some people c~ft ~ fu::#tJ~ it "Nyquist noise," because the phenomenon Johnson measured was correctly explained by H. Nyquist. Amore generic term is "thermal nois~{\:~J ~ ~Jj Some journal articles on sitnilar experiments are listed at the end of chapter. You might also want to go back and look at the original wor:~(j~ij of Johnson and Nyquist, published in J.B. Johnson, "Thermal Agitatioij)~~ Nyquis@}f of Electricity in Conductors," Phys. Rev. 32, 97 (1928), and H.

"Thermal Agitation of Electric Charge in Conductors," Phys. Rev. 32, ll~Jj (1928) ,.;:::::~:~ . \)]!

-::::=::;~ Ji ))Ji ~t: ~f/

## 3.6 Measurements of Johnson Noise

-:::· {( :::;:::3.6.l. Thermal Motion of Electrons .f:::: ~:;:: ·?\We wiU outline a simple model of thermal noise as presented by W. Henry ~\/(see references). The model is based oo random thennal fluctuations of .?\ ~lectrons in a one-dimensional resistor of length L and cross-sectional area "}}A. The resistor bas resistance R, and a voltage drop V l R across the f \ ends. The current I, and therefore the voltage V. arises from the thermal :1;······ '!I { \fluctuations that allow more electrons to move ooe way than another in ~/ some short time interval to.

ff\ On average no current flows through the resistor, and the average value ~?of V is zero. That is, { t (V} 0.

'l:-: ~~:).

j'f pn the other band, the thermal fluctuations still give rise to a finite voltage \ ~:~ a function of time; in other words V (t) -:/= 0. Therefore. the variance4 ~'/'.,,f.· . : · : .· o . f V is not zero; namely, .r.·.· <( · crt = = 2 2 = 2 ((V - (V))2) {V } - (V} (V } :fa 0.

f ?

~\}this quantity {V 2 ) cri is called the thermal or Johnson noise voltage, j { ·and it is what we will measnre in this experiment.

-t(: From Ohm's law and the definitions of current and charge, we can write :%!~•"!•(' ' crv cri R !,:LR, \:i to ijf .

.wbere L is the lcngtb of the resistor, and crx is the net x motion of all the ~f .~le~n:ons in the measuring time to. If we c?-11 reduc~ th.is to _th~ motion of an f.=:::::. mdiv1dual electron, then we can use a cmcroscop1c descnpuon of cWTent Iand _resist_ance. If there is a tot~ o~ N independent and random electroo ~::motions (1.c., "random walks") time to, then in i{: ~ } ax = .JN<1d, ~~r~ ?4:,-:. . ---- '\( 4The ~tudent may want to review varioos definitions in the theory of statistics, given in ;_-{; :-Chaptec 10.

~: J"!;:::.

/\}ilf ::::::::::: 124 3 Electronics and Data Acquisition . }••••)• • .?1• •,~ .·~ -l .:::::;:::~ Therefor~l}J~ where ad is the average distance that any single electron moves.

e O"d · ·::::::/]

--JN-R.

av= (3.17J}Iffi L to .:::::::::~ . .·.·.·.·.·-~0; timei\~* Now N is the total number of conduction electrons in the resistor . • ·::;:;::;::?f.: to, the number of walks m ttme so ..: :::::::~ ·-:-:-:-:-:-~ = = ::ii!!!!{~ N (nAL) x to nALto, r r . -..-::::::::;:~}.: ti.m.·i.·/.·J.·.I·-;.;.- ..: where n is ~e. number d~nsity of conduction electr_ons _a nd -r is ~e between colhs1ons of a single electron. The ftuctuatton m the motion o~.-~/J~ \::Jt.1 single electron is .·.·.·.-.·~:?% o-J =: (d = (v;-r 2 = (v;}r2 , .· :f-:-:?-x-J:wm.

k·t:;:{;:;:t;.Il and this is_ what we connect to temperature by { E) ½ m {v j) . ½ where m 1s the mass of an electron and we note that motion 1s o~tJ~ in one dimension. Th_e fac~or k is Boltzmann's constan'. which defintii;lf ~ energ_zrii the fundamental relationship between temperature and internal Therefore .\::::t~ kTr2 .\ {)~ 2 \{i/Jj crd m .

.-:::::::;;® We note that (see Eq. (2.14))

.}Ji ._:tiJj L 2m L ---=-p=R~ \::::}~ A ne2r A ·:}{t~ where p is the resistivity. 5 ·-:-:-:-:~ /\Ij Finally, put this all into Eq. {3.17) to get - ·.·.·.·-··-~ 2 2 :::::/:;)~ 2 e crd 2 _:/?:$ tJ )\!]~ o-v L2 N R )II ~:nA:~k:tr · ··:-:-:-:-:~ R2 2 :}-:-:f-:-f~@M = ~ n: r kT R2 , : to ) )~~ 5 The definition of r used here differs from that used in Section 2.2 by a factor of 2. T~~f is because we are dealing with a single electron. ./ :ti~ .·.---.{~ /::::~~ :::;:::~i \iii~ )f!i!i ft 3.6 Measurements of Johnson Noise 125 :::::::::: ~11: or (V2) = 2k: R. (3.18)

{(It is customary, however, to express the noise using the equivalent :l]!J: bandwidth t. v l /210. Therefore, we have .-.·.·. (V 2 } = 4kT R6.v. (3.19)

........

....... ·.

-~:::- _:\· In order -to measure the voltage V, we will need to amplify or at least { (process the signal in some way. Let g(v) be the gain of this processing :{\ circuit at frequency v. Then the output voltage fluctuation d { V 2 } integrated f \ over some small frequency range dv is given by •:•:. . :-:..

=:f\.

.:; i~i~~~· \ /Measurements are made by integrating the signal over a relatively large .~\ :bandwidth fl. v. This bandwidth is typically determined by the gain function {}j.-(tJ), which is ]arge only over some finite frequency range. We therefore J} pbtain the expression -~:::::::· } } {V 2 } = 4kT RG 2 t'..\v, (3.20)

~II ~here G and /::. v are constants defined by J...: ?-:-:t-:. 00 2 = { 2 0 /j. V g (v) dv. (3.21)

z=f/ lo ]!! i,6.2. Measuremen~ ·I:::ie will measure the Johnson noise in a series of resistors, and use the result })·~ determine a value for Boltzmann's constant k.

:3i~((· The setup is shown schematically in Fig. 3.22. The voltage across the \ {@istor R is immediately processed by an "amplifier," which essentially =r ~:iultiplies this voltage by a function g(v). The output of the amplifier is =tme·asured using a digital oscilloscope. You will use the oscilloscope to \:fu~asure (V 2 ), given by Eq. (3.20). By changing the value of R (simply by ?}P:hanging resistors), you measure {V2 ) as a function of R, and the result ~f :~Ould be a straight line. The slope of the line is just 4kT G2 ~ v, so once {&~ti have calibrated the gain function of the amplifier, you can get k. (You ,I'.·,·.·.·.· .

==~~~ assume the resistor is at room temperature.)

·;:::::::· ....: -:-: .

..· -·.·.· ~kt ~·:-:-:-·, ~--=-:-:-.

l@\· .......

•.•, /::::::1;=.•"

-::::::::::. .

12& 3 Electronics and Data Acquisition :-:-:-:-:·- J!l t~ <tI~.r~.

. .: ::::::::::?~ ))?

Digital Mi Amplifier Oscilloscope ,};:}@.

·:-:-:-:-:~ ·.::::::;:I ;g~ FIGURE 3.22 Schematic for measuring Johnson noise.

J·::j:::/=1:=~$, Let's look a little more carefully at the properties of the amplifier. .

~~(f will be working in the several tens of kilohertz range, so to estimate gain we need, take a bandwidth ~ v =. 10 kHz. The digital oscilloscopf{ (3.~2fil cann~t make measur~ments ~uch s1naller than around 0.5 m V, so Eq.

·tgJI imphes that the norrunal gain G must be on the order of 1200 or more J~ ha~.f measure the noise in a 1-kQ resistor. The amplifier also needs to low noise and good stability itself: if we are going to use it on such a sni4.\Ji~ s_ignal. A ~gh-gai~ opamp with negative feedback (see Section 3.5) soun1t~ like the nght solutJ.on. {{:~I fac~t~ The bandwidth of the amplifier also needs to be considered. In ttj?Ji if we are going to do the job right, we want to make sure that all b!

bandwidth limitations are given by the amplifier, and not the osciffJi 9lti loscope, for example. That way, we can measure the functton g ( v)

~;f~~1 0?1Y· ~e amplifier stage The. oscilloscope_ bandwidth will depen~ on av~tII amebase us_~'. that 1s, the ume over w~ch the output v~ltag~ 1s great~~r}j aged and digitized. As long as the oscilloscope's bandwidth IS Ji{~\ than the amplifier's, you will be OK. You ensure this by putting y~'.#,!J~ bandwidth filter on the output of the amplifier. In the beginning, ~il~ use a commercial bandwidth filter with adjustable lower and upp~t{~ limits .-:,:-:-:-j 3.2j~/~.1 ~~ Th~ first "ampli~er" you use, there~ore, is_ shown in Fig.

For now the bandwidth filter 1s Just a box v.rith an tnput and output, ~~:!~~ !OU with knobs can _turn.-The gam-proauc~g ~atn5:ttne-a:n:rpIBre1,'v'lt~\I other hand, 1s essentially a cut-and-dry application of opamps and negati.Y:~t ffl feedback. In fact, as shown in ~ig. 3.2_3, two .such negative ~ee_dback loo~ff.ij ~li~j are cascaded to get the appropnate gain and input charactenstics. The hi~~ff~ loop uses a HA5 l 70 opamp and a low gain, while the second stage is .\J~ <<?~ !.<:::IJ~

## 3.6 Measurements of Johnson Noise

In HA5170 z::::::: •:-:-:-· •:::: .·. Band Pass -;:::::-- ~tu Filter j; Out FIGURE 3.23 Amplifier scage for rneasurcmcn1 of Jobnson noise.

NC + V Ou! Bal ~?: z·t;::: ~t.r::-:-: ~il!l1t:· Bal - In +In -V f::'pJGURE 3.24 Pinour diagram for I.he opamp chips used in this experiment We are uol ?/ii"sing I.he "Bal" connections. The notation "NC" means "no connection."

Ji(tio and uses a HA5147.6 Good starting value, to use arc R1 10 ll, } {R2 = lOOQ, and R3 = 2.2kQ. This gives the first stage a gain of lJ and :\}lie second stage a gain of 221 times the bandwidth fwiction imposed by {)be opamps and the bandwidth filter.

i,}{ All of these components, including your input resistor R (but not the :f~mmercial bandwidth filter), are mounted on a breadboard so you can ~§J~ange things easily. The pioout diagr.un for the HAS 170 and HAS 147 is ~J)~own in Fig. 3.24. The oparnps are powered by ± 12-V levels applied in :~f J?.arallel with 0.1-µ.F capacitors to ground. to filter off noise in the power -f !jµpply. Connections to the breadboard are made using wires soldered to *:;.-;;f'•' £ )NC connectors.

if ~::::;: .;z.;:~;:;+-:._--- ~~:=:::' ·6 1-he credit for figuring out the right opaa,ps and amplifier circuit in general goes to Jeff f}r~on. RPI Class of '94. More details on this circuit design are available.

Jf;i\ ..-:,::;: ~~:::: .ri:l:: Y/,..:, ,• ,:::::::==1 ·\.)::/::/::/::*f~ 128 3 Electronics and Data Acquisition · ·.·.·.·.i-~;~ J)/f Set up the circuit shown in Fig. 3.23. Check things carefully, especially You are not used to working with breadboards. In particular, make sure·the(:::::&.

..{.. ,l.~~ 12-V DC levels are connected properly, before you turn the po~er su~plf }~rJ on. The output from the breadboard gets connected to the bandwidth filter:f )Ji and the output of the bandwidth filter goes into the oscilloscope. The lowef and upper limits of the bandwidth filter are not crucial, but 5 and 20 ~ ( } ~ _~:/)tti are a reasonable place to start.

First you need to measure the gain of the amplifier/bandwidth filter as t1/}I function of frequency. AU you really need to do is put a sine wave input the circuit and measure the _output _on an oscilloscope. The output shoul%~ btJ.f}~ look the same as the mput (1.e., a sme wave of the same frequency v), the amplitude should be bigger. The ratio of the output to input amplitud_~t/~ is just the gain g ( v). There is a problem, though. You have built an amplifi~t/1 of very large gain, around 2.4 x , and the output amplitude must be les:~?t~ than a few volts so the opamps do not saturate. That means that the inp*-~J~ ~~;JJj must be less than a couple of millivolts. That is barely enough to see· si~~JI an osci~oscope, assuming yo~r waveform generator can make a good /?JI wave with such a small amplitude. · 3.2Jt~I You get around this problem by using the schematic shown in Fig. fl The wavefonn generator output passes through a voltage divider, cutti.iijf afI~ the amplitude down by a known factor. This divided voltage is used input to the amp~er. It is a good idea to measure the resistor valu~~}~ co1~?§f Rb.ig. and Rsman usmg an ohmme~er, ra~er than t~ trust the ~~lor up ratiWfl (which can be offby to 10%). P1~k resistors tha~ give you a divider ?ff~ somewhere between 10 and 100. It is_ also a good _idea to see the ou~ut the waveform generator and look at 1t on the osc1lloscope along with t~~(~~~~ ampl ifte rl b an d w1 "d h fil ter output. )·.·.·f.·. { · -~ ff i ·:-:•:-:-:-:~ -:-:·:·:-:-:~:m: .-<::::::::~:?!?

.-:::::::::;·~~ .::::::::::;:~ Waveform :::::::::::~ generator .·.·'.·'.·:-:-:~~ ·::::::::;~~w.

-:-:·:-:-:wh· Rtiig .·:-:•:·=·~~ ·}t}~ :::::::::~~ ··.·:.·.:·.1·.·, Digital Amplifier oscilloscope ::;:;:;:::;.~ . ··:::::::;:;;@j . ·}:::::~:~ \}}~1w.

·.·.·.·.·-~ FIGURE 3.25 Calibration scheme for the noise amplifier. .-:-:-:•:~-~ . g~ ·r1 })~ .\\;&~ ~=:::::, :&-:-:.

[:;?=:·:.·:=.·:.

~ :::::, 3.6 Measurements of Johnson Noise 129 1i: 2500 r----r-----.- - ....------r-- r-----.------.----, Negative feedback gain 11.

·~ ...

[(\ ..- .-.·.

,~,r. .- .. •••• ,,r. .• ••. . •• 1500 ~L". .- .-. :--.:·-.

~\ :::-.

~ ::::·· ...

~?::::: [::::> : ~ t: 1000 C.

~ ~: ~ :: : : : : ::· . E co ~--.·.

r ==: ,f::::=: -~ 500 1 Bandwidth limits ~:-:-: ~:::::- (3 ~?::- f\:- 0 '-------'-----'------'----'--- --L-----'----..,___----' ' ~r f : { ::: o 5 10 15 20 25 30 35 40 Input voltage frequency (kHz)

ij~\ F,IGURE 3.26 Sample of data used to determine g(v) for the amplifier foJlowed by the ~ (~ommercial b~dwidth ~lter. The simple negative feedback formula gives a gain of 2431, ~\:::-:·and the bandwidth filt.er ts set for uLo = 5 kHz and VJiI = 20 kHz.

f',t'.,_, • .

~:-:::·.

ff:.

~--·.·.

,f..,.f:-:(-:- Make your measurements of g(v) by varying the frequency of the wave- ~/Jonn generator, and recording the output amplitude. Of course, you must r}).lso record the input (i.e., generator) amplitude, but if you check it every i ?)ime you change v, you can be sure it does not change during your rneasure ~f fment. Measure over a range of frequencies that allows you to clearly see {:}:the cutoffs from the bandwidth filter. including the shape as g approaches ~f \zero. Also make sure you confirm that the gain is relatively flat in between t{)he limits. An example is shown in Fig. 3.26. The setup used R 1 l O Q, t~)R = 100 n, and R3 = 2.2 kQi so the total gain should be 2431, and lf 2 fi /\~w~ith bandwidth filter limits at 5 and 20 kHz. The main features seem to ~orrect, although the filter has apparently decreased the maximum gain l\::~_b1t.

ff): Now take measurements of the actual Johnso~ ~oise_as a function of R.

i~?~emove the waveform generator and voltage divider mputs. and put tbe ~~(resist~r. ~ou want to m~asure across the ~nput to ~e am~Ii~~r. Set the time ~{J>er d1vis10n on the oscilloscope so that its bandwidth limit 1s much larger :,( )han the upper frequency you used on the bandwidth filter. For example, \}{}iflhe re are 10,000 points (i.e.t samples) per trace and you set the scope to ~~--:,: ~=~::.

J":• J--': •-:• . : .- --.:·-: ..- .·.

;,/9:=:> 130 3 Electronics and Data Acquisition 20 .-------.--------.-----------.

Single sweep '5 0 0 -10 -20'-----~---~---------' 0 0.5 1 1.5 2

## 3.6 Measurements of Johnson Noise

~··· ~~- 1< 20 ti: _ 18 fl 116 ·-·· en ffl ::.:::. ~ 12 t::: > ;,:-: ~ 10 j9 ; .

> 8 ;:-.

~::. ::l ~::. e ~:: 0 ~~:: 4 t,-._- .· ..

:::: .. 2 :~:: .-.·.

:::::. 0 .-.·. 0 2 4 6 8 10 12 14 ~::: , r · . . · · . . . Input resistance (kn)

::::: ......

?: FIGURE 3.28 Data taken by measuring the standard deviation of the output voltage signal, !\ as a function of the input resistor value. The slope gives k, while the intercept gives the ::=:: equivalent input noise voltage, after correcting for the amplifier gain x bandwidth.

integration given a list of (x, y) values. For the data of Fig. 3.26 one finds that G2 ~v = (7.9 ± 0.5} x 10 7 kHz.

Ii Next we make a plot of {(V - {V))2) as a function of R. Note that ~ since (V} = 0, the above expression reduces to ( V2 }. The plot is shown in Fig. 3.28 and a linear fit gives {V 2 } / R = (1.33 ± 0.08} mV 2 jkQ ,:-: i->' ~::: ~=:~ and an intercept at 4 m V2 .

i: We can now calculate Boltzmann's constant k from the above data using ::::- ~::- = Eq. (3.20) and setting T 298 K (room temperature). Using units of hertz, t':-· :I:':.:':, : volts, and ohms, we write r.·.· ~:: :~:: (V 2 )/ R (1.33±0.08) x 10- 9 -23 ;.:,: = ........ k= 298 O =(1.42±0.13) x 10 J/K.

··-·. 4TG 2 ~v 4 x x (7. 9 ± .5) x 10 10 ~~: :-:-: •:--:- This result is in excellent agreement with the accepted value k 1.38 x ~:: 10-23 J/K.

r.'=:-.

:'~/,::': f'J"'>.·.

.,.,_._.

:~-=: ~,._:.:_::._: ,._._.

,._.,· ~-· ~III/ f 1~ 3 Electronics and Data Acquisition .....· .·.·«-·-· = \\/~t The intercept of the line in Fig. 3.28 is the noise at R 0. You would expect this to be zero if Johnson noise in your input resistor were the only- }}{ff :?tt~f thing going on. The input oparnp, however, has some noise of its own, due \}Jf to internal Johnson noise, shot noise~ and so on. The specification sheet for \ff~{ the HA5170 gives an equivalent input noise of around 10 nV/-JHz. How /?f{t does this compare to your measurement?

. .. ...- .-.-.-.-.-.- There are a number of variations and extensions to this experiment. For :}}~:?-~{ )tiff ex~ple, instead of simply using the oscilloscope to detennine the standard, \Jtff deviation, use MATLAB and the trace data ( as in Fig. 3.27) to get the values :)/JJ~~; and examine their distribution. You can get the data into an array trace; :}JJ~~: and you can use mean(trace) and std(trace) to get the mean and standard· ............. ..

deviation. The series of MATLAB commands used to plot the distributiori}//J f bins linspace(min(trace), rnax(trace), 50); [n, x] hist(trace, bins); stairs(x, n); The single sweep trace in Fig. 3.27 is plotted this way in Fig. 3.29. The·))l~~;~ :.)..i ,}. f•Z•f"

distribution is rather Gaussian-like, as you expect, but you could test to a> 40 2?

I::, 0 ........., ____. ....__ ____ _._ ____. .,___ ___ .....___.

-10 -5 · 0 5 10 .:}:;~~f::· Output voltage (mV)

. :::::::~::~ ~ FIGURE 3.29 Histogram of the individual voltage values from a single sweep trace. The) }}~ J }{{f::: line is a Gaussian distribution, with the mean and standard deviation determined from the ))}iii~ trace data, and normalized to the number of measurements.

J!I

## 3.7 Chaos

see whether this is really the case by comparing it to the Gaussian with the same mean and standard deviation, and considering the x2 . (See Chap ter 10 for definitions and discussions of these quantities.) Some digital oscilloscopes have the capability of performing a real-time Fourier analy sis of the input. That means that you can actual!y demonstrate that the noise spectrum d(V2 ) /dv is indeed ''white,'' that is, independent of frequency.

This is straightforward data lo talce. but wi 11 require that you learn more about Fourier analysis to interpret i.t. "

One nontrivial circuit modification would be to make your own band width filter. For example, consider the circuit shown in Pig. 3.12.7 Try assembling components that give you reasonable parameters for the gain integral in Eq. (3.21). A simpler kind of filter might simply be two RC filters, one high pass and one low pass, cascaded in series. If you want to do active buffering, though, be careful to use an opamp that works at these frequencies. Another interesting variation is to use a few-kiloobm resistor as input, but something mechanically large and strong enough to take some real temperature change. If you immerse the resistor in liquid nitrogen, for example, it should make a large (and predictable) change in the Johnson noise.

3.7. CHAOS We now discuss a measurement that uses nonlinear electronic components to explore phenomena characteristic of complex physical systems.

3.7.1. The Logistic Map and Frequency Bifurcations We are used to the notion that physical systems are described by differential equations that can be exactly solved for all times, given an appropriate set of initial conditions. This is not true in complex systems governed by non linear equations. A typical ex.ample is the flow of fluids. At ]ow velocity one can identify individual "streamlines" and predict their evo]ution. However, when a particular combination of velocity, viscosity, and boundary dimen sions is reached, turbulence sets in and eddies and vortices are formed. The motion becomes chaotic. Many chaotic systems exhibit self-similarity: that 7 This. in fact, is what Johnson used in his 1928 paper. You mighL want r.o look it up, and compare your results to his.

<::::::;::=:;::;; .·.·.·.·.-~ I/iii~ 134 3 Electronics and Data Acquisition ·.·.·.·.·-% }j\i11 is when the flow breaks into eddies, the eddies break into smaller eddies and so on. Such scaling is universal; it is observed in all chaotic systems.. .} /}%.

A particularly simple case is that of systems that obey the logistic map ··-·.·.·.·;-;<~ :n~~!:i~?c~~~t~zye;c~~~!:;;~~l;: Ill ~~~:~ \i@fJ finite time interval (such as a day or a year) or the successive "generations"

\@~ of the population. If the reproduction rate in one generation is >.., ~en it would hold that : :::::::~;@j )}~ X j+l == AX J · :::::::¾;:: -:;:}~;~:: \@Ii if."

However, the population will also decrease due to deaths. In particular )!J:tt the food supply on the island is finite the death rate will be proportional to \\~~ft x~. Thus the evolution 8 is governed by the map 1 Jil sxJ- Xj+! AXj - (3.22)

.::::::\~if A/Jj We use the term map, because given x J we can find xi+ 1 uniquely. Both - ?{}~~j A and s are assu~ed n?nnegative. We s_ee imm~di~tely that if )., > 1 ~d s = 0 the population will grow exponentially, while 1f A < 1 the populatton _:)/Jt }}iff~ will tend to 0. The map of Eq. (3.22) can be resca/,ed by introducing Ii i loWs:: Then Yi oreys the ump>J for all j.

= )}1t\ Yj+1 Ayj(l - Yj)- (3.23)

:}}it :-/\J{: The above map has the interesting property that if the reproduction rate for- ..... -~-.

"///§f one generation is restricted in the range Ill then Yi rernfil~ bounded beM:: A< , ]:::::i:::~lml:: 0 < Yi < 1.

:}/1]~/ Toe first study of these issues is due to the English sociologist T. R. Malthus ( 1766-- 1834). -:;::::::~:: _:)}~@.!

_jll

## 3.7 Chaos

We are foterested io the fate of the group after many generations, namely io the value of yi as j ~ oo. We find, as already stated, that If>.. < l, as j-. oo Yi - 0, the population d~ays to 0.

If 1 < l < 3, as j - oo y j -+ y ~ y* the population tends to a srable point y•, namely y* )..y*(l - y*) (3.24)

with solutions I)

y• =0 * = ( i-I .

= = In this case the solution y"' 0 is unstable, because if Yo E (E infinitesimal) Yoo wiU tend to (L - 1/>..).

When >.. > 3 the system behaves in a very different manner. A,<;. soon as ),. > 3 but}.. < 3.4495 ... the population alternates between 2 stable values. When). > 3.4495 ... the population alternates between 4 stable values until ).. > 3.54 ... , where it alternates between 8 stable values; for ),. > 3.56 ... the population alternates between 16 stable values, and this continues at ever more closely spaced intervals of l. We say that there is a bifurcation9 at these specific values of A. These results can be easily checked wjth a pocket calculator or a simple program. Table 3.1 gives some = = = typical results for .l. 2.8, }.. 3.2, and).. 3.5, aod the stable points are shown in the graphlcal construction of Fig. 3.30.

What is plotted in Fig. 3.30 is Yfinel vs Yinitial· Toe continuous curve is the equation of the logistic map Yf AYiO - Yt). In Fig. 3.30a the curves TABLE 3.1 Example of Stable Points of the Logistic Map }, =

## 2.8 y"' =0.6429

>.. =3.2 y* =0.5310 .. .

## 0.7995

J.. = 3.5 y* = 0.3828 ...

## 0.5009

## 0.8269

= 0.8750 .. .

Henri Poincare in 1900 had noticed such behavior in mechanical systems aud named il the "exchange of stab1lity.'"

(a) {b} y linal y final

## 1.0 1.0

i=28 A.=3.2

## 0.8 0.8

## 0.6 0.6

## 0.4 0.4 ~

## 0.2 0.2

J.. = 1.0 0 0.2 0.4 0.6 0.8 1.0 0 0.2 0.4 0.6 0.8 1.0 y lnitial y initial = = = = FIGURE 3.30 Plots of the logistic map: (a) for A 1.0 and J... 2.8; for A 2.8 there is one stable point at y* 0.6429 .... (b) For = = = >.. 3.2; there are now two stable points at y" 0.7995 ... and y* 0.5130. See the text for details of the path leading to the stab1e points.

: ··. ·: ·. <· :· ·-._ -._ ..· ·:-·.·.·.:. ·.: · ..· . -. ·.-... ·. .· .·. ... >. ,:-:-:-.· .·. .. ·:.: ·:·· . :·: · :· ·. :··.: ·: ·: ·:·· -:· .· ..· .··. ·. ._ .· .·.- .-··. ·. .· .·· . ..- :-:-:-:-:-:·: -:-:-:-:-·.:· :·:-:·:. :·· ·.·. ·.· :···. .· . ·. ...- ·> .·. ::· :. -::,:-:-:-. -:. -:·.·.· .·. · .· .· ·: :-..: -.· -·.· :-.· .·. ·.·.·-·.·. -::: ..· . . ~--.-:-.· .·: ··.· .:. -: ·.· .·.: .· ..... :·:. . ·.·. _.·.· ... :. .. ·· ...._ :: -:-.·. .. ·.·.·:·:. :·. . :.· ·:: -.·=·.·.·.·.·. .....· · . .

ti.. .i.l ~...

fu~\\\%1t•1i~t,it11tif~i[~~,:t.:~.;~~fl~!i}~f~t%\\i{fu{i:.:~•,~•'.i~~~t~~~tl~~~.~~~\~1~tifui~1,~~.. 'J.).. ~~~\,\1it~.:;~~\?[tf~\it.:~~. ._~ ._..~.

·~~ \¼L~L'.~,_~L,~O: o... 0. ......................................... _.._..,l,..:.IL_'. . ~-"""..,J>..._~1.-........... .,.... • •• +...:.a.La.::. ... ,,.--..:.-..._"li,.',,,_-.._....._..._._. .......... - ..----.......~~--··a.a. 6 ... ._ L&.o • , __ ._..._ .'-.,Lt-Lt_ &...a& ... a.a.&.a.L .. a.&.&.-.. • ,........ -

## 3.7 Ch a o s

= = for ).. 2.8 and A 1.0 are shown, while in Fig. 3.30b the curve for = = A 3.2. The lines for Yf Yi are also drawn. We can follow the path from some initial value Yo 0.1 in Fig. 3.30a to the stable point (indicated by a circle). Given Yo we find YI Yt at the intersection with the curve.

However, YI must now be used as an input, Yi, so we use the Yf Yi line to locate Yi and proceed to find Y2 and so on. The process converges to the circled point at y* 0.6429 ....

It is also evident that the same construction for the A Pcurve will lead to y* 0.0. In Fig. 3.30b we start (for more rapid convergence)

= = from Yo 0.2. We now find the two stable points at y* 0. 7995 and y* 0.5130. The map requires that one stable point leads to the next and vice versa.

When A > 3.5699 ... the population no longer reaches a stable point but takes on an infinity of values in the range 0 < Yoo < 1. We say that the system behaves chaotically. This persists in the remainder of the range

## 3.5699 · · · < ).. < 4.0, but one finds regions of stability where an odd num

ber of stable points exist. The dependence of the bifurcations on )... is shown in Fig. 3.31 where the A-scale is highly nonlinear in order to show enough detail; the vertical scale gives the values yj( j ~ oo) of the stable points.

The remarkable discovery by M. Feigenbaum in 1975 was that all sys tems that exhibit chaos follow the same (universal) behavior and that the difference .6.n An+l - An of the values of the parameter at which bifur cations (period doubling) occur converges rapidly as n ~ oo. In particular as n ~ oo the ratio An+.] - An ---- ~ 8 4.669201660910 ... (3.25)

An+2 - An+I tends to the universal number 8. For instance in our previous example An is the value of the reproduction rate A at the nth bifurcation.

However, also the amplitude of the population at the stable points exhibits universal behavior and scales according to a different universal number a. Let y:(l) and y;<2 ) be two stable points of a given branch at the bifurcation value An. We define .6.y* y*(l) - y•(2)

n n fl ' and it holds that as n ~ oo .6.y! = -- ~ ct 2.5029078 . .. . (3.26)

.6.y;+J .:}}~~ ;::~~ 138 3 Electronics and Data Acquisition ::::::;)~~~ .·.·.·.·-~ :.:):-:•J:-:h-:-~~~ . ·.·.·.·.-.-~.,a -· ·.·.·. . ·.·. .· %;: ../ f]Ws 1.0 .··-:-:•:-:-:-:00 >:/\::~ . ·:-:::-:::•:::-::~·:~~tl :)\}~=WJ

## 0.8 .-·x·.·.·t.r-.~-~zm-~~

<:}:~~ <Ill y"' .·.·.·.·%;W,

## 0.6 .):=:%®

\\JIWA .· ·:.·:.:·:.:·;·::···:1~ - • ' •• •.•4•. .

./J i]~ 0.4 :,::::::;~ .:-:/fr~~fffi .·.·.·.·-·aw t ·.\ }:WJ~~ 3.4St t3.5699 ..... ,.,.~ . ·::::::::t ~

## 0.2 :·::::;ffi

1 2 3 3.5 4,0}\:~ .·.···-:ar1~~ A.

FIGURE 3.31 The stable points of the logistic map as a function of>.. The A-scale is highly./@~ th<{:\~ nonlinear in order to clearly sbow the bifurcations. The black parts of the plot indicate chaotic region. Note. however, the thin white lines, which indicate islands of stability. {{}~ . )t@~~ This indicates that as )... increases the system replicates itself after rescaling::}JI by a f actor 1/ a, assh o wn • m p· 1 g. 3 . 3 1 ; typ1 ' ca 1 m • terv al s l O uA y * an d uA y *' \.·.)·.·.·f.·;ilWif: 2 3 . di d .... •.J-'::;::· are m cate . }(:~ The numbers 8 and a are named after Feigenbaum and are obtained bY.':}!Jji numerical calculations of maps or equations that lead to chaotic behavior(\}~~~ this}/J~~ They are always found to be the same for all problems. We will verify :)@~~~ to the accuracy that can be reached in the experiment described below.

:::}}~~ ;::::::::=:®: \j~ 3.7.2. The Diode-R-L Circuit .

....

.}\~I 1:- simple R-L-C circuit wh~r~ th~ capac~tor is replaced by a diode, _driven at:fj}f its resonant frequency, exh1b1ts bifurcations and eventually chaotic behav~:::JI The\J~ ior. This is not so surprising because the diode is a nonlinear device.

:::::::::::W· .. ""'::@.; ){1~ The intervals .6.y; must be chosen appropriate1y as is also evident from Fig. 3.31.

\I~f~ Il~~I .... ~zt:.;: ::::/¼·~ 3. 7 Ch a o s 139 R L {} a J l e + v. T It ,., ,.:-:-: ,:~::::: Conducting Non-conducling •r. .• .·.· •~.rf-· / FIGURE 3.32 The <liode-R-L circuit. The equivalent behavior of the diode in its two f~J":.::•=:. : states.

,:. .: -:-: ~;;;:::.

~;:;: ~~::::: [J 20mA rr ~::::::- __A _M_~--~ C~hode 1 10mA :~;:::::- 2V i t ,:-:.:• ~=::::: ,:-:-:- ,r .. ..-• ... •-..·· ~:::::: FIGURE 3.33 The 1-V characteristic of a diode.

'l':<-· ~==:::.

:::::::: :,.,_..: . - . _:-._:-. effect was first reported by Linsay11 and was analyzed in detail by Rollins t?

and Hunt.12 •:-:-:- ~::::: ~:::::. The circuit is shown in Fig. 3.32, and the 1-V curve of the diode in f\ Fig. 3.33. When there is a positive voltage across the diode it conducts [} and appears as an EMF of magnitude - Vr, i.e., as a voltage drop. In its :r( nonconducting state the diode behaves as a capacitor C and will draw a f/ charging current. These two states are shown schematically in Fig. 3.32 f \ where we also indicate our convention for positive current flow.

M( The source is assumed sinusoidal of amplitude Vo, so that the voltage at f \ ..

point a of the circuit is :~~~:::, : . : .. : . : .. : . : . ~· . :- · '. Vo= Vo cos wt . (3.27)

:::::::::.

i{/ 11 P. S. Linsay, Phys. Rev. Lett. 47, 1349 (1981).

:~f · 12 R. W. Rollins and E. R. Hunt. Phys. Rev. Lell. 49, 1295 ( 1982)~R . W. Rollins and E. R.

·~----·.· :~f:· Hunt. Phys. Rev. A 29, 3327 ( 1984).

:-:-:-:-· ~=-=·=· i~:::: .~...-:. . :-.

I~=-=· .·.·.·---~ .. {ilffil'X.til5151!i/Sl7:r 3 Electronics and Data Acquisition )\~I~t~~~ 'P!i"!X· /ti: current in the circuit and the voltage at point b (i.e., across the diode)

-..::-::::::~ .

be calculated straightforwardly from the discussion in Section 3.1. In -::::::::.* = - )!II conducting state, obvfously Vb Vr, whereas in the nonconducting ti ~ the voltage will follow the frequency of the source. However, the ,litude need not be the same for every cycle. This happens because the ?}~@ le does not stop conducting as soon as the current goes to zero but has ::::;:::~ :/?~ emory; it continues to conduct for a time interval <::::;::~ ::~:;:~=:=~ (3 .28) :/:If.

. /::?-@· }/ii 11 I llis expression m ~s the ~aximum current during ~e curre_nt cycle; -rm :\/I le are constants. If I/ml 1s zero then the recovery time rr ts also zero. .

>> = :{J~ lml le then rr rm. Thus the maximum current in the following :}Ji le depends on the value of Im in the previous cycle in a noninvertible ·>JW rion. We have a mapping :1, llmln llm\11+!· =} :Ill \ behavior of the current and voltage are shown in Fig. 3.34.

·-\:lffi fhe period of the source To 2rr / wo defines the cycles or generations he system. The source voltage set~ the repr~duction paramete~ through :({~ : )/f~m = Vo/ Vf. The volta~e acro~s the ?1ode Vb (m the ~onconducttng state) )t~%: elated to the populatmn y i m the J th cycle. Depending on A, the voltage /]*~ repeat~ v.ith the perio~ To, of the sour~e, or with ~riod 210, ~To, and ..

_v~ on u?til b~com~s completely chao~c. A numencal analysIS of the .){~~ ~ ,ve circwt 1s given m the papers of Rolhns and Hunt. \ }:~ ~ 31n the conducting state we find that I (t) = ( Vo/ J R2 + L2w2 ) cos(wt - 8 0) + Ae-<R/ L)t + jf Vb (t) === -Vf.

1e nonconducting state we find that J)J{:I~ · (t) = Vo// R2 + L2(.,Z - wl; )2 / w 2 cos(wt - eh) + B ,-<2 R IL> 1 cos(wbt + q,) · /JI~ = v 'b(t) 0cosu>t - l(t)R - L(dl/dt)

:::::::::w :)?Ji wb 2 = Wo 2 ·- (Rf 2 L) 2 :::::::~® -:-:-:·=··*= \J~ffi A, B, </> are constants, ./!)[@ -·-:-:-:::-l: ./ii

## 3.7 Chaos

Qf----+------------- t - v, i----t--f l3(n+1)

t,(n+1)

JURE 3.34 Toe current and voltage in tbe diodc-R-L circuit shown as a function of 1e.

7.3. Experimental Results le circuit is set up as shown in Fig. 3.32. A Hewlett-Packard function :nerator HP3325 is used to drive the circuit A fairly hefty variable induc nce (L 10 mH) is used since the diode capacity is small. The series sistance was R :: 50 Q. The diode should not be too slow (such as are rec ier diodes) nor too fast. Good results were obtained with a IN4 007 diode; her diodes, namely 1N4001 and 1N5404, gave quaHtatively similar (but 1antitati vely different) results.

The first step is to tune the inductor to find the resonant frequency of the rcuit. In this case it was found that mo/2rr 71.5 kHz::::- l/(2rr,/Lc).

Figs. 3.35a-3.35d are shown the voltage across the diode Vb and the iving voltage Vo. For Vo < 0.875 V, Vb has the same periodicity as However just above Vo 0.875 V, Vb alternates between two dif 1.

rent values as shown in Fig. 3.35a. The effect is clear, but not very onounced, because the data have been taken only slightly above the first furcation. fjgure 335b corresponds to Vo 2.033 V where the sec id bifurcation sets in. The period of Vb is now four times that of Vo.

~ain the difference between the two high-level states is very small and ?~ )\{I 142 3 Electronics and Data Acquisition .. :::::::=:J~ ·.·.·.·.·.··* Iii ·r/@~ :-ff@i ' {(@~~ FIGURE 3.35 Oscilloscope trclces of the voltage, Vb, across the diode (upper trace) and :){~::{j _\\it~:3 of the driving voltage Vo (lower trace). The driving frequency is 71 .5 kHz. (a) Immediately after the first bifurcation. Note that the upper trace is bimodal and has period 2To, (b) :}}J~3 .){/~:3 Immediately after the second bifurcation. Note that the large peaks are bimodal; the period }\~/3 is 4To. (c) Immediately after the third bifurcation; the period is now 8To. (d) Chaotic behavior. \ :/::::~ ·.·.·.·.·. ......._ .

. ,:::::::=·::::: .· ,::::::~::::::: that between the two low-level states is not observable. The next scope. ::::::::)llll traces, Fig. 3.35c, correspond to Vo 2.280 V and were taken right :\}\~ .)ff after the third bifurcation. The period of Vb is now eight times that of (:\I Vo and similar comments apply as to the distinguishability of the differ-.

= :\ff ent states. A fourth bifurcation was observed at Vo 2.340 V. Finally Fig. 3.35d shows Vb when Vo ~ 2.355 V where chaos was observed to :\)\ )Jf~ set in.

A plot of the bifurcations obtained for this diode is shown in Fig. 3.36. .-/ )fj The error in determining the exact bifurcation voltage 1 4 is ±5 m V. We :·\··J--:;½:j i(J~~~ summarize the results in Table 3.2. From these data we calculate the \I:@ 14A more precise de1errninalion of the voltage at which bifurcation occun. can be made ·::::::::-:::~ when a signal analyzer (FFf) is available. In this case the onset of period doubling is evident :_:.!_;_;_-:.:_:!_lit from the appearance of subharmonics in the frequency spectrum. .·.·.·.-~::::.

.·· ..··..-·.

..

..

..

.; ???

:~ ·.

:: ·.

- :.~....;..~."

·.·.·.·,.•.;•.; .;· .\·.-J.......i4 .~... J

## 3.7 Chaos

0 500 1000 1500 2000 2600 FIGURE 3.36 Plot of Vb vs Vo as measured for the 1N400'7 diode. The bifurcations are :/ clearly observed.. Some 6. Vb spa.cings are aJso indicated. Chaos sets in at Vo 2.355 V.

TABLE 3.2 Bifurcation Data from Measurements of Chaos .•.

Bifurcation Vo (mV)

1st 875 2nd 2033 3rd 2280 4th 2340 Chaos 2355 Feigenbaum number 8. We have = ± A2 - }q 1158 7 mV A3-A2=247±7mV }i.4 - )..3 60 7 mV ::1 144 3 Electronics and Data Acquisition >t\w ·?:?i °){fi and therefore )}ii~ = ± sO) AZ - }q 4.688 0.13 ~: =~! ]~ 2 = ). = ± 8( } _ ). 4.117 0.49. ) / :~ 4 3 :;:;:;:;::~: j These results are consistent with the asymptotic value given in Eq. (3.25)/}/JJ : _-·:}Ji even though in?ut _from only the first fo~ bifurcations was use~.

·<Ji The detenrunation of the second Feigenbaum nwnber a 1s not pos~ sible with the present data. As pointed out previously, the intervals\ !]~ Liy~ must be selected appropriately, but even then (see Fig. 3.36) the}!}~@: ~Y! a: fa~t/@~ ratios of seem much larger than This_ is due in part to the 111:/!j~ that one has ~ot reac?ed th~ asymptotic 1~egime of Eq. (3.26) and part to c:tiscontmuous Jumps 10 Vb at certain values 15 of Vo. However,f!J~ it is ev~dent from the data that .t he system replicat~s it~elf after eac~·:(@i bifurcation. Furthermore, the spacing between stable pomts m every branch.{:}~i fac<fli decreases in subsequent bifurcations by a multiplicative factor~ this tor seems to converge toward Feigenbaum's a. We also note that for the:;}JiiI !

1N4001 diode it was possible to observe islands of stability in the chaotic\/ region. ·.·.·.-.·~-- \}ii~~~ ····w.· ·\:::::~~J 3.8. LOCK-IN DETECTION )\tJl ...· .·.·.·.'?f:.=· Suppose one is studying a signal, amid noise, that cmnes at a specific)\) @ frequency. We can use this to pick the signal out of the noise. Furthermore,.))~~ !

./JI we can be sensitive to th~ phase of the signal a~ well as its freque~c!,· and that can make a huge improvement. The techynoiquu e that does all this 1as J-::\J:JI~ t call~ phase~sensitive detection. The device that do it with is called _/:::::::%.

lock·zn amplifier.

There are two inputs to a lock-in amplifier. One input carries the signal) }}% /J{@ (and the noise). The signal, remember~ is varying at some specific frequency ·\t~ which you are aware ~f. It may b~ completely buried in noise, how.ever, so you would not see 1t on an osc11loscope, for example. The other mput}}~~~ carries a reference that varies at the frequency of the signal. The signal}}~:~ way givesj}f~ oscillates because you make it do so, and ~e you do that also you the reference. For example, your expenment measures a response to ~ ;::j:~ .?ft@ 15Somediodes show marked hysteresis associated with these discontinuities. .:}J~@.j .· :\J::.::~: . ?:?i:~: ·::::;:~:~: ·.\JI ·.>}ti .: \jW f : ,r_..· .. _.·. .

:;::::- 3.8 Lock-In Detection 145 r.-.·.

:;:·-·.

~::: ~=::: ~:::: ,r:. ...:. ·- ~·=·: ~::: ~;::· ~;::· nr;-:- t=:: 11--------------- ~==:· j ~~~i~: ,:-:-: •.•.•.• f: \ · put filter Time -· · FIGURE 3.37 The lock-in amplifier acting on an in-phase signal ljjj: laser, so you turn the laser on and off rapidly with a mechanical chopper.

The motor drive for the chopper gives you the reference signal.

:_=:l=::·_l::l::_::. The lock-in amplifier takes the reference signa1 and uses it as a switch.

For half the period, the switch is "up,'' and it lets the signal input pass through it with no change. For the other half, the switch is "down;' and it reverses the sign of the signal (i.e., multiplies it by -1) before it passes. This is shown in Fig. 3.37. The result of this is a modified signal that is always positive, instead of oscillating around 0 like the input signal. A low-pass filter takes out the remaining oscillation and lets the DC level pass through.

This DC level is read off a meter, presented at some output connector, or digitized by some computer, depending on the lock-in amplifier.

Now consider what happens if the signal is out of phase by 90° with respecl to the reference. This situation is shown in Fig. 3.38. Now the output of the multiply stage is still something that oscillates about 0. The average DC level is 0, and that is the output of the lock-in amplifier. So, as \( promised, the lock-in amplifier only detects signals that are in phase with \( the reference. Most lock-ins have a "phase adjustment" knob on the front tr that allows you to maximize the output signal. If you have the phase 180° { : away, the output signal should reverse sign.

{ : Now consider what the lock-in amplifier does to noise that has some f :· .frequency other than the frequency of the signal. The answer is obvious.

t\ The output of the multiply stage will just be ajumble of noise like the input f( stage since the reference is essentially just randomly flipping amplitudes.

. : .... -- .. : ... - . · . : .. - · .

~~:::· ..- :::· •:-:-· ®)

~!~:::· :}]]~W]

·::::::::}~ 146 3 Electronics and Data Acquisition :!(}~ :{\:~ ·>tt~~~ ?::::=m .:-:-:-:-::~ :::::::::t~ ....... -;m,, :::::::::~ ··\@~ ..... fZ !iii .· ;::::::{~=: .. ·?ii <Al Filter ))f:Jj Output .·,:-:-:-:-~· ··/::::::Wj ::til Time :<?.:I FIGURE 3.38 The lock-in amplifier acting on an out-of-phase signal.

.}J ~ .::::):~ .::::;.;~:{:f~ .::::::ftM ,, y . :/::::~-@ :it Signal 6.y . ' :-:-:-:-::m: :::::::::~ -- X <~I Small modulation t!.x FIGURE 339 Using a lock~in amplifier for modulation spectroscopy.

·.::::::\~ The o~tput of the lov.:-pass filter will average to O over some tiro~ ;{]~ :}II detenruned by the RC time constant of the filter. · · )@j The lock-in ~pli~er ~s a~tually quite a versatile instrument. One of its have_/:)1 uses beyond nmse reJection ts as a spectroscopy tool. Let's say you a signal y that is a function of some parameter x. For example> you might}}~~ of polarizes\fti have an NMR signal as a function the large magnetic field that signal:}JrJ the sample. Such a thing is graphed in Fig. 3.39. Now assume the .-:;:::;:;;:~i= }!II ··:::::(:~I

## 3.9 Computer Interfaces

{ ; is modulated (i.e., made to oscillate) by setting x to some central value xo j( and making itosciUate aboutxo by a small amount 8.x. Then the amplitude f: 8.y of the modulated signal is given by .·.

:::.

:::.: dy . .·· .

8.y = - llx .

.:·:.: .>:O .· .

/. In other words, lhe output of the lock-in .is the derivative of th~ line shape y(.x). It does this, of course, while throwing out any noise lhat gets in ::;: its way. One common technique, described in detail by Dunlap (1988), I : ,• : . :. . is to sweep the value of x many times and record the output in a multi- channel analyzer. Th.is uses signal averaging to get rid of any remaining noise :::: 3.9. COMPUTER INTERFACES \~. ): Many of the experiments described in this book, as well as in many :::: :-:·. undergraduate instructional laboratories, can be done without the use of ::;:.

{ sophisticated computerized data acquisition. Indeed, in experiments such :f::: as the Balmer series in hydrogen (Section l.5.3), the Faraday effect (Section 5.7), and the y-y angular correlation in 60Co (Section 9.5.4), for example, :::: there is much instructional value in taking, recording, and analyzing data :.:- ·>. "by hand."

? Nevertheless, directly interfacing a comput.erwith the experiment makes :::: it possible to take data much more quickJy in many cases, and th.is also :::: bas much instructional value. Furthermore, soroe experiments that had .;,: :-, once been very difficult, if not impossible, in the instructional labora :::: :::: tory, can now be done with relatively simple and inexpensive computer ::: interfaces. A wide variety of commercial interfaces exist, and it is not / possible to cover all of them in this textbook. Indeed, the market moves quickJy aod different options appear and disappear very regularly. A recent ,::• publication, available free from Keithley at http://www.keithley.com/, is {\ the ''Data Acquisition and Control Handbook.'' However, a number of :} : standard situations apply.

~{ The simplest computer intetface is a "serial" interface using an RS232 l: standard communications port on the computer. The electronics on your r:: computer and in the data acquisition device to which you wish to inter j: face support a standard "handshake'' protocol for moving instructions f=: and data back and forth between the two devices. All that you need is if ~:=:::, [{ z ...

~:-::: %-;.·.

.\j@j ·)it!

148 3 Electronics and Data Acquisition :it?i ·.:.::.:.::.:.: * \}f~~~ a four-wire telephone cable to connect the two, and software to make it }Jj work. This software is very often available using a free download from the \}@ vendor of the data acquisition device. For example, for their line of digi- /Jj tal oscilloscopes, LeCroy Corporation (http://www.lecroy.com/) provides .!}@1 a program called ScopeExplorer for this purpose. There are many other \{@ examples.

It is a good idea to consider "middleman,, computer interfaces, so that :)}~ your computer and software can talk to one specific device, and then }}~ this device can be connected to any number of other instruments that ){§f ··)!~ acquire different kinds of data. This cuts down on the "interface pro- grams" that must run on your computer and with which you need to . :{@ ·.\:Ji become familiar, and gives you more flexibility for your experiments, at }Jfil the cost of a bit more expense. For example, Vernier Software & Teclinol- \!J@.

ogy (http://www.vernier.com/) sells the "Universal Laboratory Interface~'-. ..

.i\.. f,,i;l.:: (ULI~, a serial computer int~~ace_that then connects~ experiments through· a vanety of analog and digital mputs for measunng ~oltages·, _currents, )}@ ))@ scaler counts, a~d so forth_. The company also sells mexpens1v~ com- puter programs for controlling the ULI from any number of a variety of )}W computers. · :;:::/~ ····m Serial interfaces are simple, but they are slow. They transfer data one bit )/ [; \ft at a time (''serial"), and the number of bits per second (the "baud" rate) is {/W limited by the simple cabling and connection standards to some s6,ooo bits \J]

per second (56 kbits). This is fast enough for many applications, but the.

i}~l experimenter can quickly be needing (or wishing for) a higher data rate.

\Jf Faster data rates are provided by paral1el interfaces, where many /.f.• l·Y .· lines connect the computer to the data acquisition apparatus, or possi- bly through the network connections to the computer using an etheroet }}t ?\i connection and TCP/IP protocol. At this point, the number of hard- ,•.-4' .. ~.1*- ware and software options increases enormously, including interfaces ))[ designed and built in the laboratory itself. Some companies that sell such }J{ ::/@ interlaces and software include Agilent Teclu1ologies (http://agilent.com/), Keithley Instruments (http://www.keithley.com/), and National Instru- -_:)@ ments (httpi/www.ni.com/), among others. LabVIEW from National \}j /i@ Instruments is a very popular software tool for laboratory interfaces which :Jj features a graphical programming environment, but which can be diffi- \% cult to use in an undergraduate laboratory setting without the necessary ...., .,. ..

-:-:-:~.; support. :/ ~::: /%1 Probably the most popular standard parallel interface is GPIB or "Gen- ·:/1 eral Purpose Interface Bus." Also known as the IEEE-488 standard, or as tt . :-:·.~ ·-:-:,;.; ::::0.

:::::~ :\::~ ,:::::* ·-:::::~

## 3.9 Computer Interfaces

HPIB by people at Hewlett-Packard Corporation (now Agilent Technolo gies), GPIB uses an ASCII code to communicate, very similar to most serial line communication systems, but uses a 24-pin connector, allowing data to be transferred in parallel at some level. It can transmit up to I MByte per second, within this communication protocol. In order to communicate with a data acquisition device equipped with a GPIB port, some sort of computer port is also necessary, generally provided using a plug-in card, . . available from several manufacturers depending on the type ol computer.

Virtually all commercial general use data acquisition software packages provide for communication through GPIB, including ScopeExplorer and LabVIEW.

One thing to keep in mind is that the next step after data acquisition is data analysis. Depending on what software you may use for analyzing your data, you should try to acquire the data in a way that is amenable to your analysis tools. Once again, this can be solved with commercial products if you have the resources. In this book, for example, we use MAT LAB for data analysis, and it is possible to purchase from The Mathworks (http://www.mathworks.com/) toolboxes for MATLAB for instrument con trol and for data acquisitio~ although we are not making use of these specialized toolboxes in this book.

Depending on the local expertise and available resources, the vari ety of computer interfaces can become quite large and complicated. We will use a number of different options for the experiments in this book including • a LeCroy Digital oscilloscope and ScopeExplorer to measure the decays of eddy currents in metals (Section 2.2).

• a plug-in board for control and voltage readout, operated with :::_:_~:-::~_::·:_:.: LabVIEW. for a high-resolution optical monochromator (Section 6.3.3).

_ • a Vernier ULI and LoggerPro software to count and record Geiger counter signals to measure nuclear decay rates (Section 8.6).

• a Canberra multichannel analyzer and a GPIB interface to mea :::::- sure gamma ray spectra, including an experiment on Compton scattering If (Sections 8.4 and 9.2).

,·.·.· :::::- • a home-built time-to-an~og measurement system for determining the ::j} mean life of the muon (Section 9.4.3).

16Toe reader should be aware lbat it is unlikely (and unnecessary) that these options be duplicated exactly in your own .laboratory.

._{/~ .. fi)~~ 150 3 Electronics and Data Acquisition }:/:::~ ·.·.·.-.-~ -:-:-:-:-:i ·)/li 3.10. REFERENCES ::::::~~ .-\:-:i-J:-:m-:~ An excellent, popular. and up-to-date text and reference book on electron~ ics is: ·.·.·.·---~ \/Ji :)Jj P. Horowitz and W. Hill, The Art of Electronics, second ed., Cambridge Univ. Press. Cambridge, UK.

1989. .:::::::.::§.

::::::=::~ _:;:;::~:;::~ _\j j A student 1nanual for this book is also available. A good book with intro~ ductory chapters on solid-state electronics, including the physics behind)\}]

diodes and transistors, is · ) }~~ )}~~ R. A. Dunlap, Experlrnental Phy.sics: Modem Methods, Oxford Univ. Press, Oxford, 1988. ::::::::.:::i -·:::::~.=.~~ ./'·.J·.·,I,'~f·:f:;,i:.

Some good articles that discuss the physics and experimentation of {l~ thermal noise can be found in .·.

·-:::::::2:~> R. W. Heruy, Random walk model of thermal noise for students in elementary physics, Am. J Phys.· .:\.., ~. .: x]

:::A~ 41, 1361 <1973). _-. )ii P. Kittel, W. R Hackerman, and R. J. Donaelly, Undergraduate experiment in noise thermometry, Am.

.-:/~;i J. Phys. 46, 94 (1978,. \J!

D. L. Livesey and D. L. McLeod, An experiment on electronic noise in the freshman laboratory, :f:=:i Am. J. Phys. 41, 1364 (1973).

.-:-:~. .= -~ /fl There exists by now an extensive literature on chaos. Some suggested \\J references are: ·-:-:-:•:.-:- [:)J M. J. Feigenbaum, J. Stat. Phys. 19, 25 (1978); 21,669 (1979).

!Jl L. P. Kada.noff, Phys. Today 36 (12), 46 (Dec. 1983).

G L. Baker and J. P. Gollub, Chaotic Dynamics: A11 lntroduction, Cambridge Univ. Press, Cambridge, ...· .·.·.r.

UK. 1990. ::::::::~= H. Nagashirna and Y. Baba, Introduction ro Chaos. English transl., Institute of Physics, Bristo], 1999. -::}:~ \if~ ·::::::::~ .::::;:::: ':{:;:~ -~ ,·.·.-..

:::::::;=: ::::::::=:: :-:-:I.:•:.- '.:::::~~; <:::~:::~ Ji \]~ )J ,·.-J. .

;.:;:::::: ~:::::: ff =~=~:( CHAPTER 4 t \ .

r:-:.: .· r. .- .·.· .

r ..• •·.·• ~~~~~::: Lasers ~:::::: ~:;::: r~~~: ::::::-.

[( :•:•:- {/ :=::::-' .- ..· .·.

::::::- f{ ::-:: ;~::· .-.· .. - .. ·..

;::::::: .......

·.

:::::: ..- .·.· .. -.·.· ' [\\:: •.-.-.

·---·.· ;::::?

:•:-:-: ~~::::: ~:::::: :~:::::: :~::::-' :~:::: :-~-:-.

:::::: .

:;:::: •:,:-: :::::: tr Lasers are a source of intense, highly monochromatic, coherent beams of t( light in the visible and infrared parts of the spectrum. "Laser" is an acronym {{ for "light amplification by stimulated emission of radiation'' introduced {( in 1958 by its inventors, C. H. Townes and A. L. Schawlow. Toe first {\ successful operation of a laser was achieved by Maiman in 1960 using a f \ ruby rod as the la.t;ing material. FundamentalJy a laser consists of the lasing f\ .

medium, of means for exciting the medium either through an electrical !{: discharge or by an external light source, and of an optical cavity made out f/ of a pair of high-reflectivity mirrors. The lasing medium can be a gas, a fi · transparent solid, a liquid (dye), or a semiconductor. The relative simplicity j( and low cost of lasers have contributed to a wide range of applications.

f l Semiconductor lasers. also refe1Ted to as diode lasers, can be found in ~/ almost every modem piece of equipment.

ff Because of the coherence, intensity, and monochromaticity of the light {( emitted by a laser, such beams are ideal for demonstrating the properties of f( light and of optical elements. Experiments that without a laser were tedious ~;:::· f\ J'.·.· ::~::: ~:: ..

J'.·.·.

~I';. .:" :.:·:.

~.-~- ? ..· .-.

>>:·=·=~~ :, iii 152 4 Lasers :-:~i~\/(~~ .. :::::::::~:- ck}f and required great skill can now be performed routinely. We begin with brief discussion ~f ~e laser equations and a description of the HeNe las~rf \ As the first application we show how a laser beam can be expanded w1tl-(:::;:~ a pair of lenses and how to measure its spatial profile. We then discuss th~!{{· Fabry~\jj}~ two most familiar types of interferometers, the Michelson and the Perot. We demonstrate how they can be used to measure the wavelengtb~\t ~ fl~ of the ~eNe line. Before using a laser the reader should carefully consulf

## Appendix C on laser safety. :\)~~

·\))}; -:-:-:•:~~ <::::::::~ 4.1. THE PRINCIPLE OF LASER OPERATION -:-:,:-;.,;.:"& ?Ht~ . h . . d h ( 1 1 ) 'k . . fr ~..{.~. ~@ ~ L1g t is enutte w en an atom or mo ecu e ma es a transition ·om excited state to a state of lower energy. The frequency of the light is given b~/ Jj :-:-:-:,:-:~ = -w = - 1 - E2 - - E - 1 : )!J~ v (4.lLJ~ -::::::=:::~ 2rr 2rr Ti ·.-:-:-:-;;•:® = an~~fj@.

where llE E2 - E1 is the energy. differenc_e between -~e upper 1~{j~ lower ~rates (also r~f~rred to as levels) involved m the transition. Here Ii Planck s constant cliVIded by 2n -.-:-:-:-J.t -:-:-:-:-~ 34 }(/:~ 1i 1.054 X 10- J-s, (4.2J(}tfa :-::-::::-:::-::-::m:~ and therefore -:-:-:-:-:® ::::::::::~ = (4.3)}1}~ !lE luv.

::\:;:::~ th~}J~ The reason for the factors of 2n is that they simplify the writing of ti ·.·.·.·.·-~ equa ons. ;:) ;::::=m o! occu#:(Jm The transition from an ~pper state to a state _lower en~r~ will spontaneously and we designate by A the probability per umt ume for sucli.\t$ an occurrence. Ho~ever, the transition can also be .sti":ulated (induced){}~ V:7~(J@ by ~e presence of light of ~gular fre~e~cy w, sati~fying Eq. (4.3!.

~:::::Jf designate by B the probability, per umt tune per urut energy density ~#\}~ unit frequency interval, for stimulated emission. It is reasonable that presence of the electromagnetic (EM) field (light) at the resonant frequen~y\@ffi wi~{fj will not only induce transitions fro1n 2 -+ 1 but also from 1 _. 2 ~o~/JW th~ same prob~bi!ity. I~ is equally reasonable that the photons adsing stnnulated e1TI1ss1on will have exactly the same frequency and same direc,~(jf.

tion as those in the incident EM wave. These arguments were first propos~4}1~@.

-/ :::::.::::: . ·:::::::::::::=.: ::::::;:~ ··-:-:-:-~ -·:.·.·.~·-~ -:\}:~ --:{::.

--····· .r:.-:-:-.

-~:::::: 4.1 The Principle of Laser Operation 153 r:~\ 2 ----.---- 2 ----r--- 2 -----,---- ,:::::·:.: ~~:::::: ~-:-:-:- \ / ;I:::::::: 1 (a) 1 (b) 1 (c)

.-. r .. { ·.·. · .F .· IGURE 4.1 Emission and absorption of radiation between two atomic le~ls: (a) Sponta- -?:::"neons emission with transition from state 2 to state 1, (b) stimulated entission with transition ~{/ :2 ~ 1, and (c) absorption with transition l -+ 2.

[=:::::· it·· ~zjrt/ (:by A. Einstein, and the coefficients A, B are re_lated and can be_ calculated J/\ ·from a knowledge of the structure (wave funct10n) of the atomtc states ::}.:~:=:::· .

3 3 - _ : : . - : ; : , ~ ; - , : : - { : . A = 7 I t L : W . 3 . ' B = (J) f;:_3 I{ JIµ, · E Ii) J 2 . (4.4)

~:;:::: Jr C EQJr I l,C ~:/-torµ, between the 1rutJ.al and final states and Ethe polanzation of the EM ~f })ield. Loosel~ speaking, the matrix element is a measure of the average if/ value of the dist~~ _o~ the eJectron from the ~ucle~. .

[f\ The three possibilities are shown schematically m Fig. 4.1 and corre- l\/_spo~d.

to spontan~us emissio~ sti~~lated emissi~n, ~n~ abs~rption of [t\ :radiatton. We remark that the probability for absorption 1s identical to that It~!

(or stimulated emission for the same external field, a consequence of the [\\reversibility in time of elementary physical processes. So far we have talked ~f { r /:a bo~t single atoms, wh~reas in_ reality the lasing medium consists of a col ~mt lectJon of N atoms. It lS then important to know how many of the atoms are _in the (excited) state 2 and how many in the (lower) state l; we will + = ~:::/ cles1gnate these numbers by N2, N,. where N2 N1 N. The number of ~~:::=.transitions per unit of time from 2 -----> I is then given by tt> [.;.:-· R 2-+ 1 == N 2 (A + Bu ( w )) , (4.5)

;y~ ..

;:f·=<·.···.

ijf (whereas from I ~ 2 ~:-:::< = (4.6)

[]:(· R1""'2 N1Bu(w).

~t::::: ~~~( ~ere u ( w) du/ d w is the en~rgy density ~f the EM fie~d per unit frequency ~f ~\ ( :: ~terval. Normally the relauve population N2/ N1 is governed by the if?..

~~t- / ~II Ji".·.· ::::::::::::~ ·::::::::::j,• ·.·.·.--- <:::::::...: :-,'c 154 4 Lasers .-:::::::::::f ·-:-:-:-:-:-:•.

\\\t J: jl~ ).·\.·.)·.-."f,,,·.

3 --"'rr--- .}!i!}~ ::::::::::~- Dlt 1 (a) (b)

FIGURE 4.2 Creating population inversion (a) in a 3-level system and (b) in a ~-lev#,(t :Z:}~:' system. The double arrow indicates the lasing transition; while the up-going arrow 1 ~ sbo~it/f' is the pump. Level 3 must have a relatively long. lifetime, whereas levels 2 and 4 have a fast spontaneous decay along the indicated arrows. ·}i{}~~ Boltzmann distribution N2 ------ N1 Ne- 1 oc~. . . -? 4. : . : .l :: .i ~ ~. : ~ W _ We can see from Eqs. ( ~.5) and (4 .6) that for stimulated emission to m preference over absorpt1on, we must have N2 > Ni . Usually the oppos1(it:::::im is true because ~E for atomic levels is of order of a few electronvolij{J~ = << iVi{{~ w~ereas at room temperature kT 0.025 eV , ~d fr~m Eq. (4 .7 ) N~ It IS therefore necessary to create a population inversion, namely to mcre~/::ffi N2 while maintaining N1 small. This can be achieved by involving thr~@f or four atomic levels as shown in Fig. 4.2. In the three-level laser, ato~(j~ are pmnped from the ground stat~ l_ to the excited state 2 ~d quic~~\:{~ decay to state 3 by spontaneous enuss1on. If N3 exceeds Ni lasmg can ~~\t~ place in the ~ -+ 1 transition. It is, however, easier to use a four-lev~rJ~ ~Wr;@ scheme. 1n this case atoms are pumped from the ground state to 1eve1 2 spontaneously d~cay to ~~pulate level 3. Now level 4 i~ ~ractically e~p~~f{ ~ f~J® because of a rapid transition to the ground state. Thus 1t 1s much easier maintain N3. > N4 ~d a~bieve lasi~g in the~~ 41:ansi~on. · \))}[ If the lasing medi~ 1s placed m an ~po.cal cavity (Fig. ~.3) we ~;~j~ cavitlil~ assu~1e that p~otons enu_tted alo~g the cavity axis are tr~pped ~n the and mteract with the lasing medmm, only a small fraction bemg lost. W.~::~?2 *-ff[ consider a four-level laser and can set N2 = 0 and N4 = 0 because transitio~s 2 -+ 3_ an~ 4 ~ 1 are presumed fast The to~ number:::~f j ~ Jill photons in the cavity 1s Ny and n 1, n3 are the atoms per urut volume::f '}}::~~[ .//}!~ }}=~i . T{J~ ~f\ h i. 4.1 The Principle of Laser Operation 155 &x,. ../. ,:r-----, ;,:{ z~\t.

~r·· :::::::::'i,,:·.--' ) ftirGURE 4.3 A lasing material placed in 3J.l optical cavity will lase ifil is pWJ1ped lo achieve . .

..:-:·.··: ::5{:~~c1ent g11111.

.} [flt ~~:::istates 1 and 3. It then holds that ~~::::.

:.r;~:::::::· ~t? · -:::~~:: ::: ::::::ti. being the atomic density, and ~;,-:::::::: l/?. dn3 = - n3 if :. - Wpn1 - BNyn3- - (4.8)

.%:f>= dt r ~1t· ·::=:=:.. dNy - Ny dt = V BNyn3 - re . (4.9)

v~}jJiere Wp is the probability per unit time- for pumping 1 -+ 2 -+ 3 (transfer- /...

%:t/ring atoms from state 1 to state 3) and B is the probability that one photon ff:in the cavity will induce a lasing transition in unit time. The lifetime due ;}jospontaneous transitions is rand due to cavity losses re, The (mode) vol i:)\~e in whicb the photons interact inside the lasing medium is designated ...~ /j oy V. In all cases Lhe spontaneous transition rate 1/ r << B Ny, so we can w,~,:,, ( . i f;~eglect this term. With this assumption, the steady-state solution of the rate .,~uations dn3/dt d::: 1 (ie., .IO)

~tj;in the steady state, the cavity losses per pass equal the gain per pass; the J.(}aser output depends linearly on the pump power, lasing medium density, })md mode volume. Note that VB = ca where o- is the cross section for the wf~bsorption of_pho~ns ~ the lasin~ medium. . . .

;.f> The (loganthrmc) gam per umt length of the lasrng medmm 1s found It ·\\from Eq. (4 .9) if we neglect the cavity losses. Then = = d:: VBn3dt VBn<t =un3dt .-.·.

·=~=::: ~fi il!lf \:::::~:i 156 4 Lasers _i~ /11 and ii _ 1 dNy _ n g - Ny ----;fi" - <5 3 • :=)j)I]

incident tcf)}j Thus in a finite length t., a number of photons Ny (0) will grow .·· ··!··i½i ......•_ .,J Often egi. G is designated as the gain per pass through the Jasing/\1~ :::::::::~ medium. <::::~:~ <Ji ,"/)~j -:-:-:-=-~~ 4.2. PROPERTIES OF LASER BEAMS .·.·.·.·-~ -})~J -::::::::¼ /J~ Lasers emit a "beam'' of light, the properties of the beam being detennined \!Ji primarily by the optical cavity. In the cavity shown in Fig. 4.3 the radiation travels in both directions and the electric and magnetic fields of the wave {}~ )Ji must satisfy boundary conditions at the two mirrors. Standing waves wilf exist in the cavity as shown in Fig. 4.4, and only frequencies such that the ·:::J~ :/J~ cavity length is an integral number of half-wavelengths are allowed. If the t, \{f cavity length is then U 1 T = = C /ti q and v q U, (4.11)

::!/:ii where q is an integer. The frequency difference between two such adjacent ];I longitudinal modes is c Vq+l - Vq == U FSR (4.12) :::::::: .;:::;:i .·.·~~., .·.·.·.t ........ J ._::j{~ •:•:•:, ::::;~ ',",/J .\::1 ,'.",~J )f \ . :·;:~~: \ '.

\ 'J' I ': ·. : · : . ~ . · : .~ :;f .....

'\~ FIGURE 4.4 A laser cavity must support standing waves.

::::: /i:~ )[ . ·::: -:-: ~~i-r:-: [::::- ~::::: 4.2 Properties of Laser Beams 157 ~-···· ?::;::'., ~=::::: ~--·.·. G Ir =;;_------1-----_;;= -~v , ~{: FlGURE 4.5 The gain curve of a typical lasing material as a function of frequency. Only ~I/ lines with gain larger than the threshold will lase.

i ::: ~1/ ~·/:,: and is referred to as the free spectral range (FSRJ of the cavity. As an ~f/ e = = example if we take 0.5 m. we find that PSR 3 x 108 Hz. This ;~.·-· iti spacing is very narrow as compared to the frequency of optical lines, i.e., j~{ for.\.= 600 nm, 1.1 = 5 x 10 14 Hz, and t,?: = - 2e = -V- "' 6 ,::~::: q l.6 10 .

:-:,:,: V X FSR ::::::: C .- .· .. · .·.

it?{ Only a limited number of longitudinal modes are present in the emitted :~:f:· radiation. This is so because the lasing levels have finite energy width; this ::::::: width detenn.ines the range of possible frequencies as shown in Fig. 4.5 and ::==::~.

:::::::: is referred to as the gain curve. The width of the individual longitudinal ~It modes is determined by the nwnber of round trips Lhc light makes in the cavity before being attenuated; th.is is referred to as the finesse F of the ~t/ cavity. The finesse depends on the losses in the cavity. U we consider -:-:-: ::;:::: only the losses at the mirrors that bave a reflectivity R < l, we find (see :::=::: ft Section 4.6)

:;;:::: PSR c (1 - R)

Av=--=---- (4.13)

1t./R F U or to a good approximation Av= - (1 - R). (4.14)

Zrce f} .~. ..... For R = 0.99 and e = 0.5 m. we find Av = 10 6 Hz= l MHz. In contrast, ~:::: the gain curve bas a width of several gigahertz.

•%·'· ~~:~=:::::= · :;::: ~ft.

::;:,: .·.

tt~:; ~1;::· :,:-:-:-:-:m /::::/:a:;:; .··:::::=:::=:~ 158 4 Lase rs .·.·.·.·.·-~ :::::::::::~~ ·-:::::::::;~~ In the transverse direction the optical cavity is not bounded but is open/\{j However, the beam is confined near the axis and its transverse structur~jf/@j is determined by the focal properties of the mirrors and the length of th~({Jj cavity. A simple example is the confocal resonator, where both (spherical){:?~1 t/\tffi mirrors have equal radii of curvature.1 R, and R equals the distance, between them; note that f R /2, so that the focus is in the center of th~}}@j tra~sv:rs{\J~ cavity. The tran~verse b~ di~tribution can assu~e any of the modes charactenzed by the 1nd1ces m, n. The electnc field at a long1tudma(t:dffl i@m distance z from the center of the cavity and at the transverse coordinatef x, y is given by .})f* (Jix) (,Ji ·:::::::~¾ u -(x:~::) lj//i!ifiI~.

E~ H Y)

- (4.

£( X I y ) - ..tQ m Un e ' . .J)J :.(·.·}.· -.i·«fji.

w(z) w(z) w(z)

. <<·>:•:-:ij Hm, lfn ~e.the m, He~te polynomials, and Eo is the peak field valu~f/~$ For sunplic1ty we have Omitted the phase of the field. -·:}\:/m = = Of particular interest is the lowest mode where m n 0, the TE.Moo;/ J j mod e. S1 . nce nu o = I , th e fi e ld di s tri .b uti . on 1 . s a G auss1 . an .:-: . : . : :: . : . :~ . ~ .. ~ 2)

·.jf@@ x2+ E( X , y ) - - A WO e - ( ~ . (4 . 1 6· J ~ i ) ·:-:. ] ;.;- 0 :.'.½ w(z) -::::::::~ ·-::::::::::;l.

radius\Jri The field falls to 1 / e of its peak value, and the intensity to 1 / e2 , at a = The{}Jf r w(z). We refer to w(z) as the "berun radius" at the distance z.

= nonnaI(}fi smallest beam radius is at z 0, where the wavefront.is plane and to the cavity axis; we speak of a beam waist and for the confocal resonator:/}~:* /g.

(4.17)/i/l!I wo (confocal) == //ii The beam radius at the distance z is given by ,r (4.18{/!///~~Ij w(z) == wojl + (z/zo)2 , .

.· .·.·.·.·-:-!

where zo is the confocal parameter, or Rayleigh range. It is related to the})ij ,·.·.-:-~ beam waist through -}\~ = nwi_ }{I Zo (4 .19}:-:-:-.•½· ).. :::::::?/4 ))~ It is unfortunate that the same symt>ol K 1s trsett rorflftffurl~c.avdJ'ln.uidiul'l,..ruI:.:;-J curvature of a spherical mirror or lens.

;.,: ...

~::;: ~::> ~====::' 4.3 The HeNe Laser 159 r..-:-:..

r.. ..

~:::;: f ( t/ ..

;:;;::::· ;:;;:;::· f \ FIGURE 4.6 Focal properties of a TEM oo Gaussian beam propagating along z. At the f / waist the amplitude falls to 1/ e of its on axis value at a distance wo from the axis. Note the zo {{· wavefronts (surfaces of constant phase). The Rayleigh length and the di~ergence angle t \ Bo are olso indicated.

-:-:-:-: ~-(-:- :::~:::: ~~{ Thus for the confocal resonator, where Eq. (4.17) is applicable, we find z.·.·.· :.-::::::- that ::;;.-.·.

if: = .e zo (confocal) / 2.

;:::::::;.

;:::::·:·.

fk.

.Jz In this case the beam radius at the mirrors has grown by over the value at ~%~•-f.-·.>·· . th .

e waist.

~f: >> Al large distances z zo the beam divergence is given by x:::=: a::=:::. w(z) wo A.

z=:::: 0=--~-=--. (4.20)

~::::>

## Z ZO TC WO

f / f \ and for the confocal cavity t \ ~r 0 (confocal) = J21i.Jn.e, z:-:-:- /\. whlch is typically of order J 0- 3 or smaller. Figure 4.6 shows the rays, r.: ...

ff wavefronts, and beam waist in a confocal cavity. The fact that the beam ?-{} cannot be focused to a point but instead forms a waist is due to the wave ;f,: . f .. · nature of the Tu\1 field.

~?:::: Not all mirror combinations lead to stable cavities. The confocal res- ,..-.·.·.

f(: onator in particular is at the limit of the stable range and is not used in f f: practice. Instead, most laser cavities consist of one perfectly reflecting flat ~{} .mirror and of a curved mirror with radius R > 1. Usually the curved mirror if/ has a finite reflectivity, for instance 95%, and thus serves as the output cou ~t}pler, by transmitting some fraction, say 5%, of the beam stored in the cavity.

it/ x~=:::,· ~--· ..

~f:;::::.4.3 THE HeNe LASER ~::::.: x:::::.: i~:f:: ::, }The helium-neon gas laser is the most commonly used laser for simple ~t\ laborato:ry work, alignment, and oth~r low-power applications. The first ~;:::::: ~r=:=: if::: ~j1(/.·.::· ~it :::::::::::~ )i{/!l~ 160 4 Lasers ·:}:};~ :::::::::;:&.

HeNe was built by A. Javan at Bell Labs in 1961 and now HeNe la~er~\ f/fJj~ are available at low cost from many manufacturers. A thin tube is filled.))/~ with helium at a pressure of a few Torr and approximately 10% of~n eon::) ){~ gas is added. An electric discharge is established in the rarefied gas by the}}ti in\\{l application of few kilovolts between the two electrodes. The electrons aboutj){i the discharge excite the helium atoms to ~e 2S l~ve!s, which lie 20 eV above the ground state. By a fornntous comc1dence these levels(/}~~ coincide with the 4S and 5S levels of neon. Through collisional exchange/ ?~@ the neon atoms are excited to these levels, resulting in population inver.:.\ (j~ sion. Lasing takes place as indicated in Fig. 4.7, corresponding to the<{~]

·))i~ffl wavelengths ~ = :){/~I 5S 3P 1 632.8 and 543 nm \ii$ 4S ~ 3P )... 1523 nm :}:~~~f.

:?J~ffi ). = 5S--?' 4P 3391 nm.

::::::::~~~ ·:::::::~;x;3 /]@.

The 3 P level de-excites quickly to the 3 S state from where the atoms return for-·\}~ to the ground state by colliding with the walls. By coating the mirrors )J~ . ·.·.·.·-=« 5S 4P 4S .-:-:-:-:-x .{:~{i .·.·.-.....

Collisions )Ji 3P \]~ 20.SeV .-;::::~::~ :::::::~x \ti~ /!I _e_v __ _,...,_,..1 ___.._c_o_11_is_1o_ns_w·_,1h walls He 11S Ne (1s2 2s2 2p6 } ./}¼ ·:::::::;:: \Jr; FIGURE 4.7 Energy levels of helium and neon. The principal lasing transitions are indicated by double arrows. Note that the ground state is at a much lower energy. \ :~:~ ,:;:::;;;:: !I //////////:i?":'//////////////////////////////////~////////b,.

~'--~~ ~ ~ ~ FIGURE4.8 Schematic ofa HeNelaser showing the discharge tube and the cavity mirrors.

(b)

FIGURE 4.9 (a) Definition of Brewster's angle Bi,. (b) Transmission of a p-polarized ray et Brewster angle without ottcauadon.

reflectivity at a given wavelength, a particular laser line, most often the red line at 632.8 am, can be selected.

A sketch of a HeNe laser is sbowo in Fig. 4.8. The tube diameter is chosen so as to maxiro.b.e the population inversion of the neon atoms, ao empiricaJ formula relating the pressure (in Torr) lo the tube diameter (in mm) being p D --- 4 Torr-mm, usually D --- 2 mm. The length of the optical cavity ranges from 20 to 50 c.-m. As shown io the sketch the electrodes are ree-essed. The gain in the low-pressure gas is relatively low, resulting in amplification g "'0.10 rn- 1 . As a result the power level is also low, in the range of a few milliwatts. The width of the gain curve is dominated by Doppler broadening and is of order of 1.5 GHz.

A special feature in the sketch of Fig. 4.8 is the exiL windows of the tube, which are set at the "Brewster" angle Bi,. As shown in Fig. 4.9, light polarized in the plane of incidence ( p-light) and incident at Bi, is not reflected. If the refractive index of the window is n the Brewster 1, condition is i ii 162 4 lasers ··\.·:,:·:.·:.·:1:'1:>:,:.~,•,;,1• . ·.·.·.·.-...... ))J but from Snell's law /tiJ sin 0t ni sin 0 1. ':::::\ ::~ nt . -:::::::::::::: Therefore we must satisfy !Ill sin 0i n, cos 0· n· <:::::::;:~ 1 1 -:.:-:-:-:-:•:- = = ·.' -:-:-;.;.~; Forni 1.0 and nt = 1.5, Bi 56.3° and the Brewster angle, which is\:Ji~ .· ·.·.-..- :4.~ the complement of Bi, is Bi, 33.7°. Light polarized normal to the plane of{) f incidence (s-light) is partially reflected from the windows and the higher\ \:~=a .)ff~ losses prevents-light from lasing.

In Eq. ( 4.12) of the previous section we showed that the spacing between)}~i = .·,·.·.·..-.-;.: the longitudinal modes is FSR c /2£. One can demonstrate the presence of\ jJ~ /Ji~ these modes by a simple experiment using a HeNe laser. Since .e .:... 0.3 m, ·.·.·,·.-.-~ = : the FSR 500 MHz, whereas the width of the gain cw-ve is of order}:J;~

## 1.5 GHz. Thus we can expect that three to four longitudinal modes could·}\~~~

be lasing simultaneously. One way of observing these modes is to use a fast) )fij J~ diode to record the intensity of the laser light. Because the diode detects the\ f intensity, i.e., the square of the amplitude of the laser field, its signal will \ ;{~ ?J~j contain frequency components at the difference between the frequencies of the modes present in the light. . ·{} j )iJJ To explain this let us consider just two modes at frequencies w1 and w2• .............. ..

Then the amplitude (the electric field) is · ·:::::/:::: :}\i (4 .21): :::::::=:=~ :'.:;:::;::=~ and the intensity (assuming A1, A2 real) /}J 2 = 2 2 + + ? 2 }}J: I= IAI A cos cv1t 2A1A2cosw1t cosw2t A2cos w-it. ./ \:~~ (4 .2 2} ::<=:=:=:~ . -:-:-:.:.. : ~ :-:-:-:-;-;- The tenns in cos2 w1 t = ½( 1 +cos2cv1t)andcos 2 cu2t = ½ ( 1 +cos2w2t):{@~ oscillate so fast that the diode will respond only to the constant part 1A 2 /2 ){f and IA212 /2. However, the cross term can be expanded to give · ./ )~~ ·-::::::~~ = }]!

2A1A2coscv1tcos(L)2t A1A2{cos[(w1 +w2)t] +cos[(a>1 - wi)t)} . ..

(4 23)<::::~< . <Jt As before the term in cos[(a>1 lt>2.)t] will average to 0, but the diode can) ):~~ /\§f: respond to the term in the difference frequency ·~::::::~: (4 24) -:-:-:•,-: . )11 ':\·:::~~ z:·.· ,~i·:-::-:::-- fl 4.3 The HeNe Laser 163 Cf there are more than two mod.es present we expect to see nor only the ~;:;: %:-:-. fundamental difference frequency ~::;:;:- ~==== %:::: 1 .-:-.·. = ~:::: -(wq+l - Wq) FSR, 2,r ~~~:~.

~~tr:\ but also higher harmonics arising from ~::: > ,~,.:.;,:, · = -(Wq+2 - Wq) 2 FSR x:::. 2n x·=· x:=== ;;r,.,..• • ,• ~~::;: a.od so on. Data obtained by using a fast diode connected to a microwave ~,~~~.·:-:·: x-··· spectrum analyzer are shown in Fig. 4.10. The central peak is at 550 MHz, ...: :::::: and there is a secood peak at twice that frequency. (The peak on the left is 11!\I jusl the DC level.) This indicates the preseoce of at least three longitudinal modes.

::::::· ~l( ~\: ..- :-:, ~~ ::::; :;:i:-:-:, ,.-;:::: III ~:-:-:- lit~ ~:::::: i~'°It'::•::•: ::1::::: f=::;, ~y:: ~{: ~-:-:• if ~i\: ~ ::; ff FIGURE 4. LO Microwave spectrum of tbc signal from a Ca~t diode viewing a HeNe if ~k beam. The frequency scale is 184 MHz/cm. The line at 550 MHz (al J 100 MHz)

gives Lhe separation in frequency between adjacent longitudinal modes (modc:8 differ ~ { ing by two integers). This spc:c1ruro indicates the presence of at. least three longitudinal I=:=:=· modes.

,,.;,~;i U.,:- ~,::;: ~,:. .; .: ~?

~( ~:-: . ·::::::::::::= .-:-:-:-:•:. ...

:::::::::::9 ;i/1:!it 164 4 Lasers 4.4. MEASUREMENT OF THE TRANSVERSE . . @~ BEAMPROFil..E :: :}}~:~ Whilli{!/ij be:1'11 Oft~n i~ i_s desired to exp_and or reduc~ the diameter of a laser be::/;fi m.amtatrung the parallelism, the collimatzon, of the beam. This can ~cbieved with a ~air of lenses arranged as a ~'telescope." Tel~scopes were\)@~ mven~ed b! Gahleo and by Newton who u~e~ them to achieve angul~(}~~ aft~t\tjj magmficanon; the same arrangements are still in use and are named use)J~I their discoverers. To calculate the magnification of the beam we will only geometrical op~cs; this is suffi~ient for our ~sent ~onsiderationS;;ijjJ e~en though a Gaussian laser beam diverges due to diffraction effects (see:}]fa:f Fig. 4.6). ::::::::~:=W ~ ~ Figure 4. 1 shows the Newtonian (or astronomical) tele~cope consi;tin~/f of two focusmg lenses of focal length /1 and /2. As shown m the sketch th~/)~~ )<tifil lenses are converging (piano-convex), and the distance between them is ·. .· .·.·.·.~~ t =Ji+ h- (4.25) /1 . :::::::::ii the.\/il If a collimat~d ?ea~ of ~~eter d~ is incident from the left, parallel to \)f&]

telescope ruus, 1t will exit with a diameter dz, where .·.·.·.·.·,:-~ \flW (4 26) ·:-:-:-:-:-:-;.,.-:- • -:-:-:-:4:~~-:-: .·.·.-.-.~~ \/\@ .·.·.·.-.·.'.I'/.

By appropriate choice of f1, /2 we can 1nagnify or demagnify the beam. \\)@ The Galilean telescope is shown in Fig. 4.12; a diverging (plano-)/ /@ /1 f2·· \}t@.

concave) lens of focal length and a converging lens of focal length \\l~ are used. To preserve collimation the distance between the lenses must be !-f1-l I-- f2-: FIGURE 4.11 A Newtonian teJescope with magnification hi! 1 .

## 4.4 Measurement of the Transverse Beam Profile

! . .._ .. ._ ~f1-i t • FIGURE 4. I 2 A Galilean telescope with magnification hiJ i.

and the spatial magnification is given by = .

d2 d1 (4.28)

Ji The curved surface of the lens, whether convex or concave, is spherical., and the focal length is related to the radius of curvature, R, through the lens-makers equation. When the second surface is plane, (4.29)

where n is the index of refraction of the lens material. For most glasses used in lens manufacture and for visible light we can approximate n ~ 1.5, so that/,....., 2R.

In setting up a telescope certain "alignment tricks" are useful. The beam must pass through the center of both lenses. Thus the lenses must be set on the optical table at the same height as the laser. In the horizontal direction one can be helped by noting that a beam that is passing through a lens off center is steered. Furthermore, the surface of the lens must be perpendicular to the beam axis; this is most easily achieved by back-reflecting the beam.

The transmitted intensity of the beam is measured by a photodiode. (See

## Appendix E.) Since the photodiode area is small, it is often necessary to

focus the beam on it, especially if it has been expanded. The diode is backward biased, usually with a low-voltage battery as shown in Fig. 4.13.

With no incident light Ro is i¢inite. When light is incident some carriers are liberated and the resistance Ro of lhe diode decreases. Therefore the voltage across the load varies as (4.30)

:/It~ ::::::;::::;?

166 4 Lasers \:I!l.1 :\}!J$ Vs . ·::::::::::.~ ~i\II }:;:;:~~ }{t~ ··::::::::::~ t-------..

Vaut ·./ill Iii~ /J~i~1~ '. ·"·..-c--•-:-• . ·.,,:.:,:.;-;~ RL!:l/{1}$~ FIGURE 4.13 A pbotodiode reverse biased by a source VB and working into a load_ ' .::/ff~~ :-:-:-:-:-::m Telescope Focussing lens . ( } ~ Laser j ~ Photo dtod~ ::::::::::~ ,:\}::~ ·/ /}~ ·.]lj ..:r J~~WW: ":::?~:~~~)

:·' {··' ··•i""•'. ,/,,.- . ~- ~ ,•I,1 :)}\{@:!

Controller Detector )/jJ~; FIGURE 4.14 Arrangement for measuring the transverse profile of a laser beam. · ·/ii/{&1~ ::::f:\iJff At low light levels (i.e., where Ro is large) a digital voltmeter ( RL ~ )}I~ll 10 MQ) is adequate to read Yout-At high light levels the diode may become saturated, and it is desirable to use a shunt resistor; the signal can also be})?Jf~: o~:)i}{i~ viewed on an oscilloscope, but when fast response is desired, as in Fig. 4.1 a 50-0 impedance must be maintained throughout. When working at low\ }}~ }jjj~ light levels the photo~iode must be shield~d against roo~ ligh~. _ One way of measunng the beam profile 1s to record the mtens1ty received :}}if@ (i.e., the·)}}~ at the ,photodiode as a sharp edge a razor blade) is moved through beam. The blade is mounted on a translation stage that can be positioned/ )]~ in\Jt~ ~ith a resolution of few ~crom~ters. The atT~gement ~~ sket~hed ~ig. 4.14, and the recorded mtens1ty as a fun~tion o~ po~1tion gives the/ /)~ integral of the beam profile. If the beam profile 1n the direction of the blade/ :;::~:-~~ . .

··-::::::::;~ \::::~x~ ffiOtl.OD IS :'/}/&@ I (x) = Io g(x) (4.31) .;: i /: , ~~~ -:-:,:-:·.~~ - ·:, ::::::::;~ ··.·."~4.W Ill:

## 4.5 The Michelson Interferometer

~::::· ?i}.

r.·.·.

f\ (a) 1 (b} 1 • o.e ~:::::: 0.9 ..

~::::· r:-:-; 0.8 • 0.8 ;;::> : · . - - : : - .· - :- : . : · • , · . 5 ~ 0 0 . . 6 7 • • • ; , . ~ a . . ! , , i , i . ' 0 0. . 6 7 ff ~o.s • ·,i:?:- 0.5 :; . ; · : .· : • : j! o.• • :s 0.4 • ·:::::· E~ o. 3 • 0.3 -···· :;/~ 0.2 0.2 ~?-· 0.1 0.1 0 0 f:.• 0 S00 1000 1500 2000 2500 3000 3600 4000 0 500 1000 1500 2000 2500 3000 3500 4000 Poai1ioo {µm) Pos!t!Ol'I (µm)

~::: .

::::: FIGURE 4.15 (a) The transmitted intensity as a function of the position of !he obstacle {:: · (razor blade), which is moved across the beam. (b) The derivative of (a) gives the transverse <·=·· ·:::: profile of the beam imensicy. It is fitted by a Gaussian .

·.··..·· .

..: :::· ill:i . J:> with g(x)dx 1, the transmitted intensity when the blade is at (\: position x' is :::r ft = f •:.: G(x') lo lx g(x) dx (4.32)

::::· ~\: :;::: : (when the beam is fully unmasked, x' -+ -oo).

A typical result for the laser beam is shown in Fig. 4.15a where mea surements were taken every 100 µ,m. By differentiating G(x') we recover :•;.:•:.:· the intensity profile \: :::~ . - - d G(xI ) = / (x I ). (4.33)

r-.•.:· dx' •.•,• on Performing this operation the data of Fig. 4.15a we obtain the result i•r.•.· shown in Fig. 4.15b, which can be adequately fitted by a Gaussian. Toe •.•. l/e2 points of the Gaussian define the beam diameter, which in thls case ::::: .•.• = I} is 2w 1000 µ,m.

•·.· :::: :::: 4.5. THE WCHELSON INTERFEROMETER We are famHiar with the fact that wave phenomena exhibit interference; namely at every point io space the amplitudes of two waves are added linearly (they are superimposed), whereas the intensit)' is detennined _.\{{~ ..

-:-:-:-:-:-..

.. :::::;::::::. .

168 4 lasers ::: : : :::::::./'.

·:\{{~· ~plitud7. pJaJ!iJi)i by the square of the resul!ant For ioterfere~ce t~ take the two waves must retam the rr relative phase relationship over th¢.( I:j time and space of the observation: they must be coherent. Laser_b e~(Jf /~j are coherent in the plane normal to the direction of propagation \n1:f also over considerable length along the direction of propagation. Fori{\ ~]

instance, a simple HeNe laser has a coherence length .fc of order o~(Jj meters. It is therefore possible to demonstrate interference with relativef/ti .·,-.·.:,-~ ease. :\:iij ~~:f! tj The arrangem~nt of the Michelson inte:ferometer is sbo:'11 in Fi~. ~ .1 The HeNe beam 1s expanded (for converuence of observation) and ts-Inch/}~ ~~:(!@[ ?e~t from the left on the "_bean:-splitter~ B set at 45° with r~e~ to mc1dent beam. A beam-splitter ts a half-silvered glass plate o~ similar opti:\J ~ Ml)\:~i cal element that allows half of the beam to propagate through 1t towar:d tw~\li and reflec~s the other _half toward M2. This _techni~u~ ~f producin~ coherent light beams 1s referred to as "amplitude div1s1on." The mrrrors;:::}:~ MI and M2 reflect the corresponding beams that return to B. Half of the(] ~ beam returning from M 1 is transmitted through B, and the other half is.})@ reflected toward the screen; the same is true for the beam returning from\)fj M2. If Bis set exactly at 45° and Ml and M2 are exactly normal to the/J @ ·.·.;I'~.· beam direction, the two beams aniving at the screen are exactly parallel/ :=:::=~ ·Ii@~ and their amplitudes will be superimposed.

\\ ~ :11 M2 :?J ·.·.-.....

\J~·.; ::::::::~ :::::::;:j .·.·.·,.·~ ·,·.·.·.. · . .· ,::::::::~ .·.·.-..... ,, '\\~~~ ))~~t Laser ~ M1 .:::::::~ ::::~~~ <l~ .. ::::~~ ~:;:::::;: <::::~:: .·.-.~-.- /% Screen :::::::~: )j FIGURE 4.16 Outline of the Michelson interferometer. B is a beam splitter, M 1 and M2 are the mirrors in the two arms and the interference pattern is observed on the screen. }]

·-:-:-:~- 'ii ·,·.·-·.

::::B .: ::::~: -(~~~

## 4.5 The Michelson Interferometer

If the intensity on the beam splitter is /, the wave amplitude2 is Ao(z, t) Eo cos(a>t - k1,) (4.34)

(4.35)

·l :i( ';r,f :: We set z = 0 at the beam splitter, and the amplitude of the wave is reduced Ji.

1a'i.{·by each time it traverses (or is reflected from) the beam splitter. Thus ;m: the amplitudes coming from the two arms l and 2, when arriving at the ~:~-:· :<=:=--.screen, are Jt Eo ~:? A1 (Zs, t) 2 COS({t)t - 2kt1 - kes)

;r~··:·.

ill!l· ~:::· ~Ji e es where 1, e2, and are the distances from the beam splitter to Ml, M2, j/ :and the screen, resp~tively. Toe resuJtant amplitude at lhe screen is ,., ~t{ Eo :::::: As(Z: t) = - [cos(wt - 2ke1 - kes) + cos(wr - 2kl.2 - ke ~=f: 8, 5)]

i.:\ = Eocos[a,t - k(i1 + e2 + es)Jcos[k(f1 - e2)J, .·:::: ~::: (4.36)

~:r::::::- ·-···· and the resultant intensity (4.37)

lo Eqs. (435) and (4.37) we used the fact that (cos 2 (wt)) ½- Note that the light reflected toward the source also fonns an interference pauern of intensity (4.38)

·::::·-: ~:::.

ff so that %;:: ?:,:• ~r ~::::= ::::::=· It is much more difficult to observe lb than / [} 5• t::=:: .,L::: 2 ln I.his section we use trigonometric rather than exponentfal notation .

~:=:· ~f:: ~\ ~::.

~~==·· ~:: ~¾~:=:·: -):):~:~r ::::::=:===~ :·\:::::;:: 170 4 Lasers :::::::::;.

:::;:~::=~=~ -::;:;:;:;:;..-; From the above analysis we conclude that the intensity at the screen will!{}} vary as cos 2 [k(t 1 - £ 2)]. Since k = 2Jr: Ji.., it follows that when ·{}J~ .::;:;:;:;:;:~ :::::::::::=~ n 0, l, 2 .. . , (4 .39),:}}~~ .·)/)~ )!!Iii~ the screen will be bright (bright field), and when 1)

" ... -({q,.

( J.. .)}:;:;j Ill= 1.e1 - £21 = n · n = 0, 1, 2, ... , (4.40).{}t; 2 2 ::::/:~~ \?::%!~ ~~i}J~ffi it should be completely dark (dark field). For intermediate values of Th~}J§m the screen will be partially illuminated as indicated by Eq. (4.37): very tc(fj?~ idea~z:d situa?on descri~ed by. Eq~. ( 4.39) and (4 .4?) is difficult obtam m practice: very slight llllsalignment of the mirrors and even srnaoJ:flj:}\Ii I@ air currents are sufficient. to change the relative pha~e of different p~ the wavefront. Imperfections or nonflatness of the IIllrrors or beam-splitt~~\}~ at the level of a fraction of a wavelength distort the wavefront and modify/ }~~ the interference pattern. ··)/j~§i Nonp~allelism between the mirrors Ml and M2 give~ rise to "inter{/~ soJfi]

ference fnnges" at the screen. We assume that the two tmrrors are set ~at their normals ~e ~ th~ plane of incidence (~e pla~e of the pap~r in)/@~ :?=~==i Fig. 4.17), but M2 1s misaligned by an angle a w1tj:1 respect to the axis of: the beam as shown. B·ecause the rays returning from M 1 are reflected by·? }~© 90° at B, we can think of M 1 as located at Ml', and that the reflected rays {}@ J~ propagate in exact parallelism with the z axis. The z axis is defined from) / the screen toward M2 and the x axis is in the direction of the screen as\}/~ indicated in the figure. For a small misalignment angle a, a well-collimated.\{}!

::/Ji beam, and for l2, -ls sufficiently large we need consider only rays from M2 011,)ii/t~ that propagate parallel to the Z axis. Then the rays reaching the point X }:}/j the screen have traversed path lengths }\1J = + Zl U 1 ls t@m = + Z2 2(£2 x tan a)+ is, (4.41) :::::::~;:: .J I and their path difference is (4 .42),:::::::-:~~ //}t Bright fringes perpendicular to the plane of incidence will appear on the:\ /~:~ = }!Ji screen when (z 1 - z2) n).. Consequently, the fiinges are separated on ':::::::~;~ . .. \ )~?.~; i/i

## 4.5 The Michelson Interferometer

M2 - - M1' Zi z, ls l l l 0 X FIGURE 4.17 Schematic of the Michelson interferometer with one mirror slightly mis aligned. To calculate the interference pau.em Ml can be relocated al the dotted line M 11 • Vertical (to the plane of the paper) fringes appear on the screen separated by l:u = A/(2 tan er).

the screen by a distance = --- 6.JC (4.43)

2t:ana = = For example, for the HeNe, >.. 633 run and if we cake ct l 0-4 , we find tu ::::: 3 mm. As lhe angle a is increased the fringes crowd together and eventually the interference pattern is lost In the previous discussion we have implicitly assumed that the expanded HeNe was collimated; for a ooncollimated beam lhe fringes form a circular pattern. Some residual curvarure is observed even with a collimated beam when the interferometer is not perfectly aligned or when the optics have aberrations.

In the laboratory we set up the mi.Tror MI on a translation stage (the same as used for the beam profile measurements). The mirrors are carefully aligned until an interference pattern is achieved. When the translation stage .·.·.·,,:.-.-~ ):~:~=~=~~ .·.·.~.·.·. .· \/}~ 172 4 La Se rs ·'<·:-:•:•:. .

-:-:·:•:-:• =)..J~lii!l~ is moved. the interference pattern changes: for a stage motion l:;.z ?i reapf bright fringes become dark and vice versa, and the original pattern Ji pears for ~z = J.. /2. When the motion is continuous the fringe patte1jf JI appears to "walk'? across the screen and one can count how many fring~f measm'.~f]i have passed by, for a given amount of motion. It is convenient to ~z for rv25 fringes at a time; this corresponds to motion of ""'8 µ,m, wbicb.:::\~ T~~{ll can be adeq~a~ely re~olved by ~e counter on the translation stage.

wavelength 1s 1nunediately obtained from .}}{~ .···:•:•:.:,;·~ ).. = 2(~z/ N), (4.44f}~ ~j/l where 8z is the motion of the stage and N the number of fringes passed by. -:::::::l® !JI 4.6. THE FABRY-PEROT INTERFEROMETER /:::=:;:::W, /ii In the Michelson interferometer, two coherent waves were made to intx:~ffi (~(~I f ere. In. the _arrangement introduced by Fabry a~d Perot a very large theory mfimte) number of waves are made to mterfere. Because of tl#:(:):1 p~cipation of m8:11y waves, :ery sh~ contrast between bright and ~~~I~i fringes can be obtamed and this results m excellent wavelength resolutioP!.;j{:}j o#}}fil: The Fabry-Perot consists of two mirrors, often parallel plates coated 1!

their inner sudace to have good reflectivity at the wavelength of interesij)f The spacing, t, between the plates is maintained by precision space~,( )@ forming an assembly referred to sometimes as an etawn. This is sbo~{{:~4 jjjfJ sc~ema.tically ~ Fig. 4. ~8, w~ere for simplicity w_e have shown the plat~f as mfinitely thin. A ray mcorrung at an angle 0 with respect to the norm.alt:::::=:f ray~/)JJ after traversing plate 1 will undergo repeated reflections. We label the emerging from plate 2 by AB, CD, EF, etc. The path difference between{/$ )\t@ two adjacent rays, say AB and CD, is :::::;:;:;:Z,:}.

~l =BC+ CK }?:ti .:::::):=& m~}1~ with BK normal to CD. The finite thickness of the plate does not J{i~ the above relation. It follows that .

= 45<jffe ~£ 2t cos 0. (4 • ·:.:{::(:::-::-::·=:/~[ Note that CK = BCcos20 and BCcos0 = t; thus, ~e = BC(l 4\){~ cos 20) 2B C cos2 0 = 2t cos 0. Therefore, constructive interferenc:~\{~~j ::= }ti ......... :-: -:.:-:•:-.-::;; .: -:-:-:-;::::=: /@~~ ;::::: :=?-:-:-: :::::::-

## 4.6 The Fabry-Perot Interferometer

']

.r:•:•: ~:::::: . ·.

~::;/.

ij/? - .... - ~ :::<; :=?-?:> Ill ....

;.: ~:;.:-:- - :;:~:} : - ~?> ~:::::·· z.r.·.

:f.::::: X··.· ~f:.

~{ : .I'.·.·.· ,~,, . .:,...: ·,·.· f~:t::: : 1 2 .....- t _.,..

[{ / FIGURE 4.18 The Fabry-Perot interferometer. A ray incident at an angle 0 is shown.

~~/ For simplicity the mirrors are indicated as infinitely thin. Note that an infinite number of ~{ :·reflections contribute to the transmitted intensity at angle 0. ..

~:-:-:• [ > @{ will occur when the path difference is a multiple of a wavelength ~=::::.: ~-·-·.· = z=:=:· 2t cos Bn nA. (4.46)

[ /· re.

Since 0n is a small angle, n is a large number of order n. ~ 2t / A.

~:::::. The above constructive interference condition holds provided the dis- t;,:. .r.. ·. an tance form the etalon to the point of observation is the same for rays, f / name1y when the observation point is at infinity. To achieve this we use a t/ lens to focus the rays emerging from the etalon onto a screen. For a slightly ( { diverging incident beam one observes a set of rings of radius ?:::::< I'. .• ••• = [( rn f ran 0n ~ f0n , (4.47)

tr. ...r. ·.· rt: where 0n is determined by Eq. (4.46) and f is the focal length of the lens.

f{ Note that the incident beam should not be perfectly collimated but should f ( contain enough angular divergence to support the angles Bn.

rt To obtain the spacing between consecutive maxima (fringes) we first [ \ note that for 0 0, the path difference between adjacent beams, [ \ measured in wavelengths, is ;.:,-;.·, [( no= 2tj).., (4.48)

~=~:.: ~--·.

~:: ;.::· t( I',·.·.

?-:=> ~:::: ~-:-: ::;?::: ::);~:~:i~ .· .·.· .. · .. · . .

-:-:-:•:•;-"' ::=:::::::~= 174 4 Lasers .·,·.·.·.·.•;', .:::::::::::.. : :.·::.·:.:·:.:·:.:·:;4--~ which in general is not an integer. The first observable ring is formed at ~n(}f _J(:/:\1~ angle 01 where n1 is the integer closest to (smaller than) no. Thus __ _ . }}tlw.

n1 no - E ......., .

\:::}::.~ ://:~, and -::::::::::;.ffi 2(~) I :-:-:-:-:-:-~ U = -~.

€ ::::: - (1 - COS 01) Sill - . (4.49)%1 A A 2 ·?Ill .-::::::::~:::.~.:3 As we move out from the center, the ptb ring corresponds to . ·:::'.:;:;:;~!m :::::::~;~ ·.·.·.·.•,•/~~ np (no - )€ - ( p - 1). (4.50):}j~~i@ ......

.•:•:•:--~~.,~~ ~ ~sing~- (4.50) in Eq. (4.46), recalling ~e defi~ition of Eq. (4.48), drop·<{/t~ pmg f with respect to ( p - l) and replacmg 2 sm 2 (0 /2) by 0 2 /2 we find() ~ .~ that th~ angle of the pth ring is ----- _ J A ·-:-:-:-:-:~ 0p ~ (p - 1) -, (4.51).)]~ t '})~~ -:>;:::::~-~ applicable for moderately large va]ues of p, p 2: 5. As an example, if)/{ft t = 1 cm and A = 633 nm we have "A/ t ~ 6.3 x 10- 5 and the p = 11 ring:;~j~j\l will ap~e~ at 0 = 25 x 10- 3 rads; for a lens with focal length f = 40 emf/JI -<::::::::~ the radius 1s 1 cm.

Next we calculate the intensity of the rings (fringes) and the contras{!l l between bright and dark fringes. We designate by T the power transmission:)/t\mI coefficient of the inner surfaces of the etal~n: For simplicit~ we also as~ume\f that both surfaces have the same transrmss1on and reflection coefficients.·:·}}~~;.~; The power reflection coefficient is R, so that in the absence of absorption :}!I{IJi + r" = R 1. ; }:/:I The amplitude transmission and reflection coefficients are designated by t = -v r ;; i ; T and r - - -v r ; l :; ( R . _._ ·- : : : - - : } : : - ::: : / : - ~ & : :m ·w We also designate the incident intensity by Io and the amplitude by Ao~)\J ~ \fj~ where lo = ½A J. The transmitted ray B will have amplitude ·-:_-:-:-~~~ .·.·.·•·r~ A A t2ei<I> (4.52) ··/ }~~ B O , .......; ,_::,:1- :-:·:-.-~ <::::::~~ ,·,:-:-.,..,:..~ .. .:-:-:~·~.

,',:,:-.-~ .) !]ii . ::::::::=x: ::::::~:,:~ ~:::: ~l

## 4.6 The Fabry-Perot Interferometer

~ \ ~ft ~j{- where</> is a phase acquired in traversing both plates and the space between t f · them. Ray D will have amplitude ~;\;· i 'U itr Av= Asr e' . (4.53)

~::;:: ~-:-:- f t ray F ~;:::::· ~?:. AF A ,2e120 (4.53')

9.-:-:- D • :=:~::,., • tf?

and so oo. Here the phase angle 28 is due to the path difference of adjacent ~f: rays as they travel between the plates. It follows from Eq. (4.45) that f =: tf ,,r,... ' ,t H .() 27 T - 2f C -l O S 0 . ( 4 •5 4 )

t~~~f f::( · From Eqs. (4.53) we see that the amplitude of successive rays decreases ff: _ 2 = by r R: but ~ere_i s an infirute number of such rays. The amplitude of i;:::::: the transmitted light 1s ~\ ~:::. L00 = 2 [t + -~:-::-:::•: : AT Aot ei<I> r2q elqU]. (4.55)

i-':~·:. q=I t:,.-:•; This geometric series can be easily summed AT = Aot 2 e i </> I ,u , 1 - r2 e and the transmitted intensity ~::::: f{ Ir = ~ 1Arl2 = lio . (4.56)

=f\ 2 ( l - R)2 + 4R sin2 8 ~!!{ Max.ima occur when o is an integral multiple of 1t, whereas minima occur ?\ o when is a balf-iotegral multiple of ,r. At tbe maxima •:-:-: ;;.:- T2 -~::-=:-:=:-· T = 10 ~:::: Ir (1 _ R) . (4.57)

ii: t~)

min::B)

We ,~ fiat in me •:nre _of_;_o:_s:_rp-tioo ~r ( lo At me + + ~} - (1 R)2 - (1 R)2' ¼··· {r showing that very good contrast can be achieved if R is close to 1.

ff Equation (4 .56) is plotted in Fig. 4.19 for different values of R.

if ~t: -~.

~::::: , ...

~:=: ~J,. =.:.

::::::::~ 176 4 Lasers -~~ ..Q...)

C. }::::;~~ '·.< ·:-::1-;-~aa ·-:-:.:-:{-.~ ·><® <::::::::J 0 0.2 0.4 0.6 0.8 1 Fraction of an order / ;:::~~ <:::\{~ FIGURE 4.19 The width of the Fabry-Perot fringes as a function of mirror reflectivity/ ...

....

@, .. .. .

= \/~i The two peaks are separated in frequency by 1 FSR c /2r.

. ::::::~;.~ )}~ :\JJ The bright fringe will reach half its peak intensity when Iii .-.-~~,,,~,, ::::~½ 2 = 2 4R sin (0112} (1- R} • or when r (1 - R) ·::=::::z = \?~ Vl/2 In , ( 4.59)

2v 1t -:-:-:.;~ {}~ where the small angle approximation was used. The full-width at half- )}~ maximum CFWl™) of the fringe is 28112- The spacing between adjacent })t :(J fringes corresponds to a phase angle difference of 2rr, and we define the /J~ finesse of the Fabry-Perot interferometer as the ratio between fringe spacing· and the HWHM of the fringe }\ ·,:-: ..: --: .·.·-~:- v'R. ·}(:~: 2rr rr = --.

F;:: - (4.60) :?:~ fJJ J'' 1 - R -::::::: - ·\:;1 = = For a typical reflectivity R 0.98, the finesse is F 155. : )} The spacing between bright fringes defines the free spectral range of ·:/'. j"J /J the interferometer. Let the wavelength At form its pth ring at angle 8, and wavelength A2 fonn its ( p - 1) ring at the same angle. Since these two-:!} rings overlap, \} ·.·.-':· ·:,:·:.:·J;: or •.•..•.•., , I . ·.•.· .-:-:--: .;,:.; . ·.·; . :::;: .·.·.t :::i ·.·•· }~ . \~~ ,;;z--·. .

~~~*?

,n .•.·.

## 4.6 The Fabry-Perot Interferometer

~j(::: ~t:=: .

~f(Howcver, n>.. L "' n>..2 "' 2t, so we obtain that ~:i:;:;:-: = .\.

:¢~:;::: >..2 - .\.1 /2t. (4.61)

~!-:.> .

tx:=f::f::.

lf we express Eq. (4.61) in terms of frequency, v c/J... we find that W)".'./.·.·:,· ~?: = -C .

VJ - \J;i [f:· 2, ~mt ~amely overlapping ring$ correspond to the free spectral rahge already = = ~ { introduced io Eq. (4.12). For instance for >.. 633 om and t I cm the ~f/ = 2 = wavelength spacing is J),_ J... /2r 0.02 nm. However, lines between f..f.

,:.,: ' fring~ c~ be ~olved if they do not e~actly overlap and this depends on ~ff the line width, 1.e., the finesse of the instrument. Thus, the wavelength ~tr resolution is given by :;;z-:,: ::£::~::;. 1 1 J...2 = - = - -.

~{ { . d).. (l2 - >..1) (4.62)

~- F F~ tff For the above example and for F 155, d)../'A. ,.,_, 2 x 10-7, showing ~\} ·that extremely high resolution can be achieved with a relatively simple :::z:::·:.:·.::· · ap p ar a t !/:: rr Fabry-Perot etalons used in conjunction with lasers are frequently made with two focusing mirrors rather than flat plates. This facilitates the align ~?::• ment but fixes the free spectral range. They serve as high-resolution filters }!\ to select specific waveJeogrhs and as opticaJ "specllUm analyzers," which ...

t:,, r are in essence high-resolution scanning spectrometers.

i1: ,.·.·.· fJ~W ~::/.

t~:): ~?: ~:::::· ~{~.

t:=}:.

:. I ,:' . /:.;. . ·: :.:· ·, X·>: i~lt ==~:-:;· « -:-: II

## CHAPTER

#::;::· ~!~\ if::::· m==:==· Optics Experiments tf::::' ;:,ff: .<'"X·:·:· 1l •:~:::: -~{/· ~:t~\ .

-f:::.:·· "~::::::.: ~f:: 1ff: ..· •·.·.·.

~lllt ,. ..

tt.

j·:::::: #??

11>· 1{( ~t> .........

~ri,.

~f\·s.1.

## INTRODUCTION

~i::::{ fjf/ r11e wide use of lasers in so many applications hac; increased the need f.tt\ for high-quality optics and for good optical designs. We address some of o!

~}) bes~ ques_tioos in _this chap~er ~here we discuss the di~rac_tion light and ~:;:;:::,"rotation of the optical polanzat10n, as well as propagation m optical fibers.

½f{· When a collimated beam of light passes through an aperture, or if it ~{}encounters an obstacle, it spreads out and the resulting pattern contains ~/ '!)right and dark regions. This effect is called diffraction, and is charac ~ f ~.ristic of all wave ph~nomena. It can be understood b~ considering ~e D~::=:)nterference between different parts of the wavefront, which was altered rn ~)j,assiog through the aperture. The angle of diffraction is of order )..jd with lf.>..

the wavelength and d the dimension of the aperture. Thus, for visible :-:J)i_ght, apertures in the rarige 10-100 µ,m produce easily resolved diffraction .:,·.·.· ;.-;::=::patterns.

:t1 1il[J; ::::::;:::~ \WI~ }\{?

180 5 Optics Experiments ·.

:: : : : :: : :;:::::• rii/fJ{ Very different patterns are formed near and far from the aperture.

the near field we speak of Fresnel diffraction, and to observe the pattewi:i.i(tltJ J • it is convenient to form an image of it on a screen. In the far field obtain the Fraunhofer diffraction pattern, which can be observed by simptjf t~ l~nff ~ placing a screen at some distance from t_he ape1ture; more precisely a should be_used and ~e pattern observed_ m the_ focal plane. ~n the foll_owin~J i crrc~~\i1· three sectlons we discuss Fraunhofer ~iffrac~on from a sht and a <:}:~::- aperture. The results shown were obta1ned with a CCD camera.

in}i;.:$: The diffraction grating was already introduced in Chapter 1.

t~~~jJfi,

## Section 5.5_we ~~~ve the gr~ting equation and show a modem setup

can be readily digitized; also included are results on the Hg spectrum. N:~:~,ti~ we introduce the concept of "spatial frequency" components in a beani &lf~~;~ light. This allows us to manipulate an image by imposing suitable spatial W:Wii ters, in the focal plane, a procedure also referred to as "Fourier optics."

have kept the mathematics simple and emphasized the physical principlef: ~:, inst ea~. In Sectio~ 5 ._? we d~scuss the Farad~y effect, ~am~ly the rot~ti?,j{[J ~f@1 of the linear polanzatJ.on of light when traversmg a medium unmersed m ~al.magne~c field. The power o~the.lock-in detecti~n technique is.evide~ti{i m this experiment. The last secuon 1s a demonstration and measureme~t il of "Ben?''s pha~e." ~sis the rotati?n of pol~zation ~ue to a topologic~)J~ change m the direction of propagation of the light. It 1s demonstrated bj'/}~ injecting the light in an optical fiber that is wound as a helix. ··(?~ :\:;:::&f.

\it~; >Wt~ 5.2. DIFFRACTION FROM A SLIT · -:-:-:•:·.~ 4.]~ w~~ We can find th~ ~a of the. diffraction pattern the. hel~ o~ sketches_ show_n 1n F~g. 5.1. Co~s1d_er a plane wave of v1s1ble light 1nc1dei~l/ ~ on a v~rttcal s~t ~f width d. The mc~dent "rays" are nonnal to the scre:n.th~t}~ contains the slit; 1.e., the wavefront 1s parallel to the screen. We can 4•div1d~~\:~:ffi = = the slit in half (i.e., AB BC d/2) and consider the rays I an1da~t(J~J~ emerging at an angle 0 with respect to the direction ofi ncidence (Fig. 5.

~f&~ = = The path di~erence be:tween these rays is Bf! AB sin 0 (d(2) sin If the p~th _difference 1s J.../~, then at large dzs:anc~s from the slit, raysJ)~ and 2 will mterfere destructively. However, this will also happen d f ir o e r c rtai~y~~m/;~~ 1' and 2', 1" and 2", and so on, so that there will be no light in the <<im 01, where d J... ·.:::::::::~ = - . .c s)jji - sin 01 2 2 ))t~ ·.-:-:-:-9'& .::::Jj .j~ :{:~~~ :~::·, :-:-· :~:-:•' :~~~~~- 5.2 Diffraction from a Slit 181 xi!l( !:.

--~~~ -;,:-:- 0l; ; . , . ~ . ; : . -t : : , .; · - . · - d '- - - - -- ~ -- 7~~~~~~ 2 4 2' •:::::: J.-------"-=--.....L...--'---- :-f\.:: C C /,·.·.· ..

"·:-:-:-:-. (a) (b)

~~[kGURE 5.1 Finding the minima of a. diffraction pattern (a) the slit of width dis "divided"

t:7:w half and (b) into quarters. The rays are focused at infinity and the path difference is •} . .. ·.·\· -:-:?indicated .

..• :-:-:-..

}\\ f.... 4i•,·n.·.

contrast, at 0 0 the path length (out to a large distance) of all rays is {}qual and the resultant amplitude is maximal.

I)( '· To find the next zero, let us "divide" the slit into quarters as shown in { /fig. 5.lb. In this case ray I will interfere destructively with ray 3 when f (E. F = AE sin 0 = (d/4) sin 8 = 1/2. However, ray 2 also will interfere {/destructively with ray 4 and similarly for all intem1ediate rays. Thus there {(~-ill be no light in the direction 02, where ~If d )..

= -.

- sin02 (5.2)

4 2 ~}f1,bis argument can be continued by subdividing the slit _into ao (integral)

i}=)lllmber of smaller and smaller segment.s. By analogy with Eqs. (5.1) and ~1:lf we find the g;:::~zed ::,essioonfor ;. ~~e 2 ~~~ .2) (S. )

I/tor sin small angles 0 ~ 0 and =~?>: ).

if{ . 0n = n d' n = 1,2, 3,... . (5.4)

jf( .

The complete expression for the intensity distribution of the diffracted ~:{~ght is derived in the next section. It is ·\:( 2 {/. /(O)=lo[sin(~sin0)]

(5.5)

.·.·.·.· '!!. S10 0 ~:\/ l ..,.~ -.' ..

~=~=~=( ~-=<· .J.f( .,..· _.·.._.·, :Y.•:-:,:, )Ill 1~ 5 Optics Experiments foJ.ii)Jj where Io is the intensity (into a small angular interval d0) in the = i#i/@w wa_rd_direction (8 0). Intensity is the energy traversing unit area ~j }~ = = urut ume I= ISi IE x HI ceolE\2, (5 ·:-tit~ an~!i/Im where E, H are the ~lectric and ma~ne~c fields of the light wave, ,i~\~=i we usually take the time average, which 1ntroduces a further factor of Equation (5.~) h~s zeros in agreement with Eq. (5.3); maxima occur (to_fjj~ good approx1mauon) when <:=:::::>}]

<Mj = (5:?fJ~ m 1, 2, 3, ....

\\:i~ The intensity at the secondary maxima decreases as m increas~i(J~ Equation (5.5) is of the general form · }\}~ :~.?iJJ~ • 2 _ s1n x (s.iflt~ f( )

X - 2 ' X ·)!{:}~ }ifl which is graphed in Fig. 5.2. Note that as x -* 0, f (x) -* 1. )}~{~ iiI~ .. ·.·.·.-.-~ \it~ )({:~ II ___, ,.....::::=::::::-..,,,e:::.;___:::..~--+--~a,,-=:::,___:::,,...,..::::::;;;_.:;:::,,._ _____ ./ .· ii -Wd -'Aid 0 ).Jd 2")..fd 3>Jd sin o.:::::;:;;.o,:: FIGURE 5.2 Plot of the Fraunhofer diffraction pattern sin2 x/x 2 • . :;::::::-~ <ii .\::;~:;~~ ]fl: •r.· ..

:t:=:::· :&::/ 5.2 Diffraction from a Slit 183 ~-:-: x:-:-: ~=::::: ~--:-:.•• 1-- ~ --··· f-- ~:=::::· lf:-:· ,:;;-:,.. . _.

~~It

## LASER

~~:::=-::-:::: .

~:::::. T s L ~=:::: ~::;::;.· FIGURE 5.3 Schematic of a simple layout to observe Fraonhofer diffraction.

~::::: ~:=:=:- r.•.·.·.· ~=:::::= .

r,.:::::: ~:::::: i~~/ The experimental setup is shown in Fig. 5.3. The Jaser beam is expanded if \in a 4: 1 telescope T, to better approximate a plane wave and is then incident ij\(on the slit D. TI1e diffraction pattern is observed on the screen S, which is lf }in the focal plane of the lens L. Thus, we observe the image of the pattern f~{fonned at infinity. The slit width was d 200 µm and the focal length ~f(j = 50 cm, so that the first minimum appears at a distance x from the t::f: ,~:::· principal maximum ~;:::::: = = = ~[\ x f0 ,_.., f sin0 f(>-/d) 1.68 mm, ~:-:-:-:- ~---·.·.· = .

[~!}~?ere we used >- 633 nm. _A p~cture of the diffraction pattern taken [myw1th a CCD camera 1s shown m Fig. 5.4. The central spot saturates the i¾t::::r::c amera.

Instead of using a slit, we can observe the same diffraction pattern by if )'lacing a thin wire of width d in the path of the beam. Since it is easier to @-:-:-:-: r~-·:--:·.-·.:-·.

~:::::::.

.·.·.·.·.

m~==:::::- .. ,.,.. ... ·.

J'".";'.·,· ~=~:~\.

-:-:-:-· /:. . :-: :-:-:,:, •:-:-:-· •·::: :::;:,· ..: -:-:-· ..

..• :::::: ··::::::-.

... : .: : - ; : : - : : : - : : , - , :- . .

;.::::::::. .

·:::::::::: {ijoURE 5.4 Diffraction pattern from a thin slit observed in the focal plane obtained with :fi cco camera.

..; ~::: ..- -:-:-> .~:;:: .-;;. .: -:, J:.:-: ~i;:: ,.•..J-·..··. .

%·:· t:::: :--.-:-· ~~:i: ::::-::-:::-::;-::;·=:a1a )li//if 1M 5 Optics Experiments ·. .

obtain thin wires (or hairs) than to manufacture thin slits, the former .ar~}@~ eq~~!{J]

often used for demonstrating diffraction. That the two patterns are rJ.{?}j valent (except in the forward direction) is known as Babine!'s principle_.

illustrate the principle we assume that the incident plane wave is ''unifor#i/J~ and infinite" in extent in the x direction. Thus, the amplitude of the wav~{/j is independent of x, A (x) A. Immediately after the slit, the amplitug~\)j ?\:/~ B is given by .:1 B(x) A -d/2 < < d/2 .· :::-:-:-:-;;:-/.

(5.9}.t~:~ :)i!fJfl~ B(x) 0 lxl > d/2.

'tlii{Jij In the presence of the obstacle the amplitude C of the wave, just past . . b ·.·.·.·-~--~ ob stac1 e , 1s given y .:\:::;J::_x; . </lfi C(x) 0 -d/2 < X < d/2 ._·:}}1~ {~.lQ)\:~ C(x) = A lxl > d/2. . .·. ·.·.---~m ..} :::}.:@ . ":::}1;~ Combining Eqs. (5.9) and (5.10) we can write ??}~ ...: :::::~~~ (5.11l//i~ C(x) A - B(x) (valid for all x).

·}i/=}m We know that when the amplitude is constant for all x, the wave propagate~/\~ only in the 0 0 direction. Thus for angles 0 # 0, the constant amplitnd~)Jj ·/\JW.

does not contribute, and Eq. (5.11) becomes .. )JJ@ C(x) -B(x) (valid for 0 # 0). (5.12}.i:::::?-;;~ ··trii It follows that the diffraction pattern, which is proportional to the squai~!\:l {/i~ of the amplitude i;i/ill 2 = 2 IC(x)l IB(x)l , : /1j clirectigf is the same in both cases. Equation (5 .5) remains valid but with the = :)JJ 0 0 excluded.

f?]

Another case of interest arises when instead of a slit a square apertuf t~~t{@.

is used. The result is shown in Fig. 5.5 and consists, primarily, of single-slit diffraction patterns along the x and y directions. The intensi~j~ of the maxima in directions differing from the x or y axes decreases vefyj~ "dl . :-:-:•:/,~ rap1 y. }}~~ 1::1 -/ ::::~ '()~ •-=::> .·.·· /:::::· ~/[:

## 5.3 Calculation of the Diffraction Pattern

V...; :::; .

;,:._ ...: -:-; Ii ~I~\ :=-::::- -:-:• ...· :-;., -::::.

~rr ~:::= ~=:::: • ;~:::: ,.::::::: ~~;::: ~;:::::· :~~\ ..

~::;;: ~::::· .

; ......

%.?

~~::::· 6 ~.,-::,-::- : ~t:=::::- :~ii FIGURE 5.5 Diffractioo from a square aperture.

~·t:: %·:-:•: =~if s.3. nm

## CALCULATION OF DIFFRACTION

tf! , ....• •• •• PATTERN ¾:::::-: ,.·.·.· tfi:; Jf}:ro obtain an expression for the diffraction pattern formed by an aperture, it/ we will make use of the Huygens-Fresnel principle. The principle states ~\)hat every point on !he aperture D is a source of spherical wavelets with ~}\amplitude and phase detennined by the incident wave. The.~ "secondary"

~?/wavelets propagate at all angles and interfere at every point in the obscrva ~})ion plane to detennine the diffracted wave amplicude. We take the incident ~}{wavefront parallel to the aperture plane, whereas the observation plane is : /Jocated at infinity (Fraunbofer diffraction). This is approximated in the ~}~etch of Fig. 5.6 where we show both the aperture and observation planes \jmd two typical rays to the observation point P'. We need be concerned if~ly M with the transverse coordinates. In the aperture plane, the point ~:4~specified by the coordinates {, 7/, whereas in the observation plane, the ~Jbint P' is specified by x'. y'.

~\:· Because we observe at infinity, R, the distance from O to the observation %•Z¢·· mt is very large (and equals OS') as compared to the dimensions of the .~)!pertu.re; therefore, rays OP' and MP' are to be considered as parallel.

·~ 1,?ben the path difference between the ray OP' (from the coordinate origin tiW P') and the ray MP' (from the source point to P') is the length OB ~~:;:- :ft ...: •:<· ~:=:~:: ;• §i J!i/r 186 5 Optics Experiments f/ .·.-.·.··===~ .-:,:,:.;-~~ ill ' }![if[!

.·.·.·.-....* ~ x' FIGURE 5.6 diffraction. .. .... ·,· r,;z,_ !!i~t vec~[II where MB is perpendicular to OP'. If we designate by q the unit along the ray OP' we obtain for OB ·-·:.}·.}·.·:-~~W J :-?}JI i~{i~ (5 · ?t:=~w.2.

.·.·.·.·.·.·@ The direction cosines of the vector OP' are )1111 = = (x'/ R) u and (y' /R) V -)if}=ft prnMJ~ ~d are well defined whether R_ is finite or tends to infinity. The difference between the two rays 1s :\:::::::=·Jj= -:-:-:-:-:•:•/~ :.:-:-:-:-:-:•% 2n .-:::::::::::~i cs ·.stft]~ ~<p [ ] 14r==-=1-/.X = T + ?;u 1JV .

Without loss of gener'.'1ity we set the ~efe~ence phase of the ra~ 0 P' e~@~j -t~M~Ji to O; _we can then wnte f?r the _contnbut:J.on of the source pomt M to ./i}}§i amplitude at the observation point P' ···:::::::::)~ (5;·1$fl~ ·{iii/!& For simplicity we dropped the time-dependence e-iwr; d{drJ is ·Ul.¢=~~:.§: . ·-:-:-:-:,·,.~:--...

differential element of the aperture at the point M. ·:}!:Jm ·}!{lg ))if1 :-:-:-;,;:~ ':!!}ii ,.JI:

## 5.3 Ca Ic ulotloo of the Dl tt,aotl'" Patlern

:\ To obtain the amplitude at the point P' we must integrate the contribution source points. the ; \· from all If amplitude and phase of the incident wave are / : constant over the aperture, we directly inlegrate Eq. (5.15). For the case of »:.t·.· a square aperture with dimensions 2to and 2T10 the integral is elementary, i{= :;::: ;(~~ A'(x', y') = T/0 fo e1.2T,rl fu+1111ld{d11 ~f: ..

->70 -{o tF 4{0110 (5.16)

~~{ ::§:~:: i \ 'fhe intensity is given by the square of the amplitude ; m:· [sinr'f :;;.::;:;:: ~i~? = l6{J11i {ou)]2 [-sin____;.f_2::_11ov....;...)] 2 J(x',y')

:;::::: (5.17)

:f:: y{ou TT/OV 4'~;::: ;J and is proportional to the square of the illuminated (aperture) area. This is ,;f typical of diffraction phenomena. as compared to incoherent illumination, V. .• { i which is simply proportional to the area.

f/ >> 1n the case of a long vertical. slit, 110 {o, the intensity varushes very -r: rapidly for u # 0. (Note that r,v becomes large and the exponential in :J;_pq.

(5.15) oscillates rapidly, its average value tending to zero.) Thus we ~f observe a horizontal. diffraction pattern confined to the x' axis, as shown if = in Fig. 5.4. Exactly on the x' axis, u 0 and Eq. (5.17) reduces to 'f {ou) ] 2 [sin ("/ sine) ]

= sin ( J (x'. y' = 0) l6{J115 = Jo ,r: 2,r [ T{OU sin 0 (5.18)

,-:":;'.;: = = ~t)n the last step we made use of the relations u x' / R sin 0 (valid for ~(IJ' = = 0), where 0 is the angle from the z axis and {o d /2; we also set ~lft6{J115 = = lo to represent the inceosity at 0 0. Note that the above result ~f~s exactly that given in Bq. (5.5).

v.~fj We now consider the case where the amplitude of the incident wave is 110L ~f:constant over the aperture. Such variation can be introduced deliberately by ~r placiog a suitable mask over the aperture, or because tbe incident wave is :-:-: ~ti ?} ,;z.•;__._ V,•:• / 1111 1~ 5 Optics Experiments ·.

modulated in magnitude and/or phase. In this case we express the ampli~~(}I on the aperture by . · :-:-:-:-:-:1 : ..: \\t~ ·}\!/~ F(~, r1), .

.· :-::::::::::=:@ fonn::/:!::lm~ and the amplitude at the observation point P' (Eq. (5.16)) takes the (5.1;-~:-:/-=:-I=-~}I =ff A'(x', y') F(I;, 11)ei?f(1;u+qv)d{d1J.

The integration in ~q. (5.19) is ov~r the aperture; however, since the ampli/j§@ tude of the transm.itted wave vamshes beyond the aperture boundary, ~~}~~ can extend the integration limits to infinity. With this modification, we s~~\~~ Founrt}~ that the far-field ampli~de, i.~., in the focal plane of the l~ns, i~ the ~tateme~tJI transform of the am~litude 1~ ~e near field. To exp!~n this note that Eq. (5.19) 1s very s11mlar to the more famtl1ar Founer tran~f,~ the fonn between the frequency and time domains. If F (t) describes tim~\i~I depe~denc_e of a pulse, then A (lu) describes the spectrum of the freq tienci¥{~ ·-:-:-:-:-tj contamed m the pulse .

. }}}~ l ··\t:i~ = +oo iwt A(lu) F(t)e- dt. (5.2Q}\J~ <{:!J~ -oo ~~f/~}~j Similarly, in Eq. (5.19) F({, ri) describes the spatial ?e_pendence in aperture plane and A' (x1 , y') can be thought of as descnbmg the spec t t h r e w s i ,.. ,i . / . //. } ..l.. : .f * .• , ~ . . . , .

of "spati~ freq~encies" 2rru/l and 2rrvj)... We will make use of concepts m Section 5.4. ..::::::::=:W.

·.\\\~ :::::?@.1 ··uwr~ 5.4. DIFFRACTION FROI\il A CIRCULAR APERTURE .· ,·,.·..,· .·.·-~ ·:.:·: ::: · : .·.· \ ;.; j ,:;.-, .; ~tead of a sli~ we shall now use a circular aperture. Some skill is requirei///~I m manufactunng such small apertures~ but they can also be purcha&ecf :}@ angl~f@~ commercially. The smaller the diameter, the larger the diffraction diamete~f{~ but ~e transmit~ intensity decreases at the fo~rth power o~ the J[ tb:if making observatton of the pattern correspondingly more difficult In :ff~ present experi~nt the aperture diameter was d 150 µm, which is ··\J~ good com~rorrus~ for ~e HeNe wavel~ngth. .

To obtain the diffraction ~attern, we mt~grateEq. (5.15) over th~ c~cul~J & ~J{j aperture. To do so we rewnte Eq. (5.15) 1n terms of polar coordinates <<ti ::/}:I ·<JW ·-:yJ~!

~::::· ~;:::.

~~=~:: 5.4 Diffraction from a Circular Aperture 189 ~::::: r~=r=:> 1J y' ~~~~~: ..- .. ·.· ~~~i~~ •:.-:-:• f} ~~~~~~.

::::;:· f{. .

ft: s x' ~::::::.

r.·.·.· [\ ~t( ~>·.

FIGURE 5.7 Coordinate systems in polar coordinates for calculating diffraction.

r.·.·.·.·.

~f·:>:::>::.··· ~f}: shown in Fig. 5.7 . In the source p]ane we use the coordinates a, ¢ so that ~mt {=a cos¢ rJ a sin(/>, (5.21)

~··· ~{\ ??:{/whereas in the observation plane we use p, ¢' so that , ..- .. ·.·.

?::::::·· sm tt x' p cos¢' y' P 4>1 = - = = = - = = u a cos¢' v a sin ¢' ~:;::: R R t R R t r.-.·.·.· (5.22)

f< ~{/ where a p / R is the sine of the radial diffraction angle. Expressed })n terms of these new coordinatest the argument of the exponential in ~f(_Eq. (5.15) becomes t/ u.·.· .

2TC 2,r ~/\ i - [(u +·11v] = i - aacos(t/) -¢ I ). (5.23)

t}? ).._ )._ :::::::::· ~J/~ince the origin of the ang]es is arbitrary we can set¢' 0 (the pattern if) imst be rotationally symmetric about the axis). Thus the amplitude at the if (~gle 8, where sin 8 a, is given by i~~::;::;!:;: :: f A' (a}= {2,t ei 'f aacos,t, ada def>. (5.24)

Jo ~::;::::-: o ~~·~-·\·8·e re ~;/ ao is the radius of tbe circular aperture, and we have assumed uniform WtJ11umination.

~~:::: ~~---:-:-.· ..· .·.

:<-~ /:.: I\:· ·trt ;1.JJ 190 5 Optics Experiments The integral in Eq. (5.24) cannot be performed in terms oftrigonometrl<t{/j . ./ .!..!.J. /i .

functions but is well known. One finds that .

aoa) · :\:}}~ 2f 211 ( A (a)= JCa , (5.25)::}:~ 0 2 /}l!

f aoa .

tbe?J~ where 11 is the Bessel function of order 1. The intensity is given by '.·.·.·.·.-...-.

square of the amplitude · -:))~~ [211 ( 2 ) Ii!

faoa)]

rra5 2 l(a) (5.i~ff~ ( ) 21f i)[i}~j Taoa .

illunil/}~ We recognize that the intensity is proportional to the square of the = similat\t;(,0 nated area. Since a sin 0 is the diffraction angle, Eq. (5.26) is Eq. (5.5) with the replacement of the sine by the J1 Bessel function. ···{}}1.1 Equation (5.26)is plotted as a function of its argument, x (2n /)..)ao~@f§~ }..~...~....I in Fig. 5.8. TI1e zeros occur at the following values of x, ·:'.::/}~~~ = = = x1 3.83, x2 7.02, x3 10.17, etc., whereas the maxima fall in between. The pattern is that of an intense centrijf: }~ 5~9V. \J disk surrounded by alternating dark and bright rings, as shown in Fig.

·)f ){J The first dark ring occurs at an angle e~ 3 3 cs.d]j/1

## 1.22 ~

= = 1 filn 01 : ~o where Dis the diruneter of the aperture. If the lens used has a focal leng,ij(J f.

the radius of the first dark ring on the screen occurs at '\}}{ (5.2Ji!il Pl 1.22 (~) A.

that can#l.i/1 Equation (5.27), firsl obtained by Airy, gives the smallest radius -ffl~1~: obtained by focusing a beam of wavelength A with optics specified by / -number ( f / D). The shorter the focal length, and the larger the ape~ii 1$~J the smaller the focal spot and thus the resolution of the instrument.

central disk contains 76% of the total intensity. · .)})

$.\f~ The experimental setup is the same as shown in Fig. 5.3, except the slit is replaced by the circular '))inhole.n Figure 5.9 is a CCD ptij~)

could)i~I;!

ture obtained with a 150-µm diameter pinhole. Three dark rings )??

·!}} ·)]/!)

~t ::::: ~ 5.4 Diffraction from a Circular Aperture 191 :,::/ ~.I".: ..~: ; •:••: .l'.1• •• • y .,/"::::: .,:.: ~··:·.

I\ 1.0 ~:::::: .-.·.·.

::?} 0.9 ~:::::: ~=::::: 0.8 t} 0.7 .:::::: .:::::: :~~\ ii 0.6 0.5 ft I 0.4 .· 0.3 ·.·.

··.-..· .·.

~~::: (.;.:: 0.2 •:•:-: ::::::- •::::::· ··:-:- 0.1 :,~ify F:aunh:fer -~11 FIGURE5.8 The d:strib:tian :or :-:a.9from : ckcular aperttue }(_ as a function of x (21r/).)ao sin 8; 0 is the diffraction angle and a the aperture radius.

:•:-: }l: measured at the angles .,:.:-:- ---.. ·, · ·· r ::; u ::: a1 = (5.25 ± l) x 10- 3 radians ::;::: ::: :: ~ . a2 = (] 0.5 ± 2) X 10- 3 radians t \ :::/ a3 = (14.5 ± 2) x 10-3 radians.

·.;::::. .

{}using the values for the zeros of 11 as given previously, we obtain the \)0rresponding values for>../ D ·::::::: ?/ (A/ D) = 4.3 X 10- 3 , 4.7 X 10- 3 , 4.5 X 10- 3 .

=~::: ::::::-.

:f These results are self-consistent and predict a pinhole diameter D - ) ) 40 µ,m, in good agreement with the: "nominal,, value.

;J:: =-=~:::.

~:;::::: ;a. ... ,,.. •.• ":~::::: ::::::::: ,,.. ........ .

,,.===~~=:· J'.•.•.·.· ::::-:::: ?@@m -:::::;:::::j 192 5 Optics Experiments :;:/::~=W.

· JI .·.-:-::-1:-:-;j } )\{i~ ·.:)\t@ \IU!li diamete{{l)

FIGURE 5.9 Observed diffraction pattern of a H.eNe beam from a pinhole o( }!){~j 150 µ.m.

>:::::?.?ij ilf 5.5. THE DIFFRACTION GRATING '.

th~/i[J/}~ We have already made use of the diffraction grating and discussed physical principles in Chapter 1. Here we will carry out a more detailed/:::i}i~ )if analysis and demonstrate a compact spectrometer using a digital readout.

If instead of a single slit, two slits are illuminated by a plane wavefront{}@j a series of intefterence "rnnge~-par!hi.1t ~t\!c..,~1it4L will. aop.e . ar on a fat:(){i screen. This is the classical experiment of Thomas Young (1800) shown ir({J Fig. 5.10a. If the spacing between the slits is d, the intensity distributioni.)i]

on the screen is 1 \!\~ (5.29f.l 1(0) 4/ocos' ( ~: sin0) · The angle 0 is measured, as usual, with respect to the normal to the plan~/)1 containing the slits. If one of the slits is blocke~ the fringes disappear anc(/j the transmitted intensity is lo. })!!; );!i!/j 1We take the wavefront parallel to the plane in which lie the slits.

})

::.::·:;::· .::::::: .~(\it '.,.: , ·.

.· .·.--"

;,,,:-:-:• %:•:•.

·~::::.

[}

## 5.5 The Diffraction Grating

~:: :~:::: ~f:: Iii ~:-:-: J_ ~=} i~'.:·: ::•::. d ~:-:-: ft T [-:-: ::;-::::: [~::- »·:-: ::;·r: ~--.

,u._:. ··:.-· ::!-:,:-: ,._.._.:, ~---·.·.

~l ~~~::=:>:::.: (a) (b)

~~::?:::(:: 1:G~ 5.10 (a) Young's two-slit experiment. (b) Multiple-slit interference, the diffrac- ~-:-:- ooo grat.mg.

::E:::-:-: ff( !~f In Eq. (5.29) we have not included the effects of diffraction due to the ( width of the slits. Let the slit width be a. Then Eq. (5 .29) is modulated by the ~f( diffraction pattern of Eq. (5.5), and we obtain for the intensity distribution Iii e)]

(nd . )

[sin sin 2 (~a ~-::::: J (0) = 410 cos 2 - sm 0 . (5.30)

;~-:-:- ). -1(,a\ sm• 0 -:·:· .

.-:-:-:- [1!/,"} ..

If instead of two sli_ts. severaJ equid~ntly spaced slits are illuminated [f{ ~y the wavefront, th~ m~erference max.1ma become much sharper, and the ~~} ·mterference pattern 1s given by 0)]

}~~\ [sin ( 1r/ sin 2 = N -:::::: I (0) Io d (5.31)

xf / sin ( 1r>. sin 0)

~--.·.·.

=~:::::: :-f \Here dis the spacing between the slits, and N the total number of slits; we }}'.have not included the effects of diffraction because in practical applications f)he slits are so narrow that the modulation is not important. Note that ... ...

i\~: Eq. (5.31) reduces to Eq. (5.29) for N = 2, as it must.

. ~~( What is ofp articularinterest is that the pattern contains principal maxima ~~{}when the denominator of Eq. (5.31) becomes zerot namely when ~-:-:-:-:-:-:- .......~ ::;::::: = = :{/ sin0 ±n)../d, n 0, 1, 2, .... (5.32)

.~ 1 .,.-..: . .. · · r . : - . . · ...: ::::- "• • >> ·~:::: ~~}~\ \ti~ 194 5 Opt i cs Exper i ments ):•::-:::;•::;:-::g-:~ .<mt~ The intensity at the principal maxima can be found as follows. Near a prin~{}f!

pal maximum (rrd/1) sin 0 = nrr + E and therefore sin((nd/1) sin 0] ""s)))t~ so that Eq. (5.31) can be written as . :}\j~ /:/:;:;:;3j 2 2 2 \{}j I(B) -L [sin[N(nn+E)]] -l N2[sin(NE)] -L N2 (sin x)

max - 0 E - 0 NE - 0 X , :}}}} .·.·.·.·-·½- ))]§ (5 .331::::::::::j . ?\:~~i = = where x NE Nrr(d/l)b..0, and b..0 is the departure of 0 from the{/ff condition of Eq. (5.32). Since the function (sinx/x)2 1 as x 0, ~e}{Jj -4 -4 = .))fj intensity at the principal maxima [b..0 O] is .

·:.)/Jj = 2 Imax N Io. (5.34)-... :-:-:-..-x .-:;:::}:?:~ \\i.~ This pattern is shown in Fig. 5 .11. · · of The width the pruicrparmcOO.fuir 1ctgJ:>n-h"'~!f~6r.s.t.minimum of the·:\J)

function (sin x / x ), which occurs when x ±n, namely ) ]

:.:-:-:- (5 35) )j • • •' .'·:~ j -: •:-: ·-:-:. .: ~ , Note that (Nd) is the total extent of the region covered by the slits. Thus \)

the principal maxima are as narrow as if the wavefront diffracted from a }/ slit of width Nd. By combining Eq. (5.35) with Eq. (5.32) we can express \ \ 10...----.....----.----,..---~~--.---.------,-----, '!!!ff /!

,c::- 40 -z~.

.S 30 .E ..

0 L-~:::,..io..C.:,..Z..."--L.~~~U-..ll.....l....J.L...lo..Q~"-£.)..1-ll-L...lL-~~=--.__J -2 -1.5 -1 -0.5 0 0.5 1 1.6 2 (dn..)sinB FIGURE 5.11 Different orders of monochromatic light scattered from a grating. Note that the principal maxima are very narrow peaks, whereas the secondary maxima are suppressed.

Plotted for N 5.

::::::.

ra cti on Grating 195 the resolution of the system of N slits by cos 0 ~ - . (5.36)

Nn A diffraction grating is equivalent to such a system of many slits and can be used either in transmission or in reflection. The angle of incidence Bi can be different from the normal to the grating, in which case Eq. (5.32)

:•-::--:-:. must be modified to read ':a ~::: . J r - . .. . · •• ' s . m &i -sm . 0r = ±n d )._ t n = 0 , 1. 2, ... . (5.37)

The diffraction angle is 0r and is taken positive if it is opposite from Bi I! with respect to the normal. These definitions are shown in Fig. 5.12. For a = = reflection grating n 0 corresponds to specular reflection (sin 0r sin Bi), .......

.. ·.·.

Reflection gratings are often manufactured so as to enhance reflection at particular angles. Reca11 that Eq. (5.37) was already used in Chapter 1 (see Eq. (1.16)).

The arrangement used in the laboratory is shown in Fig. 5.13. The light source is focused on the slit and the emerging beam is made parallel by lens Ll, which has focal length f1 = 20 cm. The parallel beam is incident on the 4 x 4 cm2 grating, which bas 1200 lines/mm. The angle of incidence was chosen to be Bi 55.7 °. The beam diffracted in first order was focused with lens L2. identical to Ll, onto the "reticon" where it formed an image of the slit.

The reticon is a linear array of pixels, which can be read out on an oscilloscope. In the present case the array contained 128 pixels; the clock speed was 80 kHz so that a pixel is read out every At 12.5 µs. The pixel Grating FIGURE 5.12 The convention used for labeling the incidence nnd reflection angles for a reflection grating.

196 5 Optics Ex·pariments Light source t -- Slit .f L1 Display/Scope Ret ol ckt FIGURE 5.13 Layout of a simple grating spectrometer read out by a reticon (a o~~# /Jij :-:\:Ja~ dimensional solid-state detector array). .

. ::::;}:f~ . ::\@ti size was Lixo 100 µ,m for a total array length of 1.28 cm. Thus we havt( )&, • f the conversion actor -::.\·.:·.}··'•tZ$•.%.

/ill = = and sffice ~x f M, f :cm ~m/~s. (S.3&!

Li0 0.04 mrad/µ,s. (5.39):::\t ~ }/t1 The spectrum of a Hg arc lamp is shown in Fig. 5.14a. The horizontal//:~ scale (sweep speed) corresponds to 200 µ,s/cm. The speclrllm was observe<f()}f in first order, andfromEq. (5.37) with 0i = 55.7°, d = 10- 3 /(1.2 x 10 3 ) in·:\{~~ we find that for the green line of Hg (Ag= 546.1 nm) )/ }~ = = sffi0r sffi0; - 0.170, namely 0r 9 .8° in the quadrant opposite to the incident beam. The secon,()t order appears in the same quadrant as the incident beam at Br = 29° as))l . F' 5 13 ·.·.-....., ../ sh own 1n 1g. . . :?:::~:: The green line corresponds to the peak on the right-band side of the grap~(J~i ····:::: (Fig. 5.14a), whereas the doublet on the left corresponds to the yellow lin~/ j]

= = ()..1 577.7 nm and A.2 579.1 run). Knowledge of these waveleng~f}if allows us to make a more precise calibration of the spectrometer, including}\J .-.:~\~::~ ))~~i ·,·.·.·.·.. · ,::;:::;B ..

··u· • . ,· · . ,r· ·. . · ·~. . - • - .;

## 5.5 The Diffraction Grating

(a) F. 2 :'.o.";'-. • .. ' ..•. ' . : .. , •... f.''.2~.'':5 .. ~~".'. -~ .... ~ .~.~P •' •J -------- rI · ·~ r,f; .

'' ____ I • 1,F; AililP&C: FIZ•IW ,1:,MIWWW4tfA 7 g ,,,. ~; ~ ~ ~ ': r· •.

t. .....•.................

it .:.21s:ol'-'. .. ·• ,i,; 1.n.rms-· · L .J > . . t . ;,- . 2 . • "o • o • o· • m • s • · • • • • ·• . ·; . ·,t . .i . a:5 . 0 . C .. l:o . ·i . - . 1 . 2 (b) '-. !~.~ •'. • •,' '" .. •" • • .. f ~~~ .~~-~~-~ .... ~ .~P i, :t ' t ,( • 1 • 1• ' ' i , I ., ' • I ,_ ~ ' \'V1.~/\'\f\\'V,p\ I r""'-: ~ rvWV\~m1~ -~! ~ j . f ' i : <i I ~ t , ~ _,. ::•...•:,. . , . . . . - . . . . . - . · . - . - . · . - , • - • · • - • , . \ .. , .. . t .-1- . • . I h .. • . . • . • . • . • .. • .. • . • - • .. • .. • .. . • . •.•_•..!.!.!.:.!.:.:.,; ~ 183.0µ.s 12•239.0µs oJ:56.00µs 1/61= 17.SSkHz PIGURF. 5. I 4 The observed ~pectrum (a) of the green line anti yellow clonhlet of the Hg spectrum obtained with Lhe spectrometer of Fig. 5.13b. (b) The yellow doublet on an expanded scale.

ousalignm.ent and other -instrumental effects. Differentiating Eq. (5.37)

with 0; fixed, we obtain nf:i.).../d -cos0rA0r. (5.40)

= = In our case n 1, cos0r 0.99 and A>.., from the fust yellow line >..2 to = = the green line Ag, is A). 33 nm, or t:-,.0 40.0 mrad. The time interval between these lines as measured off Fig. 5. 14a is tJ.r 1030 µ,s, and thus the calibration tJ.0 39 x 10-3 mrad/µs (5.41)

in close agreement with the direct calculation.

To measure the fine structure of the yellow doublet the sweep speed is increased so that the scale factor is 50 µ.s/cm as shown in Fig. 5.14b.

.)!iJ?~ 198 5 Optics Experiments · .}{{~ <<=l~ :-:-:-:-:-~ One can no~ re~ognize the ~esponse of individual pixels. The separatiQif)Jfil of the two lines 1s 56 l.LS; using Eq. (5.41) we find f:l8 == 2.18 mrad and{::::::@!

......

JJJ!il from Eq. (5.40) liA "' 1.8 nm.

Ji Our result is only in modest agreement with the accepted value of -6.l ==()f

## 1.4 nfil This is not surprising because one pixel, the ultimate resolutioii()/~

~?J1 of our detector in this configuration, contributes an uncertainty of bA 0.42 run. Thus one must be cautious when using digital techniques, whid{' .(.{.§...J.J ..a ~.

often do not have the advantages of the high resolution of photographi((<tm fibn or of visual observation. ::})~~f:j '.JJI 5.6. FOURIBR OPTICS In Eq. (5.19), we showed that the amplitude of the electric field in the focal)[]~ plane of a lens is ~e Fouri~r transfo~ of ~e ne~-field ~plitude incident\/@~ on the lens. We will now give a phys1cal discussion of this result-and show))~j how it can be used in practice. These considerations were first introduced))~~ by E. Abbe in Jena, Germany, but found much wider use as lasers became}{Jj available. '::::::}:~ :' :·:-:-:. .: ..r:-: A transmission grating is a repetition of regions in space that alternatively{:/:~ transmit/absorb the incident wavefront; we can represent the transmission.)/{~ are:(\]

of the grating by the "square-wave" function shown in Fig. 5.15a. We immediately reminded of the analogous square-wave function of time that?\ ]

has period T, and thus frequency tJ 1/ T. Therefore we can assign to the /{j 'II -l :--d---1 T :.,__ d T [•s-1/d] !•s-1/d]

.___...__ _. ___. ________. ,.__.....__ _ X ,___...__ __ ,__ ________ x·-:-:-:1- ·\J (a) (b)

·.::;::~ FIGURE S.15 (a) Representation oft he transmission of a grating; the spatial spectrum con--)j "s = tains the fundamental frequency 1/ d and its higher harmonics. (b) If the transmission·:::;:?, \(;i is sinusoidal, only the frequency Vs === l / d is present in the scattered wave. · . ........

~: ::: ;: :=:=: ):·/=·= · .;:;:: ·.·.· ·. . · · . .· ·. . .. . .

"<·:•

## 5.6 Fourier Optics

·-· grating a spaJial period d and a spatial frequency I/d. Spatial frequency { is measured in cycJes per unit length and has dimensions of inverse length.

{ For instance, the grating used in the experiment described in the previous :::· ··· section has a spatial frequency of 1200 lines/mm. From circuit theory we } know that a square pulse in time contains the fundamental frequency as [ well as higher bannonics. Similarly the square grating contains not only jf the fundamental spatial frequency l/d, but also its harmonics n/d. This is ;::; seen when 1igbt incident on the grating is diffracted at the angles 0, with :::.

-=::· ~•.-·· . .

J..

·:::: sm 0n n d.

·-· ·-· -: .=:·· f: If the grating profile was sinusoidal, as in Fig. 5. l5b diffraction would = = occur onJy for n 0 and n J .

·•.,•·.•.

:::·: We can place a lens after the grating to relocate the far field into the F- (back) focal plane of the lens as shown in Fig. 5.16. We will then see the ~J;.-:', diffraction maxima, namely the Fourier transform of the grating: we refer :•:,:, r\ to this plane as the transform plane. If the distance s1 from the grating to wm f;1· f, the lens exceeds the focal length an image of the grating be formed ,;"::, P.:: in the image pl.ane located at s2, where .·.• .:::: i:: l l l -+- =-.

SL S2 f ll( ::::, ~t -:-: :::;· •:-; ~J !!ill!, ..:,....:.,· ~fl .~;:: ----- s, -------- -f -- ---- t t t ~~ X:;:.

/:•:.

'tli!: 1;::i: Grating Tr~~~rm :{: FIGURE 5. J6 Location of the source plane. the 1I1U1sform plane (the back focal plane of ..

;,· ·.::;:;. the lens), and the image plane.

~If )\( ~:=: ::;:::.

,::::.

ill!~ 200 5 Optics Experiments ·-:?::::=:::~ L2 '- ii/If l1 ..: :::::::::===I Laser Expand -:11111 ..,._ _____ 52 ------· ·,::::::::::::;:?._~ :-:::\::::~:~ \/]~;~ )I- I I ./ .::.: ::.:= ..: .-.-.=. : ~ , I I L3 -:-:-:-=--~m I Masks Mesh <:?JS; CCD ·::::::::?.i;@, Image plane Transform plane }!i/(~~i FIGURE 5.17 Experimental layout for demonstrating Fourier optics.

. -:-:-:-:-:~-1 This image is the F~urier transform _of the amplitude in the transform pl~;J{[/f Therefore, by altenng the pattern m the transform plane, we can modif)J{}:~ the im~ge bein~ fotmed. !here ar~ several applica~oos ~f this ?rinciple//m)~ as for mstance m smootlung out unages that contam n01se or m patteril({:(:~~ . . . ...

recogrution. . · ·: .· ·.

'-.

Y- ..

:E ..

~.

laW/}:f~ A simple demonstration of Fourier optics can be carried out in the ratory with the setup shown in Fig. 5.17. The laser beam is expanded and(}J~ allowed to illuminate a mesh with 270 lines/in. and transmission factor( ?:::@ .-.v50%. Lens L3 is used to image the grating onto a CCD camera. Variou~{\}j masks are then inserted in the focal plane of the lens, the transfonn plane/}}@ • . ·:.·.·.·.·« to modify the unage. · ::::::::=:=:-=- .·.·.·.·.·x th~{/jj The results are shown in Fig. 5.18. In Fig. 5.18a, no obstacle is in transform plane, and the pattern represents the image of the mesh. Next,/ \\j a vertical slit 1.5 mm wide is placed in the transform plane, and the pat-{}~~~ 5.18~--/iJJ tern in the image plane contains horizontal stripes as shown in Fig.

The effect of the mask is to allow passage only of components of the(!\~ wavefront that were dispersed vertically in the transform plane. These com~·}!\[ ~i ponents carry the information about the horizontal structure of the objecf (the mesh) and thus show horizontal lines in the image plane. Figure 5.18.C.:{j~ was obtained with a horizontal slit as the mask in the transform plane:/ !:\~:~ ~=t: ~t.

tr

## 5.7 The Faraday Effect

II (ill ·• r..z: ~-:-: ?.;:·: fcJ ~:-::: ~t .- !:::~:·· i:;:;.::: f{:: ~::::, • ~[:; FIGURE 5.18 Results from placing masks in tbe transform plane: (a) Image of n square ~;;;.;:-.

::::::::: mesb in the absence of a mask, {b) placing e vertical slit in the transform plane, (c) plaer ~;;:;:-- ~~:> ing a horizontal slit in the Lrallsfonn plaoc, and (d) placing a pinhole in I.he transform v./:,:, ~;::::, plane.

i;:::::.

t:-:-:-: .

~ft:~ ~tr Finally Fig. 5.18d shows the result of placing a I -mm-diameter pinhole in the transform plane. Now all high spatial frequencies are filtered, and the ~:;.:::: ~?: pattern in the image plane is significant] y smoothed out.

ft Spatial filtering by using a pinhole is often used to "clean'' laser beams t:::: that have acquired structure due to imperfect optics, dust on components.

~:-:- /?::: and other aberrations. This is analogous to using a capacitor to filter out r :::: high-frequency noise in an electric circuit.

~{ r~~/::·~·:· ;~~m ~/: 5.7. THE FARADAY EFFECT ...-~~-~ . ~-=, .=,=.=_::. : tt( S.7.1. Discussion ~;;:=:· ~~:::.

ff · As already mentioned, the Faraday effect refers to the rotation of the plane ~ ) of polarization when light propagates through certain media subject to an ~ { axial magnetic field. It was discovered in 1845 by Faraday long before .%_:i::· ~-;:;:, @::::: ~f::.

QI';•;:-:, :x-::::: ".f; ~{:?

,.,.:;.·.

Jtt~~ . -:-:-:!-:-!;-I~l l ZOZ 5 Optics Experiments . )

elec/}Jij the nature of light or matter was understood. We now know that the tric field of light is transversely polarized with respect to its direction o()\~ )..f.. J..~. :.:, z, propagation, and we can express it, in exponential notation, as -:-:-:.:-:-:-::=:: E(z, = 9?.e{ (5.42)/:{t~ t) Eoe-i(a>t-kz)e).

.. <::::::::::a Here ~e means to take the real part of the expression; for simplicity o(/}~ alway( j)tj notation we will omit this designation in what follows but it is = = implied. As usual w 2n v and k 2n / )... e is the polarization vector.))Jj which can be expressed in terms of two unit vectors (since e is restricted) \Jj to the x, y plane). We can choose linearly polarized unit vectors · :/)~)j . ·</&!

Ill = = e1 llx, ei Uy (5 43y::::;:;:~ or cITcuhrrly poflrized unit vectors . • = + e.R Ux iny, CL= Ux - iuy. (5.44}.:;:::;:~ .. :::::::;i~:a If we now examine the electric field at a fixed position z, in the case of\ {~).

. ' .' ·.·.·.·J',.:, circular polarization we will have the two components · \ };~ If ER= Eo[cosa>tux sina>tu ] · EL= Eo[coswtnx - sinwtuy]. (5.45) :{{~ /~~~~~~~ These were obtained by introducing Eqs. (5.44) into Eq. (5.42). The fields :\ /~ rotate in the transverse plane, in the first case according to the right-hand \}]

\{t rule (with the thumb along the direction of propagation), in the second .•{••f•a •,1 case according to the left hand. This is shown in Fig. 5.19 where we use a . . ' . . , · •. . .. · ·. . .••· - ,. ...,. · • . ,.1 . 1 , :\~~~}?.

,::::::::;.

~ .

.- ·.

:- . .

-- :.

?it <·:-:-;-: eR eL :-:-:-:-:; :}t .\/1 ,•,•,4,Y, :\]

·•.,·•,.•-4•...1..,.• :~ ::: :=:: · . g . ' ' ,• · .. ··..·r•. .·· <::::~: \ )!

FIGURE 5.19 The right-handed coordinate system used to define right- and left-circular polarization. ·:/:'.: :-:-:•: .·.·.·.•.

.: ::::Y, \J -::::;:: >: -: ~: ::~:: ::: ·:::::~: ··):}~ .:::~:~\ tu .•.·' 5.7 The Faraday Effect 203 ·-:·:·· :,,;-·:,:- f f.

:[f right-banded coordinate system. Note that we can write Egs. (5.45) as ?I ~,<:? (5.46)

~tt.

ff\ and by solving i }::; f/:.

(5.47)

~ff ~ ?- The Faraday effect arises because in certain materials the application i~ f{ of a magnetic field results in different refractive indices for the right and left circularly polarized light propagating along the direction of the field.

if ~teri~s that have a ~ere~t refractive i~de~ for tw~ given po!arizati~n C::l~r onentat!0OS are C~ed birefringent. Th~ b1:efriogence IS ~turaJ IIl certain ..f ;: crystals or can be mduced by the application of an electnc field (Pockets ~:f?=,;::::: a )

euect . . . . . .

~{::: The pl1ys1cal mterpretauon of the Faraday effect 1s related to the sb1ft of @\ ..

the atomic energy levels when an external magnetic field is applied. This fE is the Zeeman effect, which is discussed in some detail in the following f f chapter. Wheo the light propagates along the axis of the field the right iit = + polarized light can ex.cite only a particular set of sublevels ( ~m 1, ~\::: where m is the magnetic quantum number) and conversely for the left ~j::, = - polarized light (Lim l). These levels have different excitation energy f/ and this results in different refractive indices, nR and nL. For more details i?r the reader should consult the references cited al the end of the chapter.

l ]( We know that the velocity of propagation of the wave, the phase velocity, f ?: = is given by c1 c / n; thus the phase advance in a length L of material is ~=~::·.

;:::-:: ~if· = 2,r 2Jr V 2:,r V 0 =kL -L = - L = -nl, (5.48)

;po;:: l c' c ;:?.=<· t.~\ where the frequency v of the lightisfixed and n is the refractive index oft he i~{.

material. Tbus the right and left polarized light will acquire different phases.

If the incident light was linearly polarized when entering the material, say ••1/.· ~t along x, ER and EL wouJd have the same phase (see Eq. (5.47)). However, :;:=;;:::, upon exiting the material their relative phase would be shifted and the light, r~?

while still linearly polarized, would also contain a small Ey component.

½;:;.· :::~. .: ·: Namely it will have rotated by an angle ?f:> tt.

r,;:;: (5.49)

~.r= tk t::::: ~=:: ~t ;;;;~:: .;:;:;:~::I:~ -::::::::;::: 204 5 Optics Experiments . 1111111 : -:<){~ ·<tJ~ . -:-:-:-:-:-~ -/ti%~ <·.::<::::):m::;.~ ;::1 --:-:-:-:-:-~ }mill regio,i!}:!/1 FIGURE 5. 20 The rotation of the plane of linear polarization after propagation in a where the right-and le~-banded circular components h~ve differe~t p~e velocity. Becaus~}((@ = + ER and EL rotate by different amounts, the plane of linear polanzation for E ER Ei··.::}::r:J;~iI~ rotates away from the x axis by an angle</> = (Oil - ~)/2. .

:::::);~ . .· .·.·.·.·1@.

TABLE 5.1 Verdet Constant for Distilled Water )ill A. (run)

·:i 590 3.81 (Na D-lines)

600 3.66 800 2.04 . .•.·.·.·-·% 1000 1.28 Y!!II@ 1250 0.84 ... ·---~ \/ti "\}{[ }/}!i This is shown in Fig. 5 .20. The change in the refractive index is proportional /:/::l to the external magnetic field, B, so that we can write . ))i}j (/> Cv BL, (5.50) -::=:::=:=:x -:-:-:-:-:-~ )/tj where Cv is called the Verdet constant. We expect Cv to be a function of \:/1~ wavelength, as well as of the medium. Values for distilled water at various 1· d ' ,,.. bl 5 :-:-:-:-;~ wavel engt h s 2 are 1ste in .1.a e . 1. . _:}l~ :)j j :}Ji 5.7.2. Procedure and Analysis .··:-:-:% ))ii \?~ It is difficult to generate axial magnetic fields in the kilogauss range.

}\{f Instead, a small but oscillating magnetic field will be used. The size of }:;:::~ \}* Data from E. U. Condon and H. Odishaw (Eds.), Handbook of Physics, second ed.,.

\Ji McGraw-Hill. New York. 1967.

JI -;:::::· -;::::::.

f{.: ~=~/; 5.7 The Faraday Effect 205 :,:.:.; :-:-:-:-.

?:::::> ~!(' Linearly polarized Analyzer Solenold t ( HeNe laser Photodlode Sample r:-:-: r---i~ , r : : . - : : .: - , · L..__J Laser f1J ~~~~~~- beam ;::::< Output voltage on g[ \ Solenoid coaxial cable to dn\Ong circuit : ;;n ' [ ( FIGURE 5.21 Experimental setup used for the Faraday effect The photodiode output ({ goes to the DtvfM for the polarization calibration, and to the osci11oscope or lock·in to ::::::: measure the Verdet constant.

•·.·.· .

ll(.

the effect will be small, but the oscillations make it possible to pick it out f \ of the noise, by using lock-in detection.

~) The experimental setup is shown in Fig. 5.21. The source of polarized f( light is a HeNe laser. The magnetic field is supplied by a 1026-turn solenoid if{ driven by the amplified signal of a waveform generator, in series with a [ .·· monitor resistor. After passing through the sample and polarization ana t\ lyzing filter, the light is detected in a photodiode. The signal is measured if by the output voltage of the photodiode, and is given by :'·:":'·::'·. .

I ( (/>) Io cos2 </>, (5.51)

where </> is the angle of the linear polarization with respect to the analyzer !~( axis. We are interested ind</>/ dt and in this case the sensitivity is maximized r:-:- = + by "biasing" the polarizer at ¢0 =: 45° ~ where <I> </Jo </> (t). Note that dl((j)) d(/> di d</> d¢ - - = - - = -- Josin2</> - - Josin2</Jo. (5.52)

dt dt d</> dt dt f( We can calibrate the polarization analyzer by recording the photodiode voltage as a function of the analyzer angle. The result is shown in Fig. 5.22 ~:/ and exhibits the cos2 </> dependence of Eq. (5.51). The maximum sensitivity :? dVo/d<I> is found near¢ = 180° and as predicted by Eq. (5.52) equals ::::: V~, namely dVo/d<I> ~ 0.4V/rad.

if i The magnetic field is provided by the 1026-turn solenoid coil around 1:::=(:-.

the sample, driven by a sinusoidally varying ClllTent. The current is pro- t.:-r:-:- vided by an HP3311A waveform generator (sine wave, 600 Q output)

:::::·,: amplified by a Bogen MUIO monaural audio amplifier. The driver setup :~:::·: ~::::: ,.,,_ ..

~:;::.

206 5 Optics Experiments 400.--...-----..---------,..---------.-----, ••• • • 300 • gCD> 250 • ~> Q) • • " 0 O • ) .· : . ~ · = .• ~ . = ~ ~ ; ~ ii 150 ~ • . }~:~~~~ .. (@ 0. 100 • • ..i i 50 • t!f!I 0 1-50 200 250 300 Analyze, angle (degrees) ·.·.·.- \~{§.

FIGURE 5.22 Sample polarization calibration data. The plot shows the full range of ):j angles. .::;:::~ i:):}.

..

:: , : · : - ~~ ,:/ ':::=:~ is shown in Fig. 5.23. The wave generator provides the input to the audio Ii amplifier, and the output loops through the solenoid coil with a high-power resistor Rcoil in series. The current and thus the magnetic field are deter mined by measuring the voltage drop across this resistor. Do not ground either side oft he amplifier output signal. Using clip leads on a coaxial cable 0: measure the voltage Vc oil across Rcoil on an oscilloscope. The shape should be a good sine wave with no DC offset and amplitude on the order of 10 V peak to peak. This is achieved by adjusting the amplitude of the HP3311A and the amplification (i.e., ~'volume") of the audio amplifier appropriately.

It may be necessary to adjust the distortion on the amplifier so that the shape is alright.

The photodiode output is now connected to the other channel of the oscilloscope. The scope trigger is set to fire on coil voltage, and both chan nels are viewed shnultaneously. If the channel on which Vn is measured is DC-coupled, one sees a large DC level, corresponding to the mean light intensity on the photodiode. (This DC level should agree with what was measured with the DMM.) The Faraday effect, on the other han~ shows up as a small oscillation on top of this DC level, in time with the Vcoil. One is just able to see this small oscillation if the channel sensitivity is set to lit !}\:

## 5.7 The Faraday Effect

&.··:-:-· To oscilloscope (should be 10V sine wave} Solenoid ~t: 1!/IIIIIIIIIIII!

i:1:::::.

ff ~t~~~: I~ t r t -· ROOII Bogen MU10 > i~;: Output auc!io amplifier Sine wave '°'"' '':~;~~ o,t Coax at ;:;:-::: Tee off 10 lock-In reference i~:;:, ~f i · FIGURE 5.23 The driver circuit used to generate the oscillating magnetic field for f \ .

measurement of the Faraday effect.

==~:::: rr f ( its lowest scale and AC-coupled to the input so that the large DC level is f)

removed. Confirm that the amplitude of these small oscillations move up \L or down with the amplitude of Vcoil, wb.icb is best adjusted by changing ( \ the amplifier gain. Confirm also that the oscillations disappear if the pbo \\ . Eodiode is blocked from the laser. In fact, the amplitude of the oscillations f · should change (and the phase reverse) as the analyzer is rotated.

f: We can now check that we are getting about the right Verdet constant, j\ although it is hard LO do a careful job with the small signal on the oscil }:' loscope. From Eq. (5.50), we know that the small changes in polarization · · angle f:;.</J are related to the changes in magnetic field b. B th.rough ..

dVo b.tf> - b. Vo. (5.54)

d<P = ]

The magnetic field in a solenoid of length L solenoid and N 026 turns is given by = IL B µ,oicojjN (5.55)

solenoid -::::::::::::» -::::::::::;~ .·)?}~ 208 5 Optics Experiments :::::::::::::: \):~:~=~=~ By (5.5Jj\/t} when a current icoil passes through the coil. combining Eqs.

·~tft (5.55), one obtains an expression for the Verdet constant Cv in tenns Vo, Vc ;1, and other quantities that you know or can measure separately~}}/~ ' Consistent definitions should be used for Vcoil and for Vo, That is, if V~ it!{} .

\}\½ is the amplitude of the sine wave, we make sure to do the same for Yo. ~ . !lilt~ 5.7.3. Results Using the Lock-In /i/it~~ :~ The lo~k-in ampl!fier allows us to measure oscillati~ns ~n Vo more precis~I*=/~~~; than with the oscilloscope. Furthermore, the lock-in will remove any no1s~f=~~~ #/:ir..l.

that i.~ out ~f phase or i_s at the ~ong frequency. Refer to Section 3.8 an explanation of lock-m detection. })t~~ The lock-in is a PARC Model 120 with a fixed reference frequency 9f).~ is butJlJII..

,.,...,100 Hz. It best used by defining th~ referen~e w_ave externally, correct1rrt~ needs to be close t~ 1? O Hz so that the mternal ClfCUlt responds The lock-m mode dial is setto "SEL.EXT.'' and the HP3311A to a frequenc~t):~::~ ~~jfi~ near 100 Hz; using a BNC Tee connector the reference input is applied to lock-in, while ~e sign~ is on th~ way t~ the a~dio amplifier. This assll1:'¥:tJ~I us that we are using_ a ref~rence signal with _Precisely the same frequency 1fJI the Faraday.ef~ect signal m Vn. The photodiode output should be connec~1IJI to the lock-in mput. . \)\~~ hav~\Jl~ O~e still ne~~s ~o tune the p~as~ of the l~ck-in amplifier so as to maximum sensitivity to the oscillatmg Vo signal. There are a few ways tt?(\:~~ //}j~ do this, but the most instructive is to use the oscilloscope. .

·······=w.

1. With the oscilloscope still triggered oo the Ycoil signal, use the othi¢fi@tiI channel to view th~ "1?onitor o':'t" port of _the lock-in, with ~he swit.c~ JI tltn~f to ~'OUT x l ," which 1s the bas1c output signal of the lock-in. If the 1 doi;\fJ@ constant is set to a value much smaller than (100 Hz)- (1 ms will /J@l then you should just get the sine wave folded with the reference signaf oscillating between ± 1. That is, it should look pretty much like Fig. 3.3'!:\i/~ ·)\/W.

or Fig. 3.38, or something in between, depending on the phase setting.

## 2. Adjustthephase~ob sothatitlo?kslikeFig. 3.37, thatis, sy~etrif)j~

about the cusps, and with the cusp pomts at ground level. If you ihp th,tj/J;:::;-}.

tb~JJj relative phase quadrant knob so that the phase is 90° lesser or greater, trace should look like Fig. 3.38. On the other hand, it should change si~) J @ 'f fli b 180° .·.·.·.·.-... .-,.: 1 you p y . ..::::::::::~-:=:::: ~ \)@l

## 3. With the phase adjusted so the output looks like Fig. 3.37,

• ·,·.·.·.·/,.·,t'.•,I"

the time constant up to 1 s or so. You can read the momtor out on th¢/:::::~i!: <:1 ·\::::%~ ./J~ .:::::;:~~~31 I'< ~l< 5.7 The Faraday Effect 209 ~~~:?::::::-· DMM. or use the meter on the lock-in. Itis probably a good idea to block , ~ f) the light to the photodiode, and adjust the zero-trim so that the lock-in ...

~?::. output is 0 z.·.·.· • x::::: z.·.·.· f { Vary Vcoil by adjusting the audio amplifier gain. (You should not touch z ...

f/·- the waveform generator settings anymore, since it is now serving a dual t \ role as both amplifier input and lock-in reference.) Make a table of Vo as ~}/ _-measured with the lock-in and Vcoil. Realize that the value of Vo provided ~~{_\by the lock-in is the RMS value, i.e., l/~ times the amplitude. Plot Vo ~/( versus Vcoil and make sure you get a straight line through~- Either fit to t ::::· find the slope or average your values of Vo/ Vcoil to determme the Verdet Wf constant with uncertainty estimate. . .

~?

Results obtained by a student are shown m Fig. 5.24 for a water sample.

~f·: The parameters used to obtain these data were ~~-:--:·:.·::.:· ~-..... R = 5 ·3 n :~-::=--:::: .. : coil ,H ;-;:-".-:- : :, - : : :. -:.-:.- N = 1026 >-:·. . •• .

,~.= . ..

..

: .

0:::: . L solenoid =:= 0.265 m ~:::::::- r.·.·.·.

~ r. : ·. ; · : : . : . : · L sample= 0.265 rn.

,. .... ·.· ~:;::: i':·.·.

;:;:::::· ~r .... •·..··.. · ,r._.-. ....·..· ~=<·' r:·:· r.·.·.

~:::;: 0.7 ,_._._.

,:...:-:-: i-:•:•: > }/ s 0.6 :-:-:-: ,:. . :-:- ~::::: Q)

:~::: ..~... 0.5 · ~ • = •. : · : . : ·. ' ~ ;,_:<._-.,· :5 0.4 f( % ;..:-:-: D 0.3 it ·C, r;:;;::r:- .03 0.2 ~:::: .. 0.1 .~..:.::.: :> .-.-.··. .

o....__ __. ..__ _______________ __._ ___ _, . ~/ I ," '. ~ . . . • / =' • .. • ":·• 0 2 4 6 8 10 12 1~-'4::.':•:'.· Voltage acr0$$ resistor (V)

~/':J=" .::··' .~...{. · FIGURE 5.24 Results on the Faraday rotation angle as a function of magnetic field, )~;-.-::·;.. ob tam. e dby a stu d ent.

t;-:-: :- ;..:.-:-·- ::::::: ½···· ,~. :.:.:.· : - ~:=::: ;:;::;:: ~:-: ~-::::.

:,::.:.·, ?!Ii 210 5 Optics Experiments We first calculate the magnetic field as a function of Vcoil , = Vcoil N = 4 B µ,o-R . Vcoil x (9.18 x 10- ) T.

coil L solenoid Next we use the relation of the optical rotation to Vo, which in this case was(}~~ ¢ Vn/(0.098) rads.

The measured values (see Fig. 5.24) are = 5 Vo/Vcon (6.7 ±0.52) x 10- .

Thus we find for the Verde t constant _ </> _ 1 ( Vn ) 1 .

v- - -- - 2 - 4 BL sample L sample Vcoil (9.8 X 10 )(9.18 X 10 )

= ± /@

## 2.80 0.2 rad/T-m

From Table 5.1, extrapolating to A 633 nm, we would expect .Cv ~}:]

3.2radn'-m. The difference could be accounted for in part by the short}:~ length of the solenoid~ which results in a weaker field than what we)@ \jj calculate.

<:::;~ .·.·.·~· <::::;: :::::;: S.S. BERRY'S PHASE :-:-:-: ~:~{: We will demonstrate this effect by the rotation of the polarization vector /} }I of a beam of ligh~ as in the Faraday effect, but in the present case the light :J propagates in a vacuum. The reason for the rotation of the polarization.

is that the propagation vector of the light, the k vector, performs a closed ): circuit around its direction of propagation. This is shown in Fig. 5.25 where } light propagates from point A to point B. In part ( a) of the figure the k vector )

describes a helix on its way, munely a closed loop in the transverse plane;. :; therefore the polarization rotates. In examples (b) and (c ) the initial and ; final values of k are the same as in example ( a) but there is no looping :i around the direction of propagation; therefore the polarization does not : rotate. We speak of a 'topological" change in phase because the effect : depends on the path followed while the initial and final points (in phase. · space) are the same.

This effect was first predicted by M. V. Berry in his 1984 paper (see

## Section 5.9). He analyzed the behavior of a quantum mechanical wave

~:::: :"?(' ~:: ir: 5.8 Berry's Phase 211 ~--: ~:: ;.

11} (a) () k~1;1 ,,·=,,·,~. , ~=:::: {~!; ----"------i>- ---~ v.~-: (b) ...k:_::&Nllal~'~> --..'>.. .. ...,. k~nal A B ~~:i: ,~.= =· z:.-..: ~;::_.

:=!~:- (c)

ot. ..t ,· !1~1\'.

~}:: FIGURB 5.25 Topology of the optical fiber between A and B with k5 a.1 kiniual: i( 0 (a) helical winding, (b) direct (straight line path), and (c) cucular path ou a flat surface.

rt.

i;i:. .?.... · function when a parameter on which the wave function depends is slowly f( varied over a closed circuit. He showed that the wave function can acquire f:({ an extra phase factor even though the final state i!; identical to the initial ~~f state. It was soon realired that the same results should also hold for the -.-.•.• (:J: electric field (the wave function) of a beam of UghL Thus. the extra phase @: appears in classical as well as quantum-mechanical systems. In fact the f \ precession of the Foucault pendulum or the Bohm-Abaronov effect can be f i interpreted as manifestations of Berry's phase.

1\ Wheo the k vector of light is transported through a closed circuit sub f} tending a solid angle D.r2 at the origin, the right polarized light acquires a =f.

phase factor :.-.: -: ,., ~r= .... (5.56)

·..•.·..

•.· , r: wbereas the left polarized light acquires a phase factor :::::~rate cons~~::: I( where i and / refer to ilie ::~ Thls ls a ··· of Maxwell's equations, which require that the k vector and the two polarization vectors aJways form an 011hogonal triad.

!:_.~.:_::: To become convinced about th.is statement we show in Fig. 5.26 the un.i1 :::: sphere on which we can lndicate the directions of k. e 1, and ei. Suppose \ we start from point A on the sphere and parallel n·ansport the triad to point { B along the equator. We then parallel transport it to point C along a great { circle and return to point A by the corresponding grea.L circle. Al each point ..

it •: ::::::::::::~~ . :::::::::::::: ·.·. .........· .

. .-? ~}i~~~~f.

212 5 Optics Experiments )))t~=f k 1 . >1J11i !!

/ it I .. ((i)ij \!if~ -::;:/~:~ ,,, / .: i1 ' ' ' ' / , / ·:)\}~j 'm{){{~ FIGURE 5.26 Parallel transport of the triad of orthogonal vectors k, e 1, ei along equator and. two great ~ircles. Note that k returns to_ its initial position but e1 and ei ar~\{~ rotated by 90°. The solid angle enclosed by the path 1s 90°. ·.}}:~~~ .' .::::::::f=lt .))}j we have shown the orientation of the triad, and it is evident that upon re~m.)jj@ to A, the k vector has not change~ but the e1 and e2 polarization vectors\){~ w~·\f~ have b~ rotated by 90°. The solid angle subtended by the path that )/~m ez ..

fol1owed IS 1/8 of4 7f Or 1C /2 =. 90~ eq~ to ~e ~bserved ro~tion of e1, /{:~f Let us now assume that the mc1dent light 1s hnearly polarized along the . F E (5 47) . ·.·.·.·-~ x axis. rom q. . we can wnte {{~ .\JJ · - _l + Em - Ex - (ER EL), · :::::::::x ////ill ~~;tmpleting the circuit, we will have according to Eqs. (5.56) and ::::::::::: }~)i~i~ :::::::::~ \JI However, this corresponds to linearly polarized light at an angle :-:-:•:..-: ¢ = ½ [ ~Q - (-b.Q)] = b.Q (5.58) :ft II with respect to the x axis. The argument is exactly the same as that used in Fig. 5.20. :?t To carry out the experiment we must find a way to adiabatically change '/II the orientation of the k vector. This can be done roost conveniently by }·,J·r. .• injecting the light into an optical fiber and then laying out the fiber on the desired path. One must use a single-mode fiber in order to preserve the ./} J: polarization of the light and the path must be continuous (i.e., no kinks in ..

'% ::::;: ·.·~4.. )}~ . -:::;: ...·....•....

........

?ii '$(.·.·.

~:-:- ~:::· r::>

## 5.8 Berry·s Phase

r :::> 'Z-..

~-:-:- t:::: r:-:- ~=:::: ' r ~-:-:• ' ~{/ '-+----'_,_,-.:,"-"-+---' ?[:-:•,• e -L- ~:::::-· K:· t/ · FIGURE 5.27 Layout of the fiber winding on a cylinder. Here the fiber length is s and the ~:} radius of the cylinder r.

(r'..··..··.. · ~ f = f :: / ::. ~ the fiber). For instance we can wind the fiber on a cardboard tube as shown f ( ·in Fig. 5 .27a. If the radius of the tube is r and the length for one revolution (,'.·.>· (the pitch) is£, the winding angle 0 is given by .- ..• .· •/:•: z-:· = e;s = )£ + :~::=: cos0 s 2 (2rrr)2. (5.59)

:•:-:,:, J\ The solid angle described by the fiber is then :=::::.

f> = = L\Q 2ir(l - cos 0) 2rr(l - f/s). (5.60)

f / [:· The experimental setup is relatively simple. A HeNe laser beam is polar- f { ized and injected through a fiber coupler into the (single-mode) fiber. At the :::::- ..

.,.

450 OD +I+ • C a 1!

400 t • 0 CJ • • 350 · • a• tJ lit • • a • • 250 0 D ::::: a • 200 • • 150 CJ .... a • • a • • D a ti 50 a 0 a a • • o--_.a_O_ _,,,..__ _ _,__-----".___ _ a Q JJ_ _._ _ _ • _ .,.!.!~ :,_._ • _ _ _,__ __, 0 50 100 160 200 250 300 350 400 Ro!atlon (Degrees)

· · · FIGURE 5.28 Results from a measurement of Berry's phase. The transmitted intensity is · · shown as function of the angle of the anaJyzing polarizer. Open squares are for the flat 0.

topology, fiJled squares fot helical winding. The polarization has rotated by 245° between the two measurements.

Iii ~4 5 Optics Experiments end of the fiber the light exits through another fiber coupler and is analy~~=~ by a rotatable polarizer and a photodiode. We use two configurations;_:ottff ~til~ in which the fiber is wound along the cylinder and the other when the aiiktiJ is laid out flat on the table. The detected intensity as a f Wlction of the w®.\f of the analyzing polarizer is shown in Fig. 5.28. The open squares obtained with the flat fiber, the solid squares with the helical winding.:W.1~}} see that the polarization has rotated by 0 245° ( or it could be 115° in·-~$,{~ )\ft,~ opposite direction!).

In this case the radius of the cylinder was r == 14 cm and the P.~¥~{~ .e = 28 cm, for one complete tum. Thus s = 92 cm and : })/t® '\{}t@.

= = ·:))@j

## 6.0 2Jr(l - l/s) 4.37 sr

·. .· .·.·.·@···I·~ T~us we exp~t a rotation angle </> = ~Q = 251 ° in excell~nt agree~i#f tb~t f with observation. ~ne shoul? repeat the measurement by making more one turn on the cylinder (using a longer fiber) to fully confirm Eq. (5.53}/::::J More details on the first demonstration of Ben-fs phase with an opti~~/@~ fiber are given by Tomita and Chiao ( 1986). · )){f1 5.9. REFERENCES M. V. Berry, Proc. R. Soc. London Ser. A 392, 45 (1984).

M. V. Berry, Phys. Today 36 (Dec. 1990).

A. Tomita atld R. Y. Cbiao, Phys. Rev. Lett. 57, 927 (1986). :;:::::::~ :)i~~~i~ .;::::~=~ .·.·.-.•..

::::::::: -::::::;: ;:;:::;; :::=:=:= -:-:-:-: :: ::::: )} ·/~=~ :-:-:- .·.·-· .))

·.-...

\\~ ..: :

## CHAPTER

High-Resolution Spectroscopy In 1896, P. Zeeman observed that when a sodium source was placed in a strong magnetic field, the yellow D lines were split into several com ponents. Faraday had performed the same experiment some thirty years earlier but had failed to observe an effect because of the low resolution of his spectrograph. We also know from Chapter 1 that even in the absence of a magnetic field the atomic spectral lines have a fine structure that was eas ily observed with the smal] grating spectrometer~ with a high-resolution instrument, however, it becomes possible to observe that each of these fine structure lines may again be resolved into closely spaced components, which form the so-called hyperfine structure (hfs) of atomic lines. 1 1To set the reader at ease, no further splitting beyond the hyperfine structure has been observed, nor can it be expected for free atoms; in the hyperfine structure we include both the splitting due to nuclear spin and that due to the isotope shift.

1111t ~6 6 High-Resolution Spectroscopy '• the(/~ The splitting of a spectral line is a consequence of a splitting of en~rgy of the ~tial state, of the final state, or of ~ot_h states betw~~{JI Wit which the o:ans11Ion takes place. The_ energy-level splittm~s produced the application of an external magnetic field B (Zeeman effect) are on ~~)/~ order of _) \/:~::'~ e e fi .-:()}jmJ = = - (6.:~ff~ AE µ, · B L · B -B, r-v 2me 2me .··:::::::::;:·I where µ, is the 1nagnetic moment of the state (see Section 2 of this cbapte~i/f~ The constant JJ,B = e1i/2m = 5.79 x 10- 11 MeVff is called the BoW:}JI magneton, so that in units of wave numbers the displacement for one B~i#,(}i magneton is · -:::::::::~~ ><J~lp Av= - Av = - A E = - e - B == 46.69 B m- 1 (6,Z ~::: [ :::= J :==-~ ~ ~ c he 4n:mec ·:::::::::::.;:~ ) iii or )!!!?Ji Av 14.01 B GHz ·m B . sl ·-:-:-:-:~:.~.;:·: w1 m r1('e a. :\::=::::::?.a:::: . The hype~ne structure splitting is due to the interaction o~ the magneti¢;{/@I }i=~lli dipole, electnc-quadrupole, etc.~m oment of the nucleus, with the electrQ_f magnetic field produced by the electrons at the nucleus. The interactio~./:/@ :\}ff energy for the magnetic~dipole terms is of the order of . · c; ), !~;?

/.lN/1,{\)

= = M P.w(B1(0)) - where µN is the nuclear magneton en /LB = = µN 2mN 1837' at\iij and (BJ (0)) is the expectation value for the magnetic field oft he electrons ft the origin; it is equal to µ, B (I/ r 3 } ( except for configurations with i = Of f Instead of evaluating {1/r3 ) we recall that the fine structure splitting is(Jfi 6{\W -due to an L · S coupling of the electrons, and therefore is of the order µ,1 (l/r3 ) so that we expect ·\:J~ --11rnire A E(hfs) r-v L'lE (fs). (6 4),:?::::~ . ·:=:::?W.

-::::::)'~ ··:-:-:~::-: ::::::~~ flt

## 6.1 Introduction

6.v (Zeeman),...., 46.0 m-1 • and since2 6. v (fine stiucn1Ie),..., 104 m-1 , we find that ~v(bfs),..., 5.0 m- 1 1.5 GHz.

Thus the splitting of the lines is very small and can be observed only with a high-resolution instrument. Assuming .A.~ 500 nm and 6.v ~ 5.0 m-1 we find that the required resolving power is A - - = ~ = 4 le?.

6.A 6.v Sucb a resolution may be achieved in two ways: (a) With a large grating used in a high order, the resolving power of a grating is given by ....

>..

:::: - =Nn .•.

-:::· 6.). ' (.;,· :~~r;~~=:~:o~~:~:~.~eb:u~~~g:fa~:1.~f~a l~-~· :::- fo!~!

· · that :::: }( ::::: ::::· ::::: j ~~~!n~:~::i:l;~ever, very difficult to construct, bul can now be (: (b) With a "multiple-beam" interferometer, the most common one today ,.· \· and easiest to use being the Fabry-Perot. which was discussed in Section .., .· ;::: 4.6. One can directly observe the "rings" of the interference pattern for :~:: a diverging beam. An optical filter or a dispersive element is needed to select the line of interest Alternately one can use the Fabry-Perot in the '.:__i_:jl. . :: "scanning mode" by moving one of the end-mirrors, through half a wave length, and observing the transmission of a collimated beam. For instance a Fabry-Perot with 5 cm spacing has an FSR (free speclral range) of 3 GHz; Ill!

2 = = See Section 1.6.3 and recall that ii v / c I / >...

~;:: ~:::.

/.•., \}J{J.

i/f /if 218 6 High-Resolution Spectroscopy : even with modest finesse F 100, the resolution (see Eq. (4.62)):ift{Jf ~ v = 30 "MHz. Thus for 1 = 500 nm, namely v = 6 x 10 14 Hz .:<Jfif/f J tw.

..

( :.;-:-:-f:-i:i-:/-1:~ ;V 7 2 X 10 • In the following two sections the Zeeman effect and the theory of hyP~{ f~ fine structure are discussed in some detail. We also discuss the isotope shifff{~ ~:..,J.. JW :/.:~ and p~esent data on the s~ft between the spectral lines of hy~r~gen ~fJ ~ deutenum. We th~n des_cnbe a ~easurement of the Zeeman splitting of ]t~J.

?46.1-run green line of Hg, using a Fabry-Perot etalon. The ~~al sec~~~f usmtt~j 1s devoted to a measurement of the hyperfine structure of rubidium ·./?Jffij Doppler-free saturation spectroscopy.

~~)~@i The bibliography or: atomi~ s~ctroscopy is vast an~ because of "reach" of laser expenments 1t 1s kept up-to-date. A hst of suggeste4(:~I ··/!IM~ references is given at the end of the chapter.

i/1 6.2. THE ZEEMAN EFFECT ·.·.·.·.-,-.W, :I }/tim if 6.2.1. The Normal Zeeman Effect As already discussed in Section 1.4, the solution of the Schrodinger equa:.'.:\\ ~ tion3 yields "stationary states" labeled by three integer indices, n, l, and;)/~@ m, where l < n and m = -l, -l + 1, ... , l - 1, l. For the screened})iJ ... ·:.:-:: Coulomb potential, the energy of these st.ates depends on n and l but not)) t on m; we therefore say that the (21 1) states with the same n and l index.:}JJ are Hdegeneraten in the m quantum munber. Classically we can attribute.-{)$ .·.·.·-·;.• this degeneracy to the fact that the plane of the "orbit" of the electron may )/:~i :i)J be oriented in any direction without affecting the energy of the state, since the potential is spherically symmetric. !}~ {l If a magnetic field B is switched on in the region of the atom, we should expect that the electrons (and the nucleus4 ) will interact with it. We need/ff \J only consider the electrons outside closed shells, and assume there is one }i such electron; indeed the interaction of the magnetic field with this electron ·xi 3"Quanrum Mechanics" A. Das and A. Melissinos, Gordon and Breach (1986), .}~: New York. Or any other t.ext on quantum mechanics. · }!~ 4For our present discussion this interaction of the nucleus with the external field is so ) ]

wm small that we neglect it. /.. ;: ..

':_ ' .:;~: .::~ \~ <Ii •:

## 6.2 The Zeeman Effect

µ, FIGURE 6.1 Magnetic moment due to a current circulating in a closed loop.

j} yields for each state an adclitional energy D..E, given by ......

: , ..- . . ( . :·, : : .·.. . · D..E = mµn B. (6.5)

:::::: .... : . : .. : . : . . ·. · Thus. the total energy of a state depends now on n, I, and m and the ·:: degeneracy has been removed.

~:::.

To see how this additional energy arises we consider the classical "i~~: ' analogy. See Fig. 6.1. The orbiting electron is equivalent to a current .. -.· .

::::.:.

.-.·.·. density5 J(x) -evc5(x - r), where r is the equation of the orbit and x gives the position of the electron; the negative sign arises from the negative charge of the electron. Such a current density gives rise to a magnetic-dipole moment :::: 11 µ. = xx J(x) d 3 x = - 1 e(r xv).

2 2 f.

=~:~: 5 = Por a circular orbit, the electron is equivalent to a current/ = l::i.Q/l::i.T e/T = .-.·. = ::::. e(JJ /2rr, where a> is the angular frequency a> v /a: a is the radius of the orbit.. However, a ::::: :::::. plane closed loop of current gives rise to a magnetic momentµ,= I A, where A is the a!'ea = 1 { enclosed by the loop; in our case A Tta , hence ......· :~::: . ev 2 = - eua ~::::: µ,= - rra.

f/ 2rra 2 if = The angular momentum for the circuJar orbit is L meva, hence :•:-: ::::: e ::::: µ= - L , :~ · : . . - - : . 2me ::::: ~:::: as in Eq. (6.1).

~=a:- ;(:':.:'-, ::::: ..

-;:,·-· iI ~f.J:":.:' _:)}~:}~ .--}}}~ 220 6 High-Resolution Spectroscopy /! !

However, the angular momentum. of the orbit is given by /!11 = = ....· .· ..... _ .,.,.

L r x p me(r x v), ::;:;::::::=~- so that en µ, --L= --lui, o{~~flk where we expressed the angular momentum of the electron in terms ~ quantized value L l (h /2n )uL and ui is a unit vector along the directi_(*f~t~~Jl ::::::::::f;:j of L. The energy of a magnetic dipole in a homogeneous field is ;_}}~Ji = = - E -µ, · B L · B (6i-1J?{i:ffl ' . -<?-·.•,• ·--,,.:~~ 2 me :-:-.-:-;~;-~ ::}:::::;:;:;:;ffi but the angle between L and the external field B cannot take all possi1:)\~J~~ values. 6 We know that it is quantized, so that the projection of L on th~#::I axis (which we can take to coincide with the direction of B since no o~;~:;{::]n~j = + preferred direction exists) can only take the values m -1, -l 1, ..

of\fi@~ l - 1, l: Thus th~ energ_Y of a ~articular state n, l, min the presence magnetic field will be given by ./ /~f-1 ·>:::/===:I = + En,l,m - En,l mBµn, (6.8l/:~ .·:·.·.·--.~~ where8 :H/11 en = - .

µ,s -:::;:::::::::@ 2me :::::::::;;@ :::::::::::::a:E=: In Fig. 6.2 is shown the energy-level diagram for the five states with give~{\/J 11 and l 2, before and after the application of a magnetic field B. We note(\{~~ that all the levels are equidistantly space~ the energy difference betwee~\j}J them being ) /}]

ii/II t>E ~BB- Let us next consider the transition between a state with n;, lz·, mi and on~\ \~ = = with n f , l J, m f. As ai1 example we choose li 2 and l f 1~ so that the/Ji, --:::::~i ..

.. ;:;:;.; ;:- 6This was first clearly shown in the Stem-Gerlach experiment. W. Gerlach and 0. Stern{:Jj . .· .·-~r.x :::::t]

Z. Physik 9,349 (192).

:)Jt 7The energy in the field is positive because the electron charge is taken as negative.

me in this expression is the mass of the electron, not to be confused with the magnetic:\J~ quantum number m. ::::J~ })~ :!I :::::~;:: }Ji~ ff: ~-:-:• ~If 6.2 The Zeeman Effect 221 l:::: ~-:: ~ :: .----m=+2 ~j~{ E: / . / . ~ a m=+1 (.,,.

~{( , ~ ~~r· "'~m=O En,l=Z ~::::' ',, fa m=-1 ::::·:-.· '-.i..---m=- 2 Ill/ No field With field , ~\} :'FJGURE 6.2 Splitting of an energy level under the influence of an external magnetic field.

~~-/ The le'lel is assumed to have£ 2 and lherefore is split into five equidistant sublevels.

.·.· ,;•.·.

~}.

, .•.· .

~j} (a) (b) (cl mi +2 f :·:·.

~~f· fa I ~ 1 ~ - +1 fa t1-2 o fa )t: - 1 fa r~:::• -2 i.: mm< A ff:· l ---t--<c=-- -:-:-: ;..:.;.; • ,~:. .:.:.:.• , , . •. . . .· · . . e,s___,__,

## I ----

FIGURE 6.3 Splitting of a spectral line under rbe influence of an external magnetic field.

= = (a) The initial level (l 2) and the final level (/ I) with no magnetic field are shown, I A transition between tliese levels gi'les rise to the spectral lines. (b) The two levels after I.be magnetic field has been applied. (c) The nine allowed transitions between lhe eight sublevels of the initial and final states.

~:::> ~?= energy-level diagram is as shown in Fig. 6.3: without a magnetic field in ~} Fig. 6.3a. and when the magnetic field is present in Fig. 6.3b.

\ · However, for an electric-dipole tran~ition to taJce place between two -~·-· f :.

levels, certain selection rules must be fulfilled: in particular, ~( . ~, = ±1. (6.9)

~:}.

[ j· Thus, when the field is turned on, we cannot expect transitions between the f =: m sublevels with the same l, since they do not satisfy Eq. {6.9). Further, ( i the transitions between the sublevels with L; 2 to the sublevels with ......· .

f{ [( =:::: ::=;::: ~:;;: }itII!t 222 6 High-Resolution Spectroscopy .))ff '::: :: :; :::::;:. r = additioniil!{lr l J 1 that do satisfy Eq_. (6.9) are now governed by the selection rule9 · . \ }\/1 )}lt¼ 6-m 0, ±1, (6.101::::I::I::: ~ i\1 and thus only the fr.m;Si~ons show? Fig. 6.3c are allow_ed. } Let the energy splitting m the rmt:J.al level be a, and m the final level/ :=:::~ nil{}~ be b, and let A be the energy difference between the two levels when --,,-,t}~ ~~netic field is applied. Then the energy released io a transition i 1s given by -:::::::::::~::J~ (6.n:::::f:::@:'.:-::I:~ = + E; - E f A;J m;a - m Jb· 6.~~::::,r Toes~ ener~y diff~ences f~r the nine possibl~ n:msitions shown in~~- l~J~ are given m ma?1x form m Table 6.1; x mdicates that the trans1aon forb1dd~n an? will not take place. . /:}r~ l!,kJEi At this pomt the reader must be concerned about the use of a and ~ubf(Ji~ according to our previous argument (Eq. ( 6.8) ), as long as all levels are ject to the same magnetic field B, their splitting must also be the same, an'}}~ ·-:-:-:-:-~:::~ a - b - µ,BB ::::::::~-....i ~ - - . )})~ Thus, we see from Eq. (6.11) (or Table 6.1) that only three energy,\{i\~fil II differences are possible })\~ E;-E1=A+a(m1-m1)=A+allm, where bi.m is limited by the selection rule, Eq. (6.10), to the three valuef .. / ... J ..... I .. J ... : .

1, 0, -1. Consequently. in the presence of a magnetic field B, the sing11/(l@~ -:::::::::::=m= TABLE 6.1 Allowed Transitions from ii = 2 to l f = 1 and the Corresponding Energies}))@%~ m of initial state mof final state +2 +1 0 -1 -2 +1 A +2a-b A+a -b A-b X 0 X A+a A! b A~:: b ~ i>rnire -1 X X A _ )i!!fi~I -:-:-:·.~x=· The selection rules of atomic spectroscopy are a consequence of the addition of angulai:/\@ ~omenta. _In_ this specific case the selection roles indicate that we consider only electric~}}~~ ··:::::::::~m: dipole radiation.

!ii :-:-;:'.:~ -:-:-:-~ ·:::::~.::;::; . ::::::~x;= -·::::::%

## 6.2 The Zeeman Effect

Magnet [j/i-~----~' Souroe/ t I ,.,..-1'-, ), ~ ,, a -" B l I h J ' µ , ~ J , _ ,, ? .,, µ . eBf1 ' .1 , j ..

El -- f e ®a a--- ?-> FIGURE 6.4 The pol.arizatioo and separation of the components of a normal Zeeman multiplet when viewed in a direction norm.al to, and in a direction parallel to, the magnetic field.

spectral line of frequency v A/ h 1s split into three components with [{: frequencies v_ = (A - µ.9B)/ h, vo = A/h, and ~:::.

[ ; irrespective of the values of lt and l f. Furthermore, these spectral lines ::?:_ are polarized, as shown in Fig. 6.4. When the Zeeman effect is viewed F: in a direction normal to the axis of the magnetic field, the central com ponent is polarized parallel to the axis, whereas the two outer ones are :} polarized normal to the axis of the field. When the Zeeman effect is \( observed along the axis of the field (by making a hole in the pole face, or using a mirror), only the two outer components appear. circularly polar- j.l.\._\'..

= + ized. The lines from t:.m l transitions appear with right-hand circular polarization, and from .6.m -1 transitions with left-band circular polar ization. Toe central line does not appear, since the electromagnetic field must always have the field vectors (E and B) normal to the direction of propagation.

/ The splitting of a spectral line into a triplet under the influence of a magnetic field is called the "nonnal" Zeeman effect, and is occasionally :-> observed experimentally, as, for example, in the 579.0-nm line of mercury arising in a transition10 from 1 D2 to 1 P 1• However, in most cases the lines are split into more components, and even where a triplet appears it does not always show the spacing predicted by Eq. (6.8). This is due to the 10 Note that both the initial and final states have S = 0.

Ii!·f :-,,.~·~"'~»=~1 224 6 High-Resolution Spectroscopy .. ''' .. ! -~~: . · i .. .. t ... , intrinsic magnetic moment of the electron (associated with its spin) arid/{ will be discussed in the following sections. : }@~ ·ti!!!!!~ ·}!fl~ 6.2.2. The Influence of the Magnetic Moment ti of the Electron In Section 1.6 it was discussed how the intrinsic angular momentum (spijjJIU' elec\Jff~· of the electr~ns S couples with _the orb~tal angul~ momentum of the trons L to give a resultant J; this coupling gave nse to the "fine structure?\if@ of the spectra. 11 The projections of J on the z ax.is are given by m 1, aµ~f;J~· tot4.rij: we could expect con the basis of our previous discussion) that the {Jfl: magnetic moment of the electron will be given by \i{iffif _ µ, B µ, - 1i J. (6.l~f:::\/fj ~- ......

iJ}Jll· Consequently, the energy-level splitting in a magnetic field B would be }/i@:: analogy to Eq. (6.8): \:::::~xti = (613f?:=tff· t::,.E -m1µ,BB.

. (){@~.

mag;(J@W,~~ These conclusions, however, are not correct because the intrinsic netic moment of the electron is related to the intrinsic angular momentun{{:?-~=~f .' .· . ·.•.- ;x-,-.·.

:}\l:~t of the electron (the spin) through · ~,11 = = ~s 2 2 :, S 2 2 :, SUs (6.14} total and not according 12 to Eq. (6.6). Consequently, the magnetic moment}{{{~ \i}I@If of the electron is given by the operator ~ = + (µ,n/li)[L 2S]. (6.15)

that/ff{ 11 We will use the following notation: L, S, J represent angular momentum vectors have magnitude n..,/l(l 1), ~ .1 'r,.,/Jv+T}. Toe symbols I. j, etc. (sis always}}~~:~ i ), s === are the quanttmi numbers that label a one-electron state and appear in the above\ :iJf square root expressions. The symbols L, S, J, etc., are quantum numbers that label a state.:::::::::~~.~..: '.· .·.·,:..:.· with more than one electron and are then used instead of l, s, j. .,·· .)};*:a: 12The result of Eq. (6.14) is obtained in a natural way from the solution of tl1e)\~~· :·f ·.·.·~-.. ..

Dirac equation; it also emerges from the classical relativistic calculation of the ''Thomas::::?~~:.=:: precession." · · - ::: :: .~: ~ : ..

: : . .

II

## 6.2 The Zeeman Effect

We can think ofµ, as a vector oriented along J but of magnitude µ, /1,B8 J. (6.16)

The numerical factor g is called the Lande g factor and a correct quantum mechanical calculation gives1 3 + + + j(j 1) +s(s I) -l(l 1)

= + + ~ (6.17)

g l 2j ( j 1) .

The interesting consequence of Eqs. (6.16) and (6.17) is that now the splitting of a level due to an external field Bis (6.18)

and in contrast to Eq. (6.8) is not the same for all levels; it depends on the values of j and l of the level (s = ½a lways when one electron is considered). The sublevels are still equidistantly spaced but by an amount 6.E gµ,sB.

Consider then again the transitions between sublevels belonging to two states with different l {in order to satisfy Eq. (6 . 9) ). However, since we are taking into accoW1t the electron spint l is not a good quantum numbert and instead the j values of the initial and final levels must be specified. If we l 3This result can also be obtained from the vector model for the atomic electron. In Fig. 6.5 the three vectors J, L, and S are shown, and L and S couple into the resultant J, so that J = L+S.

By taking the sqaares of the vectors, we obtain the following va1ues for the cosines P+z2-s2 i2 +s2 - z2 cos (L, J) = 2lj cos (S, J) = .

2 SJ From Eq. (6.15) we see that µ,/ JJ-B = l cos (L, J) + 2s cos (S, J).

Thus g - - µ. - - /2- + - l 2 - - - s2 + - 2j - 2 - + - 2s = 2 - - 2/ - 2 - 1 + - J2 + - s2 - - - !2 - µBj - 2j2 2j2 - 2j2 i2, 2 2 Fmally we must replace s , and L by their quant:um-mcchanical expectation values j(j 1), etc., and we obtain Eg. (6.17).

.J ill 226 6 High-Resolution Spectroscopy ·.·.·.·.·--.-~ FIGURE 6.5 Addition of the orbital angular momentum L and of the spin anguhir./:/:~ momentum S into the total angular momentum J, according to the ••vector model." · ( \/] )!f[f fff{f choose for this example li = 1 and l f = 0, we have the choice of Ji = ~(!/~§ ii = ½, = ½. iif( ii or whereas j f Transitions may occur only if they satisfy, addition to Eq. (6.9), also the selection rules for j .:)/)J = not = ~ (6.9aii/!{lij Llj 0 , ± l j 0 j ;: 0.

. ):(JJ Furthermore the selection rules for m j must also be sa.tisfied; they are the})J;; </)~ same as given by Eq. (6.10) · ··}t[~ n--..

A ~;,7 i:L.. (6.lOa):,:-:-%-'/ . . ·.·.·~?~ In Fig. 6. 6 the energy-level diagram is given without and with a magnetic-}/ field for the doublet initial state with l == l and the singlet final state, l 0-. )} t !

Six possible transitions between the initial states with j == to the fina(\ state with j are shown (as well as the four possible transitions from))

j = ½t o j = ½)- By using~- (:-17) we obtain the following g factors !f.l s=½ g=1 Z=l 1= g=i = . 1 l l 1 1=2 s=2 s=½ = l=O J - -1 2 g 2.

The sublevels in Fig. 6.6 have been spaced accordingly.

In Table 6.2 are listed the six transitions from j = to j = ½ i n anal~ 'I- ogy with Table 6.1. However, since now a b, the spectral line is split into a six-component (symmetric) pattern. This structure of the spectral line is indicated in the lower part of Fig. 6.6; following adopted conven tion, the components with polarization parallel to the field are indicated above the base line, and with polarization normal to the field, below. 14 As = ± before the parallel components have ~m 0, the normal ones /.:J..m 1.

14It is also conventional to label the parallel components with rr. and the normal ones by u (from the Gennan "Senkrecht").

## 6.2 The Zeeman Effect 72.7

TABLE 6.2 Allowed Transitions from j1 ~ to j J = ½ and the Corresponding Energies m j of initial state mj of 3 1 3 final state +- +- 2 2 2 3a b a b A+--- A - -- - -:, X 2 2 2 2 a b 3a b A--+- A- -+- 2 2 2 2 - mF+~ +1 ' -2 3 g=J -----------~ ..... .... , ' g=2 Am=O 1t Am=±1 FIGURE 6.6 Energy levels of a single valence electron atom showing a P state and an S swe. Due to the fine structnre, the P state is split into a doublet with j = and j = ½, Further, under the influence of an external magnetic field each of the three levels is split into sublevels as shown in the figure where account has been taken of the magnetic moment of the electron. The magnetic quantum number m j fur each sublevel is also shown as is the g factor for each level. Toe arrows indicate the allowed transitions between tbe initial and final states, and the structure of the line is shown in the lower pan of the figure.

The horizontal spacing between the components is proportional to the differences in the energy of the transition, and the vertical height is pro portional to the intensity of the components; the relative intensity can be predicted exactly since it involves only the comparison of matrix elements between the angular parts of the wave function.

::::::::::=::f:}.

:-::::::::::;:~ :-:-:-:-:-:-:~ ..· .·.·.·.·.·-~ 228 6 High-Resolution Spectroscopy :-:-:-:-:-:-:--*~ ::::::x:=:m ·-:-:-:-:-:-:-J .·. ·.·.·.·.·.·.

C(?h~...~• ·.{,,·.·J.·#l';· .l"tl As ~e magne~c field i~ raise~, the sep~ation of th~ components Zeem'an/:=i ues to increase linearly with the field until the separation between co~p~nents becom~s on .the order of the fine-structure separati~n (spadijf)J~]

= ~/l /:J C 1n Fig. 6.6). At this pomt the Zeeman components from the J ~ and j = ½ - --> ½t ransition begin to overlap; clearly the perturbation cau~~~({~ affe4,f~{Jj by the external magnetic field is on the order of the L · S energy and the coupling ofL and S into J; J ceases to be a "good quantum numbe~}f/1~ ~~ft~i For ~ery str~ng. fi~lds, l, an~ S become completely un~oupled, so the orbital and mtnns1c magnettc moments of the electron mteract with ~~J~~ \/}!J~ field independently, giving rise to an energy shift = - - µ B µ.. B . ·.·.·.·.·.···-:=: -6.E L · B - 2 - S · B - aL · S .:)}:}:~ fi Ii /}t~~~ :-:-:-:-:-:-:;~ = -µ..BB(m1 + 2ms) - am1ms, (6.19:f:::;~ -:-:-:-.-;.;,;~ ri~¥~}~ In this region one _speaks of the Pashen-Back effect. The reader can more details in the references, in particular in the classic text by Cond~#.J~~~ tl ..... ,._..

and Shor ey. . -:}{J~i So far we have discussed the case where the atom has only a·sin~!fJ~~ valence electron. In Section 1.6 we considered also atoms with two vale~·¢~)]~ electrons and saw that for Hg the total angular momentum J L+S, whet.if}:~ L results from the coupling of l 1 and lz and S from the coupling of s1 atid{}~ :~/@& s2. In this case the g factor is still given by Eq. (6.17), but by using L~.

and J, the quantum numbers for the coupled angular momenta. ({J~ An interesting case arises in the 579.07-nm yellow line of Hg, which· i'$:}~:~ 1.24:/@ due to the transition from the 6 1D 2 state to the 6 1P 1 state. (See Fig.

for the energy level diagram of Hg.) As the reader should verify, by using}Jj jf\~ Eq. (6.17), the g factors of the initial and final state are both equal to the Thus we have exactly situation shown in Fig. 6.3, and the line spljijfj~ into three components (normal Zeeman effect). _}{/~ -· )/?~~i~~f .·))f~ 6.3. HYPERFINE STRUCTURE ..- ::::::::::;,: strucJ~/]I Spectral lines, when examined under high resolution, do show even in the absence of an external magnetic field. As already rnentiori~~{j~ electroif~/l this hyperfine structure arises from the interaction of the atomic with the nucleus. The largest effect arises from the magnetic-dipole mome1#//@ of the nucleus, but the effect of higher order moments are also observe~//§ betwei:iifi i A related effect is the isotope shif~ which shifts the spectral lines mas:~{l isotopes, i.e., atoms of the same element but with nuclei of different :?}it

## 6.3 Hyperfine Structure

:\t 6.:U. The Effects of Nuclear Spin ~f \. Nuclei can have an intrinsic angular momentum (spin) different from 0. ){ We use I to designate the nuclear spin which can take the values (i.e., the ...- .·. l 3 :-} quantum number) 0, , 1, •... that can reach very high values for excited 2 2 -/: nuclear states. When / > we can expect that the ''spinning" charge of i:\ the nucleus will give rise to a magnetic moment (see Eg. (6.6)) oriented ::v along the spin axis 'b :::~::: ':::/ J\ .,:,:• where M is the mass of the nucleus. In addition, nuclei exhibit an intrinsic magnetization, so that in general we have ·it·.

..; :::; •;..:-. u, -{ where is a unit vector along the spin direction, and :).· .-:-:- en ......4 . = -- 1:~:: µN ~p )( is the nuclear magneton; mp is the proton mass. The numerical factor 81 ~\ :' includes all the effects of intrinsic and orbital magnetization of the nucleus }\- and can be obtained only from a theory of nuclear structure.

i?

The magnetic moment of the nucleus, µ,, will interact with the magnetic f)

field Be(O) produced by the atomic electrons (at the nucleus; Fig. 6.7). This .,.=(< interaction then results in a shift of the energy levels of the atom by the tr amount ..: . .: -.

:=:::'· ~E -µ · Be(O). (6.20)

:~j/ The direction of Be(O) is that given by the total angular momentum of the { •,r, { ·.· atomic electrons, namely, J, so that (£)

}( > 6.E '1 (Be(O)) I · J (6.21)

.f I I I 111 .

•:-:-:, ·. .; . .

,·:,-·. ____ (/ i / : 15 This gives rise to the so-called "anomalous" magnetic moment of the nucleon; for } {·ex.ample, the neutron (an uncharged particle) has a magnetic moment of -1.91 IJ-N.

:/ : Toe direction of B~( 0) is really opposite to J because the electron has negative charge.

h=:· ~:?:i::.

i./' "<·.

230 6 High-Resolution Spectroscopy //J~ ?!i{f B1(0)

-:-:-:-:-:-:-:-:-:-~ FIGURE 6. 7 Interaction of the nuclear magnetic moment with the magnetic field produ~/}Jij ......• ·?;:;:: by the electrons at the nucleus. ·._·:/;::;):~1:.-..]

..: :::/:~;:i _i~/{!l]

Thus, we expect the splitting of a level of given J according Th~(/J$ the possible values of (I · J), whicbt as we know, are quantized.

situation is analogous to that of the fine structure, where the interac{}J~ tion was proportio~al to the (L · S) term. In that ins~ce the two angul~f )j}~ momenta coupled mto a resultant J = (L + S) accordmg to the quantum_-:)tii situation/\il mechanical laws of addition of angular momentum. In the present tW J and I couple into a total angular momentum of the atom designate4f by F· ·.:::::::::.:-1 . F=(I+J). (6.22}1 ?\}l~ <ttr An energy level of given J is then split into sublevels having all possible values of F, namely, the integers (or half-integers) .. :) )~:~ Jill!

11 - ll~F < IJ+Ii- .··:::::::::~ Thus if I == ½, the level is split into two components, with F1 = J + ½} \jJ = = and F2 I - ½ (provided J 2: ½); if/ 1, the level is split into three :/ /~ = = + components with F1 J - I, F2 == J, and F3 J 1 (provided J ~ 1) ; }(i /\J etc. This situation is shown in Fig. 6.8, and we see that if J is known, the.

number of hyperfine structme components of a spectral line provides direct / \)

information on the spin of the nucleus. . \ \{ = = \)J.

If either I 0 or J 0, no splitting of the energy levels can occur since the interaction energy specified by Eq. (6.21) vanishes. This -\ j~ is to be expected because if / 0, the nucleus cannot have a dipole :)]

moment, and if J 0, tben by symmetry, the magnetic field at the origin :/ ]

- 0 :=::::::~: B (0)

e - . :-:-:-;..: the (} Using Eq. (6.22), we can now obtain the expectation value of ·:t\~ operator (I· J) that appears in Eq. {6.21); referring to the vector model ::::::: <:::::: '·.·.·,• :::: : : ·-:-:-; :,:-: ';:::;; .....~ "

. <:=~.: <·>: :•:·='"'.

## 6.3 Hyperfine Structure

A/2 (b)

F=~ 3A/2 -- - 3 A F= 2 F=~ F=!

1so 1s0 F::::2 3 : I I I l -v I --v FIGURE 6.8 Hyperfine structure splitting of a 3 P1 atomic energy leveJ, and the allowed transitions between the hyperfine structure components of thls level and a 1 So final state I=½ I= ~- when the spin of the nucleus is (a) and (b)

we write "classically"

p2 _ 12 _ J2 cos (I, J) 2/ J and replacing F2 , etc., by the quantum-mechanical expectation values F(F 1) we obtain = + + + tJ..E [F(F 1) - / (I 1) - J ( J l)J, (6.23)

where the constant A is given by A __µ, _(B_e_(O_))

(6.24)

- 111 Ill .

Note that the energy splitting between sublevels, as given by Eq. (6.23)

(and shown in Fig. 6.8), is not symmetric. Further, if we succeed in extract ing from the experimental data the constant A, we can obtain the nuclear magnetic moment if {Be(O)) is known.

The calculation of the average value of the magnetic field of the electrons at the nucleus {Be(O)), however, is not easy lo perfonn, and depends on the orbital angular momentum of the valence electron or electrons. Expressions )i/lljf 6 High-Resolution Spectroscopy found:tf{ li for the "constant'~ A in terms of the atomic wave function can be .. ;\, .·(. -:-:f-:-:f-::•~ the references {see Kopfennan).

i1~1 6.3.2. Isotope Shift }}}~:, naturJ(}l~f Figure 6.9 shows the hyperfine structure of the 253.7-nm line of mercury when examined under high resolution. When the lines are correctlj)[}~j identified we note that the different isotopes have different energies. lnd.e~~t)~~~ i#j/fl natural mercury consists of several isotopes with the abundances shown Table 6.3; the nuclear spin, n~cl~ar-dipole magnetic momen~ and electri?.?\jJI quadrupole moment are also 1nchcated. -:\{:(J~ ~#,)JI The isotope shift arises from two effects: (a) The finite mass of c~4\ Jfl n~cle~s: The nuc~eus _is much heavier than th~ el~tron, but we c~ s1z~:::::=~~~@ sider 1ts mass as mfimte only to a first approxunanon. (b) The fimte of the nucleus: The nuclear radius is much smaller than the orbit of tli~f )~~:~:~ .. , ...•,, ... z,,l electro?, b~t we can _consider the nucl~us as a po_int_ only _to a first-orci~{{J~ th~t/}~ approximation. For light elements the isotope shift 1s mainly due to ?f t~f@I effect th~ finite mass, whereas for the ~eavy elements it is mainly due th~(\Jj the fimte size effect. It should also be evident that we cannot measure th~)iJI sh~ in the energy level of _a single iso:o~e, but on~y ~e difference in shift between two or more isotopes. This 1s shown m Fig. 6.10a. .::::=:=:::=~=~:: )..=253.7 nm ..-v 199 201 201 201 F=!. F=~ F=~ F=1 2 2 ~( '\ 199 204\ 202 200 ) 198 \ F= lll I l II II 2 -0.51o/,-0.339/ ;o ; o.230 cm_ -0.507 -0.491/-0.022 0.230 tiii))]iJ: FIGURE 6.9 Higl:Hesolution spectrogram of the 253.7-nm line of natural mercury. In lower part of the figure the various components are identified and their separation from the\ );~:~i~ position of the 198 Hg component is also indicated. (Note that the 19 SHg component appear( {}~t . th th l Li ) ·::.·:.:·./·.\·:.·:-~::0 •!.

m e spectrogram as e onger ne.

'\ti~

## 6.3 Hyperfine Structure

TABLE6.3 Properties of the Isotopes of Natural Hg (2 80)

Abundance N (nuclear µ.

Isotope (percent) (neutrons) spin) (units of µ,N)

198 10.1 118 0 0 199 17.0 ll9 1 0.876 '2 200 23.2 120 0 0 20] 13.2 121 -0.723 0.38 202 29.6 122 0 0 204 6.7 124 0 0 l( b tblnthterms oftrtbe sodlutions of the Schr~dingboer eqtt huation we ·~~ust consfidther ·.·, o e e 1ec on an nuc1 eus as revo 1v mg a u . e center o mass o e :::: electron-oucleus system. This leads back to the Schrodinger equation for a stationary attractive center (nucleus) if the mass of the electron is replaced by its reduced mass m ' =mP. --- (6.25)

M+mc' where M js the mass of the nucleus. Tben the energy of a hydrogen-like level is given by = 2 2 (l _ En hcR00Z ( M ) ~ _ hcRooZ me) ( 6 _ 26 )

n2 M +me n2 M where Z is the nuclear charge. For instance, the value of the Rydberg as obtained from tbe spectra of hydrogen and deuterium will differ by (1 - RH _::::: me ) , (6.27)

Ro 2mµ where we set the mass of the deuteron md ,.._, 2m p· This will shift the spectral lines by 3 x 10-4 , which we can observe in the laboratory.

For the heavier elements the isotope sruft due to finite mass becomes very small. Instead it is the finite size of the nucleus that is the dominant reason for a shift of the energy levels. Consider Fig. 6.10b where curve (a)

represents the Coulomb potential of a point charge. If it is assumed that the electric charge of the nucleus is distributed on a spherical surface of radius ro, then the potential will not diverge at r 0, but will be constant for all r < ro. Thus the potential seen by an _electron will be of the form shown :::::::::::::~ 234 6 High-Resolution Spectroscopy (a) 6.Ej(1) (b)

Levels for r--'o" 'T""-~~--.n.in~I point nucleus h,, -::::::::::::::~ -}/1/fll -AE,(2j1- --!:iE,{1)

-::::c:,;:;;~ I ·__ /! .

(A) (A+1) ' VN ' }if@~ hv+[AE1(1)- .6.E,(1)] hv+[6E;(2)-AE,(2)] .

:::, C: t}~~~~~i inh~tlijft FIGURE 6.10 The isotope shift of atomic spectral lines. (a) The energy levels of the.

Thttt··.Jt and final states of two different isotopes with mass numbers A and A + l are shown ..

~v.y.~:~~;~9.;: dashed lines show the position the levels would have if the nucleus was an infinitely differ_#ijJ~~~]

point; the solid lines show the actual position of the levels, which are shifted by a amount for each isotope, and for each level. (b) Modification of the Coulomb potential:.~l:::~:; · ~ ~zr ; -· : : : the nuc 1e us d ue to i .. ts 1 L - U ;_ u : te si • z e. ·::·:.:·;.:·/.-.:...~. ~. ...i... ..:@:~ ..: }}}ffi.J.~~ :::::::::1:m:::- shift·:;tJI !

by the solid curve of Fig. 6.1 Ob. This leads to a significant energy -:/\}flJI~ a function of r0• Since the nuclear radius can be expressed as . ·.·.·.·.---~'.-J ro - A 113 x 1 2 x 10- 13 cm ·.·:::::::::=:::W,:=~ - . , ){{~=%~~~ where A is the number of nucleons (protons and neutrons) in the nucleui4/@filt we see that ~ro/ro ~A/3A, which can be significant. )!)}@} )ii 63.3. Meam1rement of the H-D Isotope ShKt 111:111 aif/J{::}; The hydrogen-deuterium shift is quite large and can be measured with ....... z ..

J{~f: instrwnent of modest resolution. The results presented here were obtainecf with a Janell-Ash grating spectrometer. A schematic of the spectrometer·i~fJt]t shown in Fig. 6.11 and conforms with the generic spectrometer design intro.~{:}?-t} tJ thij}f duced in Fig. 5. 13. Instead of lenses, focusing mirrors are used to image entrance slit onto the photomultiplier tube (PMT). The advantage of usin:~( }fil§ a PMT is that very low levels of light can be detected so that the entranc.~/}Ji and detector slits can be set to very narrow width. The grating had 63().\)§i Th~/fif rulings per millimeter, and the focal length of the lens was / === 0.5 m.

10'7~\rt.w spectrum was viewed in second order with a resolution A)./)... 2 x rv tl: The angle of the grating was computer controlled so that the speed at whicl{{ !'11

## 6.3 Hyperfine Structure

•<::::;:~::::::::~----------·---------- --0 ~~ Top View Mirror • • • • • -• • • --·:.-.·-·-/ ( D . .c:::::::::::::~~}~~~~~l~~~~O!-\~·------- PMT Viowport FIGURE 6.1 I Schematic layout of the high-resolution Ja.crell-Ash grating specrrometer.

## 4.5 ,----....------..--- --,,-----.------r-----,

S.5 Deuterium: .l.=655.nnm Hydrogen: >-~655.94 nm 0.5 6SS.75 $55.8 655.85 655.9 655.95 656 Calibrated wavelength (nm)

FJGURE 6. 12 The red line of the Balmer series for a source containing hydrogen and deuterium observed in high resolution. The: absolute wavelength calibration is not exact but this has insignificant effect on the wavelength difference between the rwo lines.

the spectrum was swept could be adjusted; slow speed for high resolution and vice versa. Furthennore, the grating angle was calibrated to indicate wavelength in nanometers.

For this experiment the source was a discharge tube containing deu terium and an admixture of hydrogen. The entrance slit was closed lo a few hundred µ.m, and the first (red) Hoe of the Balmer series (n; 3, n I = 2), l = 656.28 nm, was examined. The resulting spectrum is shown in Fig. 6.12 where the hydrogen line (longer wavelength) is well sepa rated from the deuterium line. Note that the absolute calibration of the wavelength scale is off by almost 0.3 nn1; this is not important in the present case where we are interested in the wavelength difference.

:{ft~ 236 6 High-Res-o.lution Spectroscopy In tenns of the calibration we find that :))\fa; f, = })!(~~~ AH 655.94 run :-:-:-:-:-:-=·1~* ·.·:•:•:•:·=·=-=* ,',.

AO = 655.77 nm. ·.::/:;::::~~· :-:•:-:-:-:-:;;~ :::::::::=::/~W&,: 4.·.·.·.· ..• ••. .: ,.; Convert the wavelength difference into frequency difference -:·:·:-:·>:·:·X,..~ .-:-.:.·:-.:.-:.-:·.~ ~~½""~ ....... ~ VH - vo = c - AD - -A - H = -11.85 GHz, ..: :::::: M :=:=:=:~ ~

## ADAH

namely, a fractional frequency change = - = .6.VH~D 1::,,.A -2.59 X 10-4. ./i!lil1 Vo A t!!II From Eq. (6.27) we expect that dVH-D = RH - Ro ~ _ me == _ 2 _ 72 x 10 _ 4 I I VD Ro 2mp in close agreement (within 5%) with the measured value.

Ji ' 6.4. THE LINE WIDTH )}!l~i~ Since we are trying to resolve very small differences between the compo .. })}~:%=:3 .·' ·.·.·.·.•.•.rZ.:I nents of a spectral line, it is evident that the width of these components·\:}:.::~;::::~ of)}J{l~ must be narrower than the separation between them. Before the advent the laser, this was a very difficult tas~ but today laser lines can be stabilize4/:\Ji@ :}:/Jf@ to a remarkably narrow width. and used for spectroscopic studies.

\\{ffi Spectral lines have a natural width given by l , (6.28}:Jiii!i~~i~ Liv b.E h I').,..- A _,. ·- . : · - . : · - .· :• . : · • · : · · * ~· · - · : · ·! · k}<, L.l. t, ~he~e 1::,,. r is the lifetime of ~e state; this is usually negligible, since atomi~) )Jw~~ o- lifetimes are on the order of r > 1 8 s. Thus ::::::: I :::=~== ~ ~v < - - 15 MHz.

~ 27t X 1Q -8 :-:-:-:·:·:·:i.·, ::\)~~~ ..

In wave numbers we find .6.v < 0.05 m- • However, external influences)/@~i~~ <{\%§~ do broaden spectral lines considerably; the main causes are as follows: <::::;:~~:=: (a) Doppler Broadening. Due to their thennal energy, the atoms in/ {~~ the){}~Ii the source move in random directions with a velocity given by i ll -:-:·:<·t=- ·\/~l;i

## 6.4 The Line· Width '1.37

Maxwell-Boltzmann distribution. Consequently, the wavelength emitted in a transition of the atom is Doppler-shifted; this results in a broadening :: of the line, which can be shown to have a half-width ~v 10-6 ff, (6.29)

YA where T is the absolute temperature in Kelvins, and A is the atomic number "' · · ·of the element. Doppler broadening is most serious for the light elements and in sources that operate at high temperatures. For example, in an arc = = discharge operating at T 3600 K, a hydrogen line of °A 500 nm will have a Doppler width of 36 GHz, which will mask any hyperfine structure.

. . For heavy elements, as in Hg (A rv 200), ~ v 3 GHz, which is still quite broad.

(b) Pressure ( or Collision) Broadening. When the pressure in the source vapor is too high, the atoms are subject to frequent collisions, which in a way can be thought of as reducing the time interval ~ -r entering into Eq. (6.28).

(c ) External Fields. Magnetic or electric fields produce Zeeman or Stark · · splitting of the components, resulting in effective broadening of the line.

Electric fields of 1000 V/crn can cause a broadening of tens of gigahertz.

} (d) Self-Absorption and Reversal. This phenomenon is most pronoun- ced with resonance lines. As the radiation emitted from the atoms in the middle of the source travels through the vapor, it has a probability of being absorbed that is proportional to the path length it traverses and to tbe absorption cross section; this will be strongest in the center of the line and weaker in the wings. The result shown in Fig. 6.13a is that the line becomes "squashed" in the center~ that is, it is broadened.

(b)

· · FIGURE 6.13 Broadening of a spectral line due to self-absorption in the source. The solid curve is the emitted line, the dashed curve represents the part of the radiation that is absorbed, and the dash-dot curve shows the transmitted line, which is the difference of the two former curves. (a) Normal absorption, and (b) strong absorption especially in the central region leading to self-reversal.

:~•11t , 6 High-Resolution Spectroscopy . If the outer lay~rs of the source are much cooler than the middl~ ones:.·j jf{ ~ ~1dth of the particular energy_ level (due to the Doppler effect) 1s smai,~t}~ m the outer layers and absorption talces place only at the central frequencyf ~ :"ith_a lmost none ~n the wi~gs. The result is a "s~lf-revers~d" line~ sho~J~~ m Fig. 6.13b. This effect 1s very pronounced m the sodmm D lines, atid::::::~ j wit!1 when it is viewed a high-resol~tion instrument~ the line exhib~ts){}~ O~~/i~ doublet structure that 1s frequently mistaken for hyperfine structure.

can verify the origin of the effect because it varies with the voltage used=t(;t/~ -:){Jffk~ excite the source.

:Ia =<?~I~ij 6.S. THE ZEEMAN EFitECT OF THE GREEN ·} :::::,:.::~~ .. =-,=:.:: .....

LINE OF 198Hg \/)f@I~ /ill -:-:-::;~~9.

6,5.1. Equipment and Alignment 546.1-J.[J~lr i~JJI We now discuss the observation of the Zeeman effect on the).. === line of 198 Hg. The choice of the gree~ line i~ d~e to its predominance the mercury spectrum, and the ease with which 1t can be observed. In an\:t~;?

i1({@?J@; external magnetic field, it is split into nine components, as discussed detail in Section 6.2.2. In the present observations, a polarizer parallel tc{\~{: (th~/Jjf~f the magnetic field was used, so that only three of the nine components n light) appeared. Furthermore, natural mercury exhibits in the green line a({{{( ..' · . .....- .-:-.- large number of hyperfine structure components, and each of them forms a;}}~:=::~ Zeeman pattem. To avoid a multiplicity of components in one spectral line)!\@{ a separated isotope of mercury was used as the source. Hg is well suitedf }~:~f ·,·.·.·;.·. . --- for this purpose since / 0~a nd therefore it exhibits no hyperfine structure.;:/ JJ~ 6.14/ :)l.:i.

The optical systen1 used for this investigation is shown in Fig.

smalt)Jf} The Fabry-Perot was crossed in the parallel-beam method with a constant-deviation spectrograph (see Chapter 1). The etalon and lenses-:}\/ /it/ are all mounted on an optical bench to which the spectrograph is rigidly fonns a)@{ attached. The pair of lenses L 1 the light from the source into :{1§1 parallel beam, while the pair L2 focuses the Fabry-Perot ring pattern onto the spectrograph slit; the effective focal length of L2 is 8 cm, and a furthe1"<(i~t }@f magnification of 2 takes place in the spectrograph.

The discharge tube is mounted vertically, as is the spectrograph slit; the}jff slit width was J. nun. It is clear that in this arrangement not only is the ring}J/ pattern focused onto the spectrometer slit but also the image of the source.}Jf }ff A sheet of Polaroid film that could be rotated at will was used as a polarizet.

/·.~xr.;,=...,• ····>:.' .~ --:

## 6.5 The Zeeman Effect of the Green Line of Hg

Spectrograph slit In L1~ Source focal plane of etalon projection system Polarizer '\, t".::: - Etalon -- t----o----l --.:: .::. :: .:: .:0: ; < -- - -- --1,,..,...

-5 --+1/ Constant +S.S deviation prism I Doublets Slit to admit only I I I distortion<1 % light produced in I I uniform field Field-current I I control 1I Excitation coll ,.........L._ Position of (to r.f. oscillator)

photoplate FIGURE 6.14 Experimental arrangement used for observing the Zeeman effect with a . Fabry-Perot etalon, crossed by a constant-deviation prism spectrograph.

FIGURE 6.15 Optical arrangement for aligning a Fabry-Perot etalon. Rough adjustment is made by viewing the image formed by L2. Final adjustment js made by viewing the etalon from the point F (or F').

The spacing of the Fabry-Perot etalon is t 0.5002 cm; namely, the free spectral range is FSR 30 GHz. It is important to adjust the plates carefully for parallelism. This can be done either by viewing through the spectrograph with a frosted glass in the focal plane, and adjusting for the best quality of the pattern, or by a much more sensitive arrangement as shown in Fig. 6.15. A very small aperture Oess than 1 mm in diameter)

is placed at the position of the source and illunrinated with an intense sodium lamp. The Fabry-Perot plates are adjusted to be normal to the optical axis by bringing the image of A reflected by the etalon back onto A. Next, L3 is adjusted until a series of multiple images of A appears when the observer is located at I; the plates of the etalon can then be roughly adjusted for parallelism by bringing all the images into coincidence. The final adjustment is made by removing L3 so that the observer locates his eye at F (or a mirror can be used); then fringes of equal width do appear :?:::::::::~ \!i!)l~ 240 6 High-Resolution Spectroscopy --:::::::::/~ 1.8 1.6 - 1.4 0.

E 1.2 - . /id E 1 -::::::::;:;~11 0.8 ' :}'.){:~

## 0.6 }Jj

## 0.4 : !iifj

0.2 ,:::::::::::::=fil -.:i!!!ttfm 2 4 6 . . 8 10 12 14 Magnetic field B (kG) -:-:-:-:·Y·:-~ ·<:;:;:;:~::~ FIGURE 6.16 Calibration of the electromagnet used in the Zeeman effect ex:perime~~)!.r?.l~ }:/i??i The magnetic field is plotted against current; note the saturation at high fields.

<iii ~~)}i:i!

parallel to the base of the wedge formed by the two plates. As the plates whoX~(@t} moved into parallelism, the fringes become broader and finally the of /{:J image of the aperture A seems to have a uniform illumination (bright dark depending on the exact value of no = 2t /A). It is equally impoJ'ta:·I,.i ,·j _J,.: . } ·.·.·. f . :" .;~-.?·-.

plate{//t that the ring pattern be in sharp focus at the plane of the photographic -~/;i@J For this experiment Kodak Royal-Pan film was used.

The electrodeless discharge tube was placed in a magnetic field. A smalf/:\J pi:o}}Jt iron core electromagnet powered by a 220-V DC supply was used to duce the field. The diameter of the pole faces was only I ½ i n., and a sma.1¥/}~f gap<½ in.) was used. By tapering the pole faces, higher magnetic field$(@} /t~ can be achieved but this reduces the effective area of the field as well af anJfj~{ the homogeneity. The magnetic field was measured with a "flip coil"

the calibration of field against current is given in Fig. 6.16. It is seen th~}J~ ..... .,--:,.

\{J:: field strengths of 1.2 T could be reached.

??!iii 6.5.2. Data on the Zeeman Effect ·:{{]; .·\)ti th¢-\i The data presented below were obtained by students. Figure 6.17 shows 546.1-nm Hg line photographed at various magnet settings. As explaine~{} .< 11 <:::::::::::::~~

## 6.5 The Zeeman Effect of the Green Line of 198Hg

(a)

(b)

(c)

(d)

<i: (e)

FIGURE 6.17 Fabry-Perot patterns showing the Zeeman effe<:t of the green line of mer cury. (See lhe text for additional details.) (a) No magnetic field applied ~) A magnetic field of progressively greater strenglh is applied. Note the splitting of the original line into a triplet of increasing separation.

earlier, the source contains a single isotope, and the polarizer alJows only the observation of light. We note that the fringes are rather broad, but 1r it can clearly be seen that when the field is applied the single-line pattern breaks up into a triplet, the separation between the components of the triplet becoming Larger with increasing field.

The initial step in the reduclion of the data is the measurement of the diamelcrs (or radii) of the rings. To this effect a traveling microscope was used, and readings were taken directly off the plate; care must be taken to ensure that the travel of the microscope is indeed along the diameter of the rings and that the crosshairs are properly oriented. When the fringes in the pattern are as broad as those in Fig. 6.17. it is much more accurate to measure the two edges and take the average ralher than try to set the crosshairs in the center of the fringe. The ring radii squared in the absence of the field provide the calibration of lhe data.

242 6 High-Resolution Spectroscopy 0.4 0.3 0.2 - ::/ttJ - 0,1 ./ )J{t~~i ·\ll - 0.1 -0.2 ·::::::::::w \)/~~: )@J~ - 0.3 Jill - 0.4 0 2 4 6 . 8 10 12 14 16 Magnetic field 8 (kG) . ::::::::~ : (sel}~f~ FIGURE 6.18 Results obtained on the Zeeman effect of the green line of mercury tbf@~ f ~xt). ~e o~served displ~cement of the ~ ee components from the zero field value (of }:J~::]

smgle line) 1s plotted agamst the magnenc field.

Iii A(fffi~~?, Next the radii of the rings for the exposures taken at 1.0, 1.5, and 2.0 were analyzed, and it was found that the central line is not shifted. However,;)JjJ }):/Ifif the following shifts are observed for the outer rings for the LO-A data: = = 6v+ 6.81 GHz 6v_ 6.60GHz.

The complete set of data is plotted in Fig. 6.18, and we see that as predicted}}l~~\ _·/i/Jt,} the spacing varies linearly with the field, yielding ,:::=::::?-?-:: b.v = (7.2 GHz) x B(T). (6 30) -:-:-:-%-:-: · ·!i@lN The green line of Hg (546.1 mn) connects the S1 state to the 3 P2.::ffil~j Its Zeeman splitting is shown in Fig. 6.19 where the g factors have been}fAf§: calculated according to Eq. (6.17). Since the polarizer was set to selecf\f f only components arising in transitions with ~m 0, we expect to observe/ ji; .)jij~t only the three central components, which will be separated by ~~8 µ,: = = 6v (g,- Et )B B. (6.31} )!f.}i ·:::=~:=:: Cl

## 6.6 Saturation AbsorJ}tion Spectroscopy of Rubidium

3s, / ----4(--- ', . ' mF+2 ...

.,,. +1 g=J .....

~m=O 1t r t t I I I I 1 I .1.m=±1 cr ( FIGURE 6.19 The Z.eeman multiplet splitting of the 546.1-nm green line of Hg. It arises 3 3 / from a S1 to P1 transition.

By comparing with the experimental result of Eq. (6.30), we obtain µ,B = 5.95 x 10- 11 MeV /T in good agreement with the accepted value of µ.,B = 5.79 x 10-11 MeV /T.

.· From these data we conclude that indeed spectral lines are split into com :' ponents when the source is placed in a magnetic field. Further, the splitting :: observed was in excellent agreement with the theory of the anomalous :. Zeeman effect; the normal Zee,nan effect can be exclude~ since the energy .· di ffe re nee between the components of the line was not µ.,BB but ½µBB; ·. compare to Eq. (6.1).

. 6.6. SATURATION ABSORPTION SPECTROSCOPY

## OF RUBIDIUM

:: 6.6.1. Introduction :· We mentioned in Section 6.4 that if an intense spectral line is passed through a region of dense atomic vapor of the same element it may become absorbed {ff~~.---: ii////i : 244 6 High-Resolution Spectroscopy · ' .}{}~j t!)ff \~ at the center of the Doppler pattern and develop seJf-reversal ( see Fig. 6. ~ fte.e:::::::. .

We can take advantage of this effect to make measurements that are '·, ..· .·.·-½c~.- ~ •' from the Doppler effect · }\}}~ tf¥/i~ Consider a rnonocbrom.atic (laser) source of which we can sweep ~t!f{~ ~equency. This i~ easily a~hieved with 1:11any la~ers and in_particular diode 1:15~rs. as discussed m tbe followmg s_ect.J.on. ~e light (the pu~)J~ liit~:=:=~~: beam) 1s mcident on a vapor cell and tuned m the region of a strong from the ground to an excited state. If one monitors the transmitted ligh{~t&~ a function of fre~ncy,. a ~ppler-bro3:'1ened absorption spectrum, su(/~~ :(}J.~ as shown schern~cally m Fig. 6.20a, will be obse1:"ed..

c~V.ti~ Next we take light from the same source and direct 1t through the t~f}i~ in the opposite directi~n and monitor the trans_mission at D2_- ~s is 6?;{JWI~ probe. beam~ the e~penm~~tal arrangement bemg as_ shown m Fig.

The signal at D2 will exhibit the same general behavior as D1 except th~~:;:~~ )Jtfflj there will be a sharp spike at the center of the profile: see Fig. 6.20b.

.·.::;:};~f.W.: ,,,.::::~:=~~2~ ·)!!ii~ (a) (b)

"o ·<<J~ . ::\::;::I=:-l~i/lflfi ti ------+---_.

_:{ttli ]ii!fll ·.· ::::;:::;::~1;E:=:: .- :, : ,:.:-:-:-;:..-,:0·-· t1jf/J/i~ FIGURE 6.20 Absorption profiles of a resonance line: (a) The pump beam and (b)

probe beam.

Grating spec,t.r,o,,m, eter D t~ ~"!..

saturated absorp1ion :::::::::;:;,~ \ D1 _.)}}~ Pootod4/i}l~ J Lens o/)(?§~~ ·-:-:-:•i'l ~ Dopplerbroa~ned · :::::::·~; .({Jf% absorption -:-:-:-:-:-=-W FIGURE 6.21 Schematic Jayoot of the saturation absorption experiment. .- .:: : : :::::~~:;~~ \\~@ -:,:-:-~~~ YiJ@ -·-:-:,;,-;.;.:~ .\iJfj .-:;:;:J*

## 6.6 Saturation Absorption Spectroscopy of Rubidium

Let us examine what happens when the pwnp beam of frequency v+ (refer to Fig. 6. 20a) is mc1dent on the cell: it excites atoms with a particular : velocity V+ moving toward the wave vector of the laser beam. When the pump has frequency v_ it excites atoms that move in the same direction as the wave vector kp with velocity u_. At vo the excited atoms have no velocity component along kp. 111e probe beam bas the same frequency as the pump at all times but its k vector is opposite to kp. Thus when i = vi v+, the atoms excited by the pump cannot absorb photons from the :: probe since they are moving in the V+ direction, namely along the probe i = = wave vector; similarly when VL v_, However, when VL vo the atoms that could absorb the probe beam are a.lieady in the excited state due to the •' i.: presence of the pump beam. As a result there is less absorption and a spike appears in the profile when v sweeps through vo. The spike is very narrow !.=_=:.

as compared to the Doppler profile.

==· :=· The situation becomes more complicated when there are several lines :=: (that is, hyperfine structure) under the Doppler profile. For a single line of ::: ::: frequency vo we found that the spike appears at vo. For two lines present ::: ::: at vi and v2,, one will see spikes noL onJy when the laser frequency reaches ::: VL = v1, vi but also wben 17 :-.

:> = + ·=· VL (v1 v2)/2. (6 32)

iii ~~:.

spikes are "cmssover" lines and a,-e often sttonger than the d~ect Saturation spectroscopy can be easily observed in rubidium, cesium, and sodium and is used to lock lasers to a narrow frequency. For a practical ::: ...

{ 17Note 1hat if for the laser frequency '-'l the Doppler shift (for the pump beam) by 11 class of atoms with velocity liq is va, then I.he state that is excited has frequency v 1 wbere ..

;.;. . Por the probe beam the effective frequency (for this same class of atoms) is ::·.

r::· .

r If this frequency happens to correspond to another atomic transition, say at frequency ''2· then the absorption will again be saturated. Therefore the condition is •.· •.

:;: :::-· :::, or ::;.

•, :-::: { as given by Eq. (6.32).

·.,,..•. , ·.-·.

:.;.• if ::::: f.

246 6 High-Resolution Spectroscopy :1~/i.l. f ,.c.oooo, :t\=:::=r apparatus that can be used in a teaching laboratory, Thorla~s ?1ar~~f{~ complete setup to demonstrate the effect. An excellent descnptJ.on offfie experimental details can be found in a classic paper by K. B. MacA@:@* A. Steinbach, and C. Wieman, Am. J. Phys. 60, 1098 (1992). ·:::\:/::::: ·./)it}~ JJllfi~ 6.6~. The Rubidium hfs Spectrum Rubidium is an alkali (Z 37) with a single 5s valence electron o~~~~ , the _cl~sed shell o~ krypton (n = 1, 2, and 3 fully filled, 4s 24p6 ). N~f ::/t:1~· 1.

rub1dmm has two isotopes ..

··.·.·.·.··:-::p-,&; ..

85 = ~ :\ii!i{~~LI·.

Rb with nuclear spin J ··/\:i~::1 87Rb I = 3 ·:)/f~~~ 2.

-:-:-:-:-:-:•:1-:~ <h~)gij~ In the absence of nuclear spin the ground state is a S1 /2 state and 2 2 include4,J~f~I excited states are P112 and P3/2· When the nuclear spin is ·;f }@j~ energy l~vel diagr~ is a~ sho':n in Fig. 6.22. .

We will work with a smgle isotope, Rb, and cons1der the transillc~~ from the ground state to the P312 excited state. In this case the ground ~~/, )ijii!iil -F=4 -F=3 .·.<·>:-:-:-:-:-~ /i!/il 121 MHz 267MHz ro-7-2 15P312!

63 MHz ~157Mliz ~ 2 -- 1 ?.9 MHz 72MHz 0 ·.·.·.·.·.·.·.·-m: §;J - F==2§;]

02s780.23 nm --F=3 D2=780.23nm 5P112 818 MH7. 5?

- 2 - 1 >}ill .··:::::::::;~~ t~:::::!!:J F""3 }!i)~ 3.036G'H:z :::::::'.:~=~ 85Rb (72%) 87Rb (28%) .J '.

:f .: ;.: ..l ''}; .

.·.·.-.,.~;,,•.•,; 85~li!:}~~t FIGURE 6.22 Energy level diagram of the low-lying atomic states of rubidium: (a)

Md~)~Rb.

:::::?% .11;f1@m :r.:-:•.

f } ~::::: [ ( ·· 6.6 Saturation Absorption Spectroscopy of Rubidium 247 ~::::::- , ...... ·.

\has two F levels ..J,r'..-·..·· ..

.r. .. ·.· i:':=::: = = ~::::: F 3 and F 2, r ..· .·.

~=:::· r ..• .·.

r. .· .·.

( ::-whereas the excited state has four F levels ..: -: r~: -:-· ~:\ = ,.. ..· .· F 4, 3. 2, and 1.

~:::::: ~:?:-· ..

f (.As can be seen from Fig. 6.22 the bfs in the ground state is quite large, of :?,~\the order of 3 GHz, so that one can tune the laser to select transitions from ,.,.. .. ·.· = = t{either the F 2 or F 3 state. Obviously the P1;2 state is too far away l /to cause confusion. However, the Doppler profile, which is of the order t •..

t/of 1.0 GHz, covers all four hfs levels of the excited state. Recall that only [ \transitions with ..6. F = 01 ± l are allowed for electric dipole.

,:-:-:- ~:::.· The ]aser frequency roust be at 780.23 nm, which is in the infrared. It {\s conveniently obtainable from a diode laser. The diode laser is mounted f\n an external cavity. which is used to select the desired wavelength and {\tan deliver up to 10 mW of power. Usually it suffices to send 3 mW to the ~)pump beam and only a tentb of that to the probe beam.

~,•,1:":.·::.

...

:.. : 1~-:-: ,:. .: -:-:-: ;.-:-:-:-:-: }{6~6.3. Saturation Absorption Experiment :::::::::: \~{\\fne overall schematic of the experiment is shown in Fig. 6.21. The diode / \ ~ser is mounted in the heat sink on a thermoelectric cooler to adjust its '.I",",·.·.· / \ ~mperature. The cavity is completed by a grating that returns the first-order }}4iffraction peak into the laser. Thus, the frequency is tuned by adjusting / ))le grating angle with piezo controls.

rr:-·.

The diode laser output is a very strong function of laser temperature.

{\ Figure 6.23 shows such a calibration curve, and one selects the appropriate \ /temperature with the help of a medium resolution spectrometer. Then the ( \ piezo is set to sweep the frequency! and one adjusts the laser current to ~\ ~hift the central frequency while the pump beam is going through the cell.

(:\At some point one wil1 observe fluorescence, with an IR viewer or a CCD fa camera, or by monitoring the transmitted beam.

(: At this point one can reduce the sweep and setup for saturation absorp ( )ion measurements. It is convenient to display tbe probe beam on a scope {)vith the sweep on the horizontal axis. A picture of the observed fluores- ff • • I?:~ciegn. ce and of the saturated. absorption of the probe beam are shown in 6.24. It is always possible to run a second low-intensity beam through ·4·.·.··.

,, )/ lilt 248 6 High-Resolution Spectroscopy 40 .-----,-----.----r----....-----.-----.--- (~I)

(l)

t- 20 15 · ·\:/I:i:§11 ·j!f 10 .___ _ ___., ___ ___,_ ___ ,__ ___ .___ _ _.._ _ _..__ ___ , _- :-::::<:;::::t:::i 792 793 794 795 796 797 798 799 ·;:}{Jfilffl 1 (nm) the u~_~Jf@j FIGURE 6.23 \Vavelength as a function of temperature for diode laser {:/:~ii@ experiment. ·, ·-::::::::'.;%%~ (a) (b) ;:~ -:~ ::;:~ :~ii ~:=~ }~ffij :fl :::-::~ ·===m ,_.;~ -:·½·/ :::::?-: ·-·-·» ==:====I~~ .th.¢:=:::~ FIGURE 6.24 (a) Fluorescence emitted by the pump beam when properly tuned onto t~ Rb resonance line. (b) The probe beam signal when the frequency is swept over the entfrf \ }}J Doppler peak. The displaced curves are due to hysteresis in the piezo electric driver.

->M~ the nonsaturated part of the cell to obtain the Doppler absorption proaj¥,Jf :}J} and subtract it from the saturated absorption. :.

Data obtamed by students on 85 Rb pun1ping from the F 3 grou~iti{ state are shown in Fig. 6.25. The two prominent lines are the crossov#i~ lines [v(F' = 2) + v(F' == 4)]/2, and [v = (F' :::: 3) + v(F' = 4)]/2, aQ4it = th#lj the v(F' 4) line can also be distinguished. On the assumption that \@J sweep is linear, the position of the other expected lines is indicated.

...

...I . ,.

/!E~

## 6.6 Saturation Absorption Spectroscopy of Rubidium

~ ;~;11,i 6 High-Resolution Spectroscopy .

fJt Finally Fig. 6.26 gives the subtracted saturated absorption spectrumf 87 R b starting from the F = 2 ground state. Ag r un the prominent lines are ffi~:}: = = = = 3)l}if1 crossoverlines[v{F' l)+v(F' 3)]/2and(v(F' 2)+v(F' = lip:~f~:; the v ( F' 3) line is also evident. The location of the other expected is indicated. · )}}}=-- As is evident from the data tbe saturated abso1ption lines are very sh4¥f Thus instead of sweeping the laser frequency one can use a servo cir,aj1t/ to keep the laser frequency fixed on one of the lines (actually on its sloffe.:)l~ reaching a stability of few megahertz, in absolute terms. · :}}l~.

']J1J: 6.7. REFERENCES E. U. Condon and G. B. ShortJey. The Theory ofA tomic Spectra, Can\bridge Univ. Press, Cambrig~::i UK. 1951. This is one of the most complete theoretical treatments on atomic spectroscopy, buf ~~: an advanced level .::::::;;:;:;~~ • •- :.-:-:,1:. .: . ....

H. E. White, Introduction to Atomic Spectra, McGraw-Hill, New York, 1934. This book cot;1tiju-$f:: or semiclas$W~t~ :.-: extensive data on atomic spectra. and the treatment the theory is based on the approach of the vector model ··::;:::~::?« H. Kuhn. At~m,ic Spectra, Longm.an's, London, 1962. A good book on a slightly more advanced l~iff$J'~-_ than Wlute s book referred to above. .._:;}:~:::,• •~ S. Tolansky, High Resolution Spectroscopy, Methuen, London, 1947. A very comprehensive .ind !=~¢M:;:::=:½~ ··::/=:::/~ treatise on the instnunents and techniques of high-resolution spectroscopy.

i,#¢.J~ H. Kopfe.rman, Ni,clear Moments. Academic Pr~. New York, 1958. This book contains a complete discussion of atomic hyperfine structure, of analysis methods, and of the conclusi'.~.t1i-:::::=-~ obtained from it ·)){:}~ W. Demtroeder, Laser Spectroscopy, 2nd ed .. Spiinger-Verlag, Berlin. 1996. A very comprehe~~~}~ \\~ttj and up-to-date coverage of the field.

':i/!I <:;:;:::::di ··<rrtr# :111~1 @I ··~:::::::~~~ \)j{~ .}}i~ -<tti .;:;::::,:-i~ ·-:::::;:;;;.:m ):}~~ :-:-:-:-:~~ \ \}@ ..

-::::::::: /U@~j ::::::::?-.~ .)if!-1 ·\t:~i {( if

## CHAPTER

::::::: it( 0-:·:·:· :=::;::-:-:- l::::··.

Magnetic Resonance :-::·-:-:-:- ~?:· ~:::::::.

Experiments ~f( :9:,:·::: ::: ...

~f{· ~[::;::: ~:::::- ?Jt( :::::::::: :-:-:-:-· 0~--·-:-·.: ~-=:::' ~:::: ..

~:::.=::::r::::.. .

~ill; ~::::::.· x::::: :=;:,:-:- ::::::::::.

:=;:-:-:- .

:::.::::::: :-::-:-:-.

:::::::::.

x·-·.· :::.:=:::: ...

~-::: i~"}::::-:: :::;:-:-: II z=:=:· rr.·.

~{: l\··.

:::::::::.-::7.1. INTRODUCTION ~t z ...

f ( .we saw in the previous chapter that when an atom (or a nucleus), with t,/ -angular momentum L (or I), different from 0, is placed in a magnetic field ?X-·:·?.

,. B the states that correspond to different values of the quantum number m ...

?f: acquire an additional energy ,,.:-:- ~~\ .

= - 6-E Bm. (7.1)

~ :: »:::: L t~::\::- X•·.

Here µ is the "magnetic moment" of the atom or nucleus, When electrons i / ·:are involved,µ., is on the order of the Bohr magneton µ.,B while for nuclei r~\::µ.

is on the order of the nuclear magneton, µN. 1n convenient units !z.·.·.

::?::-:- ~f \ = µB / h 14.01 GHz/T ~{ 1-lN/h = (µB/h)/1836 = 7.62 MHz/T. (7.2)

l:==:: ,x..-.·.

~?: ff::: If ..- .·.

-:-· y:J;,j~ 1 Magnetic Resonance Experiments • /)!~:,,.,,,.....

>ODO( ----me=+1 e=1 a ---..-----+-me=O ----me=-1 FIGURE 7.1 Splitting of an energy level with l l into three components when.t>J~~} in a maonetic field ::;:/::::::~=~ 0 \11 = Jnif' In Fig. 7 .1 is shown the splitting of an energy state with l I its three sublevels. As discussed in Chapter 6, in optical spectro~91.f} fig,µt:~f.

we do not observe the spontaneous transitions (labeled a in the between sublevels with different "!2'. b ecause they d~ not satisfy the sele~jijij~* rule b..l ± 1. Instead the splitting of a level ts observed throughrt~t stnall difference in the frequency of the radiation emitted in the transiclf:9Si~~t i :.1 between widely distant levels (with !:t.l ±1). It is clear that if we th~~:=: directly measure the frequency corresponding to a transition betweene n~rl~ su~le_vels of the same s~te, a much more precise knowledge of the ){ti~ sphttmg would be obtained.

The selection rule b,.J == ± l is applicable to electric-dipole radiati~@t~ however, transitions with b..l = 0, b,.m = ±l do occur when magnetf.*ff f ~ dipole radiation is emitted, but the probability for such a transitio1(!~f ?~il~ 1 2 ~ reduced by a factor ( v / c ) from the case o~ elec~c dipole transition.

= ¥him o. = therefore conclude that spontaneous trans1t:J.ons with t:..l !:t.m will be very rare, especially if the system can preferentially return to::j~}Ji = ± o~~;f~~Ji ground state (lowest energy state) by a !:t.l l transition. On the ~a§iJfil hand, in ~e presence o_f an_ electromagnetic field, indu~ed transitions a probability of occurnng 1f the frequency of the field 1s equal (o r at lea$,\}:@ .·.·.·.·.·.-.......

tr~/J§.

fairly close) to the energy difference between the two levels; induced sitions toward higher or lower energy states are equally probable. Furth~)~~ tti~/}f the transition probability is proportional to the square of the strength of su.fflf }]

electromagnetic field (that is, the total number of quanta) so that if a ciently strong radiofrequency magnetic field ( of frequency vo) is availabl~fJj magnetic-dipole transitions should take place. ·.:}}}& J~ This fact is, of course, central to the operation of the laser discussed {if an4.}t~

## Section 4.1. In that case the atomic state has an electric-dipole moment

\ )§{ 1F or atomic systems v is on the order of the velocity in a Bohr orbit, namely, (v / c) 2 ~-(}~ 5 X 10-6. f::;:;:l;;;:;: :!!!if!

~::::::: ·>:··· ~{{

## 7.1 Introduction

~11\t · ~it~ctric-<lipole transitions are induced by lhe extemal electric field (at the ;~p:tical frequency) of the laser beam.

· -/\By refening to Eq. (7 .2) we see that for a 1-T magnetic field the energy ~riuttmg of either nuclei or electrons fa11s in the range of frequencies that /&11 be easily generated It is also of interest to estimate the magnitude '"(it.the radiofrequency (or microwave) magnetizing field, which we wiU '\designate by H, to distioguisb it from the static magnetic (induction) field f{:j?J; = in vacuum B µ,oH. Art H field of magnitude HY/4,r A/m~(equivalent );to a B field of l 0- T I G) corresponds to an energy flow of ft}:,;· ,------ , (l(p)- :::: t :~ J :::: ~ )=- 1 ~-O 2 l 4.7!' X JQ- W H =- -J2 x - :::::;2.35 x 1o2-2, 2 Eo 2 8.85 x 10 4rr cm h:·:··.

1)\ (7.3)

~:-:->.

ffjhjch can be easily generated. Calculation shows that this field strength is .:ii@equate for inducing transitions. Finally we must be able to detect the fact ~fifiat a tnm.sition took place; this may be done in several ways and is one of });he distinguishing factors between the various types of magnetic resonance ~-.-... .

0/:~xpenments.

if} For e~ample, in the first ~agnetic resonance experiment.' performed by '\/l. I. Rabi and collaborators m 1939, a beam of atoms bavmg J = ½ w as ~({passed in succession through two very inhomogeneous magnets A and B t={ shown in Fig. 7.2. A homogeneous magnetic field existed in the intermed.i {{ate region C where a radiofrequency (RF) field was applied. If a transition +½ ):{took place in region C from a state m tom=-½, that particular f / atom was deflected in an opposite direction in field B and thus missed ff the detector. Hence, resonance was detected by a decrease in beam current Z•.·.

~\ wheo the frequency of the RF field was the appropriate one for the magnetic .r• •• ~::::: field strength in C.

~::::: ..-:-:-: :,..,:.;- /~··· t/ m=+l ~,%a~~~~ ~~;~: ----- ~y D -- ----~~~1r:fr~m;-=:~r1t dHt D ::;:: <ii~~'r.J-.=o~----~dz~----_-:;:-;:=-l~rctor ~t :~:· ~ ~ Oven ~ )

~,.· :,.:, :::: ?; Slit .~.· f: FIGURE 7.2 The atomic beam arrangement of I. l. Rabi and collaborators used to detect f· mag.oetic resonance transitions in atomic energy_Jevcls .

·, \f .·.

:-.: . .. ·· .· ::: 0/ i/ill!if 254 7 Magnetic Re son a nee Experiments <ittt~:~~ ~~ ob.S~\if?~ Another method for detecting ~e occurrence of resonance is to ·---~~~ the absorption of energy from the rad.infrequency field when transitj~.•.j f::"l"/_.oz~ w.6stJ toward higher energy levels take place. This technique is used in magniiiif: nuclear magnetic resonance (NMR) experiments and in electron resonance (c alled "electron spin resonance," ESR) experiments. In e~lf.~} detet,f?,.: iments with atomic vapors or transparent materials it is possible to the magnetic resonance effect by changes in the polarization of th~. at@jjt.

radiation (D.m f 0) or by selective absorption effects. :()t§§~ Apart from its intrinsic interest as a way of inducing transitions berw~l~~ ~ bec~:¢,t.r the energy sublevels of atoms or nuclei, magnetic resonance has ~ .#*-~~ft · an important tool of physics. The atomic beam experiments of Rabi ~ his cow?rkers led to very precise measurements of the hyperfine stru~~@I@ w1.1:{~; of atonuc syste~ and thus to accm:ate values ~f.the nucl~ar moments ..

nuclear magnetic resonance expenment transitions are mducedH ·boetw~.~~~fir=rtfm~ the sublevels of_ a nucleus placed in an external magnetic field: the atom to which the nucleus belongs must have J 0 (d 1amagn()~'.{ and/It,){£~ material), sin~e otherw~e the nuclear spin would be coupled to J large elec~o~c magneuc mome~t would mask the effect. ~y meaanri{~~}~~:lf~{I~~~ sue~ expenments, nuclear magnetic moments are measured directly :?:::::::::I~ a high accuracy. .

·9ijfi~ The Nrvt:R signal depends not only on the nucleus under study but also the environment in which the nucleus finds itself. In fact the observatio~:§;f)W~~ nuclear magnetic resonance in solids and liquids depends on the relaxati9):ff~t%==i nucle~t~~?i.t of the nuclear spins through their interaction with the lattice. Thus, infonnatitij]flfJ magnetic resonance studies have yielded a very large amount of }\fl~t on the properties of many materials in the solid or liquid state.

Soon after the first successful nuclear magnetic resonance experime~W:{fjl]~ proton:~}Jf!f~ it was realized that the width of the observed resonance line for ~~'./I@} was mostly due to inhomogeneities in the constant magnetic field used split the energy subl evels. When a very homogeneous field was applied, ~~}/}]~~~ proton resonance line was shown to exhibit a fine structure on the order qf) {$.~i whic~\lm=I

## 0.01 G (10- 6 T). This structure depends on the organic compound to

the hydrogens of the sample belong. With even more homogeneous fiel4f )~ a hyperfine structure on the order of 0.001 G (10- 7 T) is observed. It if)~~ ····~· ...

this fine structure that has made NMR such an important tool for analyticaj(!W,:~~ . . >>=·=·=~w- eh enustry. <::::::::it~~ tran{)J!~ The term electron spin (o r parmnagnetic) resonance is used for siti~ns bet\~ee~ the Zeeman levels of quasi-free electrons in li~uids a~~\@w solids. In pnnc1ple, we should always measure a g factor of 2.00 (1f we de~,:/:~~==~~ .}}fm ·.·. i ·~ / J .... 1~ ~.r /)~It .·.·.·,~"F,1'.

~::;:·· 1111::. 7.2 The Rate for Magnetic-Dipole Transitions 255 f?

r ff t \ with free electrons); instead a great variety of g factors and structure appears in the resonance lines due LO the different effective coupling of the electron ?f with the crystalline field. These effects depend on the relative orientation r( of the magnetic field Bo and the crystal axis. Thus, electron spin resonance f:: is a very important tool in the study of crystalline structures as well as in / [! the identification of free radicals in chemistry, medicine, and biophysics.

'"··· ~:\ This chapter is organized as follows. In Section 7 .2 the conditions for ·.-.·.· f i ').

inducing magnetic-dipole transitions are discussed from both the quantum {/ ·and classical point of view. In Section 7.3 we introduce the mechanisms r :' essential for the observation of energy absorption in nuclear magnetic ~k resonance and electron spin resonance experiments, namely relaxation and saturation. We also discuss the idea of free induction decay and ~}-::pulsed NMR The techniques and results of nuclear magnetic resonance / \ .experiments with protons are presented in Section 7.4. We conclude with (( ·a discussion of an electron spin resonance experiment that operates at t/ ·microwave frequencies.

{: As was the case in the previous chapter the discussion is limited, and f( the reader may wish to refer to some of the many excellent monographs \ : and texts on this subject. A list of suggested references is given at the end } of the chapter.

l:t:: 7.2. THE RATE FOR MAGNETIC#DIPOLE ~(. TRANSITIONS ::: :\: 7.2.1. Quantum Calculation ::: ,:, :;: The experimental signals in NMR involve the participation of many nuclei.

( ln this section, however, we will consider the effects associated with a :=. single nucleus: we use the terro a single spin. We will return to an ensemble \ of nuclei in Section 7.3.

( Let us consider, for example, a nucleus with angular momentum I (mag fiJ + [:. nitude l {I I)) and magnetic momentµ. oriented along the spin axis.

· For nuclei it is customary Lo express the proportionality between the spin I and magnetic moment µ, by µ. ynl. (7.4)

where y is called the gyromagnetic ratio; as can be seen from Eq. (7.6)

:(l.

below, y has dimensions of radians per second-tesla. The gyromagnetic 256 7 Magnetic Resonan ca Experiments ----I< i µBo)

____ , (21-tBo)

~ ~ ' ------ 0 111t=+½ ----!(Jµ.Bo)

----i (i µ.Bo)

FIGURE 7 .3 The energy of the four sublevels of a nucleus with spin / = ~ whe1i;~j~ in a magnetic field Bo. Note that the energy depends on the "orientation" of the sp\1'(~".ti.ft:.

J~ = G+1). ·::)>~;~;~~==. .

respect to Bo; the magnitude of the spin vector is 111 {i!il!f ratio y cannot be calculated from a si1nple expression such as fow;t~Jq the #r~t~f. .

the g factor of atomic electrons in Eq. (6.17). (For instance, for = :\}/~J?~ y 5.586 µN, where µN is the nuclear roagneton.)

Bo, caii·fiit. .

In the presence of an external magnetic field the nucleus ~ any ·of the (21 1) sublevels labeled by m1 as shown also in Fig(?&!~ \}ftr We can then write for the energy2 of these sublevels (see Eq. (7 .1))

....

. -:-:-:-:-:;::: )~}})/fJffkI E 1 µ, ..

It = - T = Ii Bom -y Bom, =}[~11JJ1 ~o ~1at the energy difference between any adjacent sublevels (Am ·/:/:::::fl 1s simply .--:.:-:-:-:-:-:& b.. E \\::=:::?::~ - = y Bo = wo. (t6$~~ Thus for protons in a field of 1 T the resonance frequency will be = = vo 5.586µ,NBo 42.581 MHz (Bo= 1 T).

= ½~ ~-µif{[ Consider then the simplest case, nan1ely, / for which only two = +J.

levels exist, m =-½and m In addition to Bo, let a weak field_.ff.1/ ij rota~ng in a p~e nonnal to Bo w~th an angular frequency cv be introd~~~1f@ Talcing the z axis along Bo we wnte the two components of H1 as _.)>Jf _ ___< H_,>x Hx = H1 cos wt (H1)y =Hy= Hi sffiwt, ; Instead of energy, we use for convenience angular frequency; the transition frequ'en,tj}~~ is D.v == (l!i.E/1i.)/(21r) wo/2rr. ··){}{ 1/I :: =:::;:;;: ·:::::::::.

}( ~ft 7.2 The Rate for Magnetic-Dipole Transitions 257 \{{ ..-:Md we assume that ]\( µ0H1 Bo. )the additional energy of the nucleus, due to the field H1, is tl yh rn_;, ~I = /L · 81 = (H,l, + Hyly) = (l+e-tw, + Le+iwt), .,.

.-:-:-:-· (7.7)

.,,---.·.·.·.

·~=::::: '.-'.~::::: ..

Jwbere3 -::::::::·· = + {( I+ Ix i ly and /_=Ix - ily, (7.8)

~:,:::::-·.

{:.Sjnce the energy specified by Eq. (7.7) is very small as compared to that { liven by Eq. (7 .5), it can be treated as a time-dependent perturbation4 ; fttius, to first order~ the transition probability is proportional to the absolute .{#.w.iare of the matrix element re·· :::::\ . TiH = + .M. y 2 I ( flf+e-iwt f_iwtli), (7.9)

~:::: {~here i and f stand for the initial and final state. As usual the matrix .?:element is evaluated by perlorming the integral .-.·. f .,, -:)t ,.,rtf .,, = d3 d (7.10)

{/ .M ip f Jl. I ip I X t , :.:::::- :::~\f{w here :H1 is the perturbing energy of Eq. (7.7). We must include the time ~ependence of the wave functions i~:)

=~)e:7(( zl\\ :: :::: ~ (7.ll)

"\(Here primes refer to the final state, and u(l, m) stands for the time f:(independent part of the wave function. Evaluating Eq. (7 .9) with the help ;:::::- ...-- ..··..·-- -- ..· .·.·, /:: 3we expand the exponentials and obtain ~1> Ut ros a>t + i ly(-i) sin a>t) + Ux cos a>t - iiy ( +i) sin mt)

·~~ ..: : - ::- : : - :- : = 2(1.x cos mt + ly sin mt).

\ :· 4 See, for example, E. Fe:mu, Notes on Qu.an.Jwn Mechanics, Lecture 23 Univ. of :{.Chicago Press, Chicago, 1961.

i:-:-.

1?.=r ~:-:-.

~t {?-:: ~f :.

~ :::· 258 7 Magnetic Resonance Experiments of Eqs. (7.10) and (7.11) we find that j [-i ( ,v) r]

= + },/!///ltf M { (/, m'lf+ll, m) exp Ii dt J [ (E E' ) ] } :-·.·.·.·.·.·.·---~ + {/, m'II-ll, m} exp -i ~ -w t dt .){}ff . ' , )?}ti}?

(7'1:i]~ The matrix elements of the operators I+ and J_ are :-:-:.::-:-/x-.f-Jlj .. ::::::::=~==1w- 'll + + (m +Im)= ./1([ 1) - m(m 1) S,.•.m+l :i,!I (m'ILlm} =JI([+ 1) - m(m -1) Sm',m-1, •.

only co1111e4\i{fl and thus I+ connects states with m' - m . l while L = = states m' - m -1. For I ½t he above matnx elements reduce tc(l.;{~@ essentiaitfi/j~ for eith~r I+ or / __ The integrals ov~r time in Eq. (7.~2) are o atjif/% functions (but see below) expressmg the conservation of energy· <:}Jij showing that the transition probability is different from zero only if )1111 m: m = = + and E' - lilV for l = = E - E MJ form m -1, (7.13)\??i: -:::::::::;;::% )f&.

that is, when the angular frequency of the rotating fi~ld is equal to the energy/f difference between adjacent m sublevels. Using Eq. (7. 6), the condition~\;}~~~ of Eqs. (7.13) become simply }/~]

!II mo= liy Bo= WllQ. .

To complete the calculation of the transition rate we must integrate (the.)):~f absolute square of Eq. (7. 12)) over the density of final states. This leads to)/)

Fermi's o-olden rule6 ·. )Jf ~ ~ Rif = Ii IMI p(E), (7.14) i/!JJ \]

5see E. Fenni (1961), Lecture 28. ){ 6see E. Fenni (1961), or L. Shiff, Quantw,t Mechanics, Chapter s. McGraw-Hill, /j New York, 1968. }:~ }{

## 7.2 The Rate for Magnetic-0.ipole Transitions

•:•:-. p~ er / \ where R;J is the transition probability unit time (or transition rate) from l / the initial state i to the final state f. In Eq. (7. t 4 ), Mis the time-independent ~f :.

part of the matrix element given by Eq. (7 .12) ( that is, without the integrals).

~?:: p(E) is the "density of final states" and gives the number of states f per ~f ( unit eoergy interval that have energy close to E'. For example, if the final f {· -s.tate f has an extremely well-defined.energy Eo, then p(E)-+ 8(E-Eo); t\ ..

if the final state has a certain width due for instance to a finitf lifetime or if:::- other broadening effects, then p ( E) expresses this fact mathematically.

~f y...

We require the function p (E) to be normalized and can also express it in [ / -: tenns of frequency x:·:··· ;,,:.-.·.

~t = = ~f/. p(E) p(hv) h g(v)

%:;::::::: 'th r~r--·r.·. Wl ~-- j . ..

~:;:::- p(E)dE = g(v) dv = I. (7.15)

~:=::: ~f:- x:::::- ~=~\ Combining Eqs. (7.12), (7.14), and (7.15) we obtain for the transition rate l/ = ½ ·in the case/ the elegant result =:::::: ~=·=-· ~::::: y2H.2 - j- : : - - :• : : - - : , R-t/2-++l/2 = R+112~-112 = g(v). (7.16)

~=~:~· 4 ;,.:.:•.

~::::: In the above equation v is the frequency of the perturbing field (RF or ::::::: :.:.:• /.·.·. microwave). and g ( v) gives the shape of the resonance line; note that g ( v)

;,:.:-· will be significantly different from zero only for v ~ uo. Note also that ~~=~=.

~:::: in Eq. (7.16) and in the equations leading up to it, H1 must be expressed ~::: in tesl~ namely its value in amperes per meter must be multiplied by ;:-:• : , - t : . : · : . : · : - the permeability of free space µ,o. We have deliberately not included this .-.·.·.

~::::.

factor in the equations to avoid confusion with the symbol for magnetic ~~~~: moments.

~==:· -·--.· :::::: There are two important comments we want to make at this point. First f : ..... as can be seen from Eq. (7.12) or (7.16) the rotating field H1 will induce -½ +½ ~::::: = = ,,t.·.·. transitions from mi to m f with exactly the same probabi ;;:::::- = +½ = -½.

~:? lity as from m f to m, As a result, in the presence of the ,t.·.· .

..• . . . r·..· field H1 both levels will, on average, be equally populated. This argument ~~~: :=:: ~·.·.

remains valid for any value of the nuclear spin. Secondly, while we used a perturbative calculation the two-level system can be solved exactly in terms 6,".-:-·, of simple functions as described, for. instance, in the Feynman Lectures, :-~·>.

~::::.

~:::::: : .. : .. : .. : . : · . .

~:;:: ::::::· ~,,le?· .

~:.:-: /Uttt~ ://ff;; 260 7 Magnetic Resonance Experiments \\\Ii~ Vol. ill, Lecture 30. 7 We will make use of the exact solution in Section:;ij£· :{:}?f: when we discuss pulsed NMR and free induction decay.

/)jl)Jlt 7.2.2. aa~iW Inrerpnmtion :; j .c~t(~~ Below we show how the effect of a rotating radiofrequency field mi4fe~t understood also on the basis of a classical model. Consider again a with spin I and magnetic moment µ, = y Iii. Let J be the magnitude t•> '. '.f' ..~.... •,i.4] ,r:.,:,,;1 ', angular momentum, which classically 8 will be just J = nl, and let it ijj:~: an angle 0 with the z axis as shown in Fig. 7.4a. If a constant magnetic:ji,'fiJffl mag1~~,:~ Bo z is appli~d along the axis, the field will exert a torque on the moment, given by >:{:j~:: q\i.j,' µxBo y(JxBo).

T= Tiris must equal the time d;tative of the anglliar momentilln - = = -(7:~J~::~ y(JxBo).

}(?l@J.

dt ...

The solution ofEq. (7_.18) leads.to a precession of the angular mfreoqmue1em~rJt!i e.

vec:or J about the z axis, preservmg the angle and at an angular wo mdependent of 0, ·::\:::::::~ .·.·.·.·.·.·-~-~ :;:;:;::::::::»}.

ldJ/dt I . .. ··-~- WO = - - -- Dz = -y Bonz, (7. 1' .9)}~~ ·.\\(ff, l/xnzl .

where Dz is the unit vector in the z direction. · :{)}{)

This phenomenon is called the La.rmor precession and the angular:fi;~{/@.

quency given by Eq. (7.19) is the "Lannor" frequency. It is fascinati~g{@.

even though not surprising that the Larn1or frequency has the same vaiij~)i!

as given by Eq. (7 .6) for the transition frequency between any adjac¢#({~ levels (~m ±1). Further, since the angle 0 is preserved, the energy)~(\~ :/{:}J the nucleus in the magnetic field remains a constant ·:_>\@~ ~1J~]

E =-µ,·Bo= -yhl Bo cos&. (7,. 1 We now introduce an additional weak magnetic field H1 oriented)~]§~ tl\f~~~ the x-y plane and rotating about the z axis (in the same direction as: ···<{Jij ·~t~ See also A. Das and A. C. Melissinos, Quantum Mechanics, Section 5.1, Gordon Breach, New York, 1986. : :;:::::;}:;::: . " .. h.

8 = Instead of its quantum-mechanical {QM) value / n.Jl(T+1). ·:::){~~~ <:r., ) J!I

## 7.2 The Rate for Magnetic-Dipole Transitions

{a) (b)

~:::: ,.•,·· ..· 1~( -:-: •:-:, ·=·· I /:::: I t i l ;:~:!: fe----..I .i---,-.. ..

~f ,t, '\._ , /,, :ft -------- , ~ I , , jf } : FIGURE 7.4 Precession of a magnetic momentµ, when place.d in a magnetic field Bo .

.; :f . = (a) The spin precesses with angular frequency <ao y Bo; the angle 0 is a constant of the =i:: ... motion. (b) In addition to Bo a weak magnetic field H 1 is now also applied. H 1 is rotating ~: t : µbout the? z axis with angular fw:iuency wo and thereforeµ, precesses about HI with angular ~?

freqnency (1)1 y H 1 : B is no longer conserved.

:;?;:::; #',', :~{ ?:::: "Lannor precessing'' spin I) with an angular frequency w. If the frequency -f i wo, .. w is different from the angle between the field H 1 and the magnetic --.-. ;.: "{/ momentµ. will continuously change so that their interaction will average ~\ out to 0. If, however, w ::::: mo, the angle between µ, and 11 is maintained ) / and a net interaction is effective (Fig. 7.4b). If we look at the system in ;)j- wo.

a referenct:: fraIJ1e rotating about the z axis with the angular velocity \ : then the spin wi1J appear to make an angle i/1 = 90° - 0 with H and if according to the previous argument will start to pre.cess (in the rotating ~n f rame) about H1. This corresponds to a "nutation" and a consequent change ?fthe angle0._w hich implies a change in the po~enti~ energy o~the nucleus ir m the magnetic field (Eq. (7.20)). The change m 0 1s the classical analogy ~ \ to a transition between sublevels with different m. We see that (a) such d\ transitions may take place only if the rotating field has an angular frequency f } = a>o = y Bo, and (b) that the angle 0 will continuously change with tr (I)

an angular frequency WJ y H1. The effect of the radiofrequency is to ~if ?\ populate., on the average. all values of 0, that is, all levels, equally.

However, if the_ field H is ~?lied only for a short time t, su~h tb_at ~\ <.<>1 t i!, then a spm that was ongmally at an angle 8 (w.r.t the z axis) will f( l/ find itself at an angle 1( - 0 (or at aa angle 0 from the -z axis). This is -½ = = +½ .

the equivalent of the QM transition from m to m lf the field i} = is applied for a time t such that w1t 2rr, then the spin will eod up at {{ the same angle w.r.t the z axis (in the :5ame state) and so on. By applying :::··:· ~;:: ~:;:: :X:~•?.·, ~'.:: .-:.::::: ::;;: >, -:~:~:• !.-....~ .· .} :{:}}~ ::': ::: :~::::::~:-4 262 7 Magnetic Resonance Experiments ·:::::=:::=:::::=~:.-: ·::::::::::::::::~: :::::::: :;:::::::::!

RF pulses of selected duration we can thus manipulate the spin sta~{w.JJ!~ wt ·1 1 m ake use o f th" 1 s 1 'd e a 1 . n S ec 11· on 7 . 3 . 4 . - . :: . : :·.:·::.:·.:·:-:·:-:·:.::-:.«.;. .

/if/lilt 7.3. ABSORPTION OF ENERGY BY THE : _.·).·.\·.I·;•,J. .....}._ ..

## NUCLEAR MOMENTS

7.3.1. Relaxation and Saturation )

We saw in the previous section that a radio-frequency magnetic field ~Y::~:~~a elec~§n/~§~@ induce transitions between the magnetic sublevels of a nucleu~, wfilki:):r~ or atom. In the case of atomic-beam experiments the atoms are free, ;~}fl in nuclear magnetic resonance or electron spin resonance experiments nuclei ~r electrons are in ~onstan~ interaction ~vith th_eir surrou~dings. T~~r:~f~ ni~Mt~~ are ~1amly ~o ~pes of mteractions: (a) spm-lattzce, by which we t? Bo1tzm~a1I ~e 1~ter~ctlon with the t~ermal bath that tends restore the Iam_~fJil d1stnbution, wh~re _the s~m can relax by tr~s.femng ene~gy to ~e and (b) spin-spm, m which the nuclear spm interacts with a ne1ghbor»li::;:]WJj -Ai@I nuclear spin, but the total energy of the spin system remains constant.

~:f }~@ a matter of fact. it is the spin-lattice interaction that makes possible ~~/J~j observation of energy absorption from the radiofrequency field when :}\}~:~@ resonance frequency is reached.

the .of)i{f@ To understand this last statement, consider again simple case nucleus with spin/ = ½-In the ~resence of a magnetic field Bo it is spMf\f* into the two energy sublevels with m =+½and m =-½. As remark~~??~ :))//1 before, the rate (Eq. (7 .16)) for transitions (m +-21) ~ ·\i{/jfj m :=: - _21) (7.21~t/Jt 1~1, me is equfil to rate for transitions -½) +½).

( m ->- ( m = (7.21bh,<<<-· The nun1ber of transitions per unit time is given in either case by Rif Nt, where N; is the number of nuclei in the initial state. Further, transitions of ) }~~~ the type in Eq. (7 .21a) absorbenergy from theradiofrequency field, whereal{ft II

## 7.3 Absorption of Energy by the Nuclear Moments

;.:::: ...: :::: ./ :transitions of the type in Eq. (7.21 b) give energy to the radiofrequency field ~\ :(recall Eq. (7.5)). Thus the net power absorbed from the rad.iofrequency }}field is (we also multiply by the energy necessary for one transition)

t:;{::: P = [ N+112 x R ( +- 1 -+ - - 1 ) ] liwo } . 2 2 - f ::: ( :- - [ ( 1 + 1 ) ] wo N-112 x R - 2 --+ 2 ·::::: :-:-:- }( = (N+t/2 - N-112) R!uuo. (7.23)

~~:::: }} Thus if N-112 N+t/2, no net power can be absorbed from the field .

.f / However. if we consider a system consisting of a large number of spins in ff equilibrium with its surroundings, it is known from a very general theorem \ of statistical mechanics that every state of energy E will be populated :f according to the Boltzmann distribution "':-:-: ;\ N(E) Noe- Ef kT (7.24)

... ......

f:::: : with k the Boltzmann constant and T the absolute temperature in Kelvins.

\: It follows that for a system of N particles with spins I in the presence of a if magnetic field Bo, each m sublevel will be populated according to ~~:-r:- ~:?

N ( mynBo)

= + + (7.25)

N (m) 21 1 exp kT .

~~::-:::: ~:-:- The normalizing factor was approximated by N /(21 + 1), which bolds 9 ~/ << for y!iBo kT; - myliBo is the energy of them sublevel. Note that T r.·.· in Eq. (7.25) is the te1nperature of the spin system and equals the lattice ,r..··..·· ;::-: :::::: temperature, if no external pern1.Cbations (such as the radiofrequency field)

,._ .. .

,. .... · t: are present.

,_._.

fr··. It follows from Eq. (7 .25) that the populations N + 1 /2 and N - l /2 entering ,_._. = ½)

,_._ Eq. (7 .23) of our previous discussion (I will not be equal. There will r ..· .· ,r. .-.• .. · be a number of excess nuclei Ns, in the lower energy state given by rr ...·· ..

~::: r.·.· ;,:::. /iwo) - /iwo)] , = = ~::: Ns N+I/2 - N- 1;2 N [exp(+ exp (- ::~=:· 2 2kT 2kT ~~=:.

~-- ~::( ~::: 9Expand the exponential through first order. to obtain correctly r.·.

r~==: m=+l t.·. N(m)=N.

t,-;.

i:: m=-1 :,'•.-_":-·.,:' ~::: ::::: :•:• ~::~ /!!II/IL _ 7 Magnetic Resonance Experiments for abdW,/li/1~1; and si:11ce fuoo is always much smaller thank T, we may write the equation ···:::::::=:=:=::-~ :::)}_fj{~i N luvo N ~ - -- · (7 2~---·.···-~ s 2 kT . . -~:r::::::::::J,a ~·r.·..·.{·.·f.·l-l-~.·~ It is only these Ns nuclei that can contribute toward a net absorption }(?I@.

energy, and the power absorbed from the RF field is given by ://Jfa N (limo) .·.·-:-:-:,....--:-:~ = = - - - P Ns x R x fiwo x (lw>o) x R. (7 .27f})J~ 2 kT .. ·.·.·.-.. ,.,. .., .. ..

-:::::::::::~:% fotf{fff: Before proceeding fi..nther, we introduce some numerical values: protons y = 2.673 x 10 8 rad/s-T, so that for Bo = 1 T and T . 300 K w.~/i{®, ·'.)iJ!/@~ obtain · \/}tW.

- Ns = - wo - li = (2.67 x 10 8 ) x (6.6 x 10- 16 ) eV - 6 ..

~ 4 X 10 , .:::::::::::::;:~ N 2kT 2(1/40) eV ::::::::::::·-~:--/2 ··:::::::1:j furthe(/j~ij which justifies the approximation used to obtain Eq. (7.26). If we consider a sample of 1 cm 3 of water, the nwnber of protons contained ~1(}f~ . t .·.·.·.·.·.·.,.·;."/.

\/){@.

1 1S N = No (2/18) = 6 10 23 (2/18) = (2/ 3) 10 23 )!!/@ X X X X .

ff we use for R 1/s (as can be seen fromEq. (7.16), this is a conservative \ {{: value; R, however, can be as large as l <P Is as discussed below), we obtain }{i !)}~ from Eq. (7.27) · P = (liwo) x (N x Juvo) x R~ 5 x 10 10 eV /s = 8 x 10-9 W. / I!

2kTs -::::::::: <{/ (7.28)

This is a very small amount of power, especially since the applied radiofre-· <{ quency field may be on the order of milliwatts. Therefore, a sensitive null / \ -;;r method greatly facilitates the observation of nuclear resonance absorption. .

In writing Eq. (7 .27), we assumed that the power absorbed is propor- / )

tional to the number of excess nuclei which we now designate by ns; ){ <?

however, as transitions are induced to the upper state, the number ns will )i continuously decrease. The decrease will be exponential at the rate R = - Rt ns Ns e .

Soon the populations of the two levels will be practically equalized, N + 1/ 2 ~ N -1 /2, and no more absorption will be observed.

## 7.3 Absorption of Energy by the Nuclear Moments

However, while the radiofrequency field tends to equalize the popu lations, the "spin-latticeH interaction tends to restore the Boltzmann distribution at a rate characterized by I/ T1. We say that the nuclei are "relaxing" through their interaction with the lattice, and the characteristic time Ti for this process is called the spin-lattice relaxation time. Therefore, in the presence of a radiofrequency field tuned to the resonance frequency, the number of excess nuclei at equilibrium ns depends on T1 and on R; if << >> R 1/Ti, then ns ~ Ns, while if R l/T1, ns ---4 0. The value of n can be easily obtained = + (7.29)

ns 1 2RT1' where Ns (Eq. (7 .27)) is the equilibrium excess of population in the absence of the radiofrequency field.

By using Eq. (7.16) for R, we obtain Ns = - ------.

ns (7.30)

I+½ 2 y H/T1g(v)

From the above result we see that when too much radiofrequency power is used, the number of excess nuclei n decreases, and so does the resonance signal. We say that the sample has been saturated, and the ratio ns/ Ns is frequently referred to as the saturation factor Z: ns 1 + z. (7.31)

-Ns - 1 ½y 2H/T1g(v) :=: 10 Let n == n + 1/ 2 - "-1/2 be the instantaneous excess of nuclei in the presence of both radiofrequeacy and relaxation. The effect of the radiofreqoency is to make n -> 0 dn)

( = -2Rn.

dt RF (The factor of 2 arises because each transition up decreases n+ 1/ 2 by l, and also increases n_ 1/2 by 1.) The effect of relaxation is to return n ~ Ns (dn)

d(Ns - n) 1 = = - dt dt -(Ns - n) T1 relax .

EguiLibrium is reached when the sum of the two rates is zero; that is, N -n 5 = -2Rn + Tl 0 which yields Eq. (7 .29).

·:::::::::;:::::(,¾ (;-:; ·:-:-:·:-:-:-:-~ .,, .· } .·.·. f ····· t ··· - .,, Z66 7 Magnetic Resonance Experiments . . · :::=ig theref'.~fJJB The maximum use:nl ~alue of the ra~ofreq~ency po_wer depends on the relaxation tune T1. For sohds, T1 1s large (1t ~es a l~t~~~ time for the spins to reo~ent themselves in the equilibri~ position)~)t,J~~~~ therefore only weak radiofrequency fields may be applied. For exam.pf~~}~~~ forpr?t~ns in ice Ti _10~ s. In contrast, i~ liq~ids, especially in solutf~Jj{)@f contammg paramagnetic 10ns, the relaxation time for protons 1nay b~\~({~f~ short as Tt = 10-4 s. ·//:=:::::Jt#::: ·}t@rr~m ]ii 7.3.2. Line Width and T2 : . ·.·.·.·.·.-.r.~-~~.

(~~}~Jtf Just as optical spectral lines can be broadened by external factors wid~f@il

## Section 6 .4) the NMR sign.al is not pe1fectly sharp but has a certain

~~fJ;@.f Excluding inhomogeneities of the magnetic field Bo over the size of s~ple, ~e pri~cipal cause for_ the line width_ is th~ interaction betwe~wi@~~~j ~.~tJ~~*fl ne1ghbonng spms. In the classical analogy of Section 7.2.2 we say .~¢iii~}{:~ the spin-spin interaction is destroying the phase coherence between ~f {fij~f precessing spins and the rotating radiofrequency field. Another way· thinking of the spin-spin interaction is that one nuclear spin produces::~ft~:;:~fi local magnetic field B1ocaJ at the position of another spin, which then fin~~/Jf@ \ }(:}~:ff~ itself in a field !!il~~~~~i~i Bb = + ·:)i/f Bo B1ocaJ :: : : :: :::::~::::~ Wo = Bb . : :? : ttt and consequently has a resonance frequency y slightly differenf from WQ. To estimate this effect, we calculate the magnetic field produced/ /Jf?

by a magnetic dipole one nuclear magneton strong, at a typical distance o(:/)~~fJ /?/ft

## 0.1 nm

(µo)

/J.-0) JLN = - eli 1 .)}l@H Btocal ~ (- - X - - X - :::::::::::=:::::::: 4ir r3 4n 2Mp r3 ' }(ff)

where µN is the nuclearmagneton en/2Mp and /J.-0 = 4,r x 10- 7 V-s/A-m.//1{]

/{/ff is the permeability of free space. Numerically we find that .·::t}f)

Btocal - 5 x 10 T, ..: :;:::;:;;:?:: -:/:::~~::::: }\JfI which is a significant broadening of the line. In liquids and gases, however, iS:·:/)f{~ the reorientation of the molecules is so fast that the average local field very close to zero, and therefore very narrow lines can be obtained. /:}tr ........

· ,.-.,_._, In Eqs. (7.15) and (7.16) we introduced the function g(v) to describe.)}\~~/ ..b 1c·"Wi\lb1"61. .1 cac~Hiffi'-1 iTnc.'Vf\:r~'"'sa.tb.1ttt~~ , ,a~.~ 'i.,~1w~l.lywc\Jtr.\_ • ; :: : • : • ; • : ( ,? t _ ~ ,,, ~ •"I ::::::=:~::~: :::::::~~;: .)I 7. 3 Abs o r pt i o n of En e r g y by th e Nu c I e a r M om e nt s 2.f,7 the spin-spin interaction. Since g ( v) has dimensions of inverse frequency, namely, of time, we define one-half of its maximum value by T2 2 g(vo) T2. (7.32)

where vo is the resonance frequency in the absence of any broaden ing effects. T2 is called the transverse relaxation time. In view of the nonnalization condition (Eq. (7.15)), ..

g(v) dv 1, (which also fixes the dimensions of g(v)), we see that a short T2 implies broad lines, whereas when T2 is long, the line is narrow.

Using the definition of Eq. (7.32), we can then write for the saturation factor Z (Eq. (7.31)) at resonance (7.33)

= 4 It is of interest to estimate T2 for protons when B1ocal 5 x 10- T as found previously. From the uncertainty principle ~E ~t ,..., li and the line width ~ E y B1ocal so that I 1 T2 ~ ~t 7 x 10- 6 s, ,"-J -- -----,/n.). ., B1oca1 (5.58µN where we used Yp 5.58 and µN /Ii= 2n x 7.62 MHzff (see Eq. (7.2)).

Finally, as already mentioned, inhomogeneities in the magnetic field introduce spurious broadening effects that not only mask the fine structure of the line but also decrease the signal amplitude: hence the use of very homogeneous magnets and ofthe "spinning sample" technique.

7.3.3. The Blocb'Magnetic Susceptibilities11 F. Bloch, who shared with E. M. Purcell the Nobel prize for the discovery of NMR, gave a macroscopic description of nuclear magnetic resonance, 11Titis section may be omitted without a loss of continuity and the reader can proceed directly to the discossion of the experimental technique and resu1ts in Section 7.4. However, the discussion should be quite helpful for understanding the meaning of the "dispersion"

curve as well as the obseJVed line shapes for both absorption and dispersion.

. :@11 ·-//j@jj• 268 7 Magnetic Resonance Experiments · .) i/Jtl t 1¥!i~{JI~ where the ~ffect of the RF field is accoun~ for by the p~l~rization of (~f{/f~i~ nuc~ear sp~ns._We kn?w that ~h~n an electnc (or ma~ettzmg) fipeldo El_~ Jttilm H) IS appli~d In a regmn_ contauung matter, the matenal becomes (or magnetized). We write ··:::::::::=:=:=:=~·===~ (7.3i~;):f/flll = x,E = P M XµH, po1ariJ:f/{~~ll~ where Xe and Xµ, are the electric and magnetic susceptibilities. The tion is due prunarily to the alignment of the permanent electric (magneticf )f~~~~ ?f applie1)}§i~f dipole mom~nts of the atoms or ~olecules in the directio~ the field. Matenals that have such dipole moments and exhibit large polarj//1£]

ization should be called paraelectric (or for large magnetization,_th ey art(}jffi~=~ . d ed alled . ) ·.·.·.·.·.,.-.-.·~;::-~ m e c paramagnetic . . }/)~~:~h·::~ magnetiq/]@~I J The refractive index of light is related to the electric and "bill' . ' ,'.·.·.i·.ll·..-.·. ~.. .? .

susceptt ties, since .::<::::?;:;:;::=~:f==-~ = + = + ffld E (1 x,)Eo µ (1 Xµ)~ : ))){~ ~1- = - c 1/(..floµo) ,- + - --- + - - . ::::::::::::;:::z.:=:- n == - - - === J(l Xe)(l Xµ)- :::::::::::::::t::::: c' I/ C./Eli,)

·.-::-r:-:r·=·=t·=-J=--~...:r-:-:~a j{Jfj The refractive index and therefore also the susceptibilities are a function off -~ .........

\/}Jf J the frequency, as is evident from the familiar phenomenon of the dispersion of light Thus the susceptibility at optical frequencies differs from the statie:./{~J{J 12 of){Jfj one and is a function of the frequency. Frequently the transmission light through matter is accompanied by absorption that may be strongest/)?}fj .. · ...· .·.-,.. .................. !

at a particular resonant frequency. We may account for the absorption by} }}~:~{ ~ :)}/ft attributing an imaginary part to the susceptibility.

The same formalism can be used as well for the description of nuclear _)j(}f ~ magnetic resonance phenomena. The static susceptibility arising from-. )/}t~ ){f}i the nuclear moments in an otherwise diamagnetic material differs from .·.·.·. . · .. - ......... ~ . . :' zero, but is very small and difficult to measure. For the radiofrequency ..\ /}~/ ~ JI "b.li . ··/.·:.·:.:·:.·i~-::::-·~:::::t::· susceptt 1 ty, we wnte ..

x(u,) x'(w) -ix"(w), ··:\}l t 12For optical frequencies and for almost all materials, Xµ. is Oa nd the variation inn arises <::::J:~~~~ entirely from Xe.

.II ·-::::::?~ ~ .·.·.,.-.~~-

## 7.3 Absorption of Energy by the Nuclear Moments

where both x'(w) and x''(w} exhibit a resonant behavior when w reaches wo = y Bo. The real part X' ( w) is given by , 1 [ (wo - w)T2 ]

= 2 + + X (w) xowoT2 1 (wo - w)2T/ y2H?T1T2 , (7.35)

while the imaginary part x''(w) is given by x ,, (w) = -l xowoT2 [ -----l- ----] . (7.36)

2 l + (wo - w) 2 T} + y 2 H/T1 T2 xo Here is the static magnetic susceptibility defined as in Eq. (7.34)

Mo= xoHo, and T1 and T2 are the familiar relaxation times introduced before; the term y 2 Hi2Tt T2 appearing in the denominator is a measure of the saturation as defined in Eq. (7.31).

Equations (7.35) and (7.36) are shown in Fig. 7.5 under the assumption that y2 H?T1 T2 << l; they have the typical behavior of a dispersion and a power resonance curve. We also note that Eq. (7.35) is proportional to the derivative, with respect tow, of Eq. (7.36). By adjusting the detection equipment, we may observe experimentally either of those curves, or a combination of both, as a function of Ct.Jo - w. Experimentally we can vary (a) (b)

I-!' ~ f f

## 0.8 ~ 0.8

- IN .·!-IN_ /0.4/ 0 0.6 0 0.6 ~ 0.4 ::, .!:: :-- 0.2 >< >< -4 -3 -2 -1 1 2 3 4 -4 -3 -2 - 1 0 1 2 3 4 -0.2 -0.4 -0.6 FIGURE 7.5 The radiofrequency magnetic susceptibilities near resonance. (a) The real part of the susceptibility exhibits a typical dispersion shape (Eq. (7.35)). (b) The imaginary part of the susceptibility exhibits a typical absorption shape (Eq. (7 .36)).

.· :-:-:-:-:·:·r:.r.

..··..··..··. .. ·· , ., ·.

,..

. _ . · ,.

. /)~~;~;~:i= 270 7 Magnetic Resonance Experiments ·{{:):(I=~-~~ .-:-:-:.;,:-:-:-:.~- ~~ ))})

wo - 1nagnetic wo = a~!~fij;: w either by sweeping the field (c hanges y Bo) 0 the{fmtif;-: RF frequency, or by sweeping the RF frequency w, while keeping Bo fixed. )){fl ::::::::::::::::~.

. :: : : : : :; ;::::::...-: 7.3.4. Free Induction Decay and Pulsed NMR 13 !{ :}}~:;- ·)}{\t NM.1fW.{{~ It is convenient to consider again the classical interpretation of ---~ ......

fieidjs, ~~ cussed in Section 7 .2.2. Refer to Fig. 7.4b and assume that the RF rotij~-1~ applied along the x' axis in the rotating frame, for a short time t' such)mt\d"

a,1 t = y H 1t = 1t /2. Then the net magnetization vector M will be into the x'- y' plane; in fact it will be along the y' axis. In the labor~~~fi.t~~ m);ijiJ~ frame this situation corresponds t.o a magnetization vector rotating = A.¢~.U.ttr~ x-y plane with angular frequency wo y Bo around the z axis.

The~)j@i~~ is fixed in the laboratory frame with its axis in the x-y plane.

rotating magnetization will induce an RF si~al in the coil at freg°:encY"/@$' ~ ~ec~ that now M(t) = Mx cos wt+ My smwt. This sequence 1s sh?:W~ 10 Figs. 7.6a and 7.6b. ~ . . A . -:-: f -: . -:- f ~ l - § ~ ~ ~ ~ow long will the sign~ persist aft~r time t? First of all because the are m contact with the lattice there will be a tendency for M to return ~J~f~~ T@J~ alignm~nt with the~ axis (recall that there i~ no RF field ~er time t)r. el~~r@I re~axa?on process IS :haracterized by the time T1, the s~m-~attice a*l:::~: atton time mtroduced m Eq. (7.29). Usually, however, Ti 1s farrly long au~§{ f~~ the individual spins that contribute to M become dephased either bee of tfeld 1i:i.homogeneiues ot oetacrsetJ11me-sy1u~piai~i\'C.'l' At!no.u~'.-~.i~J&~ fa(:}% spins are completely dephased (i.e., when they are pointing uniformly s~I~ili all directions in the x-y plane) dM/dt through the coil vanishes and ((Jj does the induced signal. This effect occurs on a time scale T2, which usually shorter than Ti. Thus we observe a decaying exponential as showriCtl T/ .·.·.·.·-·.•,I'.

in Fig. 7 .6c. In general the decay constant is designated by and conta~~f f)

the effects of the spin-spin interaction, magnetic field inhomogeneity, and/ }:~ . l . 1 . ···. \ ··. ·· I . ··. ::•:.-:-• ~.../.: spm- attice re axation )]Ji 1 1 + 1 + ......P f.

= ~B (7 3?X::~:-:-: T* T2 T1 y o- . ..!: ::i;:i~== ~ This section, too, can be omitted on a first reading without loss of continuity. How/)};: modem}f§ ever, it provides insight on the interpretation of transient effects and of the (CW)\}~ NMR techniques that are based on pulsed excitation rather than continuous wave ::::::;::t: measurements.

·.·.·.-.•.

-:-:-~~- /}~ ·\]!

~:::?: it::::<

## 7.3 Absorption of Energy by the Nuclear Moments

f·:·:·:· ??::::::· ~---·.· ~;?{~) ~t z' (b) z (c)

~:::::: ~{\( ~---·.·.

ff( r.·.·.·.· M :;;::::::· ?:::=::::: y ~JI{.- I ~ ~:~ ; : : : : : : =~ : , X t-= 2 W , - o r - --..lc I I ( ~~::::.:. Pick·up coil t=.!! _J_ I t=O [ \::: 2 yH t ?f.IGURE 7.6 Free induction decay following a.rr /2RF pulse. (a) The magnetization vector ~}U in the rotating frame of reference before the application of the RF (t = 0). (b) After t{ihe 1t/ 2 pulse, the M vector will precess in the stationary frame with angular velocity WO· I>cc.) = f The induced signal in a stationary coil in the x-y plane will have period T 2.Jr I wo } ~d will decay exponentially with time constant T2 -:--:-: .

:.i::-:- :::::· .-.·.· [ \Therefore the free induction decay (FID) signal contains information on ({both the resonant frequency wo (namely on y) and on T2 for the sample [(being investigated.

f (' Note that if one performs a Fourier transform on the ·FID signal, wruch }\ is acquired in the time domai~ we obtain the spectrum of all the resonant )>frequencies of the sample. This is much more convenient and efficient than {. searching for each resonant line separately.

/ : We now briefly return to the quantum-mechanical description of these \ phenomena. It was mentioned in Section 7.2.1 that the response of a two \) .level system to a resonant perturbation can be solved exactly in quantum -½ (· mechanics.14 If at t = 0 the spin is in state m = the probability of \ finding it at time t in state m :;= + ½ i s •, ::: 2 P+1/2 sin (w1t/2), (7.38a)

n = -½ with Wt y Ht . The probability for the spin to remain in state m = is (7.38b)

\: as it must be since for a two-level system it must hold that P-l/2 :· P+1;2 1.

14see footnote 7 of this chapter.

::::::::::::::½ ..' ·.· ... ........... .

.: : : : : : : :, :::::. .

:}}ti~ 272 7 Magnetic Resonance Experiments . · .. . ··..··~.··..··-. .·-..,...·.....-..

First we reconcile the result of Eq. (7.38a) with our perturbative cal~!£ I l rate)~f}} lation for the transition rate obtained in Eq. (7.16). The transition of course, the time derivative of the probability and we have ){:}~=~- -:-:-:-:=·=,#·· .::::::::::=:~ :(??~ dP-112~+1;2 = -WI . = -Y H-1 .

sin w1 t sm wit. ·-:-:-:-:-:-:~m dt 2 2 · · ::::::::::::~ ~]!iii The perturbative calculation is valid when a>1t l, and therefore we ·\t:J?M expand sin wit to first order to find that )/td~ ~{!/t~ 2H/ dP- 1;2~+1;2 y (?.

dt 2 t. '· ··.·.)?:::=:~~~ (7.16) (7j~~:::1 This re~ult seems differen! ~m Eq. but we realize (bat Eq~.

are valid ~s l~ng as the imtial an_d final stat~ are_ no! otherwise d1stur~~(J{j ::1 = vq-}J~ over the trme interval t. The maximum such tune 1s given by T2 ½ g ( (see Eq. (7.32)). Thus 2 2 dP- i12~+112 Y l-l1 ( ) . \:::::::::~.~"

vo ·····~ ----- - _ _.... g :\}@®, dt - 4 .

w~-:l-:/-:/-:/-:/-:{-;~~ as expected from Eq. (7.16); we recall that in deriving Eqs. (7.38) it assumed that w wo. Note also that ::-::::::=:=::% -:-:-:-:-:-:-:;,.:: -:•:-:-:-:-:-:~- !jlll dP+i~z;-112 _ dP- 1;;+112 :: \}\j as repeatedly emphasized for the transition rate. ·· It is clear that applying a T[-pulse (wit = n) to a spin ½i n the sta~\){]

m = -½ will make P+ 1;2 = 1 and P- 1;2 = O; namely the spin will fli~·://lf \/t]

states, as we also concluded fron1 the classical analogy in Section 7 .2.2·, However, what is the result of a TC /2-pulse ( w 1 t 1r / 2)? Then we find}{:~ th Jil at l .

= = P+1;2 2 P-1/2· :)}~ \::::% = + ½ = -½ \]~ Namely the spin is in a coherent superposition of them and m :}tt states. It is described by a wave function )Ji . !ii (7 40) ·:::=::~:~ =:=:=:~·= -:::.::.. :":'Jx'"'• ...., ..,,..,.

::::::~a;: -:-:<;x {jj "•'•' ~~~j~: 1-:::::=· 1~ij

## 7.4 Experimental Observation of the NMR of Protons Z13

Ji 'fhis represents a spin oriented in lhe x-y plane, and in the presence of f:}: a magnetic field Bo along the z axis it will precess15 in this plane with {} angular frequency wo y Bo. The quantum and classical descriptions lead f : to precisely the same conclusions.

/f.

We conclude with the remark that the same formalism is used for atoms ~~:::: .... .-.:,: when rwo states of energy EI and E2 are connected by an electric-dipole !I e moment d. lf such an atom is subject to an oscillatory electric field at the ,,:,;::·. resonant frequency between the states, wo = (E f - E; )/n, transitions will •:.: ~ ~~;::. occur. Of course wo is now an optical frequency cacher than RF frequency.

~---· :::;::::::·· If the atom is initially in the state Ii) and the optical field is switched on at ~?

if r = 0, the probability 16 for finding the atom in the state If) at time z is ~- ~:::: 1) , f~Z-::-:.: = 2 PJ(l) sin (~': (7.41a)

ft!

l%~:-:- and ·~-·lr;.•:.: : for finding it in the state Ii) 2 (~ I: ~ ~= < ~ - - · :: . : · P1 (t) = cos I) . (7.41b)

~:::::.· ~it These are of course the exact analogues to Eq. (7.38).

n = ~ff The precession frequency for the atomic case 1 £ 1 d/2/i is called the Rabi frequency. With the availability of lasers one can achieve strong ,::~:!

enough electric fields to generate 1r /2, ir, etc., optical pulses. In this way II atoms can be placed in speci fie quantum states. Such manipulation ofs jngle atoms has recently found applications in quantum cryptography, and it could eventually lead to quantum computing.

~:-:..

7.4.

~t~t~~~~~~~~~THE !I: Ii 7.4.1~::::::deratlons [\ ,~ ... " ~ -/:. , ·- ': To observe nuclear magnetic resonance we need a sample, a magnet, a ~[~: source of electromagnetic radiation of the appropriate frequency, and a ""'·'· ~-_:-:, detection system.

~:!:: ~~:":' ~::: 15Se.e Das and Melissinos (1986) cited in Foolnote 7 of this chapter.

:::::::: 16 Here we gloss over the fact that d is really the matrix element of the electric-dipole ~~:( r.·. operator between the initial and final states.

I\!: ::"~:·,· ~ilit ,,_._.

~:;-:, .: . ': . : . : . : . . : . :: .. : .. : .. : .. : .- :: .. : z.

:: : : : : : =::::::. ...

.) tilt 274 7 Magnetic Resonance Experiments . . . . . · . . .' . . . ·. . · . .- . - - ,....·.. ...-. .....· . ..

-·-:-:-:-:-:-:-: .:/:{::;:fa~ : The magnetic field should be fairly homogeneous, and therefore-ifiift~. .

advisable to choose a good magnet with polefaces at least 4 to 6 in)~}~· :.; magniiltJ --: diameter. As discussed in Section 7 .3.2 inhomogeneities in the field broaden the line and reduce the peak amplitude; to obtain reason~bl~/t vJ.

~~l{@i results, the inhomogen_eities over the volume of _the sa~ple shoul~ be than 1/1000. The ch01ce of the field strength 1s arbitrary, prov1ded·:fu~t:~;: t, How~y.jifJ~ resulting frequency lies in a convenient radiofrequency band.

12 fie)1:fi§~ since tbe signal-to-noise ratio increases (improves) as v~ , high are preferable; commonly, magnetic fields of 0.5 to 1 T are used: and:-f'Qt:~~.Wh _)i}{§~ protons this corresponds to freq~encies ~f _20 to 40 MHz.

The sample can be any matenal contauung an ample supply ,?f proto~~{~~~ p~~n, water, mi?eral oil, or any organic subst~ce coutaiuiu~ bydrogm¥::@lj So%!]~ will, m general, g~ ve a proto~ nucle~ ma~ettc reso~ance _signal.

care must be exercised to avmd matenals with long spin-lattice relaxati~~=}~~Wjj po~~tJ~~ times T1, since ~ey will sa~urate at very low levels o~ ra~ofr~~ency and therefore giv~ weak signals (s~ Eq: (7 .33)). s_urul8:ly 1t 1s p:ofit~~~@ia=M ti~~J~itfj to have a narrow ~ne: hen~e matenal~ with l~~g spm-sp_m relaxa~on mstan~~fl~ T2 ar~ chosen. Lt~uids will meet ~s cond1nou, and m ~ost ~ .i!

the width of the !me will be detenruned by the magnet mbomogenet\)f (T2 3 x 10-4 swill give for protons a line width of 10--· 5 T). Plain 41'.lt?~{ manganeff j~ water makes a good sample, or tap water doped with 1 wt% nitrate Mn(N03)2 or copper sulfate. ·-::):/{~~ magne~\{f~} The size of the sample is limited by the area over which the ·t~\I~Jt~ is homogeneous~ but also by practical considerations of the coil used couple the radiofrequency to the sample. In usual practice a l-crn3 sample~i~.}tJtWw~ ~f adequate; it is contained in a small tubular glass container, around which wrapped a radiofrequency coil as shown in Fig. 7.7 a. The whole assem~It\t1} sinc¢.\t@J is then inserted into the magnet gap and should be secured firmly, :\/~~it vibration is picked up by the coil and appears as noise in the detector.

In deriving the probability for a transition between them subl evels, ancf }ff} ratating/{j]f in all our previous discussion, we have assumed the existence of a field at the angular frequency w close to wo. In practice, a magnetic fiel~\J~~ ?f {jf@ oscillating. lin~arly as A s~n wt is estab~ished ~ the interior the _radiofr~f :.

quency cml (Fig. 7.7a). Lmear hannomc monon, however, 1s eqmvalent t~}}~~ ?p\{@~ two rotations in opposite direction of amplitude A /2 as shown in Fig. 7.

A A <:::::~J:; A cos wtnx === -(cos wtnx + sint.vtny) + -(cos(-wt)n.'\: + sin(-wt)ny)}!):1: ?J~ 2 2 .· (7.42).::::::::~==-~ }II }I~i ...

-.-.- ?f::::: ~-:.;.

~f}

## 7.4 Experimental Observation of the NMR of Protons

,.·.·.·.

~}( (a) Palefaces (b)

~:::::: , ..· .·.· ~:=::: .,._._., 2A ,.. .. ·.

~-=<· ~=::::.

~~~~~;.

[(; ~:::::.

r.·.· .

[ (:FIGURE 7.7 (a) Schematic arrangement of a nuclear magnetic resonance apparatus. The !:f: sample is placed in a homogeneous magnetic field and radiofrequency is coopled to it by :~:/ means of the coil. The Helmholtz coils are used to modulate the constant magnetic field.

t.·.·.

(:_::(b)Alinearly oscillating field of frequency w is equivalent to two fields rotating in opposite t / directions with the sarne frequency w.

::::::: : ~:::: ..

::::::: - ?\ where nx and ny are unit vectors in the x and y directions. The component if : rotating in the same direction as the precessing spins will be in resonance / \ and may cause transitions; the other component is completely out of phase ~) : and has no effect on the sample.

}( When the radiofrequency reaches the resonance value wo, energy is ( :. absorbe-d from the field in the coil and this fact is sensed by the detector.

/ Because of the low signal levels involved and the difficulty of maintaining {\ a very stable level of radiofrequency power it is advantageous to traver.se }/ the whole resonance curve io a relatively short ti.me. Th.is can be achieved ( : either by "sweeping" the frequency of the radio.frequency oscillator while { : maintaining the magnetic field constant, or by "sweeping" the magnetic f.

field while the frequency remains fixed. In early NMR experiments as / :- well as in this laboratory the choice is to sweep the field with a pair of f_: Helmholtz coils, 17 as indicated in Fig. 7 .7a., because it is easy and does not !{ require fancy frequency generators. The sweep coils are fed with a slowly / : varying current, 18 which results in a modulation of the magnetic field B. ) If this sweep covers the value of Bo, which is in resonance with the fixed frequency of the oscillator, a resonance signal modulated at the frequency of ::=;·:··:··· 11 A pair of coils of diameter d, spaced a distance d/2 apart and traversed by current \ . in the same direction, produce a very homogeneous field at the geometrical center of the :=::: configuration.

l ( it 18In the absence of a sweep generator and audio amplifier the 60-Hz line voltage can be used through a variac and an isolation transform« ~::; t~ .;,: , .

·.·.

1·.· ;:-: .

:?}::::::!-,..

276 7 Magnetic Resona nee Experiments ...... ·.: Gen:rator - Attenuator - Bridge - Receiver - .O scil~/· ·-:}:::: .: -:·: ....... ·.- <:Ii/ill :::t~~ :: Sample and .)Ji rf coil __.. ____.,' '{ ;.~f. .J ~ ~- f - f ~ i ' ·.·.·,:,;:;z,,j, /i)ilffl ,_-- ------:,, -;--.-....: w.

,. ...} }:m -'.-:-...: -~ Helmholtz .. Filament _ Variac .. )]~ colts transformer ·\ C==:;t.,;;-;;: -:-:-.-::~~~ ,____-,--t___.._~::::: :.· .·,n . • ~ 110V ac FIGURE 7.8 Block diagram of the nuclear resonance measuring apparatus."

tag~){~ the sweep will appear at the detector. A modulated signal has the adva n of easier amplification and improvement in the signal-to-noise ratio by(}fJ using a narrow bandwidth detector. ,.. )(\\~ \\i The radiofreq1::1ency oscillator and detection circuit can be of severaf designs. Today, commercial frequency generators ·ar~··a~. .- w1,Srori~()}$.

the RF drive and low·noise amplifiers for the detector. A single coil if}} used as both a transmitter and receiver. A block diagram of a CW NMJi)J apparatus as used in this laboratory is shown in Fig. 7 .8. The signa(j} was detected by a bridge circuit; this arrangement has great sensitivity)}: but can be used without retuning only over a fairly narrow frequency) / range. ·})

Commercial magnetometers often use a "marginal oscillator,, circu1{} design// where the oscillator and detector are combined in one unit. In this the RF power is kept low so as to allow the direct observation of the}/ absorption, as well as to avoid saturation of the sample. To cover a wide:{ ·r frequency range the coil containing the sample is changed since it is part of the resonant circuit that sets the oscillator frequency. A unit suitable for\\ 1~ootatnDLjiemonstrations is available from Klinger Educational Products, < as well as from other sources. · ::: [ ( .•.

~ :::· 7.4 Experimental Observation of the NMR of Protons m re: if: 7 .4.2. ~tection. of Nu~le~ Magnetic Resonance ~:=: · WJtb a Bndge C1rcwt ft jf\ The coil in which the sample is located is part of a resonant circuit with f{ high Q. The Q value. or quality factor, of a device is defined as 21e times ,~. ? the ratio of the time-averaged energy stored to energy dissipated, in one ...

f \ cycle. For a coil of inductance Land resistance R, tr.

'> f :::- Q 2rrwL :::::::: =-- (7.43)

f \.

~-···· ::-:::: ;.::-:,: When resonance is reached, the real part of the magnetic susceptibility , ~ ~.,;. : : ~. : · : : . : • : , (Eq. (7.35)) changes, and thus the inductance of the coil also changes.

,..

~~::: ' :: Alternatively, an increase in the imaginary part of the susceptibility (Eq.

;~,;:.:·.:·::, (7 .36)) corresponds to the absorption of power from the field and thus to ~:-: ~ ;.:: : .· : . : · : . . increased dissipation and therefore increased resistivity of the coil. This ~~-: ; ~ .,:. : - : : : - . . small change in the Q value can be detected with a bridge circuit, as shown ....

~;,.:: :::· in Fig. 7.9.

;.:,:.: :?-:=::: The radiofrequency voltage is applied between points a and g (see % ..

f ~-:- :: : . Fig. 7 .9a), and therefore radiofrequency current flows through the load ~ ;.,::- :: :- :· . L and the dummy branch D; if the bridge is balance~) no voltage should :=::-: appear at the point d (since band c were in phase and of the same ampli ~:::: ~::::, tude. and the signal from c and dis shifted by )./2). Any slight unbalance ~:-: P,:::::: i~'=:·>·' of the bridge produces a small voltage at d. The actual bridge circuit is t( shown in (b) of the figure. The R'C' elements are effectively generating F:=:::- t::; :r:< -If:'-.:".· .

:.-:-: f . ..J, ,", _ .. ·.·. •. . . . .

....... ·. (a)

:::::: .·,.·.· ::: .,_:.,~ ·: ~==:: :;;:: s ~,/'.::'.;:· n .s b C •:-:-· ~:::: 't: ~( !

~-:-: ~::::- ~-·.· .

?:=:::.

~::::.: r.·.· FIGURE 7 .9 A radio.frequency bridge circuit that can be used for the detection of nuclear ~=::: ~~:: magnetic resonance. (a) Schematic arrangemen~ note that L is the radiofrequency coil.

r::·::--: ,- {/ The )../2 line ascertruns cancellatioo at the output of tl1e signals from band c. (b) A practical ~--·.

radiofrequency bridge circuit. For resonance conditions see Eqs. (7 .44) of the text ~~::.

l\ :..::..:.:.> ",,.'.-,·. -.·.,.

~--· ~/: '.!-~:~~ 278 7 Magnetic Resonance Experiments ·-:::::::::::::;::,,'1/hll59;"

:(i)Jl~ the "-/2 phase shift and L is the sample coil. The conditions for balan~~itI~ /:::::::::::::; + = =\j}@f( Resistive balance: (JlC1C2 (1 C' /C1') R' Rp 1 (1~~®{11 Reactive balance: C + C 1 + C2 ( 1 + C 1 / C 1' ) = 1/ L(Jl, ~ ~l~I!jl!

~here Rp_ is _the parallel resistance of the _coil. The bridge is_ bal'.111ced app~~:~~rd 1D the res1st::tve mode, ~he~.t he change 1Il the_ Q of the coll will may 1n/ffi¢;f.

an absorption curve as m Fig. 7 .5b, or the bndge be balanced 7Jfil'jf~ reactive mod~, when the signal a?pears _as a ~spersion curve as in Fig.

The experunental results obtamed with tlus arrangement by a studenttt.mi~1# s~own i.n Fig. 7 .10. The s~ple was 1 c~ of water doped w~th mang~ij~@~~ 1n the re~~Y:i~ rutrate [Mn(N03)2]. In Fig. 7.10a the bndge was balanced mode, whereas~ Fig. 7 .1 Ob it was balanced resisti~ely. The sweep, ~e°::!~~ to 1 from the 60-Hz line vol!age, corresponds approximately 10- T/dh~$!Jf[{,I :-:::::::::~=~=:=• at the center of the oscilloscope trace. ~. ~w.;ijtim The exact frequency at resonance can be measured ~uite precisely 6 maWl:~~~l=B (c rystal-controlled) "wave meter" to better than 1 part 1n 10 • The rot~AAi~~r~ fie!d is measured either with a Hall probe magnetometer or with a coil flux-meter. ..::::::::::~f: ;:~ From the ~xperimental curves of Fig. 7. l Oi t is found that the frequ~f at resonance 1s .··-:.::::::::::::::::-~ . ··:-:::::::::::::::::%t ..· .·.·.·.·.·.·.·-·-:m'.

vo 28,141.48 ± 0.63 kHz. ··\:::::=:=:=:=:~~:=i~J .· .··..··..··..··..··..··..··..·.··.·-;9~,)J~ "::;., ../ i\lt~ : fllll::m~ :· \{ ··::\:/t=··---~=,.\tJ~~ . 'jlj!jlll ;:;::::=tit tl l : ]!)]!{~~!

. ~. ?~~~=~ ·:::::::::::;~:~ (a} t ... (b) t---- .: . :;: . :: . ; . :: . :: . :: . :: . = ~ ¼m~ . ~..

:))/t=I Sweep=5x 10-4 cm/sec= 1 gauss/cm (at the center)

nuclear us~i~l FIGURE 7.10 Results obtained from the magnetic resonance of protons bridge circuit: (a) Dispersion curve and {b) absorption curve. The oscilloscope sweeP::~~f~~~ ofJt)~~j linear at 0.5 ms/cm, which corresponds to approximately 10-4 T/cm at the center }}/I sweep.

<:::1 ;://~~~ .:::::::=~~:~ .-::/:J;;~ ~:.:::r:·:: .r...· .·.· -.·. 7.4 Experimental Observation of the NMA of Protons Z79 z::::· r.·.·.- r:.-.· ~::::: f[: ~lf Using a rotating coil Hux-meter at the field position previously occupied by the sample, the magnetic field at resonance is found to be ~:::, Bo 0.6642 ± 0.0020 T, I~:=f:· and hence It~ = B2nvoo = ± 7 Y (26.618 0.08) x l0 rad/s-T (7.45)

-··· , ~fo: in good agreement with tbe accepted value ~1i: y = 26.73 x 107 rad/ s-T.

~:::: :::::: ~( Clearly, it is much easier to measure ratios of nuclear moments to high ~\ accuracy than to establish their absolute value to the same accuracy.

~if To obtain the g factor of the proton-that is, the connection between f !f magnetic moment and the nuclear magneton-we recall that ti· ~Ii Thus from Eq. (7 .4)

~:: ~:: yft y 1 = - :=::: g = - -- = 5.56 ± 0.02, !-:i.

jjjl: where we used the deri:~ val::o;; (7 .45)) and µ.N / h from Eq. (7 .2).

Ii We have measured the proton magnetic moment of the proton to an accuracy ( : of 0.4%.

\ 7.43 Measurunent of r=:=:- Jn this laboratory no pulsed NMR experiments were carried out. However, -under certain conditions one can observe the free induction and its decay f· with a CW apparatus. This happens if the field is swept rapidly enough ?i through the resonance, in which case wiggles such as Lhose shown in Fig.

## 7.11 appear

}. The interpretation foUows the discussion of Section 7.3.4. Far from resonance the field seen in tbe rotating frame is Bo, i.e., along the z ax.is.

As resonance is approached the Bo field is canceled in the rotating frarne and only H is present. This results .in rotating the M vector into the x'-y' \ . plane. After the resonance is traversed the effect of H is again minimal, { but the magnetization remains in the x'-y' plane, and it induces a signal at ~~~ :•:· ~i- .••'·, ~t ~:: 280 7 Magnetic Resonance Experiments .. . :p ·' fl~ . '. . ...... - ~·.-_. .... ,.,..,. • .#.,1'4" • ~<).. ., ~. .._ .,..~---- • .,: 1 .,· .. "*'sf-tf :;:::::::- ·l·.··J;t\Kt•:~~-·-·· .·. .·.. •,.·. .- .. · .• Gauss 4.5 2.25 o I « I I , I I ' I I l .l f \ 'i sec 2x10-3 10-3 o ·.·\j t~ t ~ o.2x10-3 sec/cm .

{a) Linear sweep (b)

maiitfi~{: FIGURE 7.11 Nuclear magnetic resonance signals of protons obtained with a oscillator circuit. (a) The swnple is wacer-saturated with LiF. (b) The sample is water-cJ#if.~~ :{:fwl with manganese nitrate. A linear sweep of the same speed is used in both cases.

Afl = !' a frequency w(t) Bo(t), which differs fr~m ~- The two :<equ9e¥~:~~IiIl w(t) and wo beat agru.nst each other,_ and this ~1ves nse to the w1~gles.

peTT~.t~ can clearly see that th~ frequency difference mcreases (the beating th.~tij@i@ shortens} as the field ts further away from resonance. The effect relevant for _our_measurement is the exponential decay of the envelop~:g1:;I the beat oscillatlons. ::::::::::;::-:~ ttii}~~ We still must explain the wiggles that appear in Fig. 7.lla before resonan~e is crossed. T~ese are present beca~se the spins h_ave not depha~@/JI by the tune the sweep 1s restarted and contmue to rotate 1n the x-y p~~=J:::=I::?: $.

~amitf Indeed they ~ absent from ~e trace of Fig. 7.11 b where the water IJJJ:t/~~ was doped with manganese rutrate as compared to water-doped with figlJfff }~ in the sample use_d for Fig._7 .11 a. The shorter T2 in part (b) of the ·-:{:?J@ leads to more rapid dephas1ng.

If a linear sweep is assumed, the beat signal has the fqrm · {\}lj )(}ffe l dH e- r1r; cos [- y - t 2 ], (7.46f/W 2 dt :-.-:-:-:-:t }})~ be~f f~ where t 0 when the resonance is traversed. Note also that the frequency increases with time since · -:-:-:,:~ \ }~a:: \?$ 1 dH a>t,= -y -t. ;::::::'.:f."}.

2 dt ,·.·.·-~ /}[}$.

b~\i!

From a measurement of the wiggle envelope, information about T* can obtained. This is shown in Fig. 7 .12 where the data are well fitted by ait@~

## 7.4 Experimental Observation of the NMR of Protons

z:::::.· -~ll\( .v., :;: :, i~f-=-:- [::::: ~ ~ ~= : :: - : :- :: > ' - . ( 0 I.} ..

~::::-.

:f:::;"

~?:t ~:/ 9~,:::::-::::-.

t:::::: ..-::=:::: x-·=-: ~?:.

/\ \ 0.1 0.2 o.3 0.4 o.s 0.6 0.7 0.8 ::::::: ·:::::· Time t (ms)

{ \-FIGURE 7.12 Semilog pJot of the amplitude of the "wiggles" of the resonance signal } / shown in Fig. 7.1l a plotted against time. It yields an exponential decay of the amplitude ::-::-?· w t't h a tl-me constant T.* = 2.4 x 10-4 s.

~~:=: ::::: \j:i: exponential yielding .·f·/· r* = 2.4 10- 4 J 2 X S.

Z·.·.

rr ..· .·f. · When we convert the measured value of T* into a magnetic field (see Eq.

f\. 2 (7.37)), we find that ;:::;:;: z:-:-· ; f :::: \ ::: 2.6.Bo = -* 2 - . = 3.2 x 10 -5 T, ~~::::-::-:. T2 y ~::::·.

t( namely, that an inhomogeneity of the magnetic field, over the size of the f( sample, of 0.32 G is sufficient to cause the wiggles observed in Fig. 7. I la.

[\ We also conclude that T2 for this sample is longer than 2.4 x 10-4s.

'/:-: ;..:-:-:-· /'.,,.,-.·.· t~.~·:=.·:-:.

~f _ 7.4.4. The Effect of T1 ~:;::.· ~:::: i\ In Fig. 7.13 we show a very simple marginal oscillator circuit 19 that is ade- f:-::- .-\.

quate for demonstrating NMR signals. The first transistor supplies constant i{ ;:::::::.

r ::.---- J. R. Singer and S. D. Johnson, Rev. Sci. Inst rum .• 30, 92 ( 1959).

;.:.·.· f\ [} ~x·t· ":::::::::::::::~· .\}}it 282 7 Magnetic Resonance Experiments . <<tf~j-j :\{tJ~ -9~:\i/)fj .: : : ~:: :::::::::::::.

.' :: :::::::::::::=:~ !i!ill: 0\ii!i!/f D1 1-¥\J SpF r 1 (2N502) A B (1N56) T 2 {2N247) o . • . : . - · ~ . :- ·. : t • ·. : . · • . - : · . - - - : ·. . . • . : . - - .. - 10pF :-:-: I -:. .: I •:• } : . .. : .-..

Coil 10 K 10K 0.01 J!ll , 1K 0.01 ·.·.·.·.·.,·.·.r. .• ,.• • ·':\::ii1il jl lf' flGURE~ :-O~ si~:p~e trMsistoriud n~l= =~etic ~~-• crr~L . .:::::::::::1 -:;m111it~~I .. f: ::~\:;::'.:~II~ !11 current to the coil a~ched to point A. ~y c~ge the Q of :he ,1\J~ appears as a change m voltage at that pomt, which is then amplified ~ t{i the ou~ut transistor. The circuit will osc~ate i~ th~ range of 2-80 depending o~ the resonance set ~y the coil LC crrcmt. ·}/{)~ Data obtained by a student usmg a l-cm3 sample of water doped w~~{~}:~ {4¥/:/~ manganese nitrate are shown as a function of RF amplitude in Fig. 7.

oscil)i~JJi The amplitude is controlled by the 10-kQ potentiometer in the fi~. ·,~·.·.·I.·.J- .. : @;..:,.,.. ..

tor loop of the circuit of Fig. 7 .13. The data were obtained in a Bo = 0.8 T (vo = 33.83 MHz}. The RF level as measured across met/::~ th' : . ~ .. ·. F · .... \ ..- .-~f,_J-,,•,, coil is indicated for each of the traces shown in the figure. Note the NMR signal increases with increasing RF power until the RF amp,!f)?!

tude reaches approximately 0.5 V. Beyond this point the signal decreas~~}J®, because the sample is saturated. From a knowledge of the Q of*§}{~ ~f /J@ coil one can convert the RF amplitude to the corresponding value of rotating field H 1 and thus use the data to find the spin-lattice relaxatiq4}i~~@ .-:/{jf~ time T1.

~ote als_o that once the sample _is sa~ted there i~ suffici~nt magne~j}~ zatton left m the x- y plane to begm showmg a beat signal (wiggles) aft~}!:J~ scaJ~)i§f passage through resonance ( see Fig. 7 .11h ). For convenience the time tl~#JtJ on the oscilloscope trace in Fig. 7 .14 was set to cover a full cycle of :\\J~i 60-Hz sinusoidal sweep.

-.:t)f~ .. ·.·.·.·._;..,.x }()iij JI :-:::;:::::~ 7,5 Electron Spin Resonance 283 20 mV/cm (a) rl level 0.125 V 0.2V/cm ---·1-·--··---·---· - . t ' . (b) rl 0.2 V 0.2V/cm (c) rf 0.3 V 0.2V/cm (d) rl 0.4 V 0.2V/crn (e) rt 0.65 V Sample Is saturating secx10-3 20 10 0 t --- FIGURE 7.14 Nuclear magnetic resonance signals from protons obtained with !be cir cwt shown in Fig. 7.13 as a function of the amplitude of the radiofrequency. Note that initially the output signal increases wilb increasing radiofrcqoency amplitude but at a level of approximately 0.5 V the sample is saturated and the signal begins to decrease. The s.ignal of 0,5 V is sbown in Fig. 7. I lb.

7.5. ELECTRON SPIN RESONANCE 7.5.1. General Considerations So far we have discussed transitions between the energy levels of a proton or a nucleus in the presence of an external magnetic field. Transitions between the energy levels of a quasi-free electron in an external magnetic field can also be observed. We refer to this case as electron spin resonance (ESR)

: l!ll!lllf 284 7 Magnetic Resonance Experiments .·,:.:-:-:-:-:-.-.r.

as already mentioned in Section 7 .1. We expect the transition freqti~~~Jj~ for ESR to be approximately µ, B / µ, N 2000 times higher than tha.(~~ rv NMR. Namely for similar laboratory fields the resonance frequency:Jift~ the microwave region. ){{/ ~;: ~ift Atoms or molecules that have J -:fa. 0 in the ground state will exhibit ctln!@f_ effects. Such atoms or molecules are paramagnetic (the atomic spins oriented by an external magnetic field), hence the use of the term eledt:~{?

diffic~1fti~:[ paramagnetic resonance. In solids, however, it is much more ..

. che~.·.·.e·.-.....~...... .:t t find electronic states with J # 0: this is due to the fact that in the ~.

s()Jhit~~J:-::· binding of atoms into molecules, the valence electrons get paired off, .. ·. ·.·.···.lj,~·.• each atom appears to have a completely closed shell. For example, in N'.~ijij~:~ the sodium has a 2 S 1;2 electron (n = 3, l == 0) outside closed shells{~j§f the a = shitlf/k chlorine bas 2 P3;2 electron hole (n == 3, l 1) inside closed However, in the NaCl molecule, the sodium appears as a Na+ ion,)@i~ hence presents a closed shell configuration, whereas the chlorine apJft.:~§: ~Wfi~ as a c1- i~n again with c~mpletel~ closed shells. Consequently, the ~ molecule 1s completely diamagnetic. :-/?:~~=~ sus~ijj~f Nevertheless, it is known from the work on static magnetic s~g~ifol tibilities es~ecially at low temperat~res. that c~rtain salts show paramegnetism. Namely they contain ions with permanent magn¢@:::::-: moments on the order of µB. In particular, compounds containing-°ionf{~ t~fi j{~J~ of the "tran~ition elements" _of the periodic table are frequently found :)~)W,J~ paramagnetic. An example 1s the compound copper sulfate (Cu(SO) 4 wbich the double valence results in a Cu 2+ ion. For copper the n = 1/J{~~:~$.

and 3 shells are completely filled and one electron is in the 4s statt~/ $.}(jffl Cµff:/1~ that Cu 2+ has a hole in the 3d shell; thus the ground state of the Ji@I ion has l = 2, s = ½, and, consequently, J # 0, so that it does pos~.~-~#:f magnetic-dipole moment. In an external magnetic field, the ground --~~~~tr~ will be split into sub1evels and resonance between them can be establi~ij~~f{ ~i and is inde~d observed. The actu~l situation, however, ~s mor~ complic~~[f due to the 1~fluence ~f the electnc field of the cry~talli~e lattice. )\\{/~ ~~f(j~ . Electro~1c magnenc ~noment~ can also ~e found 1n s?lids when the orgamcf~lft~I 1cal bon~ 1s broke~, as m org~1c free radicals. Especially, the a:y~Wij DPPH, diphenyl-p1cryl-hydrazil ((C6HshN-NC6H2(NO2h) shows (the#~f ~ strong and narrow resonance line, with a g factor very close to 2.00 stjiif l~ electron value) and it is therefore frequently used as a standard. The ture bebafewtJif of the molecule is shown in Fig. 7 .15, and the ''free-electron"

comes fro~ the single elec~on bond in ~oe of the nitrog_ens. Electron-@fflif~ ~Y:}aN resonance ts also observed m other matenals where unparred electrons .:1 111 ..: ;.~- ,~,. :-:,: t ?

{ii 7.5 Electron Si:tin Resonance 285 ~ll\i t=:::·: #?!( ..· ::~:: : • tilli: .

:i~:~:; %:::,·· > ·~!/ FIGURE 7.15 Chemical structure of DPPH (dipheoyl-picryl-hydrazil), (C6Hsh,N {::° NC6-Hz-(N(½)3.

im: .I'.·.

/:=~st. such as crystals with lattice defects, in ferromagnetic materials, and W/ in metals and semiconductors.

·~/r.·.·:.·: The much higher frequency of the ESR transitions is advantageous f f because the energy absorbed from the microwave field for every transi ·}:j: .tion is much higher than that in the NMR case, thus leading to a much ;,; ..

t{dmproved signal-to-noise ratio. Furthennore the separation between the -~}/ energy levels is much larger, so that they remain resolved despite their ?f:·:iarge intrinsic width.

·%·?··· The resonance condition is detected, as in the case of nuclear magnetic ~\\ resonance, by the absorption ofe nergy, and for th.is reason solids and liquids J\ are much easier to study thao gases with their very low densities. Mucb of :::: :-jf our previous discussion on transition probabilities and relaxation mecha [ f nisms is eq~ally ~pplicable to electron paramagnelic resonance. Howeve_r, the population difference between the energy levels (see Eq. (7.26)) 1s \ ·much larger because of their greater energy spacing. A difficulty with ESR \ :: is that the width of the resonance line may be prohibitively large, since both It:-'·} e sp~-lattice and spin-spin interactions are s~ong~r than in the nuclear th.

;:;- magnetic resonance case. In order co reduce the Line width, the sample may / be cooled to low temperatures (lengthens the spu1-lattice relaxation time)

f f and/or the paramagnetic ions are diluted io a diamagnetic salt (lengthens the ~=[: spin-~pin interaction ti.me by effectively increasing the distance between ~ -::. the spms).

tJ\ When measuring electron paramagnetic resonance lines in solids, a great ~/ variety of g factors are obtained. This is due to the differences in the ~r coupling of the unpaired electron's spin with the orbital angular momentum; z} the strength of this coupling depends very much on the position (in energy)

l} of the adjacent levels of the ion as they are modified by the crystalline field.

if Further, the electron paramagnetic resonance lines show hyperfine structure ~;:=:: ·~·· •·.·· .,{ :.

l;';,: Jj} 111/[l • 7 Magnetic Resonance Experiments )

l~'i~jijf{ characteristic of the interaction of the nucleus with the ionic energy this structure in tum can be used to positively identify small traces ·~t~~~t element contained in some unknown sample. Similarly, the organic{tf~~f ide~ijfy\ ..

radicals show characteristic lines ( g factors) that can be used to h~s.\n61~.

them and show hyperfine structure as well. 1n fact, a radical that structure (like DPPH) may exhibit such effects when the sample1is prep4t.~/ti :)?tiW in a liquid solution.

.)}r}n\irf~l :ii 7.5.2. The Electron Spin Resonance Spectrometer .l.·. ·.·'.·.··i·-xlJ. i In this laboratory BSR is observed _using X-band spect:romet~. 'lbe ~J~,~{j X-band refe~s to the frequency. of the nncrowave source, ~hich ~s 10-~Hz re?Ion (Ji.t ::::: 3 cm): Microwave coropon~nts and :l)lu_mbmg,~i!~~Ji ~:~J{i readily available. ~schematic of the spectrometer 1s ~hown m Fig. 7 .1 20 sh9~~f@.

~t first appears quite elaborate. Ho:'ever~ the basic_ components ~ i{j m bloc~s separated by the dotted lines can ~e easily understood.

co~ec~ons between compone~ts ar~ m~de w1~ an ~-band wa 0 v .9 eg ~ u ) l~ f ~ f { l f ~ @.

which 1s r~tangular copper tubmg with mner dimensions a= b - 0.400 m. .

P.1:::j::f::/::@::~:=~:-1 The microwave source (block A) consists ofa Varian X-13 klystron can:::::::~ ered by a Hewlett-Packard 716B power supply. The klystron frequency "Iocijf@ffi be controlled by the KLSP modulator, and this feature is used to the klystron frequency onto that of the external reference cavity shbwi(Jijff~ block B. Instructions for tuning the klystron to an appropriate mode ~~?~~~j locking the frequency are provided with the instruments, and after a whiJ~{Jj one becomes familiar with the procedure. The sample cavity is shown);ij/{W, Jj block C together with a phase shifter and tuner. There are also provisiortf ~·. · .·.·. ·.·,.·· for measuring the wavelength. Detection is accomplished in block D, b.Y.(fi',/ co.ri.i.f.}.~....:..~ J the equivalent of a microwave bridge, which uses a "magic tee" to indicat~i)}~ pare the sample signal with the reference frequency. Block E ai.'.~(/i the magnet power supply and a set of Helmholtz sweep coils, which driven by an audio amplifier at a ramp generated by a function generat~#j} Finally in block F is shown the audio part of the detector where a lock-(tj,}}j detector can be used when the field is modulated. Otherwise the main fieldi:?~j .·:-.-:-;~~~ ~l\~ can be ramped under computer control, which also records the signal field. : ~) )~ . ::::::::::;:3 A very simple ESR demonstration apparatus operating in the RF range, and thus ·~{@ very weak field is available from Klinger Educational Products. -\ :)~: i!!!!!!I~ ·-\::;:~ }!@ . ·••.·••.•· ../4 ' ,..ii.

:; ::: =:~f.

m1en1.1a1ar V6Jl.abt& llthmua.ti:ir

## SOOD&

Klyslron @ JnoflijhUOr ~I ~I L_ Tunat:m> I I ® I I !1 c .3 a 1 v 1'\ i f t .! y 1 0 W'M M ru rJ s g ff e l t'l;) I il t I L - ~~- L - OI.i - d ------ ----- I I 11iffntlohz 1-........---- ~----~ - ~r --- -~----- ----= I coUaM j I (lf&dtCmttgnel ,,,.....,-------lilililll L...1...-~--,---.....a.-/ / jI LJ......__i CC led< I amptiflar tr, Cofr4)1.ilef I lruncibnj !l !' • -' Amp I Aud'io Amp gen I "

I I I I I ® J Mac.u1 l I l~ e-on-vol -- --------I I- ---- ---------------I FIGURE 7.16 Schema.tic cf the X-band ESR spectrometer.

~111t, ~8 7 Magnetic Resonance Experiments ·-(???~ We now elaborate on some of these components: :::::::=?:=:=:~ (a) Propagation in the Waveguide. Only certain modes will prop_~gijtf;: }\{tf/"

without attenuation and the wavelength Ag in the guide is given by ·:::::::::::;:;::~ .. •f, j}={J 2 + 1 1 1 1 (m/a) (n/b)2 (i@llf = = Ai Af - A~ A2 - 4 where Af is the free space wavelength and a and b are the inner d,imensWAf.{,".

:{\{i~ of the guide; m and n are integers. Since a= 2.29 cm, b 1.02 cm, and Af ~ 3.2 cm = = we find that only the m 1, n 0 mode can propagate, and Ag= 4.5 cm.

In ~his m~~e, the electnc field 1s completely tr~sverse to tbe ~s of:~~~~i~ TI.!in~~::&ffi gmde; this 1S called the TE10 mode. The field lines for the traveling wave are shown in Fig. 7 .17 where the density of field lines is proportiqij~Jt~ - . ·.·.·.·.·.·,·-.-if.:: -·:::::::::::::ax~ to the field strength.

··:::::::J:~ //;/J;~ <m1 zJ i} /il Top view _,::::::::::::@ Sicl& view Cross section atA-8 ......

t~ ----~::_ ,, ~,' \if~{~ Perspective y )/if ~ ~/.. --Electric field \{~!

z x ·----Magnetic field ~(/f~ FIGURE 7 .17 Configuration of electric and magnetic field lines for a traveling wave in /Jj rectangular waveguide. J..g is the wavelength in the guide.

·/::i~ i} %:· 1::::::n: ·::::.

~ ···· (b) The Microwa,e Caviry and S~:~ from { { apart of the waveguide ending with a shorting stub, Lo set up a standing r/r\ wave. The sample is placed so as to be located in the rniddle of the magnet palefaces, and then the (shorting) sliding stub is adjusted so that maximum f f :B field exists at the sample. From the configuration of the standing wave "'·.·,· ,.;.:)\pattern. maximum B field occurs at a distance x from the short, where !> = + ~) ,, , ~1rnr.

/:? · w ith p an integer. Since the microwave field must be normal to Bo jt is 1/: preferable to place the guide in the magnet with its wide side parallel to l f ~,½<"·'·{ _the po e aces.

., if (c) The Magic Tee. This is the heart of the bridge circuit, and is used to "J/ ·compare (interfere) microwave signals. It can be osed in different configu /{ rations but in the spectrometer used here it is set up as shown in Fig. 7.18.

if - Let EI be the reference field and E2 the signal field. The power at DR ~~.·.·.·.

. ?i: and DL are :.:::::: .,:;?::: ~~:?· PR,= IE1 + E2l 2 :::: IE1!2 + IE2f + 2Re(E1E 2 )

.,~~~\: '-:-:-: Pi_= I Er - E212 = 1Etl2 + IE212 - 2Re (E1 Ei} .

;tr ti ~t~r Signal Reference ~l\!l [} E, ?::::: ~·::,,- ~} ;,:-:-: ~} ff ~::: ?::?

~=:== fJ'4-·.:·:.

FIGURE 7 .18 The magic lee used in the ESR spectrometer. A reference field and signal ~::::' field are mixed within the tee to provide a sum or dit'fereoce in the output anus of the lee.

'l:·'.

;i~: fl: ,.·.• ~:::: ~:::: ~::: 11111 7 Magnetic Resonance Experiments : ..- :-:-:-:-:-:-:-:•::,: If these two power levels can be subtracte~ we have a signal, S. equaJjij/~f~ li~i!lllii Ut S = 4Re (E1Ei} . • E 1 = ER e10 , ER is real. ·:.{:}ff:;~ :)i/}]]l/tl = + E2 Eo(l x), Eo is real.

fi#ii!JI = mt Then recalling from Section 7,3.3 that x(w) x'(w) - ix"(Ql) we that (7-4j~iilfl = + x' + x"

S (4EREo)[cos0 cos0 sin0].

By selecting the phase o~ the reference signal, we can select the desir~J@i __ curve. For 8 - 0 we obtatn . :-:-:-:-:-;-:~ s = + (4EREo)[l x'(w)J. :I:,I x' Since only (w) is modulation dependent the signal ~allows the dispersiJ~Jf curve (Eq. (7.35) or Fig. 7.5a). For 8 - :rr /2 we obtain . ··:}}t§m s = 4(EREo)x"(w), //{~ :::::=A=ai~ /}Jf namely the absorptive part (Eq. (7 .36) or Fig. 7.5b) . If the reference phasf bY[f( j~ is not set properly the signal is a mixture of the two curves as given . .·.·.·.·.·. .

Eq (7 48) ~ • • • -:::::::::;::% (d ) Detection. One can use bolometers in the two arms of the magic tee./ :{}~i .•••......, I',~ These are devices where the resistance changes as a function of incidenti\:}ti .. ·.·.·.·.·.·«.,,-.

powe: and are q~te se~si~ve. It is. however, simpler ~o use in the magic}{@@ tee rrucrowave d10des sumlar to those used elsewhere 1n the spectrometer:))}@ /:})% for diagnostic purposes.

the\f\ W (e ) Lock-In Detection. If more sensitivity is required one modulates the)\J@ Bo field and sends the difference of the signals from the two anns of magic tee to the lock-in detector. When the modulation width is much,\\!~llii less than the line width the detected signal represents the derivative of/{{f ))tm the absorption (o r dispersion) curve. This can be seen from the sketch of 11: Fig. 7.19.

. >J~ 7 .5.3. Experimental Results .· ::::::~~ ·:::;:::::::~ ::::::::::~~ \}J~ Results obtained by students are shown below. The magnetic field wa~ \/fj modulated at I kHz and the lock-in detector was used. The modulation ·:::::~~~:;:

## 7.5 Electron Spin Resonance

Ba Bb FIGURE 7. I9 Effect of smaU-aroplirude field modulation. Toe output is proportional to the derlv11tive of rhe absorption curve and is muimum at the lJOints of inflection.

7ij 0, Cl) -1 .·,· l( -3 ... -5 ....

0 20 40 60 80 100 .•·'•~ · .•:• .•..•. .

FIGURE 7.20 Resonance signal for DPPH as a function of the magnetic field. A small '.

modulation was applied to allow lock-in detection, and therefore the signal gives the derivative of the absorption curve.

::: ::: .

::: amplitude was kept low so that the derivative of the absorbtion line wa.c; .· ..·.. . · , observed. The field was swept through the resonance by slowly ramping :;:· .: • :. ' :. • the magnet current The frequency was measured by using the wavemeter, ••:'.· · and the magnetic field by using a Hall probe.

:•: ::: ..·•., Figure 7.20 shows the results for DPPH. The field measured at the :•:.:. two ends of the sweep21 was B(0) = 0.3370 T and B(lOO) = 0.3480 T.

..;: .·: ::: ::: 21 The number in parentheses refers to the markings on the x axis of the computer ploL :.,.

.··..

.. :: .· .

:> ::' ::: 292 7 Magnetic Resonance Experiments The field on resonance is Bo 0.3402 ± 0.005 T, The{i/i@}W where the error arises from the error in the Hall probe calibration.

frequency was found to be · :/:}?~ "i!UtI@w- vo = 9.578 ± 0.010 GHz, .·.·.·.·.-r .... x . . . . :/i!i!(f~ :}/:JJ)

the error reflecting an estJ.mate oft he accuracy oft he wavemeter calibration.

fil Thus h vo 1 9 .578 GHz \ /:t:~ }!{ff¾ goPPH == JLBBo = 14.01 GHz/T 0.3402 T = 2 · 01 ± 0 · 03 ( 7 .4 9 } )/}l~ in good agreement with the accepted value I .::::::::~~ 8DPPH 2.0036. . · The width of the line is fairly narrow, of order ClB 8 x 1o -4 T at full · }j ~~ :\Ji!

width.

Figure 7.21 shows data for a CuSO4 sample under the same conditions.

The frequency is the same as before but the sweep of the field is much wider.

= = It extends from B(O) 0.2690 T to B(l00) 0.3750 T. The central peld is found to be Bo= 0.3146 0.005 T, 1....---------E-PA- -----------.

:/)!!

· ·. . · · . . - ·. .· .. ·· ......

:::;::~~ \Ji . ,:::~~ -1------~---------~-,..........--..-----1 <I 0 20 40 60 80 100 . .· · r .~ . 4 ,· ·:::~;: FIGURE 7.21 As described in legend to Fig. 7.20 but for a Cu{S04)-7H20 sample. >;:;: Note the large width of the line. {~ ·· ..

-:-:•: <8 .:::~ ):} .<::j .·~· ):;

## 7.6 References

so that h\Jo 1 9.578 GHz= _ ± 0.0S = 2 17 gcuS04 B

## 14.01 GHz/T 0.3146 T '

/1,B 0 where the increased error is from locating the center of the line. This result lies between the known values of the two g factors of the Cu2+ ion.22 What is strikingly different from the DPPH sample is the width of the line, = 4 which is ~Bo 290 x 10- T. This is a clear indication of the effects of the crystalline fields in broadening the energy levels of the Cu2+ ion.

7 .6. REFERENCES A. Abragam, The Principles ofN uclear Mo.gneclsm, Oxford Unlv. Press., Oxford. I 96 l. An outstanding work on nuclear magnetic resonance, where the treatment is theoretical and advanced, but very complete and clear.

E. R. Andrew, Nuclear Magnetic Resonance, Cambridge Univ. Press, Cambridge, UK, 1956. A shorter text cont.aining experimeatal details as well~ it is very useful to students in this course.

C. H. Townes and A. L. Shawlow, Microwave Spectroscopy, McGraw-Hill, New York, 1955. An extensive and comprehensive work on the subje<:t, mrunly treating the molecular spectra obtained in gas.es.

a E. Pake., Paramagnetic Re.rnnance, Benje.min. Elmsford, NY. 1962.

D. J.E. lugram, Spectroscopy ar Radio and Microwave Frequency, Bunerworth. Stoneham, MA, 1955.

Very helpful for the study of paramagnetic resonance in solids and crystalline materials.

E. Fukushima and S. B. W. Rolder, E.rperime11tal Pulse NMR. Addison-Wesley, Reading. MA, 1981.

22 For a crystal the g factor depends on tbe orientation of the crystal axis with respect to the magnetic field. The sample used here was crystalline (powder), and therefore one cannot observe the two g factors. CH and g1_.

## CHAPTER

Particle Detectors and Radioactive Decay 1> 8.1. GENERAL CONSIDERATIONS ......· The terms radiation and particle used in this chapter require clarification.

The term radiation here designates electromagnetic energy propagating in space (crossing a given area in unit time), but specifically of a frequency higher than that of the visual spectrum, namely, X-rays and gamma rays.

Visible, infrared, microwaves, and radiofrequency waves are not included.

Because of the quantum-mechanical aspects of the electromagnetic field, such radiation can be described by a flux of (neutral) quanta, the photons, :=_::_· = = :-:- with an energy £ h v and a momentum p h u/ c, where v is the 1)/ frequency of the radiation. These quanta interact with electric charges, and \( the probability for such interactions is of the same order as that for the interaction of two charges.

:_._~:!:!=· The tenn particle here encompasses all entities of matter (energy)

.·.· ::::- to which can be assigned discrete classical and quantum-mechanical :::::: properties, such as rest mass, spin, charge, lifetime, and so on. The use of t · (~ •:-:: /.: :Citf!:; i/i!/i~i!/!i 296 8 particle De te cto rs and Radioactive Decay . .· : hydrog~#/t the term "particle" is not always clear: for example, we speak of a pijfff~ molecule, w?ereas_ w~ refer to the nucleus of the hydrogen atom, the ton, as a particle. Smnlarly, the electron~ the neutron, the (almost) tnass~¢:~t_t \~ neutrino, then meson, e~c., are referred to~ particles; the same ten~fj!{\~ 10~?/~ frequently used for a fission fragment, a helium nucleus, or a heavy that of a cert~\*lil Th~ visualization of~ pru.ticle is massive po~t-~escrib~g_a tN:~ffi traJe~tory under the influence of external f~rces and 1IDt1al conditI.ons; provides a useful model for many calculations. · {}/~?:I 13 thej{@%j Since particles have dimensions on the order offermis (10- cm), cannot be "seen" even by electron microscopes, 1 but their impact on cef.~}.)J@ mo#JWJ tain material~, or p~sage through them, can be n~ticed re~d~y. Even re~arkably, 1n certain subs~ces and under sp~c~c cond1tJ.ons the whol~}}~ traJectory of a charged parttcle can become visible and be permanentlj\J~W:: th~tJJI recorded. ~us, a ~arti~l~ detector, or ra~ation detector, is a _device produces a signal (intelligible to the expenmenter) when a particle or pho{}~~@~ ton arrive~; if ~e. device rev:a1s to the e~perimenter the whole trajectory{}]~[ of the particle, it 1s called an 1mage-fomung detector. . ':::\\i~:~i:i of/Ji~~~ All detectors are based on the electromagnetic interaction of the charge dif~i!/~:f l the incoming particle with the atoms or molecules of the detector. The ferent types ofi nteraction (ionization is the most common) and the differenti}Jf;f; .·. ·.· .·.·.·1/.·.· principles of amplification of this interaction distinguish the different type$-{{{1.f .........· .·Y.·.·.

of detector. Neutrons, however, are detected through the interaction of the·}/:=::~;:::: charged particles of the detector to which they transfer energy. This occurs:\i/} f ?\tr either through elastic collisions of the neutrons with protons (hydrogenous, the·)!]} materials), or through neutron capture in certain nuclei, or through production 10 7 of fission by the neutron: for example, n+ B~ Li+a. :}}~\ In the following discussion we will be concerned with signal-producing :}{}\ devices, which we classify as follows: }/{ {/J{ (a) Gaseous ionization instruments, encompassing the ionization cham- :}ff ber, the proportional counter, and the Geiger counter, \ii (b) Scintillation counters, <J} (c) Solid-state detectors, and ·.· .,. .... ,._ ·f t (d) Other detectors.

}Jt Such detectors can be designed so as to respond to the passage or anival :}:?

of a single particle or quantum. They can also be used as integrating devices -<:::-:::- \~~~~~~~ :/:;:~ :\f 1H igh-energy electron-scattering experiments (which serve as a sort of microscope)

have, however, revealed much about the electromagnetic structure of the proton and neutron. . )f )•••1•- 1,. ....

....... ,.

./ ii . ~=::;: 8. l General Considerations 2!f1 \. (as is frequently done with ionization chrunbers), giving a signal propor- 1( tiona1 to NE, where N is the total number of particles crossing the instru } m.ent per unit time and E the average energy deposited by each particle.

} In evaluating a detector. the following properties are taken into co::~d;::s::~ty, which defines the minimum energy that must be depo \ sited in the detector so as to produce a signal; related to it is the.signal-to / noise ratio at the system's output.

:: (b) Energy resolution, in certain detectors, which are large enough to stop the particle; the signal may be proportional to the initial energy of the .. particle. In other cases the velocity of the traversing particle can be mea sured, as in Cherenkov counters, or in d E / dx (ionization per unit length)

detectors.

(c) Time resolution, which characterizes the time lag and time jitter ·· from the arrival of the particle until the appearance of the signal, and the distribution in time (d uration) of the output pulse; related to it is the dead time of the device, that is, the period during which no (c orrect) signal will be generated for the arrival of a second particle.

(d) Efficiency, which specifies the fraction of the flux incident on the counter that is detected. It usually is fairly high for charged particles, but can be as low as a few percent for neutral particles and for photons.

Particle detectors play a most important roJe in nuclear physics, and in many of the experiments described in this text some type of particle detector is used. Just as the spectrograph was the paramount instrument of atomic physics, so the Geiger counter and, later, the NaI scintillation counter have been the paramount instruments of nuclear physics.

In the following sections, we first present a brief discussion of the interaction of charged particles and of photons with matter. Then gaseous ionization instruments are described with specific emphasis on the Geiger counter. This is followed by a description of the scintillation counter and the measurement of nuclear gamma-ray spectra. The following section deals with solid-state detectors and the measurement of the specific ionization of polonium alpha rays in air. Other detectors are mentioned, and some specific experiments using these detectors are described.

2 It is interesting that the first particle detector ever to be used (by Rutherford in his alpha-particle scattering experiments in 1910) was a scintillating screen, a technique that came again into prominence after 40 years.

~ <; 11111 8 Particle Detectors and Radioactive Decay Finally, note that precautions should be taken when handling radioact;.y;Wf{i sources. We recommend that the reader review the material on radiatiof()(fj safety in Appendix D before undertaking the measurements destribed.U .{:}}~:~ 8.2. INTERACTIONS OF CHARGED PARTICLES

## AND PHOTONS WITH MATTER

8.2.1. General Remarks As already mentioned the interaction of charged particles and photorit}{ffi with matter is electromagnetic and results either in a gradual reductiQ~))ffj th:f{]~ of energy of the incoming particle (with a change of its direction} or in absorption of the photon. Particles such as nuclei, protons, neutrons, an4.()~@ n-mesons, are subject to a nuclear interaction as well, which is, howev~t(/f!

of much shorter range than the electromagnetic one. The nuclear intera¢+.))f:j tion may beco1ne predominant only when the particles have enough energy.{{(!~ is~,·/.·.·).·~··J·:·*·"'"' to overcome Coulomb-barrier effects. A nuclear mean free path, which f //{~ approximately 60 g/cm , is the distance over which the probability for \}j}~ nuclear interaction is of order unity.

Heavy charged particles lose energy through collisions with the atomi1.t/ {{:?

.·.·.·.·.-.·.4 electrons of the material, while electrons lose energy both through col--/ :}j~ lisions with atomic electrons and through radiation when their trajectory( {}~~ is altered by the field of a nucleus (bremsstrahlung-see Section 8.2.6):()}li Photons lose energy through collisions with the atomic electrons of the.}}\~~ material, either through the photoelectric or the Compton effect; at highe1f• :,•:.:·.·\.:· ..~." -·,~J-:.

·.·.·.•.;,".-•. t.

energies photons interact by creating electron-positron pairs in the field of·}}}~~ ?)ff: a nucleus. .· ))\t A brief review of definitions will be helpful.

~.f\Jl (a) Cross Section. We define the cross section, u, for scattering from ·\J~~~I single target particle as .

= _ _ ct scattefOO flux_ _ (S. ) :; mcident flux per umt area · ::::::::it-:: . '}J~ Thus ct has dimensions of area (usually cm2 ) and can be thought of as the/ .. \ .... t .... j .

area of the scattering center projected on the plane normal to the incoming,:.:}::;;:::: beam. If the density of scatterers is n (particles/cm3 ), there will be n dx ){J 8. 2 1n t e r a ct i a ns with Ma t t er 299 --- (a) (b)

~~s ----+- - - - F - lu- - x - s dx- 1- dx~ FIGURE 8.J Scattering of an incoming flux of particles by a target: (a) Area covered by flux is larger than the target area and {b) are11 covered by flux is smaller than the target area.

scatterers per unit area in a thickness dx of materia.L and the probability d P ls/ lo of an interaction in the thickness dx is a-(lo/S)

= = d P ---(Sn dx) (Jn dx, (8.2)

lo where Sis the area covered by the scattering material and Io is the total flux incident on the target; thus Io/ S is the flux per unit area as shown3 in Fig. 8. la. The result of Eq. (8.2) is not surprising since d P must be proportional to n and dx: dP <X ndx, a is then the factor that transforms this proportionality into an equality.

Nuclear cross sections are on the order of 10-24 cm2 (one barn), as expected given the geometrical size (cross section) of the nucleus = rr R2 = 3.14 10- 26 A213cm2 Cfgeom X .

(b) Differential Cross Section. For a single scatterer we de.fine4 da(8, r/>) flux scattered into element dn at angles 0, <p dn incident flux per unit area It follows that ..

..

. r2rr {1( da lo Jo = d</J d0. sin 0d0 a, 3OccasionaUy confusion arises because the area of the incoming beam may be smaller than the area presented by the target as shown in Fig. 8.lb. The definition of Eq. (8.1) is valid in either case and always leads back t.o Eq. (8.2).

4 See the discussion on "solid angle" in Section 9. L I/ii 8 Particle Detectors and Radioactive Decay ;_ J~ wbe~e the integrati?n is ~ver all angles. If after the scattering proces~)ijf :/}Jti particle emerges with vanable energy, then , .

{:@I d(f(0, "'· E) t@I dQdE .

flux with energy E, within d E, scattered mto df!. at angles 0, if>.:){\{~:~ t/\{~~ - incident flux per unit area .

·.·.·.·.·-·-·-·I It follows that Jill [ o0 d 2 o-(0, ¢, E) dE = d<J(0, ¢) :){jJ§~ Jo dQ d E dQ ~ )}t~~f.j . . . . . //~~Jl~ where the mtegratton 1s over all possible energies of the scattered flux~:::/:::~~~::?:f.

(c) Absmption Coeffic~nt. To obt~ the p:ob~bility for scatterin~,i~Jll 1~$~ a length x of some matenal, we_ consider_an mcident ~ux per uni~ Io; I (x) represents the flux at a distance x mto the matenal. Accordmg·:ta.:;~:?Jffi .-/iA\}11 Eq. (8.2)

.·.·.·.·.·.·····-~ (g:iffli = = -dl(x) l(x)dP l(x)crndx; .?}(}~ thus ·.-:•:-:-:-:•:•,..,-.~ <::::;::::::::=:~ }:(:=:=:~%~ - = = -o-ndx l(x) loe- unx_ :)}it~ 1 ' . :::::::?;::::~: :j-:#-:-:-i:•}:-:-l:-@~~ If we designate by P(x) the probability for scattering in a length x, .:\:}til have J;i/'//I P(x) 1- (~obability fo~survival in a length x)

- 1 - e unx - 1 - e K,'t ···-:·:·:·:·:-:~m - - , .· (!)!]~ = = whi~l(JW where K crn is the absorption coefficient. Similarly>.. l/an, J& has dimensions of length, is called the absorption length, or mean free pa~f ::::::::::::=la -:?:)):ft The density of scattering centers n is given by .}/II n pNo/ A if we consider scattering by nuclei ne pNoZ/ A if we consider scattering by electrons (8;4;}\W ·:)!i){:fJ nN pNo if we consider scattering by nucleons, o(,¥:~11 where No is Avogadro's number 6.023 x 10 23 and pis the density m~fi!

material in grams per cubic centimeter; Z and A are the atomic and ·1 .......

,:,,h numb e r, respect:J.ve y. -:\/:::~~ ... ,, .. ,.~ Xii!?@ :1 ?tJW r:: f •.· : ·:'

## 8.2 Interactions with Matter

-:-: ::::: :=:.: Often we wish to express the absorption in tenns of the equivalent matter :::·. traversed, namely, t = g/cro 2 . Then the thickness of the material can be .;•..,..•:. - . expressed by d~, where .: ,• t d{ pdx.

The mass abSOllJtiOn coefficient is defined by ~, K :::=::=::: µ = -, (8.5)

,.·. p ~::: ;.:;:: so that the fraction of a beam not absorbed is :::: ~::: --:,:, l - ~> (8.6)

lo= e ~ - :=::: Similarly, if the region of interaction is very thin, the scattered flux is given lj;_'.l:_.

. directly by ~}· :;::: ls= loan dx, for exrunple, for nuclei, .~,.: :.

:f:· ~~~;:· j_ 8.2.2. Energy Loss of a Charged Particle ~~/ ,I'.·.

When a charged particle collides with atomic electrons, as we have already .~= .=.:.· . . , . · -· . . .. · ·· . ..• • •• . seen in the Frank-Hertz experiment (Section 1.3), it can transfer energy to :;;::·· ,.·.· ,.·. them only in discrete amounts. It can either excite an electron to a higher :;:::· ~~::: atomic quantum state or impart to the electron enough energy so that it wiU :::::: leave the atom; the latter process is the ionization of the atom. Since in our <=::: ?::~: present considerations the incoming particles have considerable energy, ,.·.· J: r:: the process of ionization is by far the prevailing one, and we will use lhis tenn in the discussion.

~j: Let us consider then an atomic electron at a distance b from the path of f:.· a heavy charged particle, of charge ze, mass M, and velocity u, as shown f:: in Fig. 8.2a. If we assume that the electron does not move appreciably [j( dwing the passage of the heavy particle, we can easily obtain the impulse if transferred to it due to the electric field, E, of the passing heavy particle: ~::. +00 f +oo :z:.:, 1 =:::·~·- = _ = :-:=::::: /J_ Fj_(t)dt e -oo E.1(1)d1 Ill 1+00 = +00 dt = -e :«-:· e 1 E.L(t)-d dx Ej_(x)dx.

:~::;:::;:: - oo X V -oo ~t ~f:.

~··)-:-::.

~ './• . , · · 302 8 Particle Detectors and Radioactive Decay (a} (b)

ze,M ~-+-'-t!'t-..

:::!!}}f~ V -:-:-:-:-:-:-:-:-:~ ·:::::::::::::::@.

b ~--------ll~l~--,.d~iii!!!@}~]j e,m 1--dx--- ..

W:::#::::i:i:!:;H::I=:= ~ FIGURE 8.2 (a) A particle ofch:"'ge ze._ mass M, and velocity u p~s by an electron ti an unpact parameter b. (b) The differential number of electrons w1th an impact paramet~t}~:~~ .))if b in the interval db is given by the volume of the cylindrical shell 2n bdb d:x.

:}{:~~~~~1 We use only the component of the electric field normal to the particl~/if trajectory since the longitudinal component ave~ages to_0 when inte~~mrl from ~oo to +oo. However, from Gauss's law, mtegrattng over a cylin4::¢l}.ttt~llI of radius b, coaxial with the trajectory (see Fig. 8.2a) 1 w + e have = f = l T_\LA~1 00 = - 2 + z··e· \ ,··-. f ··..· @ -..·,... . · · ·~ ~ ffi} ~ i.

4rrze E · dS E.1.2nb dx and E.1.dx b ........

.:)}J~f~@ - oo hence \}ft~ 2ze 2 ./:==~=l~:~ = vb· I.1 }{}f?M collisi6. * :-: / ;:- ? :-: 1 -:- ~ :-~ . Since the electron was originally at rest, its momentum after the = ··}))\ff, p I 1., and the energy transferred is ::Ji P2 2z2e4 E(b) = - = 2b2. (8)11:::::~ 2m m v ·.·:-:-:-:-=-=·=·.·:/1- . ·-:-:-:-:-:-;-:-;.@- Thus E is a function of the impact parameter b. To obtain the total enerij{}@ )~$ lost by the heavy particle per unit path length, we must count how mari'f :}Jif@i electrons i~ encounters and ave~age ov~r ~e im~act par~eters. .

~f{?J@ From Fig. 8.2b we see that ma cyhndncal nng ofradms h~ width and unit height dx, there are contained 5 ne2n:bdb dx electrons; hence \/)j~ .·.·.·.·.·.·.·-~ 2 4 ·. . ·.·.·.·.·.·-·-=-;:~ )))t~ dE(b) _ 41inedxz e db - m v2 b :::::::::~::m ':<t:iJW.

and ·):;:;:;i;~ ..· .·.···-?·~m = 4nz2e4 [brrw<] , ·-:{_:}f~ _ dE ne In (8,8}:~~=-i dx mv2 bmin ·:::::::::::~:% ·)i!f)f~ 5ne is the electron density as also given by Eq. (8.4). .<·.·.>·.-..l; mf.$ ::::::=::~~ )!/{@ ·-:-:-:-:,;~ :::::}:~ ./\)1

## 8.2 Interactions with Matter

where because of the logarithm we had to use finite limits on b rather than 0 and oo. The finite limits are imposed by physical considerations: for bmax we consider the distance where the time of passage of the heavy particle's ::::-:·__·=;=:=:_;:::_··::: : field becomes of the same order as the period of rotation of the atomic electron in its orbit. Thus b I = -V .

-r=-= or bmax (8.9)

V V ::::: ? 6 For the minimum value we equate b to the DeBroglie wavelength of the •:•:• ::::· electron ~=: :::: Ii 1i ~::: = - = -. (8.10)

~::: bmia ,:.:• p mv ~:~: V We then obtain :~::: ....... [mv 2 4 2 i~~~- -d-E = 4nz e ]

---ne 1n -- . (8.11)

,·-·.

:r:: ..:• :•: dx mv2 !iv 1::: ~.

The frequencies of the atomic electrons v are, however, different for [: each orbit, so that a suitable average ~ust be taken; we thus replace (liv} ~---· ~t with an average ionization potential I. Finally, inclusion of relativistic ~=-: effects and a precise calculation give t=::: ,,._:- ..

: - ~-=_·· 2 4 2 ; ; , ~. .. . _ : : -- :. _ : : - .· -d-E = 4 - n - z -n e e [ In _ 2mv - /J 2] (8.12)

r.--. dx mv2 J( ] - f!>2)

,--·.· ~:::; ~?

for the energy loss of heavy particles due to ionization.

t = In Eq. (8.12), {3 v/c, and we see that the energy loss is only a function r: of the velocity, v, of the charge ze of the incoming particle, and of the f:, electron density, ne, of the scattering material. Note that in Eq. (8 .12), m is ~~=:=-:::-: ~f the mass of the electron while the mass of the incoming particle does not ~:;:: appear at all.

~( Before further investigating Eq. (8.12)~ we should note the following ~:=:;: effects: ~f- f?

(a) Equation (8.12) was derived on the assumption that the incoming [~t\ particle is not deflected, and thus il is valid only for heavy particles; for electrons the term in the parentheses must be slightly modified.

,n r··- 6A n alternate approach is to set hmin sach that maximum energy is transferred to the f:. e lectron. Because of momentum conservation we have Pmax = 2mv leading to bmu, = f : ze2 /mv :::::: .......

-~=::· ...: :: •:-:- ·;::: JI·.·.

.~ ..

=..

:.: :.

~~=:: 111111 304 8 Particle Detectors and Radioactive Decay also nuciijf/J~ (b) Electrons lose energy through their interaction with the and this is the prevailing mechanism at high energies. That is, the electrdnf.i@i is acceleraB.iitJ trajectory bent by the field of the nucleus, which implies an ..........

·Jcqiwfla~ (since the velocity vector changes), and from electrodynamics we ''bremsstrahl~j@}Ij that accelerated charges radiate. This radiation, called s .

. di d . 8 2 6 ·. .......... )Pf.

1s scusse m ecnon . . . }({f:~ (c) Forextremelyrelativisticparticles, v ~ c,/3 ~ l,Eq.(8-;12)predf¢titiJ 2 = E/mc1f/ffel{f a continuous rise in dE/dx proportional to In y where y 2 1 2 1/(1 - {3 ) 1 . Such a fast iise, however, is not observed experimert~~~J~ This is due to polarization of the medium: the electrons that are heing°!~tf~ ~edue(?J~f jj m_to motion by the field of the incoming particle move so ~s to effect of the external field. Consequently a much slower nse with en~~:~ 7 /?///~ results; the correct expression is .

.·:::::::;:;::;~m.

2y _1]

dE] _ 4nz2e4 [ mc2 + '/\:~}?:m ln-- (8"j ;~'.{;:.::-~ dx ion - mc2 ne [' 2 ' · ~J~{;f~l where , " J = 4nn,ze I == .

r®p For silver bromide I'~ 48 eV.

( d) For low-energy particles we obtain from Eq. (8.12)

dE z 2 z2M dx v2 2E :-:-:-:-:-:-:-:-:-:-: -:·::::::::::::::::i where M is the mass of the incoming particle and E its kinetic en~~Jj The above expression (when applicable) is useful since a measuremerif~f;::~ /)[ff@.

dE/dx and of E identifies the incoming particle Ee:) M. /: _;III ex •')}i~i emulsl~Af.iJ~ (e) In image-forming devices and particularly in nuclear 1#¢.~f~f the density of developed silver bromide grains can be used as a sure of the particle's velocity because of the dependence of Eq. (8.12fAA(j Eq. (8.13) on /3. However, the density of the track depends only on en~~:~3 \)}~{}I~ 7 See J. D. Jackson, Classical Electrodynamics, 3rd ed., Section 13.1, Wiley~ New Yp~ij} 1999.

>I ij-: t==:· i-t

## 8.2 Interactions with Matter

x~=r-:·- :i=:: ~::::- transfers <5 keV, since when an atomic electron acquires more energy, its ::?:::- X:=: own track becomes visible and separated from the primary particle's track; ~\ ~/ such electrons are called knock-ons or delta rays. The energy-loss expres ~>· f ::, sion for energy transfers <5 keV does not exhibit at all the relativistic rise of Eq. (8.13), but for high values of y, stabilizes at a plateau 1.2 times the J~::?::: minimum value.

1:=:: ~r ~:=:- The energy loss of a heavy particle in a typical absorber, suc}l as nuclear emulsion, as a function of the logarithm of its kinetic energy (in units of ;:::f:: rest energy) is given in Fig. 8.3. Strictly speaking, this cwve holds only for a given absorber and all singly charged particles, since we know from f .

Eqs. (8.12) and (8.13) that dE/dx is a function only of the velocity of the ( incoming particle and its charge. (Note that K.E./mc2 = y - l, which bas l( a one-to-one correspondence to fJ.) However, the general behavior of this ).{ curve holds for all absorbers.

f: We do recognize four regions of interest: (a) near the stopping point where a Bragg curve is applicable (see Fig. 8.32); (b) the low-energy region ~f where the 1/ v2 dependence of Eq. (8.12) dominates, and tends asymptoti i !

..... cally toward the value l /c2 ; (c) the relativistic region, where because of the ~t · = rise of the logarithmic term, a minimum appears approximately at y I; .~t and (d) the screened region in which Eq. (8.12) becomes applicable. Had \ polarization effects not been included, the rise of the d E / dx curve in this -?

last region would be steeper than indicated in Fig. 8.3. The lower curve \ . in Fig. 8.3 (energy transfers <5 keV) is applicable to the grain de,nsity in .!I nuc!eM emulsions.

·-:-: 1/v2 =::: Slopping Relativlstic Screening ?· region f' 3 region ?· (Bragg E :.:. /curve ) b0 , -::: ~ Total :=: > 2 :-:-· :!

?: tu~ :::: "bjCJ .... 1~ 1 ·:=:·' ...: .; 0.1 10 •:~: ~.r. ' y-1 ""•,-,• ·{! FIGURE 8.3 The universal energy-loss curve for a singly charged particle plotted in ..f MeV/(g-cm-2 ) against y -· I. Note the upper curve for the total energy loss and the lower /curve for energy Joss involving only energy transfers smaller than 5 ke V.

.~.... .

.....

•::: :~:: .,.. .. .. · · . ... ·.

..- .. · •::: ~ ll /l)il 8 Particle Detectors and Radioactive Decay If we choose to calibrate the abscissa of Fig. 8.3 in ·units of.e n~ij~i univ~¥~aH!

(MeV) of the particle rather than by y - 1, we will not have a ·-·~ ......

curve any more, but for each particle the energy-loss curve will be sh#'(~t }~ = \Yh~if~ horizo11tallybymi/m2, insuchfashionthatdE/dx]m dE/dx]m the 1 2 corresponding kinetic energies 11 and T2 result in the same valui ~ii.f ~ .)/f)~~ y - 1: · :11= :: = 1111 ~(y - l). :: This is shown in Fig. 8.4~ which gives the absolute value of energy<i~Jfj~ . . .... ., .;,,: -dE / d ~ (in Me V /(g-cm- 2 )) in air for protons (c urve 1) and n: -me_ij~~~i = f~t#~f~~ (mn 140 MeV ; curve 2), where the latter is shifted to the left by a - 0 150 <::::::=::::;:;:~ mrr mp ~ . . .::::::::::;::::~ Further, if we consider particles of different z, the energy loss will dUf:et.m thee1\~f.Mf~ by the ratio (z1/z2)2. In this fashion we obtain curve 3 in Fig. 8.4, to!tff~?~ loss of alpha particles in air, which is shifted (with respect to curve 1)

= 2 \4/i~~~ right by a factor of ma/ mp 4 and upward by a factor of (za/Zp) ..

the If we now turn our attention to the dependence of d E / dx on abs6ifj~ ~~ oi(~llfi material, it is clear that it will vary rapidly, due to its dependence If instead we use - dE/d~ (the energy loss per g/cm2 of rnaterial}J~t}~ -::\}=::::::~ variation is much slower since , .·.·.·.·.···",/"

,: ..: ,:-:-:•:.-:~ ·> :-:-:•:•:•:- z •:: ::::::::::::~ ne = pNo .' :-:-:-:-:•: ..; - _:.:) }j ?:::::/~ and . .· · . . · - . . · · . . · ·... · ·. ... . · · . ., . .

.?)i@ ·-:-:-:-:-:,;-: = ::::::::::::~ d~ pdx_ :< : :: :: : : : :::=~ .::::::::::;::~ .::::::::::::=~ Thus .':){~[~~{~~i ,·.·.·.-.. ..

, ,· : ::I:::::I::: " ~ ' dE = Z 2 - :?::=:::~ - d~ No A z f(/3, I), so that the energy loss per g/cm2 is larger for low Z materials, neglecti#.ii~~ i, the small dependence on the average ionization potential. Curve 4\~(( Fig. 8.4 gives -dE /d~ for protons in lead, which is indeed lower than$,~@~~ in air, but not by a large amount. · ) )}~ sin~fJ An approximate universal figure for the energy loss ofa relativistic charged particle in any materials is 2 MeV/(g-cm- 2 ). })jt . .: ::::::~~:: )ft ::; if[ -- ' ,I I )01 14)00 ,.... ~ J}.

800 !'... ·-.~? ~% ",£'~ '64 ...... ~l'-,,,. ~ t\..

soo I, ...... ' ' ... ~,o '"

200 1>10, ' ......

.... ~6' - ~ :'. ~ J',,4-94- ~, by(tl2•4 - !'lo\ ... 'b4, J t'I Shltt 100 l' 1'~~ l'l N In 80 :"i ' I "'-~Q'. ' ~ ' ' ' • J "'!Ir,.. 'I, '- I r,!*;, I t"-. !'...

s0\ 40 ~~~ ~. "'- Shift by _mo ;4 "I'...

a> 30 ' ~'' mi> 'I"-..

~ 20 I i " ·~Ii) "' ~ ' ¥j\'t; i"-r,.. ~~ .....

I .. ~ ~~~ - f 10 .. l 1, ·' I'... ' ~ .. .. .....

8 .. ...

6 ShH1 by !! m l!! p .. -0.160 ...... - .._ '- .......

l !"-.. ......... "'t-....

4 .... " .......... ....' ,.... ...

...

3 .. ...___,L_ ..... .....,...,i,.,.

--r... .. ,I 1o' 10"

O.l 0.2 0,3 10 100 Kinetic energy, MeV PIG URE 8.4 Energy~tos.s curves for different eharg~ particles in air and io tead. Note how au lhc curves are related to each other.

Ji\IlW, .:-:-:-:-:•:•:·%'~ ){/:J~ 308 8 Particle Detectors and Radioactive Decay ·-:-:•:•:•:·=·w.

?Utt~~ ·c1 .

8. 2 .3 . R ange of a Cha rge d Pa r t I e ·. ::::::::::::::::~ ··.·.·.·.·.·.·---~ Since the exact expression for the energy loss ofa charged particle is kno~J/!!)i;f ~o n:corni#:ti{{~ it is ~ossible ~y integration find what total len~ of material a~ ttm ?artJ.cle of given energy Will traverse before COllllilg tO rest; this 1S Callif its range R, and we can set / {:\~{?J : :-:-:-:-:·=·===-~-= = R dE - })\tt Eo la -~dx ...:::.:.:: :·:=··:~·=z~.~:f..i&, 0 d X ·-::::::::::½;.-).~ ·.::::::::::~=~~ ·.·.·.·.·.·;'.·,-.~· or conversely, since d EI = z2 ne f 1 (/3) and d E M /2 (/3) d/3 (M}#Jfffej . . . 1 ) .:.)..).~..,\ I. ~ the mass of the 1ncommglo pa rtJ.c e , .. : la/Jo _:}f)@f@ R l dE M f2(/3) M R == la o dx = -z z n - e Eo - /1 ( - /3) = - Z 2 - ne o - /1 - ( d /3) f 3 = Z - 2 n -F e (.Bo - J / { /:{ / i f i~ ~ ~11::::=~==i (s.

. . . . ·. :;:;:::::::~:=~~ That ts, for the same velocity the range 1s proportional to the mass.:9;f}~ml the incoming particle, inversely proportional to the square of its charg'.¢;{@{@ and inversely proportional to the electron density of the stopping materi@'./@~~ diff~ii}I?:i@.

Extensive tabulations of range curves for different particles and J~ ent absorbers are available. 9 Also various empirical formulas have lxxff ~I Ji devised; for exampl~, for el~ctrons, Feather's expression gives for the rari~,f of electrons of alummum (m g/cm'} R 0.543E -0.160, E > 0.8 MeV, (8.l~fjfi -:-:•:-:-:-:-~ .//1@ where E is the initial kinetic energy of the electron (in MeV ).

grai~#/{~ As suggested _above, it is highly preferable to express the range in per squared centlmeter, because then the dependence on the absorber matt,({j rial is slow (since ne/ p = NoZ/ A), resulting in a larger range {in g/cm ... ? .. J ... \ . i .. % * .

in heavy elements. · :::}}:::~ alpaj({~ Figure 8.5 gives the range (in g/crn ) of protons, rr-mesons, and f1 til function As p~cles as a of t~eir ki~etic energy for air. explaine_d Fig. 8.4, the Jr-meson curve 1s obtamed from the proton curve by shif!:i~Jt/ ~ = ?:¥JI /3o, to th~ le~t by the fa~tor mrc /mp 0.15 to reach the same but als~ I'!" = mult1ply1~g the ~rd1nate v~u.es by mTC p 0.15; for the alpha par 4 nc 1 ~ f ~ l w l l the curve 1s obtained by shifting to the nght by the factor ma Imp -:•:-:,:.;,:-~ ·/i/lt~i~ 8 Nonrelativistically we have the simple relation dE M c'1-f3 d/3.

9 by s)f see, for example, the compilation the Particle Data Group (2000; see Section :;:::::::~;I \\lffi }}/ffi .. ::::::=m,'i11- })}=ffi.

~%».~~-<·~~~~,»»~~~~~~~~»~~~"!'~~--~~:~:--.:~~:·:-ai:~:1:~;~;.:,;~:1:1;~:•:1;-;1:~;1>>:<1;1;1>:•:(<1:1~->:<·>>>~<,~,>>.<,.,>.,>.,.'.'.·.···<·~<·>>~<·~<·i<···~·>>·,:.·,:.:,·.·.:,·.·.·.·.·.·.·.·.·.·.·.·.·.·.·.·.·.·.·.· ·.· ·.·.·.·.·.·-~.· • • • • •• • • • • •• • • • • •• • •' '• ·.·.·.· ·.· ·.· • • • • •· •· • •• _,,.,l , .,,,,.,,,..

_...

I-"'' / A'~~~ .. .. v ~tr ,9 ,,.., V _,,/ too I J~~/~ / / / / "'v ..

30 ,,,,,. ,, ,,, 20 1 ....~... x/ -/ r v ( .,,,Y ~I,,' .,,,..

10 ,, ~"-/ k-"' ~~ 5 ·;t; -~~ ~ v·t-$'" wrti'Y C\ E I 3 "11, 5 , " 'v'o-~. . , ~ 2 ,- . , ,1/: 1/ c;n ~ / /I / / O> ,,, [ n C C :I : , 0 0 . . 6 3 == ... . ~ .... .,,v / ,, .,,... ~~

## 0.2 Shift by 0.15 1,., .,,. x,,, / V

+ .,.. ,.. ,,, ii V / ,.,, ,, j 0.1 > .r ..

.. / v.,.

.. ..,,,,,, -/"' ,, 0

## 0.05 c- V/ Shiftby4/

re ,....

## 0.03 ./

0.02 ,r ..,I,,"' /l ,,v. / 0 V / om x' V ,,,,,,.ii"

.,,,,,, 0.005 0.003 /''

## 0.002 ·~

0.00'1 1 2 10 100 iOOO Kinetic energy. MeV FIGURE 8.5 Range curves for different particles in air and in lead. Note how the different curves are related to each other.

]j ;;Jffif f ) !//ii 310 8 Particle Detectors and Radioactive Decay multiplying the ordinate (first) by ma/mp ::: 4 (due to the different m~ssj{\J 2 = \}/f and then by (Zp/Za) 1/4, hence leaving it unshifted.

Finally, the range of protons in lead is also given. The concept of range,()}?; loses its meaning, however, when the amount of material that the particle\?} fre~((f must traverse before coming to rest is on the order of a nuclear mean path as explained in the introduction to this section. 10 }\}~ )If 8.2.4. MWtiple Scattemg In discussing the passage of a charged particle through matter, we have{/]

neglected up to now its interaction with the electric field of the nucleusiJ=~ . .· .·.·.·%•.

because indeed the energy transfer to the nucleus is minimal. However/ \~~: . ' •• .r.,, ..

when a particle of charge ze, mass m, and velocity v passes by the vicinicy(f~~ of a nucleus of charge Ze, it will be scattered (Fig. 8.6) with the Rutherforcf\~1 ·.;,:-:-:..}; cross section ::::::~::: (e /AiE da I 2Zz) 1 :-::::::r.:~ = 4 6}Uf}~ drt mv2 sin40;2' (&.l . }!f~ showing that the probability for small-angle scattering is predominant.,,-For\ }{ /?J such small angles we approximate the angle of deflection by :}f = -6.p = 2Zze ' (B .l ?)}·.·.·!.·f.·~.

p pvb ))} {@ where p is the momentum of the particle and b is the impact parameter.

During its traversal of the n1aterial, the incoming particle suffers many\{~ )j small-angle scatterings. It can be shown that the resultant scattering angle 0,.

after traversal of a finite thickness of material D, has a Gaussian11 distrl-)} bution about the mean 0 0; the probability for a scattering through an/ } angle within the interval d0 is )} .·.·.-- (e) ·,:-:,; :/;~; P(E>)d0 - 1- exp [ - -1 - ] . · :: .· : . : · : · : 4 = aJ'lJr 2 a .:i :~:i .·.·. .

= /02 Toe standard deviation is a (the root mean square scattering angle). /}!

.. :~/i 1°For heavy ions, energy loss due to collisions with the nuclei must also be considered.·{!

11See Chapter 10. /} .'./·

## 8.2 Interactions with Matter

ze, v, m lZe FIGURE 8.6 Deflection of a charged panicle when passing in the vicinicy of a nucleus.

Note the scattering angle 0.

For the mean square scattering angle we have 2 2 4 - = 81rz Z e ( aovp )

02 2 2 nD In 4/3 2 . (8.18)

v p 2Z ze where ao is the Bohr radius. We further simplify Eq. (8.18) in order to exhibit the dependence of 02 on the incoming particle's charge z, ve]ocity /3, and momentum p, as well as on the material's thickness D, the density of nuclei n pNo/ A, and the atomic number Z: we obtain where F is a slowly varying function of the parameters of the incoming particle and the scattering material (it contains the logarithmic term and constants). Furthermore 1/(Z2n) is proportional to the ..r adiation length"

Lrad of the material (defined in Section 8.2.6 below), which is frequently tabulate<L so that we finally write /D(l 82 = \01nns = z21.2(MeV/c) 'JI:; + €), (8.19)

p/3 where 10\nns is in radians, and p must be expressed in MeV/c; is a small correction 12 depending both on the scattering material and on /J / z of the incoming particle. When we are interested in the rms projected angle, the numerical factor in Eq. (8.19) must be replaced by 15 (MeV/c).

312 8 Particle Detectors and Radioactive Decay 8.2.5. Passage of Electromagnetic Radiation (Photons)

through Matter •:•::::::::;::::::¾ ~;}{{® As mentioned in the introduction to this section photons lose energy or ·:\\=::::::% absorbed in matter by one of the following three mechanisms: :::::::::::::::~ ./:JJfil (a) Photoelectric effect, which predominates at low energies~ :~\)JJJ: (b) Compton effect, which predominates at medium energies (below . M V) d ..· .·.·.·.-.., ..,..::2:.

few e , an .·}\ :~~~=-.. ~ (c ) Pair production of electrons and positrons, which is dominant in th~}}i~l • .. :-:-:-:•:-~~··:•j high-energy felYJOn. .-:;:::::::::::x;:~ b .\ :\:~~:::;:: which//!f@i The relative importance of these processes and the energies at they set in are best seen in Fig. 8.7, which gives the cross section/ ))§~~ of{}JJ.fil for the interaction of a photon as a function of its energy (in units the electron's rest mass). We will now briefly consider each process\ }l:li~ . ::::::::;~~f3 separately. -::::::::,:-~:: .:::::::~~;~~::;: (a) Photoelectric Effect. We speak of the photoelectric effect when)\)f.ti the photon is completely absorbed and all its energy is transferred to an}}!l f:!

atomic electron. Consequently the photon must have enough energy tc:{))§~J ... ·.·.-..............._ .,.

excite the bound electron from its quantum state to a higher state or intp,:::::::::=~:=f= \\J@~ the continuum; the latter process (ionization of the atom) is much more '·.·.· .-,.. ..... ,.. ....· probable. Since the binding energy of the inner electrons in atoms is on \ :::::~::~:: i{}}J the order of kiloelectronvolts, as the frequency of the photon is increased and it reaches the value of the binding energy of a particular shell, 13 :{{t}} :{Jfi a new "channel', opens, and we expect a sudden rise in the absorption /}f~: cross section. Apart from the onset of new channels, the overall variation · :/f~~J of the photoelectric effect is a rapid decrease as the third power of the pho- ton frequency (as v-712 ), thus resulting in the curve shown on the left in :}Jf; if]{ Fig. 8.7. The cross section for the photoelectric effect is derived in Reitler · (1954), 14 from which we give the nonrelativistic value for the ejection of :{}~f \Jl i one electron from the K shell, when the photon energy is not too close to 13 Note that n = 1 electrons are said to be in the K shell, n = 2 in the L shell, n = 3 in the M shell. etc.

14w.

Reitler, The Quantum Theory ofR adiation, 3rd ed., pp. 207 and 208, Oxford Univ: Press, Oxford, 1984.

## 8.2 Interactions with Matter

Pair production ""

Photoelectric / (,..,1 Compton c=:~~:::-~:::i:·=::.e:~___t.__----1 O'n,omeo.~ O.Q1 0.1 1 70 ,100 -y=hwmc2 FIGURE 8. 7 The cross section for the interaction of photons with matter as a function of their energy (expressed in units of the electron's rest mass).

the absorption edge, OT 1!5 = 2.Ji. [ OI> 4 hv2]- 7/2 (cm2)_ (8.20)

( 7) me Note the dependence on the Z of the nucleus, indicating that L shell and higher-shell ejection is less probable because of the screening of the nuclear charge. Here a,- is the classical Thomson cross section, which is derived from the simplified assumption of a plane polarized elecromagnetic wave scattering from a free electron (it is assumed that the displacement of the electron is much smaller than the wavelength); we obtain [_i:_]2 r5, or= = 8Jr 8Jr (8.21)

3 mc2 3 where r = e 2 / mc2 is the classical radius of the electron= 2.8 x 10- 13 cm.

Note that the Thomson cross section is independent of the frequency of the incoming photon.

(b) Compton Effect. In the Compton effect, the photon scatters off an atomic electron and loses only part of its energy. This phenomenon, which is one of the most striking quantum effects, is described in detail in

## Section 9.2; the cross section for Compton scattering is given by the Kleio

Nish.ina (K-N) formula, shown in an expanded scale in Fig. 8.8. The energy of the photon is given on the abscissa in units of the electron rest mass 15 y = h v / mc2 , and the ordinate gives the ratio of the Compton cross section uc to the classical Thomson cross section cry.

lS Not to be confused with the usoal definition of y for a charged particle y = E / m c2 , introduced in Eq. (8.13).

] iiill 314 8 Particle Detectors and Radioactive Decay ::::::::::~==i \\::=:::=; II/ 1.0 0.8 .•.·•·•·. .... ·.·;J t5"" 0.6 0.4 0.2 0 L__ _ _j__ __. .,L_ __ L.__ _.:::::::::t:::=::~---1...

·::/:i?i~::f fi O.o1 0.1 1 10 100 1000 . y- hvl~c2 .

FIGURE 8.8 The rauo of the Compton scattenng cross secuon, ac, to the const~F:\:::[J #.}fW Thomson cross section, at, as a function of photon energy expressed in units of the electron'.

rest mass. }\::=:~~:~ )!()~~~ We give below the asymptotic approximations to the (K-N) Comptoi(j~~~ . • ·.·.·.·..;-..:. ...• X ..

scattenng cross sectton: -:/{{~~ . .·.·.·.·.·%·..-~ F or 1 energies: -:\}:~:m OW ac = a-r (1-2y + ~ y 2 + · .. ) y = hv/mc 2 « 1 ,: 1:111 ::::::::::::i .:::::::::::.~ For high energies: :\/\~ 3 1( 1) .·.·.·.·.··% :}//j ac = -a-r- ln2y + - y = hv/mc2 >> I. (8.22f)t ~ 8 y 2 ·-:):/:~:~~ (c ) Pair Production. In pair production a photon of sufficiently higf,(/tl ' ,•.·.·.·.·.·.I'., energy is converted into an electron-positron pair. For a free photon con~/:=:::=¼ servation of energy and momentum would not be possible in this procesi{)/~ so pair production must take place in the field of a nucleus (or of anoth~ ({J~ electron), which will take up the balance of mom.entum. Clearly the thresh~=)ff!

old for this process is 2mc2 (where m is the mass of the electron), henc#,)/lf& fh:~{f j 1022 keV . The cross section for pair production rises rapidly beyond ·/i})iJ&, threshold, and reaches a limiting value for hv/mc2 ~ 1000 given by16 (28 2 ::::::::::~:;?i ·:·::::::~::fi O"pair = 1 Z 3 r 0 2 9 tn 1 18 / 3 3 - 2 2 ] (cm 2 ). (8.2~ :: f ::t~ i : ~ I 1 1 ::1 see Heider (1984), p. 260. \ :/){~ . ·;.;.;,:;;::,.; <:::;:;:-ij ·-:-:-;,;.;.::, .:! !!!!!!~~~

## 8.2 Interactions with Matter

Since both the photoelectric and Compton effect cross sections decrease as the photon energy rises, pair production is the predominant interaction mechanism for very high-energy photons.

It is advantageous to introduce the mean free path (L pair) for pair production; when a photon traverses a material with density of nuclei n, 1 I L pair= -- - ------------- ., (8.24)

no-pair (28/9)(Z2n/137)r5 ln(l83/ Z113 ) • where we have dropped the small tenn 2/27. Thus, the attenuation of a beam of lo photons will prpceed as I (x) loe -xI L pair. (8.25)

In conclusion, Fig. 8.9 gives the total absorption coefficient for a photon traversing lead as a function of its energy (in units of the electron rest mass).

Note that 1<p ap2n because there are 2 K-shell electrons per nucleus Kc crcne electron density Kpak Upau-n density of nuclei.

The dashed curves in Fig. 8.9 indicate the relative contributions of each of the three interaction mechanisms.

\ I

## 1.4 • 9, I

:::- \~ 1-u 1I • \~ ? \~ lg ~ c 1.0 \ \~ l (1) ·tr, Cl)

C 0.6 \ . f4!

.Q i . 5 .. . \ \: / \ . I .2 \ '>· cC 0.2 '':<"' ' ___..__·--= .......

0 ..__........_____.,_,___,,.......:;'--I=--,____._, _·. ........ -"-----1-..-

## 0.1 1 10 100

y=hvlmc2 FIGURE 8.9 The relative conoibution of the three effects responsible for the interaction of photons with matter. The absorption coefficient in lead is plotted against the logarithm of photon energy (in units of the electron's rest mass).

316 8 Particle Detectors and Radioactive Decay 8.2.6. Interaction of Electrons with Matter (Bremsstrahlung)

Since electrons carry charge, their interaction with matter must follo~}\}@ along the lines given in Section 8.2. Because of their small mass, however;/!{:~]

i}}@ their interaction with the nucleus results in significant energy loss by racitf mode!{:J~ ation; this process, called ''bremsstrahlung," becomes the dominant .·.·.·.·.·«. ..

of energy loss for high-energy electrons. · ){}§~ We can obtain an estimate of the cross section for ''bremsstrahlung'' frorri\J~;J a classical nonrelativistic model. Consider an electron (charge e, mass n{}()j us:UiJ1 and velocity u) passing by the vicinity of a nucleus of charge Ze, and let 8.6f}){i{l assume that in the collision process the nucleus does not move (Fig.

The scattering angle of the electron is given by Eq. (8.17), and the chang~))f{l ..............

··:/\jfj in the velocity vector of the electron is :,:,:,;.;.~' ·)!}~~ 2Ze2 ~v= - . (8.26).:,:-:-:~.-·.

mvb The radiation formula for an accelerated charge is 2 · 2]

== - d E = -2 e- [ (~• ) - (~ x ~) .

P(t)

dt 3 So for our case, since Pis nonnal to~.

= -2 e- ,~• , 2 dE(t) dt.

3 C .·.·.·..-.-...

!ill By a general theorem of Fourier analysis, if L: )?} 2 )ii/I = [: £ IA(t)i dt, then also f = 2 e2 +oo 2 E - IA(w)l dw, C -oo 17 see Jackson (1999), p. 666. In Eq. (8.27) y was set equal to 1; similarly Eq. (8.28}\ J = :J:: should include a tenn (1 - /J2) l/y2 • which was also set equal to l.

\]~ )[ }I/

## 8.2 Interactions with Matter

where j+oo = l A(w) ~ A(t)eiwt dt (8.29)

v2rr - oo is the Fourier transform amplitude of A(t).

Using then Eq. (8.29), we obtain in analogy with Eq. (8.28) the frequency spectrum of the radiation 2 2 = 2 ~e [ + 2 ] = 4 ~e 2 dE(w) 3 JA(w)i2 IA(-w)l dw 3 jA(w)l dw. (8.30)

To evaluate_dE(w) we must perform the integral indicated in Eq. (8.29)

:-: with A(t) = 1~1- We assume that the acceleration 6./3 occurs in a very brief interval of time, on the order of r a/v, where a is the characteristic distance over which the force is appreciable ; then j+oo A(w) = _l_ l~l eiwt dt = { $t:if3 wr < 1 (8.31)

v'2rr - oo 0 wr > 1.

If wr > 1, then~ will be several oscillations of the exponential term over the region where l~I is different from zero, and the integral will average to zero.

The integral results in a rectangular spectrum for the emitted radiation, as shown in Fig. 8.10, with 2e2 4Z2e4 dE ----- 1 - = - 3irc c2m2v2b2 Wt < (8.32)

dw =O wr > 1.

· · Next we integrate over all impact parameter b to obtain the total radiated energy at frequency w when the electron passes by a nucleus .. lbmax dE(w)

x(w) d 2rrbdb, b . (1)

·· mm = = bmax a rv and in view of wr "-' l we also let classical considerations (see footnote 6)

,·.

L . Ze2 brnin --2.

r:-· } 18Because A(t) is real, A(w) = A*(- w).

;::··.

:} 19 See, for example, W. K. H. Panofsky and M. Phillips, Classical Electricity an.d ::::. Magnetism, p. 304, Addison-Wesley, Reading, MA, 1955.

,._.

. ·. _.·.

:::: ~:: .....

::::: :::: ::::-: .-.-.· :=.. _::. : 318 8 Particle Detectors end Radioactive Decay ·< <<tr~~ 1/t (I) ·\:::::::~~~ accele~~~ijf~~§m FIGURE 8.10 Idealized bremsstrahlung spectrum resulting from the sudden ·:::::::::=:~::~J~ ]l :!../3 l of a charged particle. · .Jffli The cross section O'brems, giving the probability of emission of a photoJ~if x :\)ff~ energy lu.cJ in the interval d(luv), is related to (w) through -:-:-:,:-:•:-:·~ = ))@{@J (n.m)abrems(w)d(Tiw) x(w) d'1J, . . . . . . . /tJ~WA {!}}~@ resulting m the classical nonrelat1v1st1c bremsstrahlung cross section .

z:~2 ( cs.#)!I e\)2 (c)2 ~~- O'brems 136 1n ( m~3 ) • ,u. me v nw Ze w \:{:::;;@} ~tJJ.f~i The average energy loss per path length, -dE / dx, is obtained by 9)ill~ grati?g over all ?hoton energies (the square pu1se) and multiplying by density of nuclei: \}::::{@ :?::=:::~~~ Ji~ = = - ~E fn(luv)<Jbremsd(MJ) n(MJ)(Mlmaxl<Jbrems· ·)!?I!i Substituting 1/137 = e2/lic,ro = e 2 /mc 2 ,and(luomax) = Eo, theenergf@rwW: . <.·:.f·.·.· .··~%- f th I b 0 . e e ectron, we O tam (c)21n ( :)fJfil dE) _ 16 Z n Eor 2 mv ) (8 34:\);-:/-/:-/:l-·i.u~.

-( dx av - 3 137 O v Ze {w}av · · Equation (8.33) is a fair approximation; the correct quantu.m-mechanicij{@~ r~~mlt, including the screening of the nucleus by the atomic electrons, ~~J~ given by20 :::::::?~: ·j]~~j ~:::i (8.3 Sf JII 20see Heitler (1984), p. 253.

jil ·.)J@ ' .. :::::~::;=::;

## 8.2 Interactions with Matter

The mean free path for bremsstrahlung by an electron, called the "radiation :_l:·--\:;-: length," is defined as 1 1 = --- = ----------, (8.36)

f Lrad 2 no-brems 4(Z n/ 137)rJ 1n(183/ zl/3)

....

= = ) . which is obtained from Eq. (8.35) by setting Lroo dx, when -d E / Eo ij 1; the tenn (small as compared to the In) was dropped "> .·.· To show at what electron energies bremsstrahlung becomes important, r:-: ~::: we note that •:•: :-:- ,·.·. (dE/dx)rad ZE(MeV)

:::: :::: ~::: (dE / dx )ioniz 800 :-:: F: This is shown in Table 8. I, where we give for some common absorbers, Lract, as well as the electron energy at which bremsstrahlung loss becomes •.·.· ~;:: ,..·.....·. . equal to ionization loss.

•:-: k Equation (8.36) is amazingly similar to Eq. (8.24), by which we defined :=:: L pair. We have .l'.'.

:~:= -:-: 7 -:.-:- = :"'.:•' Lrad 9Lpair, indicating that in matt.er the mean free path of a high-energy electron is of I; the same order as the mean free path of a h.igh-energy gamma ray; this is the reason for the phenomenon of the electromagnetic cascade. first observed in cosmic rays.

If a very high-energy electron is incident in the annosphere, it will soon (after approximately 330 m) emit one or more high-energy gamma rays.

These gamma rays wiU soon again (after approximately 330 m) produce electron-positron pairs. Each of the secondary electrons and positrons will again radiate, and so on. until most of the energy of the primary electron TABLE 8.1 Radiation Length of Electrons in Different Materials Electron energy for MateriaJ (dE/dx)rad (dE/dx)ioniz Air 330 m 120MeV Aluminum 9.7 cm 52MeV Lead 0.52 cm 7MeV 320 8 Particle Detectors and Radioactive Decay FIGURE 8.11 Formation of an electromagnetic cascade. Note that high-energy elec~ :/?:: (positrons) radiate gamma rays and the gamma rays later convert into electron-positr~if)}t pairs and so forth. . ):({:~: '))\~ (o r gamma ray) has been transferred to many less energetic electron~{/:;: <\ft (Fig. 8.11).

In another connection we have already used L rad in Eq. (8.19) for mul{)J ti.ple scattering; from Table 8.1 we see that in heavy materials scattering/\}?- ..... ·.·.i:.·.· will be much more pronounced. Note that multiple scattering is the same{/{~ for particles of the same momenrnm. Thus, at low energies a light particl~)){ will scatter much more than a heavier patticle of the same kinetic energ~( (j ( p = ffein). This is clearly seen when observing the tracks of low+(}~ energy protons and electrons in an in1age-fonning device; the former ones/ \/ are, in general, straigh~ whereas the latter ones suffer multiple scattering/ \{j through large angles. \ /{: ::1 8.3. GASEOUS IONIZATION DETECTORS; S. .l~:::~GER COUNTER 1/11 or{]

As mentioned earlier, most particle detectors are based in one form another on the energy lost by the charged particle due to ionization of the)\ !

\J medium it traverses. In a large class of instruments the detecting material }if is a gas; the ionization potentials are on the order of 10 eV, but on the average, for example in air, the charged particle loses 30 to 35 eV for eacb)J 21 thus))

electron-ion pair fonned. By collecting the free charges that were ::::::: :-:-:-i 21 -: :: = ~: This is due to additional interactions such as excitation and elastic scattering. ,,·•..··..·r . :::::: .·.·.r ·.·.· ·.·, ·.·.· :-:·?: ~::;>· 8.3 Gaseous Ionization Detectors; the Geiger Counter 321 v.::::· .::::: Insulator / ~ ~~-------~ jl\ Jt -.·.· z:::::: v.=:::::· f:::: - - ~:::.

{ / FIGURE 8.12 Diagrammatic arrangement of a cylindrical Geiger counter; the central wire }( is cbarged to B+ through Re while the cylindrical envelope is held at ground. The output . / ~ \ signal appears across RL· ~·.

:-:-·' ..: ,:- } ( created, it is possible to obtain an electrical pulse, signaling the passage of { {. the charged particle.

\ ( The simplest type of gaseous detector consists of a cylindrical chamber ·'\ \ with a wire stretched along its center, as showo in Fig. 8.12. The chamber ·}(: walls act as the negative electrode, and positive voltage is applied to the / \ central electrode. Under the influence of the electric field, the electrons are }/ collected at the center while the positive ions move toward the walls. It is }/ desirable to collect the free charges before they recombine in the gas; this {( is mainly a function of the pressure of the gas and of the applied voltage.

:f.

If, however, the voltage is sufficiently raised, the electrons gain enough d:( .

energy to ionize through collision further atoms of the gas, so that there is a '\i:.

significant multiplication of the free charges originally created by the pas- ·=::: sage of the particle. In Fig. 8.13, Curve l gives the number of electron-ion pairs collected as a function of applied voltage when an electron (mini mum ionizing) traverses the counter; Curve 2 gives the same data, but for a much more heavily ionizing particle. Thus the ordinate is proportional to the pulse height of the signal that will appear after the coupling capacitor C (in Fig. 8.12).

.. Referring to Fig. 8.13. we see the following regions of operation of t( a gaseous counter: in region II the voltage is large enough to collect all r-:.

the electron-ion pairs. yet not so large as to produce any multiplication.

t(: A detector operated in this region is called an ionization chamber. As the ..? .

voltage is further raised, region ill is reached, where multiplication of the f ·.- original free charges takes place through the interaction of the electrons as ( .: _the_y m_ov_ e through the g~s toward the collecting electrode. However, over \ :_· -:-:-.· ~ ..- . : · : . 22 It is also, of course, a. function of the specific gas or mixture of gases used.

;:::.• :::: : ~::.

~::: .;:::,_ ::::· .,,~::: 322 8 Particle Detectors and Radioactive Decay G,ei.g . er-Mull&r I counte.r. .

Recomb,nation Region of I before collection I 1010 limited t~tion prop<>rtional!ty l ,, Proportional I I I. . amb .,. e _ r I counter I IV I 0 (l ) ii fl I m -=:?

8 t 1 l I [);scharge) . . · · . .· · (/J . - 9 c:: 1a6 I I t I region iI - I I .·.· E N C z z:;J 104 I 0 250 500 750 1000 ,...

Voltage, volts FIGURE 8. 13 The number of electron-ion pairs collected when a charged particle tra verses a gaseous counter of average size plotted against the voltage applied bet<.veen the electrodes. Curve 1 is for a minimum ionizing particle. whereas curve 2 refers to a heavily ionizing particle. Note the three possible regions of operation as (a) an ionization counter, (b) a proportional counter, and (c) a Geiger counter.

a considerable range of voltage, the total number of collected electron-ion pairs 1s iab'iy·p.rupti..cmaLto the original ionization caused by the traversal in of the charged particle.23 A detector operated tru.s·regn,ir ~.:tlloo.a o.,;o·· portional counter, it has an advantage over the ionization counter in that t signals are much stronger, achievable gains being on the order of 102 to 1( Finally, further increase of the high voltage leads to region IV, where v, large multiplications are observe~ and where the number of collect electron-ion pairs is independent of the original ionization. This is region of the Geiger-Muller counter, which has the great advantage c very large output pulse, so that its operation is s1mple and reliable. Indr The proportionality does not have to be a linear function of the applied voltage.

8,3 Gaseous Ionization Detectors; the Geiger Counter 323 at such high voltages, once a few electron-ion pairs are formed the elec trons produce more ionization at such a rapid rate that regenerative action sets in, the whole gas becomes ionized, and a discharge takes place. At that poio~ the resistance between the central electrode and the chamber wall becomes negligible, and the counter acts as a switcb that has been closed between the high-voltage source and ground; this discharges capacitor C through resistor RL (Fig. 8.12). Since C was charged at B+ (on the order '> of l 000 V), very large output signals may be obtained. For example, if the number of electron-ion pairs collected is 10 (as given by Fig. 8.13) and C 0.001 µ,F, we obtain Q 1.6 X 10-19 X 1010 = = = (8.37)

V C 10-9 1.6 V.

By scaling this result according to the graphs in the figure, it is easy to appreciate the difficulties involved in the amplification of proportional counter and ionization-counter signals.

The disadvantages of the Geiger counter are the loss of all infonnation on the ionizing power of the charged particle that traversed the counter, and the long time necessary for restoring the gas to its neutral state after a discharge has taken place. However, the simplicity and good efficiency of the device for single-particle detection bave made it a very common nuclear radiation detector.

8.3.2. The Ionization Chamber The main dif-ficulty with ionization counters is their very low signal output If they are used, however, in an intense flux of radiation as an integrating device, high signal levels can be reached; in that case the output signal corresponds to the total number of electron-ion pairs formed (per unit time) by the radiation. In this fashion ionization chambers are frequently used for monitoring X-ray radiation or hlgh levels of radioactivity; in such applications tbey are far superior to Geiger counters, since the rates are so high that a Geiger would be completely jammed.

When an absolute measurement of the created free charges is made, as with an electrometer, ionization chambers may also serve as standards of ionizing radiation. Most commercial instruments, however, amplify the output pulse and are directly calibrated in roentgens ( or fractions of roentgens) per hour. For use in the laboratory an ionization counter )Ii1/II ~4 8 Particle Detectors and Radioactive Decay Model 2526 ("cutie-pie") manufactured by the Nuclear-Crucago Compaey,//ffi rang~iii/i/{{j is sugg~sted for radioactivity surveys and as an X-ray monitor in the of 0-2.:,00 mR/h ·.·:-:-:-:-:-:-~-:;.-~ • ·<:::;:::::::;:::~~ chamt(\/Jt Below we describe a very rudimentary "student-type'' ionization ber that was used in this laboratory for measuring the r~ge of alpha))!\~]

particles emitted by 210 Po. Figure 8.14 is a sketch of the ·apparatus; i()l/@1~ consists of a flask with a 5~in. outer diameter, its inside wall having beetj{:}J@ rubbe1(!)/tf coated with a conducting material (such as aqua-dag or silver). A stopper inserted at the mouth of the flask acts as a support, electrical insri~{/@]§j th~}:)ff!

lator, and vacuum lock. Through the stopper is fastened a brass rod at 210 24 tip of which has been attached a 20-µ.Ci Po source, which is thus) /ijfJ.

located at the center of the flask. A 180-V battery is connected between the/ (@~} is.?/J~1i flask walls and the rod supporting the source, and the ionization current measured with a Keithley electrometer. .{/[~~ The energy of the 210Po alpha rays is 5.25 MeV, and their range iri))lf{ walls\f}@j air at stp is 3.93 cm; hence the alphas stop before reaching the of the flask and deposit all their energy in the gas. By using the number of\ }tt,~ approximately 30 e V per electron-ion pair, mentioned at the beginning of)))J~@ ··' \.•t• t•4iJ.J;,,.,

## Section 8.3.1, we would expect per alpha particle a total of

</ ?:=:?:'=:3 5,25 x 10 6 /30 = 170,000 electron-ion pairs ', .\/\?~ \})i/Jj (the true number in this case being closer to 110,000).

:o~~:~ :~:::~tr::sxw~::::~;;, :: :::~::::::s/s 1 if 111 I= 1.6 x 10- 19 x 7.4 x 10 5 x 1.1 x id'= 1.3 x 10- 8 A, (8.38} !!!!II which is readily measurable. . }////JiI will a .\\/~ If now the flask is slowly evacuated, the alpha particles traverse {?J longer path before stopping; however, as long as the alphas stop in the gas, :}!J~ the saine number of electron- ion pairs is formed and the ionization current .\\~@ should remain flat and independent of pressure. When the density of the :}JJ air in the flask becomes so low that the alphas reach the wall before losing /·.·.J·.·.44l-.- all their energy in the gas, fewer electron-ion pairs are formed and the will /J~~ ionization current drop monotonically with decreasing pressure. · 24SeeAppendix D.

.:ill ,. ~ "' . "' -a. ' .• .. . ,. ,. ' .> -~ ~ • A ~ • . I , • • -' A ',, ' >. c . + . + . ~ ~ ,_ t:,j Ii COCl2 ~; 180~~ttery /""' To sliver Valve KEtthlay coating Jll l , Source elactrometer Manometer Silvered Flask . TopuJ FIGURE 8J 4 A simple arra.ugement for lhe determination of the range of aJpha particles in air by rnea.sur1tlg the ionization current as a function of chamber pres6ure.

326 8 Particle Detectors and Radioactive Decay : 11111 0.9 Pc=51.5±0.2 cm 0 0 0 ~ I 0 ..8 T=25°C -rx- Atm pressure= 76.3 cm .-•:-:-:-:•:•:--::~ -<(

## 0.7 )1

\::\)~.m :-:-:-:.:-,-,.~ _.__·:;)(\fl

## 0.6 '----'--.L-..1..---'-----'------''---~....___ ___._ __. ___

\))jjjj)J~tj 20 25 30 35 40 p (c: Hg} so 55 so 65 . •:::;:::;::·~~~ ion.iz~ijf~tfj FIGURE 8.15 The results of the measurement referred to in Fig. 8.14. The P\#,{~f~ current is plotted against residual air pressure and a decrease in current begins at )\)%1i

## 51.5 cm Hg. This corresponds to a range of 4.02 cm in air at stp

.. Aii!!!!!i~ Data obtained in this fashion by a student are shown in Fig. 8. 15. Inde~:, t\?J.

the expected qualitative behavior of the ionization current is observed; froitt?:=~ ± ~¢.}{j the breaking point we conclude that at a pressure of 51.5 1 cm Hg, range of 21O Po alpha rays in air is R = 6.14 cm. Hence at stp (760 mm Hgf)j 15°C) ·. .· .·.·.·.·-~ )!{!!~~@ /:)!/:~ P Tstp = 51.5 288 _ ...

Rstp =Rx ~ x - 6.14 x x = 4.02 ± 0.1 cm.·::::::::::::::}E rstp T 76 .0 2 98 :::::::::::::::~ . . :; : ::: :;:;:;::=% in good agreement w1tb the accepted value of R stp = 3.93 cm. _})t}~ From the ordinate of Fig. 8.15 we note, however, that the ionization ~W.:=:::=~ ..· .:.·.·.·.·f.-.t"';..,~-.,.

re?t ~s three orders of mag_ni~de lower than the es~ate ~ven by Eq. (8?~)f proc~gt~t~ tlus ts due to the recomb1natton of the electron-ion parrs, which M!J~i at a. fast rate because of the long path in the air, the high pressure, isJfilJti the low value of the e~ectric. field a~cel~ra~ng _th e electrons. This ::/:/:~:i example of a low-efficiency mtegratmg 1omzation chamber.

j-J:-:-:•~:~•:I•:-~ 25 Some loss is also due to self-absorption in the source, and the geometrical solid is only 2Jr . ··,-:?::\::::J::=-i=-~ t . ' .. --·i :::1 ::::r::::~ ?Jtfil ~;: ~~ t..· .

## 8.3 Gaseous Ionization Detectors; the Geiger Counter

...... )( . 8.3.3. The Proportional Counter 1~/.:·:.:· .

~( We will not describe in detail the proportional counter26 bat only give f .

the results obtained by a student using such a detector in connection with -~{ the experiment on the Mossbauer effect (see Chapter 9). The advantage ~( -: of proportional counters lies in the detection of very low-energy X-rays / > ....... or gamma rays, which can hardly penetrate a scintillation crystal, and / :· when in addition good energy resolution is required. This ~ i s the case in f { the Mossbauer experiment from 57 Fe, where it is necessary to identify a -:{ 14.4-keV gamma ray in a strong background of 123-keV gamma rays and f:.

5-keV X-rays.

/:I The proportional counter used wasv Amperex type 300-PC. It was filled ;\· with a xenon methane mixture at a pressure of 38 cm Hg. The equip ment used for amplification and pulse-height measurement28 is shown in } \:' Fig. 8. 16, and the counter was operated at 2100 V. Figure 8.17 gives the ·:~/ results obtaine~ where the number of pulses is plotted against the discrim ~/: inator channel. The large peak at Channel 12 is the 5-keV X-ray; the small {( peak at Channel 26 represents the sought-after 14.4-keV gamma ray.

As we know from Section 8.2.5 (Fig. 8.7) the predominant interaction t\ of low-energy gamma rays in the gas is the photoelectric effect. The cross :-{/ section for 5-keV quanta is on the order of 6 x I o-24 cm 2 , so that if the {\ counter represents approximately 50 mg/cm of material, the efficiency for ~~{ gamma-ray detection might be as high as -·-·. z il\ 3 3 24 6 X la2 X 50 X 10- X - X 6 X 10- ~ }0%.

~::/ ){ : Using the data from the 5-keV peak, we obtain for the resolution of this ll! = proportional counter, b.E IE= 1.7 / %, 12 14 J{.

where for 11£ we chose the half-width of the peak at half-maximum (after \/· background subtraction) .

........

.......

l} For an cxtensi ve discussion of proportional and ionization counters, see the Encycwpe ~t( -dia of Physics. Vol. 45, Nuclear Instrumentation ll, Springer-Verlag, Berlin, 1958, articles .-f by H. W. Fulbright, pp. 1-50, and by S. C. Curran, pp. 174-221.

\ / 27Manofactured by the Amperex Corporation and obtainable from Scientific Sales, Inc., }{/ Long Island, N.Y.

:\ : 28For a more detailed ruscussion of pulse-µeigbt spectra see Section 8.4.

-:-: -:::: ·•··· 328 8 Particle Detectors and Radioactive Decay ) 1111 i//ilf High voltage < /11 t fl .;-:-:-:-:. . ..= ·: r-----, ..--------, ~

## I I I

I' P roportional I--1 Cat'hOde 1-.. - counter I I follower t t L----J L ____r Linear amplifier ,-S-in-gl-e d~lan ne - l - an - a - ly - ze - r - - , I I I __ IDiscrlmin_at_or l--1 Amplifier I_ - I I IL _____,I ....,_.

I 1 ACL Mod. 20506 Scaler FIGURE 8.16 Block diagram for pulse-height measurements using a proportional counte~/{~~* ':::::::;:~:;: . :.'.?::::=~~: /\It 2500 :i\f!

. ffifj

## §

.·.·~~.. - .r.

Ji/ :)@f~ '}Jj -:-:-.,;-l ·\J~ 5 10 15 20 26 30 35 :l!!II~i Channel ··;,:·.- 57 a{fj.$ FIGURE 8.17 Pulse-height spectrum of the low-energy gamma radiation from Fe if J~ obtained with a commercial proportional counter. The pronounced peak at channel 12 ··.·.-.x ...

the 5•keV X-ray while the smaller pefile at channel 26 is the 14.4-keV gamma-ray line use<t:~::~ .· .·.• in the Mossbauer effect. ::::;;::~ ... :.-.:.·.Y.h ' ))!

-:-:~~ :-:-.-._% ..:: ::~=~ :::::;* .. ·.:.-:.~ 8. 3 Ga s e o us I on i za ti on Oe te ct o rs; the Ge i g e r Count e r 329 8.3.4. The Geiger Counter; Plateau and Dead Time It has been pointed out in Section 8.3.1 that a gaseous counter operates in the Geiger region when the voltage between electrodes is sufficiently large; that is, the traversal of a charged particle initiates a discharge in the gas, and as a result a pulse appears at the output that is independent of the original ionization. If the voltage is further increased, spontaneous discharges occur, making the device useless as a particle detector.

Because the principle of operation is simple, Geiger counters are simply constructed, the geometry of Fig. 8.12 being typical. For certain applica tions, the thlckness of the walls is an important consideration, and Gejger counters may be built with special thin windows (usually mica of few mg/cm ). Glass envelopes for Geiger counters are fairly common, and various pressures as well as mixtures of gases are used.

Another important consideration for Geiger counters is the "quenchingu of the discharge initiated by the traversal of a charged particle. Until the gas is returned to its neutral state, the passage of a charged particle will not produce an output pulse; this is the period of time dtrring which the ...

counter is "dead." The quenching of the discharge can be achieved through the external circuit (for example, in Fig. 8.12 the charging resistor Re will introduce such a voltage drop that the discharge will extinguish itself), through the addition of special impurities (such as alcohol) to the gas of the counter, or by both methods used together. The circuitry necessary for the operation of a Geiger counter is also extremely simple. A single stage of amplification and pulse shaping is usually sufficient to drive any scaler.

In order to operate a Geiger counter properly, the high-voltage source must be set in the "plateau" region (Fig. 8.13, region IV), where a similar output is consistently obtained for all charged particles traversing the counter. We may then define the efficiency of the detector as the rntio of the number of output pulses over the total flux traversing the counter; since the pulse heights are all equal in the plateau region, we do expect . . the efficiency to remain constant in that same region. Clearly any parti ( . cle detector should be operated in a region where the efficiency is "flat"

\ with respect to variation of operating parameters. The efficiency of Geiger counters is 90% or higher for charged particles, but for photons it is much (: lower, being only on the order of 1-2%.

\ It is difficult to make absolute efficiency measurements for Geiger coun [ : ters. A "standard" calibrated source of radioactive material may be used, f: and the output count compared with the expected flux from a knowledge .... .

f ·.

;:::.

.:.:.:.:..: : .....

:=::- ·,·t-'.·•..· · .

::::::, r.-·.·.

::~:-:- _(!))~; .:.! ·>]j:-{:}-:.f:-i:l•~:, 330 B Particle Detectors and Radioactive Decay pfad.~li}!I of the solid angle subtended by the Geiger counter. If the counter is at several distances from the source, the consistency of the measur~ments/?

r2 relatif}.))

may also be checked through the 1/ dependence. However, a easf J measurement of the efficiency as a function of the high voltageis ~~f o~t.ki\ make; if it yields a flat plateau, this is an indication that the detect.or ates at high efficiency ( close to 100%) for the particular type of radiaticin{t vtitij(f that is incident. Geiger-counter plateaus are usually a few hundred wide and have a small slope, on the order of 1-2% per 100 V. . .. : :/ }!]( To determine the plateau, either a radioactive source or the cosmic.:raj{) ~ flux may be use~ since this flux is on the order of 10- 2 particles/cm2-s~)fJ takes several minutes to accumulate 1000 counts for a counter of average!/~ . :·.·.-,•.-.

size. As explained in Chapter 10, the emission of radiation is a randofu}t -~f }~ process, so that the standard deviation 29 of any measurement is given the square root of the number of counts, and thus the measurement shm~tii: J be interpreted as -:-}()~ ·/(\~fg = ))ii@ 1000 ± 31 1000 x (1 ±0.03) counts .

-:/ }}i or in common parlance, 1000 counts give 3% statistics. The high v..oltag#\]~!

should be well stabilized, usually to a few parts in one thousand. . .}}}!

Figure 8.18 gives the plateau found by a student for the RCL30 typ~(@ 10104 Geiger counter. A 10-µ,Ci Co source was used for the measur~f} ~~!\j ments, and the standard deviation at each point is shown by the size of dot. The plateau begins at 1100 V and is approximately 250 V wide; ~~~~(~ discharge region begins at 1400 V. ")((~ .::III The slope of the plateau, from Fig. 8.18, is Next we our atte~ti::~::e ~~::::::Geiger counrer aheai~jjl]j rum mentioned. Indeed, once a discharge has been initiated, the counter will\ not register another pulse unless the discharge has extinguished itself, an?(f until, in addition~ the counter has "recovered"-that is, returned to a neutraf\ state. During the recovery period, the counter will generate an output pulsJ{)

,·.·.·.·r but of a smaller-than-normal amplitude depending on the stage of recovefy{J ,-:::::::::~ 29 Ift his measurement is repeated many times, in 68% oft he cases we will obtain N - (I . ;,{} N > N +a, where N is the average of all measurements. See Chapter 10 for the definitioi{} <})

of a.

30Radiation Counter Laboratories, Inc., 512 West Grove Street. Skokie, ill. :-\J .):~:i~ ):)~~ :::::::: /:~:} ~?~)~ :::::::~

## 8.3 Gaseous Ionization Detectors; the Geiger Counter .:331

IC ::, 2500 Pooo 1100 1200 1300 1400 Volts FIGURE 8.18 Plateau curve of a Geiger counter. Note that the plateau region extends for 250 V and. has a slope of the order of 5% per 100 V.

Horizontal scale 100 µsec/cm Vertical scale 5V/cm FIGURE 8.19 Multiple-exposure photograph of oscilloscope traces obtained from a Geiger counter exposed to a high flux of radiation. Note the effect of the "dead tlroe"

or of the counter and lbe gradual buildup (recovery) the output pulses.

·}})t]..

... ·.· .·.·.-..., .

/JIii m 8 Particle Detectors and Radioactive Decay This phenomenon of recovery can be clearly seen in Fig. 8.19, obtaine~:[:}~{:~ radiation{(@i~ by a student The Geiger counter was exposed to a high flux of the trace of an oscilloscope is triggered when the output pulse appears/}J}t The horizontal scale is 100 11,s/cm so that the shape of the output puls~f \ }~ and its exponentially decaying tail can be seen in detail. If now a seconc\\/{/i particle arrives within 1 ms of the previous one, it will appear on the same/}}J ...... ,. ..,_ oscilloscope trace since the scope will not trigger again until the sweep i~/}l~j waf\@$ completed (the screen is 10 cm wide). The picture shown in Fig. 8.19 ·--~ .....

..

obtained by making a multiple exposure of such traces. The correlation of::\~:%: ~·-· ..· .·.·.· pulse height against delay in arrival time and the exponential dependence( !J J of the recovery are clearly noticeable. If we consider that the counter is{{{:~ .·.·.·.·••. ..-,.

}/:)Jr~ inoperative until the output is restored to 63% ofi ts original value ( 1-1/ e the data of Fig. 8.19 give a value for the dead time i- on the order of (()fi ·:}!)l!

r: = 400 µ s. (8 39f ::;:;~~ Pulses, however, seem to appear after an interval r 300 µs.

The dead time of a counter 1nay also be obtained by an ''operational'?:::=:=~====~ ~/J@i technique, such as by measuring the counting loss when the detector subjected to high flux. If the dead time is i- (s), and the counting rate I{}\t (counts/s), the detector is inoperative for a fraction R1: of a second; th~)j@{j ;{}if ; true counting efficiency is then 1 - Rr. · Consider two sources S1 and S2, which when placed at distances from(f@f the counter D1 and D2 give a true rate (counts/s) R1, R2. The counter,}!)f~!

and.:)Jfi however, registers rates R~ < R1, R; < R2 due to dead-time losses, Rb + }}}~~ when both sources are simultaneously present, it registers < Ri R2 due to the additional loss accompanying the higher flux. Now, )}~=f Ri R1(1 - R~r) · R; R2(l - R~r)

= + R~ (R1 R2)(1 - Rbr).

We solve by writing R R' R' 12 1 2 -1--,- - 1 ' 1 ' - R r - R r - R r t 12 1 2

## 8.4 The Scintillation Counter

which reduces to a quadratic equation in r with the solution 1 ± J1 - R~ (R1 + R2 - R~ )/ R~ R~ r=-----2 ------2--- R12 This can be expanded in the small quantity (R~ R; - Ri ) to give the approximate expression (Ri R~ - R~ )

r~------ (8.41)

2R' R' .

1 2 We now apply Eq. (8.41) to data obtained by students with the same counter used for Fig. 8.19. In practice, source S1 is first brought to the vicinity of R; the counter and is obtained, next S2 is also brought in the area and R~ is obtained, and finally S1 is removed and R~ is measured: thus no uncertainties due to source position can arise. They obtain Ri = ± 395 3 counts/s 12 = ± R 655 3 counts/s = ± R~ 334 3 counts/s, yie]ding r = 282 ± 20 µ,s, in better agreement with Eq. (8.40) than with Eq. (8.39).

The rather long dead time of the Geiger counter is a serious lim itation restricting its use when high counting rates are involved; the ionization counter and proportional counter have dead times several orders of magnitude shorter.

8.4. THE SCINTILLATION COUNTER 8.4.1. General As we saw, in gaseous-ionization instruments, the electron-ion pairs were directly collected; in the scintillation counter the ionization produced by the passage of a charged particle is detected by the em.ission of weak scin ti Uations as the excited molecules of the detector return to the ground state.

The fact that certain materials emit scintillations when traversed or struck by charged particles has been known for a long time, Rutherford being the first to use a ZnS screen in bis alpha particle scattering experiment~.

·::::::I:::I::=/=1!~~ 334 8 Particle Detectors and Radioactive Decay . · )((J~ 19;$.@fl~ The scintillation counters used currently were developed in the ,photre{J~ and ~o~sist of an organic or inorganic crystal coupled to a s~:nsitive multiplier that resi:o~ds to the light pu~es. Anthracene or stilbene. cry_s~(!}~ tr~~~{=~W make excellent scintillators, but orgamc compounds e1nbedded in parent plastic, such as polystyrene, are now widely used because of ease.ij}\j handling and machining and availability in large sizes. Such materials #~{{~~ commercially available 31 under the general description of "plastic scin~){\@ lators.,, The active materials are compounds, such as "PPO," 2-5-diphenyt¥.)faij oxazole, ?r di~b~nylstilbene, or others, and are also available in liquidforaji(}§~ Orgaruc scintillators have an extremely fast response, on the order tjf{t~ s, han4f [ij 1o -9 which can be matched by good photomultipliers. On the other because of the low density and low Z7 their efficiency for gamma-ray c~~{)~~ij §.f {$ version is not high. To detect gamma ray st inorganic crystals, such as Nal Csl, are used instead, activated with some impurity, for instance Tl (1 P#./}fj in 103 ). Inorganic crystals have an excellent efficiency for gamma-ray coh,{)}~1 version, due to their high Z; from Eq. (8.20) we recall that the photoelectrid{!&i~ ·.·.-.~. ..........

effect is proportional to Z 5 and from Eq. (8.23) pair production is propor{:]ifj ~ tional to Z 2 . However, the light output from inorganic crystals is spreac(/~f.~ over a much longer ti.me interval, on the order of 10-6 s. Such inorganic{}m 32 tbei,}@i crystals are also available commercially, appropriately encased since _.//l§.

are damaged by humidity; they come in sizes up to several cubic inches.

The light output of scintillators is proportional (as a matter of faet}?JJ ...., .

'' linear) to the energy lost by the particle that traverses the detector, thus, by})}~ scin::-:\)t pulse-height analyzing the electrical output of the photomultiplier, the tillation counter may be used as a spectrometer. This procedure is discussed~({?

on/ff in detail in the following section, where it is seen that energy resolution j the order of 10% or better is achievable. })f :\JJ The mechanism of emission of the photons in the scintillator material the(){~ is rather involved. Table 8.2 gives a chart of the processes involved in emission of light in organic and inorganic crystals. In inorganic materials.}}~~ they an/)\ it is the migration of the electrons through the lattice (until excite impurity center) that is responsible for the long duration of the light pulse.}\~~ <J~~ Even though the efficiency for transferring the energy lost by ionization ...........

to the photons in the visible region is on the average low, E ~ 1.5%/)f a scintillator still provides ample light output. Consider the case of a)(l plastic scintillator 1-cm thic~ traversed by a minimum-ionizing particle:<)t dE/dx = 2 x 106 eV per g/cm 2 ; if we take the average photon energy.}!§~ }t 31For example, from Pilot Chemicals Inc., 36 Pleasant St., Watertown, MA. )I~ 32For example, from Harshaw Chemical Corp., Cleveland. OH.

::::~~ :::=::: . ?-:-t:'l '.·.·.--- :::~ 1010 1, •.•, 1010 l• l•l•I• l•I• •.•,l •I• l•l•l•I• l•l•l•I•l •I• l•I• •.•, '•"•• .• 1•>"<•>1•1•1•1<•1•1•10101•"•"•10101•1•1•~:-:-:•:•:•:•:::::::::::::::::::::::::::::::~~:~: • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •. • • I I I I I I I • ·-:-·-:• TABLE 8.2 The Series of Processes Leading to the Emission of Light When a Charged Particle Traverses a Scintillator Materiala Inorganic scintillator Organic scintillator (Impurity activated)

Electronic structure of molecule is excited l \ Holes Electrons t . j Loss o~gy to ~ocintion vibrational states Drift to impurity center and ionize it. Emission Emission of light of thermal radiation quantum Ionized impurity center ..... Capture with emission of Energy may be transferred to / thermal radiation if other 11ecules / E,cited purity center Radiationless transition Electron drops into \ E~on of light metastable state of quantum impurity center ~ t .. :.~~-~ Thermal energy Radiationless transition raises electron ., to excited state a After J. Sbarp~ Nuclear Radiation Detectors, Methuen. London. 1965 (Courtesy of I.he Publishers).

Jill/II Particle Detectors and Radioactive Decay )

e 4 ca@.}{f~ as 3 V, we obtain l 0 photons. The efficiency of a photomultiplier and···t;6w\tj ode for converting photons into electrons is on the order of 0.1, i~{\ j geometric efficiency for collecting the photons onto the pbotocatho.dtf vituff f: usually high, so that on the order of 1000 electrons are released.

f~ ,• .·..·.t. -?.......l. ~......~~ modern techniques. however, it is possible to detect the release of a :~{\/t~ photoelectrons, or even of a single one.

Clearly the scintillator material must be transparent to the visible r~a4:t+r.n\t}w}!

ation and optical coupling to the photomultiplier must be provided.

appi~\:t:J~ is achieved either directly or through a "lightpipe," which is an in4¢jj/j priately shaped piece of lucite or other medium of high refractive s#f@f]

that traps and guides the light d~e to. tot'.11 _iI~temal reflec~o~ at its faces. At the surfaces where the hghtp1pe 1s Jomed to the sc1nt:11lator or";~~/}}~ ~~¥.{t~ the pho~omultipli~r, optical conta~t is achieved by the use of either cous fluids or special glues. Obviously the whole assembly must be 11¢~[{~~ arojfM@~ tight; ~hi_s is freq_uentl! achieved by wrapping black electrical tape the scmtillator,_h ghtp1pe, ~~ phototube. . \:/}:;~]

Because of 1ts great stab1hty and ease of operation. as well as becau's(f~~::m::X ~iji/W of its time and energy resolu~on, the scintm_ation cou~ter has ~ecoiµe high-energy:ti~ most frequently used detector m nuclear physics, especially for particles. )??!:~~ !~=~:;:i:~e!e=:~~~o:f~ ~~~~rgy Ill/I 8.4.2.

-:/(Jfi If atoms are quantum-mechanical systems and a typical manifestation·~~{} this fact is the emission of spectral lines of light, it should be expected th~(lt~ )JJJ]

nuclei, when excited, would emit similar line spectra.

Since the nuclear radius is three to five orders of magnitude smaller thijf ?~~ ·. . -.·.·.·.·.-.·.-'.·.

that of atoms, the forces that bind the nucleus (against the repulsion of tl:t¢f\{:~ positive charges confined in its volume) must be correspondingly strong~i\}j consef\t than the forces that bind the atomic electrons to the nucleus. As a tra6:4@J quence. the energy levels and the quanta of energy emitted in a nuclear .....

;/,.,.:."

sition are also orders of magnitudes larger than those of atomic transitio$.fi!~ Ji transtf Indeed, the quanta of electromagnetic radiation emitted in a nuclear f® th~tf tion fall in the gamma-ray region, and new techniques are needed for detection and for the measure1nent of their (wavelength) energy. :/(~~ ·/:}[~~ 33 t~i{}J 1n the first category, Coming 200,000 centi.poise fluid or clear vacuum grease; in latter, R 363, PS 28 acrylic glue. etc. )/!~}~ ...., . •½ ,:::::::~==~ II · 1

## 8.4 The Scintillation Counter

Further, because of the larger spacing between energy levels, it is not easy to excite a nucleus from its ground state by the simple means of electric discharges or arc sources such as are used for atoms; instead, beams of neutrons or high-energy gamma rays, or high-energy charged particles, are required However, in distinction to atomic transitions where the de excitation probability is on the order of 10 /s, some nuclear transitions have .. a very small "decay" probability, as small as 10-7 Is, corresponding to a · · lifetime of 100 days. Thus, it is possible to excite a sample of nuclei inside a nuclear reactor, or by subjecting them to cyclotron bombardment, or by other means, and subsequently bring them to the laboratory for measuring ·'.· their spectrum or for other uses. Indeed, some of the nuclei that have very long lifetimes can be found in nature in their excited state; these are the naturally radioactive elements.

We now know that the appropriate detector for measurements of the · · energy of gamma rays is an inorganic crystal. When a gamma ray of energy . . < l MeV enters the detector, it will interact either by the photoelectric effect or the Compton effect. In the former case it is fair to asswne that the ejected photoelectron will deposit all its energy in the scintillator; in the Compton effect, however, the scattered photon may or may not convert in . . the scintillator (depending on the size and geometry of the detector).

The pulse-height spectrum for gamma rays of a given energy will con- sist of a peak at an energy corresponding to that of the gamma ray and a ::::::::_!·:·:_.·:: continuum below the peak, corresponding to Compton-scattered gamma rays that escaped from the crystal before totally converting. This can be seen in Fig. 8.20 and those that follow. Clearly the larger the size of the {: crystal, the larger the percentage of the output counts that will lie in the photopeak; thus, the gamma-ray line will become more pronounced.

Most of the data reported here were obtained with a Nal-11 activated . . crystal, 34 2 in. in diameter and 2 in. wide, coupled directly to a photo :::. multiplier tube.35 (Photomultiplier tubes and high-voltage bias schemes }. are discussed in Appendix E.2.) The output pulse is fed to an Ortec36 } Model 570 amplifier, and its output is fed to a Canberra multiport mul / : tichannel analyzer (MCA). The MCA is controlled and read out through a , ...

..... · ~::.

::::: .-.·.· .~...:.::.: 34Bicroo Corporation, http://www.bicron.com/.

.· ;t ·- ;' ~ .: . : · · · . -. . · . ·• 35Toe crysW and photomultiplier tube assembJy is a commercial package from Canberra f .

Industries. http://www.canberra.com/, Model 802-3. The photomultiplier tube "base" was f:: constructed from a commercial socket and simple components.

~r 36http://www.ortec-online.com/.

f.-:• ~=-: .

:::::-·- ~::,: t~:,:.

~·-·.

=~=:, ~::: ..

::::: :.

......

::::::- 338 8 Particle Detectors and Radioactive Decay 350 .--------r----.---.....---....,.....--,------r----.----, :C U c: ) : ' ~ 250 • \ I \ - 200 • • Q)

::::, .s • E 150 • • i • "E ::, (.)

50 • _r.::~- 0 ____ __.___---1. __ ..1........._ _.,__ ____._ _. .J...__ o 1000 2000 3000 4000 5000 6000 7000 8000 Pulse height (Channels)

350 .-------r- -----.----.....----.---..-------r------.----~ .•' . I" .

> ~ Q) "' ~ 0 200 • • • •• ~ • .• . • C • • ·: .... 150 I f~f: (D a. • ~ (/l

## E

8 V .; : 0-----___JL__--..4-___ _.___ _. ....__ _. .___ ___JL__---t., _ ___;=

## 8.4 The Scintillation Counter

5+ (5.26 yr)

4+ 2.506 MeV (Z=27)

## 2.82 MeV ~1.333MeV

..

80Ni (Z:=28)

FIGURE 8.20 (Continued)

GPIB interface, in this case using a laptop computer. Spectra acquired in this way are histograms with 8192 2 13 bins. (Adjacent bins were added together to reduce the statistical fluctuations from bin to bin. This is easy to ·> do with the reshape commandinMATLAB.)Theconversionofbinnumber to photon energy depends on the combined gain of the photomultiplier and the amplifier, and must be calibrated with sources of known photon energy.

The following figures give the results obtained by a student. Figure 8.20 gives the spectrum of60Co and shows two distinct peaks, which we attribute to gamma rays emitted in the de-excitation of 60 Ni from its 2.505-MeV level to the 1.333-MeV level, and from that level to the ground state according to the decay scheme aJso shown in the figure. For comparison, we also show a spectrum taken with a 3-in.-diameter and 3-in.-wide crystal. As a measure of the energy resolution, we may consider the full-width of the peak at half-maximum, which is on the order of 480 channels, hence a resolution of 480/6000 ~ 8%. We also notice a significant background for pulse heights lower than that of the peaks, which is due to Compton-scattered gamma rays that subsequently escaped from the crystal. Tb.is background is much less severe for the larger crystal.

Figure 8.21 gives similar data for a sample of 137 Cs; here the 0.662- MeV gamma ray represents the de-excitation of Ba. Again we notice some Compton background and an energy resolution on the order of 10%. Figures 8.22 and 8.23 give the pulse-height spectra from 22Na and 133Ba, respectively. For the 22Na, the peak at 1.277 MeV arises from the de-excitation of Ne; the larger peak at 0.511 MeV arises from annihila tion radiation. Indeed, from the level di~gram of22Na decay, we notice that 350 ,----.-.-,-.. --------.-------,r------.-----, 7/2+ (30 yr} tn ...

C A , :0 • • C\I 250 1a1c 8 (,1._')

Q) • (Z=-55)

> • ' . o m 200 • 11/2- 0.6616 MeV • .. .

::, • ' (2.55m} . . c E . : . : . 150 • . • • • _,. r • . 1.18 MeV ., .

a G) . .: • --~- 1/2+ 0.281 MeV cVJ 100 -,.. .

:, 0 3/2+ • • 50 re • • '.... 137Ba (Z=56)

o- 0 1000 2000 3000 4000 5000 Pulse height {Channels)

FIGURE 8.21 Pulse-height spectrom of 137Cs gamma rays obtained with a Nal crystal, and the associated decay scheme.

350 ,----------.----.-------,----,----..-----.------; f. ..

m 300 · ' •• 3+ (2.60 yr) l C: :n • ..

~ 250 • 22 ~. a .. > _ • \ • (Z=N1a1 )

~ 200 • g • • 2 • \ . .

• • 1.275 MeV 2+ 2.84 MeV l; 150 ~- • 8. • \ • .s • • c 1ao I r • I. \J : :::J 0 0+ 22Ne {Z=10)

0 ____ __._ __.. ......... _ _..... __. ...._ _ _.__ _. ........ _........,__~ 0 1000 2000 3000 4000 5000 £000 7000 8000 Pul8e height (Channels} FIGURE f!.22 Pulse~height spectrum of Na gamma rays obtained with a Na! crystal) and the associated decay scheme. Note that the 511-KeV Jine is due to positron annihilation.

tJ 342 8 Particle Detectors and Radioactive Decay 1111 . ;1 ·.. : mt 1800 ~---.----.---..-------.-----.----..----- (I)

.£ 1400 .0 (\J !(I)

1000 • i:-:- :- i :-: f -:·=@ fi 800 • ::;}:;:;;;:~ 600 f i\@~ • : :-. : ··J/!11 400 ,·- : : ., _f.y • ·-:-:-:-:-:-:,Jij 200 L ~ •...._ } }:;\~ )!}:}i% O • • <t@~W o soo ,soo 1000 2000 2500 3000 3500 W, P uIs e h e1 ht (Ch a nne } (·.·{.·?.-.-.t...@...

crystii!}:~Jf FIGURE 8.23 Pulse-height spectrum of 133Ba gamma rays obtamed with a Nal }#:flill The decay scheme is complicated, but the most dominant y rays at high energy are at and 302 keV. . ::::::::}'.:~ :}})\]

-i::::,:::i=:-i:~~;;~ positrons are emitted; the positrons are usually stopped in the walls of source container, or _i~ the ~rystal face, and as they come close enou~J1t~ an electron they anruhilate mto two gamma rays, each gamma ray shanµJf{j the energy of the electron-positron pair.

It is one38 of these gamma r~j(j?J p~~/J& that is then converted in the crystal and gives rise to the 0.511-MeV Finally, in Fig. 8.24 is given a plot of all the observed peaks agam:Sf::!.i channel number, showing the linearity of pulse height against enef~J~ {MATLAB provides a useful utility command, ginput, for interactivijfyff® y<i#i}i identifying the peak position in spectrum plots using the cursor on eiiut.\i computer.) In addition to the gamma rays, the nuclei investigated also beta rays, and one would expect to see the corresponding peaks in the pu~~{}!

spectru11;fjli height spectrum. This, however, is not true because the beta continuous instead of being a sharp line as is the case with gamma-:--~i~:~j be~9ffi~~~~ spectra; in addition, electrons may lose variable amounts of energy at~f:;:f reaching the scintillation crystal, so that unless special precautions ··:j}}ff taken, the energy resolution is usually poor.

37 See also the detailed discussion in Chapter 9.

3&Note that they are emitted with a relative angle of 180°.

## 8.4 The Scintillation Counter

<ii 5000 C: (ti ..

.c.

i~ ~~~~~- ::::· .......

:/:,:': ..: -: :::: -: .. - . : .. - ... · 1000 ;:::-.· :::::: .......

.{( 600 1000 1500 :..•.:.·..· y-ray energy {keV)

:} FIGURE 8.24 Plot of gamma-ray energy against the central channel of the photopeaks / :. 'appearing in the spectra of Figs. 8.21 through 8.23. The detector response is obviously quite { < ·linear over this range. Note also that for a zero photon energy, there is a "pedestal" of a :{ few hundred channels. This ensures that none of the spectrum is lost below che range of the 11::: multichannel analyzer.

;:f:. )\ In interpreting gamma-ray spectra some care must be taken since spu- [ } ri?us peaks due to ins~e~tal effects or ~h~sical effects do app~ar.

[ > First~ there can be peaks ansmg from the em1ss1on of X-rays, followmg ~f photoejection of K -shell electrons either in the source or in the shielding.

~/ Also, a peak may appear due to photons that backscatter (by 180°) in the i\.

photomultiplier window or elsewhere; then the Compton-scattered elec t \ tron escapes, but the scattered photon becomes converted in the crystal.

i~J For Cs with its Q_662-Me V gamma ray, the backscattering peak appears ~(·at 0.185 MeV a~d can be identified in a c~fully ~easured spectrum.

?i:;::: Another spunous effect occurs when an mconung photon of energy£ ~~\: ejects a K -shell electron from the iodine of the crystal, but the emitted X-ray ~{) escapes without converting in the detector. The ejected photoelectron has ·'!:!

an energy E _ EK, I: where EK is the energy of the K shell of iodine, namely, 29 ke V. and will ~\ give rise to a peak not coinciding with the true photopeak. This so-called ~~-~ ...: ,· ;..:· "=: •::: . -:/:/I~~ Ill/I :::::::::::::::~ 344 8 Particle Detectors and Radioactive Decay )

"escape-peak" can be identified because it is located 29 ke belaw\jJJ~ low-energy@]

photopeak; it is most pronounced in the pulse-height spectra of ....... :-: gamma rays. :\/{{J cotiq_tff ~ The relative ratio of counts in the photopeak as compared to the in the Compton background depends on the crystal and source ge6fu{~~~~ ·.· . ·.·. ·.·,.,~,.,.

thtt.:}j etry and on the gamma-ray energy. Usually the relative counts in photopeak give sufficient information, but when the absolute numbe{_hf{t gamma rays is required, we must calculate the efficiency of the crystal}~~ ·.·.·.·.·.-.·%.- for the particular geometry and gamma-ray energy. Extensive tables)if.l ~ be..e.n..\.f..:. ?,I efficiency for most combinations of the relevant parameters have calculated 39 · \ }:f~ 8.5. SOLID-STATE DETECTORS 8.5.1. General scintiir.J/t~ We have seen how the gaseous ionization counters and the charg:;&@~ tion counters are widely used for the detection of radiation and .•.•,·.·J.-.·~/, particles. It is also possible to use semiconductor materials for the dete¢:f ~#)t tion of charged particles, especially those of low energy; such detectors 40 :/?l appropriately referred to as 4'solid-state counters.'' In a general sense, we can think of this type of detector as a soli~:l,)))

gas-filieif\ state ionization chamber, having two basic advantages over a ionization chamber: · \:}j ~vfl!

(a) The energy required for the creation of an electron-ion pair is 3 an:if \ ( as compared to approximately 30 e V in a gas) so that stronger signals /\J better statistics can be achieved.

gas-fille4/\ (b) The stopping power is approximately 10 times that of a device (since the detector material is so much denser), and thus it becomi~){ possible to stop, in the detector, particles with energies typical of nucle~{( interactions. Consequently a very large number of electron-ion pairs ~~}~ formed, leading to very good energy resolution. A 1-MeV proton stoppinil in a solid-state detector will create 300,000 electron-ion pairs, while th~)~ same proton traversing a proportional counter of 2-cm thickness woui~@ )J only release approximately 30 pairs. )}~; ::::::: 39see the Encyclopedia of Phy.sics, Vol. 45, Nuclear Instrumentation 11, p. 110.

\( 40 Toe scintillation counter is also a detector in the solid state! ·.·.·.·, <::::::: :: ::: ·::::: .......

:~/i ·. .· · , .· ·. . . .

·.\\ -:-:• 1·

## 8.5 Solid-State Detectors

~r ill!:: In practice, however, it must be possible to collect the free charges (those ft created by the passage of the charged particle) before they recombine; this wr might be done, for example, by the application of an electric field in the ft detector material. This requirement is very difficult to meet with any of the t / ordinary crystals. Clearly, the material must have a high resistivity, since ~( otherwise current will flow under the influence of the fiel~ masking the ...

f;,: / effect of the pulse produced by the passage of the particle; qn the other ~~( hand, in high-resistivity materials, the mobility of the free carriers is very ::=::? low and the recombination probability high.

~) Even though some results have been obtained by using diamond as ~/ a detector, semiconductor materials come much closer to fulfilling the ~/-requirements mentioned above. Very pure material (an intrinsic semicon- "t· r ..

ductor) is used to achieve the necessary high resistivity, on the order of r:t 107 Q-cm, and the detector is operated at low temperatures. Such devices [ / are called "bulk semiconductor detectors."

~\ A great improvement occurs when a semiconductor junction41 is used as ~? the detector volume; a device of this kind is called a barrier-layer detector.

@.( The junction is made by either of the following methods: ~:-:- f} (a) Diffusing a high concentration of donor impurities on a p-type ~\ material, usually silicon, thus creating an n-p junction.

f\ {b) Utilizing a thirJ p-type surface formed by oxidizing n-type silicon ;,:. ..

[ ( or germanium when it is exposed to air. This surface is so thin that it is ~( usually coated with gold to provide a good electrical contact; thus we have ~---·. .

~:? a p-n Junction.

f::.:.-}.·.

In either case the operation is similar, but the junction is always reverse ~:::: biased.

;.:.·.

~( Below we will briefly discuss the diffused junction (n-p) type of detec- ~/ tor, Fig. 8.25a is a reproduction of Fig. 2.20, and gives the configuration of ~ the energy bands at an n- p junctio~ electrons being the majority carriers in r.·.· t: · the left, or n, region, and holes the majority carriers in the right, or p, region.

;,:. .

~\ Electrons may not move to the right, since the conduction band is at a higher [i: (negative) potentiaJ, and holes may not move to the left, since the valence if band is now at a higher (positive) potential; as a consequence there is some f:\ repulsion of majority carriers from the junction; Fig. 8.25b shows their ~{ density distribution. We note a "depletion zone" in the region marked S -T.

~::: :x?-,···.

~.,_._/ 41 Semiconductor junctions were discussed in 2.4.2, and the reader may find it useful to z~::\ review that material.

~=-=: ~:=: ~·:: ~-:, ~:-: ,.:-: ~::: )I';'.: 346 8 Particle Detectors and Radioactive Decay -:; 11111 n p (a)

_:ti IT n p (b)

ii/iii (I p (c)

::::::;:::::1 ·-::::::::;:::: ::::::::::::;: . . ' .....· . ...... : ,,::::::::~::: • :-:-:-:. ., :. .; -1.

··:::::::::~ ·:~:::::::~ ,·.·.·. . - ........

./ }j .·.·.·.•. .· ~ :::::::::~ .~~:::::;~ n p ••••••••. .· ,1 (d) :\::::;:: FIGURE 8.25 The n-p semiconductor junction. (a) Position of conduction and valenJ/@ bands and of the Fermi level a<.-.ross the junction; note the majority carriers for each regiort{({ (b) Density distribution of majority carriers on the two sides of the junction. (c) Densify:;::~;::: spac~f}~ distribution of impurity centers on the two sides of the junction. (d) Distribution of charge on the two sides of the junction. }j~ -:-:-:-; .. .: :, ·\/~ ofii~ Next, Fig. 8.25c shows the density of impurity centers on the two sides the junction; that is, these centers which may be expected to be ionized by{@ ?!

the passage of a charged particle. To the left the donors have given electronf to the conduction band and are left positive; to the right the acceptors hav¢/f )!W .; ::: :::: .::::::: ;::::::: ''. •~ -J .:::::::: ... ::;:~:: ~r:·· f::: ~~?=: B.5 Solid-State Detectors 347 ~?: ~::: ~/ acquired electrons from the valence band and are left negative. However, f;-::r:::: these impurity centers are neutralized by the majority carriers, so that the ~( free (space) charge distribution is the sum of Figs. 8.25b and 8.25c, as ~=-=· shown in Fig. 8.25d.

r ==· :f:=:: Thus we see that space charge exists in the region of the junction, and ~~/ as a consequence an electric field (the so-called barrier) exists as well, and ~/ extends over the depletion zone. If an electron-ion pair is created in the f,~( depletion zone, the electric field is such as to accelerate the negative charge l~i/ toward the n region, where it will have high mobility (being a majority t ii· carrier); similarly, the hole will be accelerated toward the p region. Thus !\ ~.I'-.

good collection efficiency is achieved.

f { Figure 8.26 shows the same junction under reverse bias, 8.26a being ~/ the same as Fig. 2.21. Figw-e 8.26b gives, as before, the density dis- 1\ tribution of majority carriers, which are now further removed from the f> junction, and Fig. 8.26c is exactly the same as 8.25c, giving the density of f)

impurity centers. Figure 8.26d, however, which gives the space-charge dis ~f tribution, shows that the ionized impurity centers have reached saturation ~/ and extend beyond the junction. Thus, most of the applied bias voltage ii:-..

{{ . appears across the depletion zone, which now is much more extended; the [ \ limit to this increase in sensitive detector depth is set by the breakdown f ( voltage of the semiconductor material itself.

r/ ' In a diffused junction, such as used for a detector, the concentration f/ 3 of donors in the n-type material is much larger (about 10 ) than the l\ concentration of acceptors in the p-type material. Since the total free charge t> must be the same on both sides of the junction., the space-charge distribu- -~-·.· f \ tion is asymmetric, as shown in Fig. 8.27b. Figure 8.27a gives some of the ?).

physical dimensions in a realistic diffused junction; we note that most of z..

~\ · the "sensitive volume" is in the p-type material .

. :. . . , , I: , _ _ ';• _ ; . .. :• . . : _ __ : .. .:. . · ::::::: ~:::: z..,._:.._:..·. . 8.S.2. Practical Considerations in Solid-State Detectors ;;::::.

f> ~::: From the previous discussion we have seen how a semiconductor junc ~:::: ..... tion may provide the appropriate electric field within a solid so as to · .

..r....·.. ·.

·.· collect electron--0ole pairs produced by the passage of a charged particle.

:.:.;.: : =:, -.·.· _z::: . Multiplication such as occurs in the proportional or Geiger counter never .r.r.· ' ~ JP-. : :/ = .·.· : '· : · takes place in a solid, except under special conditions ("avalanche detec ~;:::: torsH). To achieve good resolution in a solid-state detector one must always ~?=:- .-.

::.

:: ·. collect all the electron-hole pairs produced. Thus the sensitive volume of ·.

~·:< *::: fk t{ :~=~=:===:· : 348 8 Particle Detectors and Radioactive Decay n p (a)

k: s· +~ n p (b)

I..

n p (c)

p+t---~ t?:- ~ "

p_t T' n p (bl.;,::~~; FIGURE 8.26 The n- p semiconductor junction under reverse bias. The plots in (a), (c), and (d) pertain to the same distribotions as described in the legend to Fig. 8.25 b~(~f }\J under reverse bias. Note the increase of the ..d epletion zone;' S' T'. .

## 8.5 Solid-State Detectors

I 10-4cmi -1-.t--

## 0.2 cm (Typfoal) ,,,...~. .. .- -11i-...,

Dead layer Particles ..

incident on this surface n p (a)

n p (b)

FIGURE 8.27 Arrangement of an n-p semiconductor junction for use in a solid-state detector. (a) Actual dimensions. (b) Distribution of the space charge.

. the detector must be longer than the range of.the particle detected; it is also !·: desirable that the dead layer at the entrance side be as thin as possible.

\ Since detectors with sensitive volumes of a length of 3 mm have been !: achieved) the use of solid-state detectors has been extended to particles of j: energies as high as 30 MeV. The resolution in energy is usually extremely { good- that is, on the order of 0.25% for alpha particles (see also Fig. 8.31).

/ The overall size of the detector is restricted to a few cubic centimeters, due / to the available semiconductor crystals; on the other hand, small size and } the absence of need for a photomultiplier are a great advantage.

( It is also possible to use solid-state detectors, not as total absorption \ :counters, but as d E Jd x devices, in which case the p region is also made {!thin and no electrodes are placed in the path of the particle. Such detectors illi:bave been made to respond to high-energy (minimum ionizing} particles r: 42Toe sensitive volume or barrier depth can be obtained from a no mo graph, as given by / J.

L. Blankenship, "Proceedings of the Seventh Scintillation Counter Symposium. Institute f ?f Radio Engineers, NY," Nucl. Sci. 7, 190 (1960).

. i..- · . : . .· · - . . · .

.·.·.

··-· r.· ..~ .·.

_ .

· .

: : . ._ ::::: :.:..:i :•:• ·.

~:> 350 8 Particle Detectors and Radioactive Decay Bias voltage 10M Pat1lc'8 ---- Discriminator and scaler 5 µµF Preamplifier Amplifier · :::::}::~ I.

• , ·.

•.: ;·· /··· FIGURE 8.28 Typical setup for use with a solid-state detector including a feedback/)ff~!

preamplifier.

as well. Semiconductor devices are also very useful for the detection of:?:~:~::: ......., .., . . .. ,.., . ..

the::)Ji:~ gamma rays. In general due to their small size, .the ratio of counts in a:.·}.·.\·J.z·i½~'· photopeak as compared to background counts is smaller than that~f or scintillation crystal; however, the resolution is excellent, reaching one part\ J m, in a thousand.43 } ' . } ... ~ ... ~ '" ~ J ~ '; ~ ' art, the/{}@.

In practice, the construction of a solid-state detector is an and attachment of electrodes to ensure good ohmic contacts may be quite.) )~t difficult. When germanium is used, cooling to liquid nitrogen temper~}Xt/ ambient/fl\ atures may be required, while silicon gives good resolution at }if]

temperature. The output signals are small, the voltage being detemtlned by the capacities of the junction and of the· amplifier input; the former.}}{)

depends on the length of the depletion zone and the area of the detector. {ff )if( If we assume a typical capacity of 200 µ.µF, then for 1-MeV energy loss~ the signal voltage is {if{ .::::::::~:: 19 6 .)t/ = - Q = 1.6 X 10- X (10 /3) ,..__, -4 V 200 0 12 ,..__, 2.5 x 10 V. (8.42) t:=:=}:::=f:=: : C x 1 - It is necessary to use a charge-sensitive preamplifier because the capacity' }}?

C depends on the applied bias; thus if voltage is directly measured, severe }}{ :Ji variations in gain occur when the bias is changed. Leakage current in the crystal and amplifier noise set the limits of the smallest detectable signals. {{} Most of the hardware for solid-state detectors as well as the detectors.\::*~~: {/J{ themselves are now commercially available ; 1-'1g. 8.28 shows a typical )J~: setup with a feedback preamplifier. A surface-barrier silicon detector is used /j ::o;!:1:,n!:i:.J o~t;::~.~:,:~~ ::,:~~~~=~·· ™· ·

## 8.5 Solid-State Detectors

and operated at room temperature. Figure 8.31 gives the response obtained from polonium alpha particles of different energies (after attenuation in air). Another type of solid-state detector, called p-i-n (positive-intrinsic negative material), consists of a layer of intrinsic crystal placed between p- and n-type material. It has the advantage of a much longer sensitive volume.

...

8.5.3. Range and Energy Loss of 210Po Alpha Particles in Air In Section 8.3.2 a description of the method of obtaining an estimate of the range (and hence energy) of Po alpha particles in air, by means of a crude ionization chamber, has been given. With solid-state detectors, it is possible to improve on these measurements, as well as to study the rate of energy loss of the alpha particles as a function of their energy.

A collimated 210 Po source and the detector are both placed in an evacu ated vessel at a fixed distance of 15 cm, as shown in Fig. 8.29. Then air is allowed into the vessel, and as a function of the pressure we measure: (a) The number of particles counted in the detector, and (b) The pulse-height distribution of the output signals, namely, the energy of the alpha particles when they reach the detector.

In measurement of type (a). the same number of alpha particles should be reaching the detector until the pressure is raised to the point where the amount of material (g/cm2 of air) between source and detector is equal Slits p 0210 source 'To pump and gauge AGURE 8.29 Arrangement for the measurement of the range in air of 210Po alpha particJes. Note mounting of the solid-stare detector and source inside an evacuated chamber.

·)j}J~j . -:-:-:-:~:-:-:..:~:- 352 8 Particle Detectors and Radioactive Decay )i li~II 1l!lli l i i/!ii!!]l!Il~ C .·,:.:-:-:-:~ :- :::> ,, It I I I I J \ f \ 0 ....__ ,...__ __,_ _ ____,_ __~ _......___..,....__../. ......,~~ 0 0.5 1 1.5 2 2.5 3 3.5 4 Effective-distance (cm} -::;:;:/:~¾·:, ·:::::::::::=$~ th~:{)a%J FIGURE 8.30 Data on the number of counts from a 210Po alpha source reaching solid state detector as a function of pressure in the experimental chamber. Note that th~)j @~~j if::;:~::?.:::: corresponding effective distance in centimeters ofa ir at stp is indicated. The dashed curve the derivative of the solid line; it indicates the ..s traggling'• in the range of the alpha particl~.}\~ft :i/!!!i!{I~~~I to the range of the alpha particles; beyond that pressure the counting rate,i}}~~~:} should abruptly fall to 0. Note that since the relative position of source an4,(}f t detector is not altered, the solid angle ~Q does not change, and the only}{Jf:{ ...... ·=-=· .

variation arises from the increased multiple scattering; this, in turn~ may/\~~:;?

}jj~J result in some loss of particles from the beam. ·=·f These considerations are indeed borne out by the results obtained by ~}\/ \ .........- .-:-.-... ){:~ff student and shown in Fig. 8.30. Here the ordinate to the left gives the count$:: o(\/~f per second while the absdssa gives the pressure of air in centimeters mercury, or. equivalently, the effective distance of air at stp. The dashe~(\Jt \Jf curve to the right is the derivative with respect to distance of the countingf range 210 alp~.JfJ~]~ curve and gives the (and so-called range straggling) of Po particles. We obtain a mean range of }}}JI

## III/

~ 3 72 6 md m exttapola~ rmge R . ± 0.0 cm R = 3.82 ± 0.06 cm, .-:::=:=%·::*.~ })t~~t which might indicate some systematic discrepancy from the accepted valu¢{?~f ·.}./. J~ ~f.~r.

for the extrapolated range of 3.93 cm.

JI .:{ii ·::\::=--~ . ·,:-:-~?&

## 8.5 Solid-State Detectors

Vacuum 1800 3.8 cm Hg 9cmHg .E 1200 14 cm Hg - € ~ 1000 Pressure ::I 0 19 cm Hg 0 800 200 l I l 7 I r 1 2 4 6 8 Discriminator channel FIGURE 831 Distribution of output pulse height of the solidAstate detector for five different pressures. Note the gradual decrease of the energy of the alpba particle.

Turning now to the measurements of type (b), Fig. 8.31 shows the dis tribution of the detector pulse heights as obtained with the single-channel discriminator (described in connection with the scintillation counter). Each peak corresponds to a different pressure, and we thus note that the alpha particles reach the detector with progressively less energy when they have traversed more grams per squared centimeter of air. We set the pulse height obtained in vacuwn equal to the full energy of the Po alpha particle, namely, 5 .25 MeV , and use the linear characteristic of the solid-state detec tor to obtain the energy of the alphas as a function of material traversed.

The results obtained by a student are given in Fig. 8.32 (solid curve).

If the derivative of the energy curve is taken with respect to distance, we obtain the energy-loss curve, d E / dx, as a function of distance, as shown :: by the dashed curve in Fig. 8.32. Such a curve is called a Bragg curve.

:_ and shows a 1/E dependence45 as predicted by Eq. (8.12); for the ct. parti ½Mv :: cles KE= and the influence of the logarithmic term ofEq. (8.12) is : minimal. As the particle reaches the end of its range the energy loss d E / dx :~ drops rapidly to 0.

. 45 We might plot the d E / dx curve against energy by making use of the data of the energy : cwve to express the distance from the stopping point in energy units.

:: : : :;: ::::~,.;; : : : : ::::::::::::::::- ::: . : : :' :::.: : / -: : •: : •: : . . : : : - , · 354 8 Partic~e Detectors and Radioactive Decay .

}j!illi~ 5.5 5 / \

## 4.5 \ 11!!!!1/I[

/ \ 2 i )illll I \ ~ 3 ' / \ t1i 2.5 :\{t ~ ?j \ l!I o i 2 1 ~ -- ~ 1.5 \ :-:-:-:-,-,:1 wC y:;m 0.5 :::::::::::i~ \Utt~

## 0.5 1 1.s 2 2.5 3 3.5

:.:·::.:·.?·.-~...~..=....: :¼~.

Effective distance of air stp (cm)

FIGURE 8.32 Pl~t of th~ residual energy of a poloniu~ alpha particle whe~ it reach~:~;wa1 de~tor as a funcuon of arr pressure (plo~ howeve~, m_t e~s of the equivalent am~;, ½ J~~: of arr (stp) traversed). These data are obtamed from distnbutions such as those shown'.>J:ri:::~:~~ Fig. 8.31. The dashed curve represents the derivative of the solid (energy) curve; th.u~\\J@f@~ \}J~}~ gives the energy loss per unit length. It is called the "Bragg curve."

\)lit~~ pQ(g{)~~\ From the energy curve of Fig. 8.32, we note that in air at stp the nium alpha particle produces at the end of its range approximately 67,qQ_Q@\WJ.~ electron-ion p~irs per cen~eter, whereas at its full ener~ it p~ryo d_uus$w!.f~~jrfW~ ti only 20.000 patrs per centrmeter; these. numbers were obt~ned ajri\J~:!

an average loss of 36 e V for the productton of one electron-ion parr m :)l!i/!II 8.6. NUCLEARHALF-L~MEASUREMENTS We will now discuss the mea~urem~nts of the ~alf-li:'e~ of ~om~ short d -li ~ ~ , ¥ r/ : ~ JJ ~ I 1 ~~ !

nuclear states. A ~or~ugh. discus~1on of the ~me distnbution 1n the s~~trti; of nucle?I states 1S given m Section 10.5. Sunply put, for a 4l6a rge w1!1Jjj~ of nuclei, the number of decays per second, the decay rate R, dec~~iti 46 For historical reasons, the standard unit for decay rate is the Curie= 3.7 x 1010 JW~ (~Jf pe~s ~nd. This is the number of dec~~s per ~ond -in one gram of radium. The modem urut 1s the Bequerel, defined as one dismtegratton per second, so 1 Bq = 1/ (3 .1 x J0 10 } ~)~J~~ F or more det ai ·1 s , see A ppen d" 1 x D . ··\ ·} · ·) .~,. @.. (~: :/}]@ ){J~ }/ii 8. 6 N u c I ear Ha If-Li f e M e as u rem e n ts 355 proportional to the number N of nuclei in the sample at any particular time. That is, dN = - R =-}..N.

dt The proportionality constant is called -}.., the minus sign reflecting the fact that the decay causes the number of nuclei to decrease with time. This .·.·.· differential equation has a simple solution, namely ., t.· .· where No is the number of nuclei present at t = 0. Obviously, A charac (••••:•:•: terizes the lifetime. The larger).. is, the faster the sample decays, and the / . shorter the lifetime is. There are two definitions we use for the lifetime.

f{: One is the mean life: ~·. ..

r- -)...

The other is more practically minded, and measures the time it takes for the sample to decay to 1/ 2 its original number. This is called the half-life, and it is determined by solving N(t) No/2 fort.

ln 2 = - = 0.693-r.

t112 )..

References usualty quote the half-Life, but not always. Be sure when you · · look up a lifetime, that you are getting the half-life or mean life. A good source of information on nuclear decay half-lives is the National Nuclear · · Data Center at Brookhaven National Laboratory and available at the Web site http://www.nndc.bnl.gov/nndc/nudat/radform.html.

Obviously, we must resort to some sort of trick to obtain a sample nuclei with short-lived states that can be measured. One trick we will use is the chemical separation of barium from cesium. However, we will also create ;_;_;_: new isotopes using a type of nuclear reaction called neutron activiation.

In neutron activation, reactions with neutrons are used to create radioactive isotopes from stable nuclei. N_eutrons are produced using a plutonium .· beryllium (PuBe) source, which is safely packaged away so you cannot get near it, and allows the neutrons to irradiate samples inserted into the container. Plutonium decays by a-emission! that is, 239pu ~ 235u a, ·.J/Illf • :::fw 356 8 Particle Detectors and Radioactive Decay ;:rttl@I and the a particles react with the beryllium •::::lj!j!}j(k~ "' + 9 12 .;::::::::/~:=~w-~~.@ Be _____.._ C n .·.·.·.·.·.·.·-.-~~ ...L ~ -,r I ~ -.4, ·.:·:m.:·:.:·:.:·:l.;·:.:.:l-;.:·.~~~~ releasing neutrons. These neutrons are slowed down by collisions protons (in all the paraffin, a hydrocarbon, surrounding the source), ma\tjtt.:g{:~:~ the~ ~vailable for other reactions. Whe~ you put an isotope in ~e neou~:w~m§jJj @=:~~ rad1a~on ''oven,"_ make sure you "cook" lt for at least a large fractiomne asu.~~rJ~~I half-~e. Otherwise, .Y~U may not get enough of a rate for you ~o Typically, the radiation from these sorts of sources are easily detect¢4tt~ with a Geiger counter, and simple setups are available from a wide v~~J~@~ ety of vendors. These setups include simple interfaces to computersp~f jj ff,:®, som~(J#tI discussed in Section 3.9. The data presented here were taken with a board a desktfift @l different setups, including multichannel scaler plug-in for compuij:f:~tfli computer, and a Universal Laboratory Interlace module with a (~' •t• ~J .. ,i~.4J'.-~~.'/f.

running LoggerPro. All one really needs is an interface and software counting pulse_s from ~e Geiger co~nter (o r othe: detector and electroni1~f@i ;[ 1;~Jal~ for a ~xed pe:nod of time ("dwell time:'), reco!dmg that number, and count.mg agam for the saine fixed penod of tune, and so on. A grapbi¢ij.:;::;~JJ::: a#,J{fl ~ disp1ay of the data as it conies in is very useful, and generally part of commercial package. \:;::;::::;::X.:t:: In what follows, we discuss the analysis of three radioactive isotop~~{fijf qffjfilf with varying half-lives. A key point is the presence of some sort signal, in (Su:f;@fffu~!: ·'background" addition to the primary radioactive decay.

exampJ~:f~:ilid backgrounds are always present, at least at some level.) In the first ~ij\}%.f ( 1161n decay), the half-life is rather long, and a method for estimating sy~{f jfl background level "by hand" and for incorporating its effect into the tematic error is outlined. In the case of 137mBa decay, a fitting technig{ij@fijt~ predse1y ba.W:+?{[?i that allows one to determine the background and find the Iit: w~f life with its corresponding random uncertainty is discussed. Finally, fro~'.(/f~t:I discuss radioactive silver isotopes, which present a combined signal /}))ff two radioactive isotopes, each with relatively short half-Jives.

8.6.1. Production and Decay of 1n : ·,:::::::::: :::::;:::::~: You can produce 1n using neutron capture on a piece of indium. Indiu#i{i~f~f:~ Jlf.t~ is a very common metal used for soldering compounds, and all of na~~( indium is the isotope 1151n. The decay scheme for 116In to 116 Sn is shoW:#)~j~~~ ~i/J~j ~~ in Fig. 8.33. Note that the ground state has a very short balf~life~ on)y 14 ':-:-:-:-~:-:=:-:..:-' . \/:;~;:?::~;~ ': •:.: -:·~·=···=···. .~ . ,::::::4~. .: ~~~~~ >J~~J~~ ')@~~~~~ . <::::~::!;~~;!;~ s+ 0.06 MeV (64 rn)

1+- ---~ 11a,n (14 s)

~-----I+ 2.B0MeV (Z=48J 4+ 2.52 MeV t I 4+ 2.38Mev ~+ 2.22MeV 3.3MeV !

2+ 1.29Me'V -I--.---- o+ ' 16Sn (.2: 50)

PIGURE 8.33 Decay scheme for 1161n.

,a- You will be detecting decay of the excited state, 60 ke Vabove the ground state. The decays proceed mainly to a couple of states at around 2.3 MeV, and the available energy is 3.3 MeY, so the {3- typically have energies up to a megaelectroovolt or so. These are easy to detect in a Geiger counter.

Irradiate the piece of indium for ao hour or so. Remove it and place it on the Geiger counter platform, close to the counter window. Take data for an hour or so, setting the multichannel scaling program to count for intervals of something like a minute.

It is probably a good idea to make a semi log plot of the data, and estimate the half-life by hand, just to make sure the result looks about right To do a better job, you can easily fit the data to a decaying exponential. Just use the MATLAB function polyfit to fit the logarithm of the number of counts versus channel to a straight line. In fact, this is a case where you can accurately write the random errors of the points, since they are governed by a Poisson distribution. That is, if there are N counts in any one channel, = ./Fi, then the random uncertainty in N is 8 N and the random uncertainty in the logarithm of N is ol og N = J / ,./ii.

A sample of data on indium decay is shown in Fig. 8.34. Each channel represents 30 s. The simple fit described above is shown by the dashed line. Note that the fit is not really very good. You can see that more clearly if you plot the difference between the fitted function and the data points.

In fact, this is not too surprising since you expect some background rad.i atioo from other radioactive isotopes in the piece of irradiated solder. You can try subtracting a constant value (representing the background counts)

··:::::::::::::: .-· :.·.:-·:.-· :.•.:.• : -:-:.:-:.:-,;.. .: .·.·.·.·.. .......

358 8 Particle Detectors and Radioactive Decay ::::::::::::: ·::::::::::::: :' ~.:.:.: -:· -: :~ :: : :: : ::: . ,·,·.·.·.- ·,·,·.·.·.-....,...

,::::::;::::: ,·,·.·.·.- ....

220 •• 200 . lll cn ~ 180 .

lt:S .c ·::::::::::: ~ 160 · :::=:::::::: 11)

J C a . 140 . . : · : . , : : · : - ; . : · :: - - : · : . : . · : = , ~ . : • ~ C: .. ·,·.·.•r,.

8:::J :.

·: ::: :: ·,,-::::::;;.

._ 100 -: :: : :: : : ~ : ·:::::::::: . t . 1 0 ) .. .. .·... ··. . · . . . - .... · · E 80 :::::::::~: ; z::J .·.·.·.·. . ·.

:: 40 ....

:-:-:-:.1j 0 50 100 150 200 250 300 350 :::::::: ?})

Time (Channels)

FIGURE 8.34 Data and fits for the decay of 116In. The dashed line is fitted to a decay){/ ing exponential, while the solid line includes a constant background of 17 counts. The.:})

\iii!

multichannel scaler recorded data every 30 s; that is, each channel represents 30 s.

from the data before you fit it, and see whether it looks better. By cal- ·// culating the x 2 function, you can even optimize the background term by }} • . . . 2 ·.·.·.

mmuruzmg X . <\ The MATLAB program shown in Fig. 8.35 was used to do exactly this. )} :y: After reading in the values of channel and counts, the user is asked for a number of background counts. Then this value is subtracted from the data, :{ and care is taken to make sure the value is not less than 1. (Remember, you :)

are going to take a logarithm.) 1\vo fits are done, one that is unweighted )

(using polyfit) and one that is weighted according to the Poisson uncer- :::: tainty in the points (using Ii n reg). The results, including the x2 , are printed and plotted. By trying various backgrounds, you find that the ]owest x2 (i.e., the "best fitn) is found for 17 background counts. You can even esti mate your systematic uncertainty by looking at how much the lifetime varies as you move around in x 2 near the minimum. This can be large if the minimum in x2 is shallow. For this particular data set, we find that r 160.7 ± 2.0 ± 10 channels, 8. 6 Nu c I ear Ha If· U f e Measurements 359: · ¾ LOAD AND EXTRACT DATA POINTS ·· ·.·.· load indium.d.at chan•i.ndium(:,1); ...

•, data=indium(:.2); ¼ PREPARE DATA FOR FITTING LINE TO LOGARITHM :,: ·> bkgd•input('Background counts '); dnet911ax(data-bkgd,1); ..

ndofzlength(data)-2; edata=sqrt(data); ldata:11log(dnet) ; eldata=edata./dnet; ¼"

¼ UNWEIGHTED FIT coefa-polyfit(chan,ldata,1); fita=exp(polyval(coefa,chan)); chisqa=sum(((dnet-fita)./edata).-2); fprintf('Unveighted fit:\n'); fprintf(' tau•Y.6.3e\n',-1.0/coefa(1)); fprintf(' chisquare/dof=1/.6.3f\n',chisqa/ndof); 'l.

¼ WEIGHTED FIT [coefb,ecoefb,lfitb]~linreg(chan,ldata,eldata); fitb=exp(lfitb); chisqb=sum(((dnet-fitb)./edata).-2); fprintf('Weighted fit:\n1 ); fprintf(' tau•¾6.3e',-1.0/coefb(2)); fprintf(' uncertm¾6.3e\n',ecoefb(2)/coefb(2)-2); fprintf(' chisquare/dof=¾6.3f\n>,chisqb/ndof); FIGURE 8.35 A MATLAB program (i.e., m-file) used to fit indium data. The program asks the user for a number of background counts. then carries out the fit., and reports the t/ results. including the x2 • Although the background level can be fitted automatically using ~ ~\ t:- · nonlinear fitting techniques, thi~ program gives one a feeling for the sensitivity of the x2 f · to the background level.

~:::"

~:-:- ~;::- f).

where the first uncertainty is random and the second is systematic. Since ~{ each channel is 30 s, we detennine that ~:::: ~:-.• [r ft/2 == log 2 X !" X ~min/channel 55.7 ± 0.7 ± 3.5 min, ;.:::: :;-;:: }} which agrees well with the accepted value of 54 min. In fact, it seems we ~-::. may have overestimated the systematic uncertrunty.

,:-: ..

·.

~:::.· ,t t.,_, · ·.. ._ t:- ,.:::: ::;:•.

:,;:: .;-:-.

~:::.

II 1/f 8 8 Particle Detectors and Radioactive Decay \{JJ@ Actually, this business of adjusting the background term to minimize x ~ can be done automatically in MATLAB. That brings us into the world of}/??!

/iJJ@.

nonlinear fitting, and we will do that next. . )II 8.6.2. The. Half-Life of i m B~ . . .

Now we Wlll measure the half-life of another short-lived isotope, 137mBa.//~j~ step!)/)iffi The background is very clear in this case, and we will use that to go a /)]ti further in ow· data analysis techniques. This isotope does not need to be produced in the neutron oven. } }~!:~:: Recall the decay scheme of 137 Cs in Fig. 8.21. The daughter nucleus)(}JJJ 137Ba, is produced in its ground state only 5.4% of the time. The rest of the}{jlm time it is made in the excited state, called 137 m Ba for "metastable," which{))@ decays by y-ray_emission, but with ar~latively large half-ll!e (for y decay}){fm of around 2.5 nun. Of course, 137mBa 1s produced all the ttme, as the very\:/f~j 137 137 long-lived Cs decays, so you cann·ot isolate the mBa decay withou()J&Ji 137 )\}@~ somehow separating it from the Cs.

You can make this separation because chemically, cesium is very diffe-}i?f:i rent from bariura By passing a weak acid solution through a 137 Cs source,)}fjf bariun1 is captured and comes out in solution. Some cesium comes through){{~~!

://Jf as well, but most of the radioactivity of the solution is from t 37 m Ba. Simple kits are available 47 for carrying out this chemical separation. It is best if}}}~f ·.·.·.·.·,..···:r·.r ....

you squeeze the drops through slowly, enough to fi]J the small metal holder·:)}ff }!}Jf:i in about 30 s. Then place the holder in the Geiger counter tray, and start ·~--- .·.·.·.~.·. .

the data acquisition program. \ ::=:=:=~~==: .. ·.·.·.·.·.·.·%·.

Realize that you are working with radioactivity and hydrochloric acid:\{:~~i} Do not be careless. None of this is concentrated enough to be particu-){{ }( larly dangerous, but you should take some simple precautions. Disposabie/ }fl gloves are located near the setup. It is also a good idea to wash your hands(/}f~ .·.·.·.·.·.··::?-';· _:}}~:~f soon after you are finished.

You should choose a dwell time that allows you to get a relatively large:\ \J]

nwnber of points in each channel, but many channels over the expected)))/ decay time of a few minutes. You should be able to get several hundred{{@~~ }]=$ counts per bin in the first bin or two, and a background of less than 20 countf half-hour.):;:\f#f per bin. (The background level will be clear after counting for a ·.\/t~ You might need a few tries to get all of this where you want it. )/!iii 47 For example, from TEL-Atomic, Inc., http://www.te Ia tomic .com/.

.i ii ·:::::::f.~ -:-:-;...,.~ ·.)JI~ .:::::::·~%

## 8.6 Nuclear Half-Life Measurements

You can use the program in Fig. 8.35 to fit the data and adjust the back ground counts, but that is tedious. In this case, since the background will be very clear, you can determine it precisely by averaging over the last many channels, and subtract that number from the data before fitting. However, MATLAB gives you the ability to fit things nll at once.

What you need to do is minimi2e the x2 function numerically, and MATLAB gives you a numerical minimization function called fminsearch that can do this. You need to minimize x2 as a function of three variables, two for the exponential fit and one for the background value.

Fust, write a simple m-file called expcon.m, wbich calculates the function you are going to fit to the data: function y=expcon(x,NO,tau,bkgd} y=NO*exp(-x/tau)+bkgd; and then write another called fitexpcon.m, which calculates x2 function chisqr=fitexpcon(pars,xdata,ydata,edata)

chisqr=sum(({ydata-expcon{xdata,pars(l),pars(2), pars(3)))./edata) .A2); Do not forget that for these data, the array of uncertainties edata is just the square root of the counts, i.e., edata:sqrt(ydatal. (If any of the channels has zero counts, thea set edata equal to unity.)

Play around with some values of pars(l ,2,3) so that you have a good starting point. ( Just plot the data points, and then overplot the function expcon until it looks kind of close.) Then type the command frninsearch(@fitexpcon,pars,O, [] ,xdata,ydata,edat~ and you wi11 get the best-fit values returned. (Check the help documentation for details of the arguments for fminsearch.)

Exactly this procedure was followed to fit the data shown in Fig. 8.36.

The fit achi~ves a minimum x2 for a lifetime -r = 3.80 min~ corresponding to a half-life t112 2.63 min. The random uncertainty is determined, as shown on the right in Fig. 8.36, from the values of r that increase the minimum x2 by one unit These x 2 udata" are fitted to a parabola, and we determine the uncertainty in -r to be ±0.10 min. Consequently, we 362 8 Particle Detectors and Radioactive Decay 300 .------....--- ---,,----- --.---------.-- - -r------T- ----, 250 Fit to the form N exp{- tfr)+ 8 Minimum ? =103 Number of data polnts-==100 "iii 200 C . !!ii ro .r=.

t.> ii![!}!~i~ ai 150 0..

8::J 0 ,....__ _.. .....__ _ .......... ___ _. ....__ __ __._ __. ..___...z,.. ......_ __ _, -:-:-:-:1~ 0 5 10 15 20 25 30 35 Y!I Time (Minutes)

\:::lf.:

## 104.8 ...------..-----.-------,-----.---- ....-----

·i!I 104.6

## 104.4 '}It

/:::::=:::

## 104.2 ::::::;~::::

·-::::::=:=:= 104 .;:::;;~=== (\I> < \It i~

## 103.8 ):i:~{=~~

~ -:;::::::::::

## 103.6 i}JJ

## 103.4 :!!{1~

## 103.2 ·-:-:-;-:-:

.·)=~=~=~= ·.·.·.••·.· 103 ·.::::::~= \!}{

## 102.8 ,____ __ _._ ___ .... _ ___ _,_ ___ __._ _______ _

## 3.65 3.7 37 85 39 3095 }Ji

· ~felime :-~Minutes~- .

. ·=·=·i· F1GURE 8.36 An example of a nonlinear fit. The data are from the decay of 137 mBa, }!ij including some constant background The MATLAB function fminsea rch was used to· )j ~ }ii make the fit. The plot on the top shows the best-fit curve, while the lower graph shows the x2 minima found by fixing the decay lifetime to various values. The random error in the·\J~ lifetime is determined from the values that increase x2 by one unit. ·/ j~ .·.··~ :::::~ ·.·.·•• )i ,·.-4.,.,.

II .:)~~ 8. 6 N u c I ea r Ha If-Life M e a s.u re me nt s 363 find that 137 = ± nun.

t1;2( mBa) 2.63 0.07 This is in good agreement with the accepted value of 2.55 min.

Note that the radioactivity you detect from 137mBa decay is y radiation, which is not detected very efficiently by a Geiger counter. You might try using a Nal(TI) detector instead, keying in on the particular y-ray in ques tion. This should greatly increase your counting statistics, as well as reduce the background.

8.6.3. Radioactive Silver Isotopes Natural silver is pretty much evenly divided between two isotopes, Ag and 109A g. Neutron activation captures a neutron equally well on these two isotopes, producing the two radioactive isotopes 108 A g and 110A g. Both of p- these decay with a relatively high momentum that is easy to detect, but one isotope has a half-life of 24.4 s and the other of 2.42 min. You might want to look up the decays to get more details.

Take a piece of pure silver foil and cook it in the neutron oven for at least 10 min. Quickly take it ou~ put it in the Geiger counter, and start the program. Do not forget that the lifetime of the shorter-lived isotope is only half a minute. It should be clear from the raw data that there are two lifetime components from the decay.

Representative data taken by students is shown in Fig. 8.37. The dwell time was set to 2.5 s, but in order to get better statistics in each channel, the MATLAB function reshape was used to add every four channels together. Error bars are added to the data points using the errorbar function.

The points are fitted to a do1:1ble exponential decay, completely analogous to the way we fitted a constant plus an exponential to the mBa data.

x 2 The only difference is that them-files for the fit function and for the are :-: changed slightly.

The best fit yields half-lives of26.9 sand 3.53 min. The shorter half-life is in good agreement with the accepted value. The longer agrees much less welt but this is not sutprising. No background term was included in the fit (leading to an overestimate of the ba1f-life), and the statistical accuracy · · of the longer decay is clearly marginal. The ambitious student can explore these points using the techniques discussed for 1161n and mBa decay in the previous sections.

i~i/2 364 8 Particle Detectors and Radioactive Decay ·,:/:?:$ -:-:-:-:-:-:-~ ..: ){?~ i'\{}{®, 160 \ff~ ai 120 · C: I ~ I .l:: 100 I .0.. . \ Q) -:-:-:-;-.-;··~1 a. 80 cCl)

60 \ 40 _ 20 ...

a: --- _:\(@~w 1 200 300 400 600 Time (Seconds) ·-\/)}~ rv;J\Jl~ FIGURE 8.37 The decay of neutron-activated natural silver, fitted to the sum of decaying exponential functions. The plot was made using the MATLAB function errorbafr ;::}~j~ ··.://:l ~.@ In addition to the best-fit curve, we show the two individual exponentials separately. I II 8.7. REFERENCES : By necessity the discussion presented in this chapter is not complet~{\jJW Below is a selective list of references (including those alr~y mentionec(}Jfil in the footnotes to the chapter) that the reader may consult for additiona({{~~ u·o · m· 1c orma n. :::::=:::::=:::~: -:-:-:-:-:-:-:-..--½ On interaction of radiation and particles with matter: . ))f

## 8. Feani, Nuclear Physics, Univ. of Chicago Press, Chicago, 1950

J. D. Jackson, Classical Electrodynamics, 3rd ed., Wiley, New York. 1962.

W. Heitler, The Quamum Theory of Radiation, 3rd ed., Oxford Univ. Press, London, 1954.

On gaseous and scintillation detectors; neutron detectors: W. J. Price, Nuclellr Radiation Detectors, McGraw-Hill, New York, 195&.

B. Rossi and H. Staub, Ionization Chambers and Counters, McGraw~HiU, New York. 1949.

J. Sharpe, Nuclear Radiation Detectors, Methuen. London, 1955.

Encyclopedia of Physics, Vol. 45, Nuclear lnstncmentmion JI, Springer-Verlag, Berlin, 1958.

J.B. Birks. The Theory and Practice ofS cintillatio11 Coullting. Pergamon. New York, 1964.

On solid state detectors: J. M. Tuylor, Semiconductor Particle Detectors, Butterworth, London, 1963.

.· :-:-:-,-:~ -<:;:::j* 8. 7 Ae fe re nces 365 There are a number of good introductory textbooks on nuclear and particle physics. Some examples are: K. S. Krane. Jmroductory Nuclear Physics, Wiley, New York, 1988. This is a good basic book wilh some discussion of experiments and experimental met.hods.

S.S. M. Wong, Jn1roductory Nuclear Physics, 2nd ed., Wiley, New York. 1998. A bit higher level thllll Krane, but a thorough sur\'ey of the underlying physics of nuclei.

D. Griffiths. JntroducJion to Elementary Particles, Wiley, New York, 1987. An excellent ondergraduate level discussion of particle physics. -:.

D. H. Perkins, ln1roduction to High Energy Physics, 4th ed .• Cambridge Univ. Press, Cambridge, UK,

## 2000. A modern, up-to-date version of a classic book

Many of the details of detectors, materials, and the statistics of nuclear process, as well as an excellent summary of particle physics, can be found in: Particle Data Group, Review of particle properties. Eur. Phys. J. C 15, 1-878 (2000).

## CHAPTER

Scattering and Coincidence Experiments 9.1. INTRODUCTION Ever since Rutherford performed his original experiments on the scattering of energetic alpha particles from atomic nuclei, scattering has become increasingly more powerful as a tool for investigating the forces between elementary particles. By now it is familiar to the reader that an electron, under the influence of the attractive electromagnetic force of the nucleus, may be found in a bound state. The classical analogue of this situation is the motion of the planets around the sun under the influence of the gravitational force; they describe elliptical orbits.

In general, a scattering experiment probes a system by sending a pro jecti le "into'1 itt and then studying what "comes out'1 of it. Similarly, correlation or ''coincidencen experiments can probe a system by looking at what comes out simultaneously in two or more directions. In this chapter, we wil1 study some types of each of these measurements.

~ <} !I/II 9 Scattering and Coincidence Experiments The experiments in this chapter make use of radioactive sources. We re~-/)/ij 01nmend that the reader review the material on radiation safety in Appendix-) ){@ -)\Ji~ D before undertaking these measurements.

formal-}/?fi The concept of "solid angle" is important for understanding the ism dealing with cross sections. The solid angle is a tbree-diroensionaI))}{~ ·.·.·.·.·.-.-.-:- . a.}\:}~~a generalization of the familiar planar angle AB, which is ..t he length of circular arc Di.s divided by the radius r of the circle, i.e., Di.0 Di.s /r .}{}}l Solid angle /j,.g is the area Di.A of a piece of a spherical surface, divided)/JM~ by the square of the radius, i.e., AQ = .6.Ajr2 • Planar angles are mea-\ (j~]

sured in radians and solid angles are measured in steradians. Just as a circle))\$~ subtends a planar angle of 2n to any point included in the circle, a sphere) )J§~~ . . .·.·.·.·.·-·,::.-;:..

subtends a solid angle of 4:n- to any included pomt. /:::ti~~i \\Jtf~ Solid angle is a useful concept whenever we are dealing with some sort of detector intercepting radiation which spreads out in all directions frorn\:}~im a source. Ionizing radiation and elementary p~cle_ detectors. are ju~t one{/j/]@1 example, but you would encounter the same thing m fields like optics or\:::?=:~~ . <:::::::::::~-: somcs. ·-::::::::~==·*: .. - • • • • -:-:-: .;.. ; ;;::r:; lo be explicit, let dA be a vector whose magmtude 1s an area dA 1n\{:~::i: unif }:/~ some planet and whose direction is normal to that plane. Let -n be a ·;i{j/Jm: vector pointing toward the source, which is a distance r away. Then !!~~ = _1)

dQ n •~A~ d~L' (9 r r .)}J@i where dA.1. is just the perpendicular component of the area. A spherica1)\?l~ surface is most convenient since all surface elements are normal to th.ei\:}tt~ :-:-:-:-:-;.. ; /:• direction to the center. In spherical coordinates (r, 0, ¢),where O ~ 0 < ir<}\:}~=~~ is the polar angle and O < t/J < 2n is the azimuthal angle, a differential ,·. / ·.· : .· ? .-.. ~ • : .. · ~ .r.r t . .

element of the surface has area · · :\I=i:=:::=:iI= m::fim::::; :::h:gl~:::: d¢)

= )I x (r d0) ri sin 0 d0 d¢, /I dQ sin 0 d0 d<f>. (9.2f You will encounter this equation many times in physics. }\{J .' ·.· . ............ .:.

We can easily apply this to the common case of a ~'detector face," normaJ.(:::::a:~: .·.·.·.-,,.. .•...

. .-:.

to the direction of the incident radiation, as shown in Fig. 9.1. Let th~(:}1~:?.

"detector face" be a circular area with radius R located a distanced from~({.../.{...:.

source. There is perfect azimuthal symmetry, so we immediately integrat~j\ Jf@ JII

## 9.2 Compton Scattering

__ .. --~--··'"

_.,.-- . 0 FIGURE 9.1 Calculating the solid angle of a circular face .

..

over </> to get dQ 2N sin0d0 and integrate from 0 = 0 to Bmax = tan- 1 (R/d) to get i0f08JI.

-b.Q = - I sin0d0 0=0 4Jl' 2 n / where we have written the fraction of the total solid angle as fl 41l'. 1hls = e integral is done most easily by a change of variables to µ cos with µ ranging from cos 0max = d/,/d2 + R2 to 1. Since dµ. = - sin 0 d0, 1l b.Q 1 [ d ]

= = 2 + (9.3)

4N cos0max dµ, 1 - (d2 R2)1/2 .

= = Ford 0, A0/4.1l' 1/2, that is, the surface covers one entire hemi spbere. For d -> oo, expand Eq. (9.3) to first order in R/d to find Af'l./41r = R2 /4d2 or AO = (Jl' R2)/d2 , whicb is just what you expect from the basic definition of solid angle.

9.2. CO:MPTON SCATTERING 9.2.1. Frequency Shift and Cross Section This section deals with the scattering of electromagnetic radiation by free electrons. As mentioned in the introduction to this chapter, it is the scatter jng of electromagnetic radiation from various objects that makes it possible for us to "see" them. However, as the .frequency of the radiation is increased beyond the visible region, the light quanta have energies comparable to, or larger than, the binding energy of the electrons in atoms, and the electrons can therefore be considered as free.

.<. .

:..: ::: .::·: .... .

.· .

·.

::: ::::.

,:.·.

}:}}1 ··:::::::::::~ ::::~::::::~4 370 9 Scattering and Coincidence Experiments ·.·.·.·.·.-......

.iI II~if . -:: : : : :::::::::~ ::)}~:~=~=~~ ·.·.· ...............

.. : · .

:: .· : ;: ·.

:: ..

...

hvlc '' •• •.i,.• •' " ..

.< ?ti FIGURE 9 .2 Compton scattering of a photon from a free electron .

i i In 1920 A. H. Compton investigated the scattering of monochromJJ,f W:~~~~:~I X-rays from various materials. He observed that after the scattering,. ..

energy (freq~ency) _of the X-ra~s had changed, an? had alway~ decreasM@;.:. 1.

From the pomt of view of classical electromagnetic theory, this frequen~;~~(ffi shift cannot be explained, since the frequency is a property of the incoi;j$.J~ m,J~I ~g el~ctr?ma~etic wave (fiel~) and cannot be altered by the ~hang~~Y:!ll ~ecll?n unp~1e? by the ~cattermg. rr, on the other hancL we th.i.nJ( of mcommg .rad1at:10n as ~mg represented by a beam of photon~, we n~~!@~ fl'.~ii_l only consider the scattenng of a quantum of energy E h v from a electron; then, because of energy-momentum conservation, the scatter~4tdi = ~#.\}~ quantum has energy E' h v' < E, in complete agreement with experiments of Compton. \}/)~ '¥:ff~ ~he frequency shift will ~epend _on the an~le of s~atteri?g and can· easily calculated from the kinemancs. Consider an mcormng photon}~tti elec~~,\i~ energy E hv and mo~entum hv/c (Fig. 9.2) scattering from an (at rest) of mass m; p lS the momentum of the eleoc:t ron after scatte~nu,r~1w~tl and h~' and hv' /care the energy and momentum the photon after plan_1~t::/J1 scattenng. The three vectors hv/c, hv' /c, p must b.e on the same • '•,\ •:••}• ....? ·.-.~.....: ,f.::?. ,/~',i", and energy conservation yields :{{ti i~:\:/~: ,' (9 '~.·/..·:.-·.:·-.:·.-·:--.@1: From momentum conservation we obtain <1 = + ((~:~,?1!li::i(:~1~ h v h v' cos 0 cp cos¢ 0 hv' sin 0 - cp sin¢.

Wtl~~t}i~~i 1see, for example, J. D. Jackson, Classical Electrodynamics, 3rd ed., p. 694.

New York, 1999. > . :-:-:-:-:-:{f~} :'.:;:;:::~~ ~::::.

rr ?:.-.

;z:•:• 9.2 Compton Scattering 371 :,:•:-: :::;::-:, ::f:- ~/ Here 0 is the photon scattering angle, and </> the electron recoil angle.

~j{ To solve the above equations we transpose appropriately, square, and add ~II Eq. (9.5) and Eq. (9.6) to obtain r,.: .:..: : : , ~?.

[\ By squaring Eq. (9.4) we obtain ~!}:.

~~-·.

l]: and substraction of the two above expressions yields I,•.•,•, V - v 1 = - h -vv-,- (J - cos0}. (9.7)

me I.-.·.

fi We can recast Eqo. ~(9:.•7 ) into twoX mIo:r(e: f~am:oili,aer) f orms: (a) to give the Wift in wavcleo~ sc:~•r:d (9.8)

I ~)

to ~ve ilie eo•:: of ::~::i~~o~:, : O)

(9.9)

~\ From Eq. (9.8) we see that the shift in wavelength. except for the angular ~:;:: dependence, is a constant., the Compton wavelength2 !~( -:-:-· h/mc = 2.42 x 10- 10 cm= 0.0242 A.

::::: >> A, ·.·.· For low-energy photons, with A 0.02 the Compton shift is very << A, ~} small, whereas for high-energy photons with A 0.02 the wave t:. Ienglh of the scattered radiation is always on the order of 0.02 A. the f : Compton wavelength. These conclusions can equally well be obtained from )\ Eq. (9 .9), where the energy shift increases when E Jm c 1 becomes large.

ff For E/mc2 >> 1. E' is independent of E and on the order of E' ~ mc2 • ft Hence ),.' = c / v' = c / ( E' / h) ,..,_, cJ ( mc 2 / h) = h / me as stated before.

/ As an example, in this laboratory gamma rays from 137 Cs are scattered f · = = from an aluminum target; since E 0.662 MeV, we have Ejmc2 1.29, fl = = so that backscattered gamma rays (0 180°) wiU have E' E/3.6, ~::: T_h_e_m_a-ss of the electron me was used in evaluating h / me; by using I.be mass of the ~._ l_:-: ;:::_j::_j:: - - . pion, or anolhe. particle, we obl.ain the pion C<~mpton wavelength, and so forth.

./;,-":-, ~~~ ~;: , ..

~} ::::::::::::@J }()[!@ 372 9 Scattering and Coincidence Experiments -:-:-:·:-:-:·=lli \}{t~i qui~e.}/I~~l which is less than 30o/o of their original energy. It thus becomes easy to observe the Compton energy shift as compared to X-ray scattering//}@~ where, ifwe. a.s sume)..= 2 A, D..)..j).. !),.E/E = 0.01. · ··::::::::::::=:W ,:-:-:-:-:-:•:~~ In the ongmal expenments Compton and bis collaborators observed}:/}:~ (especially for high Z materials) in addition to the frequency-shifted\\?}~@ X-rays, scattered radiation not shifted in frequency. The unshifted X-ray~)ii)}j are due to scattering from electrons that remained bound in the atom 3 : in this(()Jt~ {9.8)\/@f]

process the recoiling system is the entire atom, and we replace in Eq.

m by m A ( where m A ~ 2000 x A x me), resulting in an undetectabl~})/tfg wavelength shift, ~)..' ~ 1 o - 7 A. ·) {ff'* Next we are interested in the differential cross section for the scatter~(ii]l@ the//}W ing of the radiation. from th~ electrons. Cl~ssical~y this is ~iven by Thomson cross sect10~ which can be easily denved: consider a plane\ \}~ wave propag~tin~ in the. z _d~ec~on with the E vector linearly polarize~)iJI along the x directlon. This ts mc1dent on an electron of mass m, as showzt\ \{:~~ = = in Fig. 9.3. The electron will experience a force F eE eEo coswt~\\Ji -:\j:~ and its acceleration will be II e=o V cos wt.

::}}}f~ According to Eq. (8.27), the power radiated by this accelerated electron .(}Jt _.·)/}f; will be (nonrelativistically, in SI units)

ii/ll dP == - _::___!_V2 sin2 e, (9.10)

4 4 I/!I where is the angle ~~een ::::on of observation the vec- 0 : and E v, :)i/Jf tor of the incoming wave. Using the expression for we can write for )/)?-ft Eq. (9.10) averaged over one cycle · fl ~ 2 )\0Eicsin 2 e.

(~~) == ( e 4 n: Eomc 2 :)(:{?

Finally, from the definition of the cross section (see Section 8.2.1.a) we')\J!J .-\J~f: have u~::tli:m:t) · ene::i;::t:::~~;:~ ar:a ____:~ = 3 A similar situation is discussed in the following section on the M6ssbauer effect, where :i :)i~~~: :}[:f;:i the nucleus remains bound in the lattice and the recoiling system is the entire crystal. · 4 . 8 <j:-: -:-j;~.;. .; .. ; , See also Sect10n .2.5.

:::::;~x~ /!l~ . -/:~:~f:a -:-:-:.:m

## 9.2 Compton Scattering

Observer • eE v= FIGURE 9.3 Classical pictureoflhescatteringof electromagnetic radiation by an electron; this leads to the Thomson cross section.

Here the denominator is clearly given by the Poyotiog vector l/¥oo (/} = - = -E2 -€ocE 2 .

0 0 2 2 /J,O Thus we obtain da ( e2 )

dD. = 4n€omc2 sin2 e, (9.11)

where e2 ----=ro 4ncomc2 has dimensions oflength, and is referred to as the "classical electron radius"

::· -:• ro = 2.82 x 10-13 cm.

FinaJly, we average over all possible directions of polarization of the incom ing wave and use the angle 0 measured from the direction of propagation of the incident wave to obtain (1 0)

+ 2 da _ 2 cos dQ - ro 2 . (9.12)

' ' ; - . · .:- '.

. -:::::::;::::-:$½~ it!/}}~~ \:}({ff.:ffi 374 9 Scattering and Coincidence Experiments :))?fm@ croii\ffffl When integrated over all angles, Eq. (9.12) yields the Thomson ... ·----w .:-: :?::=:::::=:=:-~ : section fl ··:\(f = 3 Sn ' 02 · at {9.l~J..-.·.·.-.w..

·t\:}fJ@ _))!}1%.@ (This result was given without proof in Eq. (8.21).)

~~\)Jff.~ Several objections can be raised to the simple cross section given Eq. (9.12) or Eq. (9.13): (a) it does not depend on frequency, a fact #t:>ftt~@:?.

....... .,.,.z.-••..

supported by experiment; (b) the electron, even though free, is asswn~}lt=={~ ~~[!}ii~~ not to rec~l; (c) the treatment is nonrelativistic; and (d) qu~tum effects not taken into account. Indeed, the con-ectquantum-mecharucal calculatio_if:=:::~:}i:~ ._/i!i/i{l~I)

for Compton scattering yields the so called Klein-Nishina fonnula ')l/11 :~ = rJ l +~os2\ + y (1 cos0)]2 r2 o - cos 0) 2 ] ·::::::;:::;:~tt.=-;~a + ( ) , , 1 (9 .14):?:~::~~~::j X [ 1 + cos2 0 [1 + y (1 - cos 0)] \:/:::.;:~=?.:~ ·:::::})§Ji:f: where ro and 0 were defined previously, and y hv/mc2 . The crosi}J@.j~= gij section has been averaged over incoming ( and summed over outgoingl{@@ polarizations. By integrating Eq. (9.14), the total cross section can bt~(:)ff~ obtained. We will not give the complete result here, but the asymptoti~/?f/J \?/{tJ expressions have already been presented in Eq. (8.22).

.......· .·-·.·.·. .....

A comparison of the Thomson (Eq. (9.12)) and Klein-Nishina cros~})tfJ i~{{Jfi sections, including the results obtained in this laboratory for y ::::: 1.29, shown in Fig. 9.8. We remark that although the Thomson cross section i~}){{~~~~{ symmetric about 90°, the Klein-Nishina cross section is peaked forwar&i}@f factors/i@)J strongly as y increases. This is due to a great extent to kinematical associated with the Lorentz transformation fron1 the center of mass to tbe}?}}K: gamm~j\JJ{l laboratory~ note that the center-of-mass velocity of the (indicent + )ilJ ray free electron) system is }}}// = = V cfl cy/(1+ y), where as before y = hv/mc2 )!?~iii of. /' .i..J 't.,..{,,._~ The experimental data are in perfect agreement with the results ... ·--.. ..

Eqs. (9.9) and (9.14), which are among the most impressive and convincing;}Jff';_ .

.}\i~t 5See for instance F. Gross, Relativistic Quantum Mechanics and Field Theory, Section{Jt J .... ,.~. ......... • 10.5, Wtley, New York. 1993. _\ :=:=:::=~~'.

## 9.2 Compton Sc atte ring

successes of quantum theory. In the following two sections we will describe the experimental verification of these predictions.

9.2.2. The Compton Scattering Experiment As with any scattering experiment, the apparatus will consist of: ..

(a) The beam of incident particles, in this case photons, (b) The target ( containing the electrons from which the photons scatter), and ( c) The detector of the scattered photons.

The beam of photons is obtained by collimating the gamma radiation from a 137 Cs source. An intense source is required in order to get an appreciable counting rate for the scattered photons. As shown in Fig. 8.21 137Cs ( 137Ba) emits a gamma ray of energy 0.662 MeV, and the detection techniques have been discussed in Chapter 8. Figure 8.21 also shows the pulse-height spectrum of the gamma radiation from 137 Cs, as obtained with standard equipment; the same detection equipment is used in this experi ment with the only difference that heavy shielding is needed to prevent the detector from seeing the intense Cs source directly.

A schematic of the apparatus is shown in Fig. 9.4. The lead pig A is fixed and holds the source, which can be introduced through the vertical bole (V). Another lead shield B contains the detector and can be rotated about the center, where the target is located. The lead assemblies are rather heavy (approximately 100 lb) and some provisions must be taken for adequate mounting.

For the source, a 7-mCi 137 Cs sample was used, which was properly encapsulated before being shipped to the laboratory. It should always be transported in a lead containeri and when transferred into the lead pig A, it must be handled only by the attached string. The source holder (A) bas a collimator (h) drilled horizontally, subtending a solid angle on the order of 0.03 sr. Of interest to us will be the density of the photon beam at the target, and the expected value is

## 3.7 X JQJO X 0.-007 1 = l . ]04 h /

rr , 3 x p otons cm -s, 4 2 where we use a source-to-detector distance r 40 cm, for the data presen ted here.

376 9 Scattering and Coincidence Experiments 111 : ~ (a} i/i/111 '. 11:f <i/11 ,i!!ilil ?}}1f=i . ::;:::;:;::::~==~ ·./!!!!@@~ ,j, ........ ;W,: .- :•:• :•:• :·=·:·=·x=;-}.: .../ :/j~:~~ .:::::::::-:-:~~ >)~Ill (b)

Nal ;Target -- (c)

.·.·.·.·.·.·.·.·'W:· l11 --------- 1 Scattered )1 photons :•:-:.:,:.;,;.:@· ~ .. }){~Wi Beam .::::::::::~~~ Com··.·.p·,•½.;,•r_f.~:.j~: FIGURE 9.4 Schematic of an apparatus that can be used for measuring the w.,r?& 137cs scattering of gamma ~ays from differe~t tar~ets: (a) top view and (b) elevation.

N~,~;~,it~i detector can be rotated relative to the beam drrecuon, through a large angular range.

that a less heavily shielded detector assembly is possible, but care needs to be taken so the 137Cs source is not directly visible to the detector at foiward angles. (c) Use of a.:.iJ~t~:~ target when measuring Compton scattering at large angles. By such placement the scatt~®;~~ photons do not have to traverse very large amounts of the target material. · ":;:/J~ :, '.i//Kij /:}(~

## 9.2 Compton Sc atte ring '177

In contrast to the scattering of alpha particles, there is no need t-o enclose the beam and detector in vacuum or to use a very thin target. We know that gamma rays do not gradually lose energy when traversing matter as a charged particle does, but their interaction can be characterized by a mean free path. For the 137 Cs gamma ray we find that = = 1 4.7 cm in AI~ 1 0.92 cm in Pb; ').

cr4 this corresponds to 1 cm of air, so that the interaction of the photon beam in the air of lhe apparatus (approximately 100 cm) is indeed negligible.

Also, the target thickness can safely be a fraction of a mean free path before tbe probability for multiple interactions becomes considerable. Aluminum targets ½i n. thick are quite adequate for this experiment.

Some special mention must be made of the geometrical shape of the target. We may use a flat target (such as an aluminum plate), in which ::.:::: event the cross section is obtained by considering the interaction of the total beam with the number of electrons per square centimeter of the target6 ; alternatively, we may use a target of circular cross section (such as a rod), in which event the cross section is obtained by considering the interaction of the beam density (photons per square centimeter) with the total number of electrons in the target. 7 When using a plate, it is advisable to rotate . . it so that it always bisects the angle between beam and detector, since otherwise the scattered photons may have to traverse a very large amount of material before leaving the target (see Fig. 9.4c). In that case, however, the amount of scattering material in the beam path varies as 1/ cos(0 /2), and this correction must be applied to the yield of scattered particles. These · · effects are obviously eliminated when a target of circular cross section is . . used. In addition, the scattering point is better defined even if the beam is :::: only poorly collimated. On the other hand, accurate evaluation of the flux \ density at the target is difficult. The results presented here were obtained {· by using a¾ in.-diameter aluminum rod as the target.

::::. An interesting refinement of the technique is made by observing the ~/ recoil electrons in time coincidence with the scattered photon. However, ~\ the kinetic energy of the recoil electron is ~:::· ~ff y(l - 01 = I = COS )

Te E - E E------, ~-:·. 1 y(l - cos0)

E!~I~ -- 6s_e_eF-ig-. 8.1.

,-;.:, 7see Fig. 8.1.

~==:: E} ~--:::r : •.•.

378 9 Scattering and Coincidence Experiments which at its maxim.run value {0 180°) is T(electron) = 0.662 x (2.58/3.58) = 475 keV. ··\/:}}J~ . ./ :::::::t:::i:fr~~ f~f The range of such an electron in aluminum is only 15? mg/cm (see,.

example, Feather's rule, Chapter 8, Eq. (8.15)), which corresponds .td:::::=:=:=:m cm. the casei{}}~ appr~ximately 0.06 Thus, rec~il electr~ns ~ill: in a~ost all tfy~tti stop m the target. On the other hand, 1f a plastic scintillator 1s used as Wi target, and is viewed with a photmnultiplier, the recoil electrons do prod~p~Jf ?{/}~~ft a signal that can be easily detected. Ii~ collln?_~tf . As mentioned before_, the _detection system consiste? of. a c1al Nal detector. The dunens1ons of the crystal were 3 m. dtameter.~f/§~ 3 in. thick. Data was acquired \vi.th a multichannel analyzer, with a G~Jlt~~~~ sp:¢~@t}j interface to a laptop computer. Figure 9 .5 shows typical pulse-height wi~J~:~lf~ tra, t~en at two different ~cattering angles (30° and 100°~, and ~tt~J@ aluminum target rod both m and out of the beam, but with all s.·.Thff ~ c?nditions otherwise identical: Each spectrum w~s acquired for 120 difference between the target 1D and out spectra 1s also plotted. ::;·://{~~~ By measuring the pulse-height distribution at various angles, we o~~jf~~~ ~f:~{J~ the energy of the scattered photons as it is given by the position of the don~ pro~@il topeak. This is most easily by a simple Gaussian peak-fitting to the photopeak as observed 1n the "background subtracted" spectra~.:f.®:::::::~ ~ exam~le, in the lower plots of Fi~. 9.5. Arudimen~i but quite s~cf§!f@~ Gaussian peak fit can be done m MATLAB by taking the loganthi#.},}t:~: secQnjftti the net counts in the region of the photopeak, and fitting these to a J~ order polynomial. To obtain the yield of scattered photons, we integrat( @f counts correction in the photopeak only and apply a for the ''photofrac~tj~\j~, co~tf1@ffi or "peak-to-total ratio" ~swell as for crystal efficiency. Th~se depend on the crystal sIZe and on the photon energy (which vanes~$.:}:~ spe~fff~ ~gle). Figure 9.6 gives the peak-to-total ratio (for de~ectors at a )&.

fun~~9Jf/f~ distance from the photon source) and the detector efficiency, as a :@JI of energy for several different NaI crystal dimensions. '. : :}/(JiJ~ 9.2.3. Results and Discussion · appaw:a . ,·.·.·.· . ..·. -.-~ The r~nlti: presented_ belo~ "'.ere obtained by students using the descnbed 1n the previous sectlon. .?:::i:i:Jffi a~-:-:·:l-:-i:~t--r- --~ From Efficiency Calculations for Selected Sci1ttillators, Bicron Corporation, <}}Jj~ from the online library at http://www.bicron.com. . :;(~1 }.

## 9.2 Compton Scattering

(a) 5000 .•.

4000 0 •• 3500 0 <> (I)

3000 • C: ::, 0 2000 500 • ,· 0 1000 2000 3000 4000 5000 Channel (b) 1100 ..

•• 900 • •=Target in 800 <>= Target out 11=100° f: 700 ' (I)

•.• ::: (\I 600 ::: ~ • . • • :• . ::, 500 • :::· 8 (~ 400 :::: 300 .·.· .;.: :-:,· 200 -:-: (!

~t·.

:~=:~ 1000 2000 3000 4000 5000 ;;::;: Channel ;-.•.

~::~: ~::: FIGURE 9.5 Pulse-height spectrum gamma rays in the Compton scattering appararus.

~/ : The plots (a) (b) show data acquired for 120 s both with the target rod in (solid points)

,-. +. 1 = ~::=::: aod oul (open circles) of the beam. At 0 30°, the detector intercepts some fraction of [? = the primary beam, and the rare is considerably larger than at 0 100". In addition, there ~f· are large signals due to K-shell X-rays artd Compton backscattering in the lead shielding ~ ~ ; ~ ::: - a1 both scauering angles. However, in ' each case, these background signals subtract cleanly tf away, leaving a pure Cornpton scattering signal from the aluminum target. The subtracted if: plots are shown in (c) and (d).

~. :if ~: ~t( ~:-.

,/',.".· ---~==-: ::::-: ~:;::: ~~:::.

,..;:::: ~~~:(: Ii!il 380 9 Scattering and Coincidence Experiments -::::::::::::::::j,f-:W -: :111111111 rntd (c} 800 0=3001 subtracted 600 -il:/111!11 (/)

!//ill !!

O 0114---10-'-0-0 _ _ 200__.__0 __3_ ._000_ __4. . 0...0 _0....!.Jllll!IUil5.000 Channel (d)

700 0=100° • ' •• ,I ,I~ ,l' -. 'ti'.

11111 : ,+ + ::/Itt&~!

fi + .·.·.·.·.·.·-·-~--- ~ 400 · ~,t 8 ::: 1\~,~ t :, 0 i...",:.. .....:___ _.___ _ _ .J-- '+ _ . _~ ~.:sJIW~~~~. ....

0 1000 2000 3000 4000 5000 Ch FIGURE 9.

Before beginning measurements of Compton scattering, it is worthwl co™~i]~j to ~easure the beam profile ~f ~e Cs som:ce. This is best done by s~,~J~ mating the detector and p~tnng 1t at a large d1stan~ from _the s~urce, ~m/f$= to keep the ~ount 1:ate relatively lo~- (A numb~r of d1fficu~t1es ~se at a.

th~:~~/~ count rate, mclud1ng severe dead bme corrections and gain shifts, but mo~,mij@iI~I are negligible if the total rate is less than several kilohertz.) Then by the detector through different angles, one can map out the ,~shape" of -:-:-:-:-=~1 JI ?))Ji

## 9.2 Compton Scattering

a.

Figure o.a Source dislonce 60 crn 0.7 0.6 , 0.5 asi .x 0.4 > (II 0.3 0.2 0.1 0-1--~-~-~-~-~---1 ·,• ::: 0 0.5 1.0 1.5 2.0 2.5 3.0 Energy (MeV)

,• : ; ,: : , 10 9 0 0 o % /o I . \ \ " \ \~, ' 'Z \ : '. \ ~ \' '\ \ ' ' '\ - ~ - N I , . _ ' " --- - I 6 1 1n 1 ~- : e C 0 . ; - 8 7 0 0 % % ·1----- \ \ \ \ ''. . \ ,.\ \ ' 1\1 ' ' " "- ' ~ --..J l 3 i~ ) <In : ,: , . . 0 , 60¾ . . \ · ' 'i....._2k • .

-D 50% \~ ' . ' OJ \ \ . . ~ I I d i: ) : ~0% I ... . ... . .

\\ ' C Q ~ L ) . 30% -3\~ \ l ' '. r-... ,~, ~ . .._ !In.

' - 3181n.

~~ ~ 20¾ f-'~ """" , mm "2":"' I ' '-~ ,,~ -.. ... ~- .. .

10% I - •• • II ' \ t-,..._.. ........ ~ T"'"- 0% 10 100 1000 10000 Energy (keV)

f1GURE 9.6 Detection efficiency plots for Na! crystals of various dimensions, from ·::. http://WWW.bicron.com. Shown are the peak-t~total ratio and the inoiosic absorption { efficiency. aU as a function of energy for various crystal dimensions.

~;:- f',', "···· ";-•:' :,• photon beam. For our measurements here, however, we will simply assume .....

:::: the calculated beam flux for a measurement of the differential cross section.

:-:- • ~ . : . : . Compton scattering data arc taken by accumulating pulse-height spectra .....

:::: at various angles, bolh with the target in and out, for fixed pe1iods of ti.mes.

•·.· .-.· ::::: In order to minimize the effects of gain drifts, and other changes over •...

.•.- ....· , longer times, it is best to take the "in" and ''out" spectra immediaiely -:.:, :::·:: . .-• ..••. .

••··· I( •:-:- ~~t ;.:...;.

382 9 Scattering and Coincidence Experiments TABLE 9.1 Summary of Compton Scattering Data Angle Peak Counts Counts Peak/total 0 channel (in) (out) E' (MeV) ratio Efficiency (lo-27 cm2/~r)j{{f:: ( )

20 4300 528,161 508,714 0.614 0.47 0.865 55.2 .

30 3732 97.663 81,121 0.564 0.50 0.890 42.9 40 3384 29,856 14,566 0.508 0.53 0.930 35.8 60 2810 16,382 5062 0.402 0.57 0.960 23.9 80 2258 16.268 6251 0.320 0.65 0.990 18.0 100 1922 17,482 7632 0.263 0.72 0.999 15.8 Note. Each spectrum was acquired for 120 s.

·-y{)~j arf)$.~ one after the other. (For example, see Fig. 9.5.) Data taken by students summarized in Tab~e 9 .1. In this table, E' is the photon ~ergy ~s c8!-c~at~~i}j~ from Eq. (9.9), and 1s used to look up the peak-to-total ratio and themtnnst¢.}:~:~ • • :-:-:-:-:-=x· effic1ency from Fig. 9.6. ..:.\.::.::.f..:;.:.: ~ :,.: Radioactive sources are used to calibrate the analyzer channel in tem&.\1i re . f ;·. ·J.·.·i-·%~,/"~ of photon energy. (See Fig. 8.24 and the associated text. It is advisable dataf /Jt carry out a calibration both before and after taking Compton scattering in order to check for gain shifts.) In this experimen4 it was determined thati\:}f /?ii~ Energy 0.1527 x Channel - 34.96. · .}}ii} !{} ~t Then, using the photopeak values summarized in Table 9. I, we detennin~(:\f:~ the{JJ.

the scattered photon energy E1 In Fig. 9.7, we plot the inverse of • ...... ..

measured photon energy, 1 / E', against ( 1 - cos 0). According to Eq. (9 .9)/ / f~ a straight line should be obtained, since . )/if.}.

.)ifJ!

-1 - -1 = 1 .

-(1- cos0). -:·:-:-:-:-: }\}j E' E mc2 is 1/mc2 rui(/j This indeed the result, and the slope of the line gives with \\I~ intercept at 1/E . From a least-squares fit we obtain .

·:?i~ 2 = ± mc 505 12 keV }@1.

in very good agreement with the known value of the electron mass. W~)l thus conclude that Eq. (9 .9) is very well verified and that our explanatio.ti)~ . ·.·.·.-.½ of the Compton frequency shift is firmly supported by these data. .}\ ~ We next turn to the evaluation of the differential cross section. A~??:: ,·,-.1.l,~ explained before, we integrate the counts under the photopeak. The result~/§ -:.:-:.-:

## 9.2 Compton Scattering

4..5 Slope=1.98 Mev-1 3_5 > I 3 11)

LU 2.5 ..- 1.5 0 0.2 0.4 0.6 O.B 1.2 1-cosa FIGURE 9_7 The results obtained for the energy (frequency shift) of lheCompton scattered gamma rays. Note that 1/ Eis plotted against (1 - cos 0), leading to a linear dependence.

The slope of the line gives the mass of the electron.

are also summarized in Table 9 .1. To obtain the cross section we note that da yield dQ - (dO.)N Io .

The detector solid angle is given by crystal area _ dQ = = 6.4 x 10 2 sr, r 2 where9 = = = d diameter of target ¾i n. 1. 91 cm = = h height of target 4 cm The height of the target is obtained by estimating the length of target intercepted by the beam.

.:·:.:·:.:·:.·:.:·:·::~;~b ::: :::::::::: . ·,:.:-:-:-:--: 384 9 Scattering and Coincidence Experiments - _ . .: . - ·. : · , . :- · : . . - ·~. ·· . = .· ·.· .] lillll p = density of aluminum= 2.7 gm/cm3 No= Avogadro's number= 6 x 10 }II A atomic weight of aluminum 27 = = -:-:-:•:•:•:•:·1 Z atomic number of aluminum 13, \::::::::=1 .\{/\~~ thus .·.·.·.·.·.-~ JJ!II N 8.9 x loZA electrons.

val1~tt For Io, the flux density at the target, we use the previously obtained = 4 2 Io 1.3 x 10 photons/cm -s, :/{]~ . :•:•:•:-'.•:•:-:$ ·:\)j~ and the data acquisition time for each spectrum is 120 s, so that finally .)..{../.i.l.~ l = _ da corrected yield dQ (6.4 X J0-2) X (8.9 X 1024 ) X (1.3 X 104) X (120)

···<JfJ~I corrected yield - 29 • ·.·.·.·.·.·.·.··~ \/??~

## 8.89 10

Tbe values of the differential cross section obtained in this fashion·~,rn, ?-!f,l!JI given in Table 9.1, and are also plotted in Fig. 9.8. The solid line in Fig. .

. ·:::t/~~1 .:}::::=:\m .:::::::;::::::~ BO !!111 70 :ii: :·::\\::::{~: ...

....... 60 ) )}J:mw~ ti)

~5 ··>·:·•:-·:·-:-·:.·;:iw'"/--9.·= 50 :>::::::::::~::~ ,-..

C -6\I ;/){@~i .,..

•:•:-:•:•:•:•:&- ._ :)}{1®~ ti }\t~WJ; "5 20 .·.·.·.·.·.·:w.· ::::::?Ii®: 10 ···:-'.·:-'.·:-:·Z·w· .: .:?J@fi \::::=:::~::~: O O 20 40 60 80 100 120 140 160 180 .

·)({j~ Scattering angle 0 ...· .,.~·- ·.·.·.·.·.- garnrna:#.ff@~1~~j\ FIGURE 9.8 The results obtained for the scattering cross section of Cs fo~}~!f as a _function of angle. The so~d ~e is the prediction of the _Klein-Nishina fonnula ·:::\:\:\:J:*l~: parucular energy; the dotted hoe 1s the Thomson cross section.

\)t~~fii :HJ@~~~ )!JI r.·.

~-:-: t:::.

1::_ 9.3 MOssbauer Effect 385 ~:~: ?(~ gives the theoretical values for da /dQ derived from the Klein-Nishina · · formula (Eq. (9.14)) for y 1.29, while the dashed curve represents the \\ Thomson cross section.

~} The agreement of the angular dependence of the experimental points :-:- with the theoretical curve is indeed quite good and clearly indicates the / inadequacy of the Thomson cross section for the description of the scatter / ing of high-energy photons, while confirming the Klein- Nishina fonnula.

f( On the other hand the absolute value of the experimental cross section is { : subject to some uncertainty due to the way in which the flux density Jo and [~{ total number of electrons N were estimated Nevertheless, the agreement / .. is good.

,~.~:·~.

(r".."·..

f · 9.3. MOSS BAUER EFFECT -:•:- ~:::.

V 9.3.1. General Considerations ::::: v.

,.,.

~\ . In the Compton scattering experiment, we could visualize the scattering f .· process as if it were a collision of two billiard balls in which the incom- f'r> .

ing photon maintained its identity but suffered a change in momentum t\> and energy. The phenomenon of scattering can, however. also be visu alized as the absorption by the target of quanta of the incoming beam, \( with the subsequent re-emission of these quanta; this was the model { we used in the derivation of the Thomson scattering cross section in :-:-. Section 9. 2.

Since we know that emission of quanta of energy h(vp - vCi) in the visible spectrum is due to transitions of atoms from a state of f3 -+ a we must also expect that when q~anta of this energy h(vp - v(l!) are incident · · on an atomic system in state ct, they may be strongly absorbed, with the consequent raising of the atom from state a to state /J. Evidence for such strong absorption is obtained by detecting radiation of frequency ( vp - Va)

. emitted from the absorber in all directions; it is due to the atoms that, ( having absorbed a quantum from the beam, were raised to state fJ and then \ underwent a spontaneous transition back to state a, emitting the quantum ( h(v13 - Va), but with equaJ probability into all directions. Such radiation ( is called "resonance radiation., and was first observed by R. W. Wood in \:: sodium vapor in 1904. A SGhematic of the apparatus is shown in Fig. 9.9.

\: An absorption cell was illuminated by sodium light, and at right angles to ]: the incident beam the sodium D lines were observed.

. :::::::;::::::~ 386 9 Scattering and Coincidence Experiments ii 1 j . ·:::::::::=:=:=i~ Resonance radiation ~ tT o spectrogra ~eommau,or detector , -~ 5890A __ Prlmaty beam .)//i!)~J~ . ·.·.·.·.·...-.·,@ Na lamp ce .. ::;:;:::;::'.;:~:;~0 ::::::::::::::fi:: (Na vapor} · experici~~fJI!@ FIGURE 9.9 The arrangement of an optical (atomic) resonance radiation Here the socliui:11 D lines are inci?e~t on a cell containing sodium vapor; i~ ~s then possib~fj~~ ::}\ti~ to observe, at nght angles to the mc1dent beam, the appearance of the D lines.

..} (J®, Let us note two facts: (1) Since the atom must bein state a when tberacU/@]$.

the incid~#(IJ~ ati~n i_s inciden~ a is usually the ground state of atom. 10 (2) The energy correspondiiiJJ@I@ rad1at10n mus_t be exactly of the correct h(v~ - Va)

to the separatton of levels a and /J. .·:{:\:}?::£.

now u~t,:$.J/ffil If we try to obs~rve in a similar m~ner res~nance radi~tion, a nuclear gamma ray (mstead of the sod1um D lines)~ we will obtai~;J'f?.:{j momen~/if@ negative result. This is a simple consequence of energy and conservation, which produces a negligible effect in the case of an ato~~(@lffi line. To understand this, consider a system R originally at rest; R underg~~:}~:J~ mi@ a trans_ition from fJ -+ a' where the energy difference between states)( 1/ /f and /3 is . , - < l~l::::~::::~=~ E13 - Ea - hv. (9.

<::::::::::=:::~».

As a result of the transition, a quantum is emitted, which will carry aw~{J@ momentum energy hve and hve/c; is to be determined. From Fig. 9.H1a}({:~ Ve w.~W,{jj we see that to conserve momentum, the emitting system R must recoil momentum h Ve/ c; therefore it will have energy (nonrelativistically) · ::}))ft . ·.)})tj l6fJ:J ER= (hve)2. (9· \ /ill 2mc2 an~::#.@]

°:111e available intensities of visible radiation, the absorp?on cross section, density of the absorbers are all such that most of the atoms 10 the cell must be able: ~ft:: ;t:~ cas~.:li]

absorb (and re-emit) radiation in order to yield ~bservable results. In very special o~e.t?~f metastable state, to which a large fraction of the atoms can be transferred (by some .·. ·.·.·.·...-. :-: means), can serve as state a.. .· :::::::::::~~~;: II

## 9.3 M OS·S b au er Effect

--~=O0 hv/c (a) (b)

FIGURE 9.10 The effect of momentum conservation (recoil effects) in the emission and absorption of nuclear gamma rays. (a) A system R originally at rest emits a gamma ray hv; it must recoil with a velocity VJ (hv/c)fmR, (b) A system R moving originally with a velocity Vi (hv/c)/mR absorbs a gamma ray hv; after lhe absorption the system wi11 be at rest. (c) Derivation of the first-order Doppler shift for an observer moving wilh velocity v.

To balance energy, we must have ER +hve hv, leading to (9.17)

where x = h v /2mc 2 will generally be small.

Similarly for a system R' originally at rest in order to be raised from level a-+ /3) where Ep - Ea = hv, it must absorb a quantum of energy = + 2 + · · · ).

hve hv(1 x - 2x (9.18)

If the emitted quanta were strictly monochromatic, then it is clearly not possible for a free system R to absorb a quantum hve emitted by a similar free system R', since hva i= hve (Fig. 9.1 la).

We know, however, that spectral lines have a certain width11 Liv; in Fig. 9.llb the emission and absorption lines are shown appropriately cen tered about hve and hu but with a width ~v. ff then the two line shapes 8, overlap, it is possible to have resonant absorption.

llThe minimum or "natural width" of a tine is determined from the lifetime r of the transition f3 ~ o:; from the uncertainty principle 6.E~l ~ h. and thus 6.v ~ 1/r. Other contributions include the "Doppler broadeoing0 due to the thermaJ motion of the atom or nucleus, co1lisions, external perturbations. or imperfections in a crystal lattice.

388 9 Scattering and Coincidence Experiments 1---2ER.....,_l I I hv Overlap (a) (b)

FIGURE 9.11 Indication of the energy shift of an emitted or absorbed gamma ray due .to}}!:~~ the tecoil of the nucleus. (a) The situation when the line width is very narrow in comparistif}j to the recoil energy; no resonant absorption can then take place under normal conditio~J} ):~~ . ·.·.·.·.·.·,,.,.".I thaf<::=:~; (b) The situation when the line width is on the same order as the recoil energy; note ~t\J >;)

resonance absorption can now tslce place and it will be proportional to the convolution fue ~o line shopes.

This is true for atomic systems: here h v ~ 2 e V, and for hydrogen}/~; nu?~ 109 eV; thusx ~ 10-9 . The width of atomic spectra lines, however/ )}~ is on the order of tlv/v ~ 10- 6 . Thus }j~ Ill ~ ~ .6.v 10-6 ) >> ( hv 10-9 ).

( v 2mc2 .·.-.·.·.· nuclear eV; general, nucleaJ!l////j For gamma rays, hv ""' lif-106 also, in lifetimes are longer than those for atomic systems, so that }} tlv 10-10 10-1s }} -,-...,;; - .. :<-:-: u 0 ·>>:· Thus we see, in contrast to the situation for atomic systems, 12 that :?

~ ~ 10-1), 10-10) }!

« (~: ( ~v making resonance radiation impossible. ifif/ :e In the preceding discussion we assumed the that the emitting and absorb- ing nuclei were at rest. We could, on the other hand, think of imparting to the / absorbing nucleus (by some means) enough velocity in a direction opposite./ to that of the quantum (Fig. 9.10b) so as to satisfy Eqs. (9.17) and (9.18). }[ 12 For example if,; ~ 10- 9 s, then ~ER: 6 x 10- 7 eV. Further, nuclear gamma rays )

are subject to broadening influences much less th.an atomic lines. : :

## 9.3 Massbauer Effect

For example, if h v ~ I 04 e V, and the nucleus has A ~ l 00, and we wish that hv -=mu hvc = (mc ' - ) )v (9. I 9)

we find for the velocity = 3 X 1010 X 1 i f = a3 ..

v 3 x 1 cm/s.

I 0 Ox 109 Such velocities can be obtained in the laboratory by p]acing the samples on the rim of a centrifuge and orienting the incoming beam toward one of the tangents. It then becomes possible to observe nuclear resonant absorption.

Nuclear resonant absorption would also occur if both the emitter and absorber were so massive that momentum could be balanced with negligible energy being given to the recoiling system, that is, if the denominator min Eq. (9 .16) became infinite. Indeed~R . Mossbauer showed in 1958 that for atoms bound in a crystal lattice, a nucJeus does not recoil inclividually13 but the momentum of the nuclear gamma ray is shared by the entire crystal.

This can be understood if we consider that the binding energies of the atoms in a lattice site are on the order of 10 e V, whereas the recoil energies, given by Eq. (9. J 6), are always less than 1 e V.

Since, however, the nucleus is now part of a larger quantum-mechanical system, there exists the possibility that the energy available from the de excitation of the nucleus f3 a might not all be given to the gamma ray, but might be shared between the gamma ray and the lattice, in the form of vibrational energy. Lattice vibrations-the so-called emission of phonons-are a quantized process. and the lowest energy phonon that a single nucleus can emit ha~ E kT, where T 0n is a characteristic temperature for the crystal, the Debye temperature. Thus, if the recoil energy of the free nucleus, as given by Eq. (9 .16), is £ n < k0o, it is not possible for the lattice to become excited into a vibrational mode, and the total energy of the transition is taken by 13 It is cai.tomary to say that "the nucleus does not always recoil individually." in order to account for the instances where the nucleus transfers energy to the lattice as explained in the foHowing paragraph.

:11111 9 S catte ring and Coincidence Experiments : the gamma ray. The probability of recoilless emission of the gamma ray-~ \{f{f then given by ):{\{:t (-t~) , f exp (9.20} ~- - Equation (9.20) holds at absolute zero, and for finite temperatures we !/!ii//!//111 1:1 f exp ( - (~:)). . (9.21)

Here l/i2 = (2rrv/c)2 is the square of the wave number of the emit-. /\Ii~ ··:rm}~~ ted gamma ray and {x2 is the mean square deviation of the atoms from .)\\f their equilibrium position and is proportional to T. As an example, for the 57 ...... .

:)}?::~: 14.4-keV line of Fe, , .

ER= 0.002eV and E>o 490 K; hence = = f e- 0.08 92%.

:::::::;:~:: We therefore see that in certain materials ( 57 Fe being the most suitable) the Mossbauer conditions are met; recoilless emission and absorption can take 1 place, and consequently nuclear resonance radiation can be observed. 1 It has been explained earlier (Eq. (9.19)) that we could compensate for 111 .•,·.-..........

the recoil of the nucleus by moving the absomer in a direction opposite ::::::::::: .-.·.·,.-...

to the incoming gamma ray (s o as to make the total momentum of the ·if!{ nucleus-plus-gamma-ray system zero). It follows then that if the absorption .:,:,:. .: •: is recoilless, such motion of the absorber would destroy the resonance ,, ·.

."

.: -- ~i condition. In recoilless emission (absorption) the gamma ray has energy I Ey h vo in the system, which is at rest with respect to the nucleus; if the nucleus is moving in the laboratory with a velocity v in the direction of ·.·.- ..... _ the gamma ray, the laboratory energy of the gamma ray E~ is given by a ;,::::;.:: ··;:::::: ::::::~; Lorentz transformation ):~~~ , 1 1+,8 = + = :{:t Ey - J --; i ::: : - :== 13 = 2 ; :(Ey vpy) Ey-.;/:1:: =-::: f ; 3 : 2 :~ '<. . - . .:=- - .. : .- - = .. ..~ . . .

?I where /J = v / c. For f3 << 1 we obtain to first order :::::::: .-::::-;:' . ·.·..r l:l.E = E~ - Ey = /3 Ey or - l:l.E - -/3--- V , : :: : : = : = ~ ~~ E C ::::: ·.:~* ·.·r :<-~ <::::~ ·:i:t ::·;.·:.,~;•: .·,:.:i ,·:-:- 9. 3 M lS s s b a u e r Ef f e ct 391 Thin ...

absorber Source ~ 100 G)

Detector C.

\ Counter ·0w 90 D{]

II)

"' I- -1 -2 0 1 2 ~ Velocity (mrn/s)

(a) {b)

Overtep region Emllled line depends on source velocity

## I 0 V

Absorber line (c)

FIGURE 9.12 The Mossbauer resonant a.bsorptioo experimenL (a) Diagramroo.t:ic view of the equipment. {b) The probability for transmission of a gamma ray as a function of the source (or absorber) velocity when no hyperfine structure is present. (c) The width of the transmission cl.lf'Ve is a combjnation of the shape of both the source arid absorber lines.

which, written as .6. v/v = v/c, is the first-order Doppler shift of a wave emitted (absorbed) by a moving observer (Fig. 9.10c). To obtain a quan titative estimate we consider again the 14.4-keV line of 57Fe, which has a lifetime -r ,.._, 10- 7 sand hence llv/v 4.5 x 10-13 . Thus, velocities on the order of v c(.6.v/-v) ,.._, l.5 x 10-2 cm/swill be sufficient to destroy the resonant absorption. Such velocities are easy to achieve and control in the laboratory. We therefore measure the transmission of the 14.4-keV gamma ray through an 57 Fe absorber as a function of its velocity.

Alternatively we can leave the absorber stationary and move the source.

A possible experimental arrangement, indicated in Fig. 9.12~ consists of an 57 Fe source, an 57 Fe absorber that can be moved at a constant veloc ity, 14 and a detector for the 14.4-keV gamma rays; we measure the rate of transmitted gamma rays. At zero velocity the transmission is low because of 4-rhe velocity, however, is varied in the course of the experimenL 111111 9 Scattering and Coincidence Experiments tj resonant absorption; as the velocity of the absorber is increased, howeve~{ j@ typi8)\J:iJ.: the resonance is destroyed and the transmission increases, leading to a rayj}!)ff~~ cal curve as shown in Fig. 9 .12b. We may think of the incoming gamma ......... ,. ... .r.

as scanning over the absorption line as a func.,1:ion of the velo_city, and there{\}Jjt linel\rt:tr fore the observed absorption is a measure of the convolution of the two .·.·.·.·.·.~. .- .·.·,J" ..· as shown in Fig. 9. l 2c. In this way we "trace out'' the natural line width fo}i{:}f~:!

... ' .... ·...-%· i/)tr~r this nuclear gan1ma ray, and measure energy deviations of one part in 1013 i~:{/f@J (v ~ 0.06 mm/s}. This represents a highly precise measurement and this why the Mossbauer effect is an important tool in many physics applications~})}~j:3 9.3.2. The Apparatus and Some Experimental Considerations In this laboratory the Mossbauer effect was observed using the 14.4-keV) )Jll~ 57 57 gamma ray of Fe, which follows the decay, by electron capture, of Co//}~~~~~ ))f{~f (see Fig. 9 .13). Basically the apparatus required for the experiment consists· \?J~?{: of (Fig. 9.12) (1) the source (with or without appropriate collimation), (2) ........ .

\' )ff]

the absorber and a mechanism for moving the absorber or the source at constant speed, and (3) the detector for the 14.4-keV gamma ray. From··} ?~~{?

Fig. 9.13 we note that·the 14.4--keV line of interest will be accompanied) }/{} by a 122-keV gamma ray as well as by a weaker 136-keV line. There is ))\~}: 57 ){{/?

also a strong background present from the 6.5-keV X-ray of Co, which ·}\ff follows the electron capture from the K shell. The source used was 1 mCi.

if 57 15 of Co plated and annealed onto an ordinary iron backing. :)))

The detector is chosen so as to provide good efficiency and discrimina~ ··)/J} tion for the 14.4-keV gamma ray. A xenon-methane proportional counter, \ )/{ )/lf followed by a single-channel discriminator, was used. In Fig. 9 .14, curve (a) .

gives the pulse-height spectrum of the gamma rays emitted by the source, · :}\/~ while curve (b) gives the same spectrum after the gamma rays have tra- \?}{ versed a 0.001 in. absorber. The shaded area represents the "window'' )}f?

{@fi selected on the discriminator, so that only gamma rays within these energy limits were recorded by the scaler. :{~{t: . ·~-.~,.. . .... · The absorber in this case is usually a thin steel foil, but it should not }/ ~§ { exceed 0.001 in., since oonresonant scattering increases so much as to \\~{ }ff smear out the 14.4-keV line. Further, natural iron contains only 2.17% /}if of 57Fe, so that poor signal-to-noise ratios result It is possible, however, ····~---· Purchased from Nuclear Science and Engineering Co. • P.O. Box 1091, Pittsburgh, PA.

## 9.3 Milssbauer Effect

Elewon eapllffll 0.136MeV 9% 0.122 MaV 91% -1------.......- - O.Ol4S7MeV ,12--~------ r=1.4X10_, s Fe61 FIGURE 9.13 The energy-level diagram of the 57Fe nuc:leus.

- No absotber - - - With absorber jjj c:: c:: al 260 .c.

(J c:: 200 ::, C: 150 · 0 ;; ; -I Wiruk,w .!/I II) .

~ , i= I I . (al 50 - '_r - ' '--, __ ___ ..,. , (b 0 5 10 15 20 25 30 35 Channel number FIGURE 9.14 Pulse-height spectrum of the low-energy gamma rays of Fe as obtained with a proportional coaoter. The solid curve has been taken without the absorber in place, whereas the dashed one has been taken with the absorber in pince. The shaded region indicates lhe discrirrunator window used for observing the Mllssbauer effect.

to obtain absorber samples enriched in 57Fe, and in the present experiment, such a foil (of 1 cm2 area) was used; the 57Fe concentration was 91.2% and the thickness 1.9 mg/cm2 (approximately 0.0001 in.).

The motion of the absorber can be achieved either by purely mechanical arrangements, or by a transducer of some type. Examples in the former ) iiiilt 11111 9 Sc a tte ri n g,._..a_n_d_C_o_i_n_c_id_ e_n_c_e-Ex_p_e_r_i_m_e_n-ts----~~~4-- · :)

1A SOK 3.9K 20K HeUpot 1K 3900 0---~11.+.G..V., ._._ _... __.. ...,__ __ _,. _100_n __.__.JI'-____ __, 5K 5K ·::/IM§ the){~Wt FIGURE 9. 15 An amplifier circuit capable of driving a speaker coil for use in Mossbauer experiment. · ::::::;:~~·:~·· .\i!JJl!It category are a plunger driven by an appropriately shaped cam (logarithmic\/J/JlJf spiral r === k0) or the rim of a wheel rotating about an axis that is not:}}\~/ normal to the surface of the wheel. In all cases of mechanical motion,,.-/}~1{ special attention must be paid to decoupling the vibrations of the driving)({lJ motor from the absorber. ·.:/:=::?:=~· chosen,:\j}f For the present experiment, a device of the latter category was ...... .....

namely, a loudspeaker driven by a sawtooth current (see Fig. 9.15). The/ {f}~t source was mounted on the core of the speaker and the absorber was kept}(@/ )\f/ stationary. The driving waveform was obtained from the horizontal sweep .\\l} of an oscilloscope after amplification.

To calibrate the speaker, a micrometer screw was mounted in a special·?}~/ :}i@ manner above the speaker. By listening, the experimenter coul~ discern when the screw touched the speak.er, giving results to within ±0.003 cm }f§f \fJ J out of a maximum travel of 0.2 cm. Assuming that the speaker is linear small'/i§f with current, the calibration shown in Fig. 9.16 was obtained. The variation in solid angle with the change of source-detector distance does) )~~{: \J.@l not affect the results obtained. It is also advisable to gate the scalers s~ :ft~@ as to count only during the linear part of the motion (and in the desired . ) ' .. ......

. 'II~ direct ion -=-=·=···=····· -:::;;::-;~ 9. 3 Moss b a u er Ef f e ct 395

## 3.5 .-----,------,-- --...--- - ---,------,

3 Speaker caJibrallon

## 0.274 cm/100 mA

-e o 2.5 gi 'g 2 ...

1Qu)

1.5 0.5 o------~--- ~--~--~ 0 100 200 300 400 500 Current to speaker (mA)

FIGURE 9.16 Velocity calibration of the speaker used to provide the motion of the source in the Mossbauer experiment.

9.3.3. Results and Discussion In Fig. 9.17 the results obtained by a student are given~ the abscissa gives the velocity of the source in millimeters per second, and the ordinate, the counting rate at the detector. It is clear that maximum absorption occurs at zero velocity, in accordance with the hypothesis of recoilless emission ( and absorption) of the gamma ray and the conclusions reached in the previous sections.

The full-width at half-maximum for the zero-velocity peak as obtained from Fig. 9.17 is rapp 0.70 mm/s. If the two curves shown in Fig. 9.12c are assumed to have a Lorentzian shape, then the apparent width app can be related to the true line width through r = + f'app/ 2.00 tenn correcting for absorber thickness.

Thus we find that r(14.4 keV) ~ 0.30 mm/s ·and L\v ~ o-12 -=-,..,_,l ' V C :-:-:....-,...:. ..: •: )}ff .·::::::;::::::: 396 9 Scattering and Coincidence Experiments l illi!ll ·-:-:.:~•:•:•: i/~~~~~\~~: /It\ 200 · :\JI\ t~ 1 aa ____ :::i~:: l 60 .....___.___ -------· ~tm ·w -~ 140 11)

eC: 80 ,___ __ __,_ ____ .__ ___. .....__~____.'--___ _, 0 2 4 6 8 10 Velocity (mm/s)

FIGURE 9.17 Results obtained for the Mossbauer effect of 57Fe using a 57Co source on .-):};~:;:;?1,~ ordinary fron backing, and an enriched 57Fe absorber. · :(f{t}~ !I ;~c~~~/n fair agreement with fue accepted value of ~v/v It is clear that in Fig. 9 .17. apart from the zero-velocity peak, there alsc((\J)J appear subsidiary peaks at v 2.5, 5.5, and possibly also 7.5 mrn/s. What}{i\~f?

is the origin of these peaks, so reminiscent of the hyperfine structure o({}(fff .·.·.·.·.·.·.':.-.,.,·.·.· }:\:}~~:~:~:!

atomic spectral lines? ...

the\/fiif Indeed this structure of the Mossbauer line is greatly dependent on type of host material in which the absorber (o r source) nuclei are embedded?\f~{t~~ In natural iron, there exist strong magnetic fields at the site of the nuclei; a~:{{]{J a result, the nuclear energy levels are split, giving rise to a "Zeeman effect'\{{)*}~ for splitting ! sta~/{@ii~~ the nucleus. Figure 9.18b shows the of the excited . . . .!)}@lii Most of the discrepancy can be traced to the considerable thickness of the absor~r,~\:(:~~w~~: The probability for interaction is given by / )J}gr~ ~ ······Jm·· P ctofa(No/A)t, : a-o;'.#.}J~~ where t = absorber thickness~ 2 x 10- 3 g/cm 2 , No/A= 6 x 10 23 /57 ~ 10 22 /g, = 18 2 = recoill~!t:::~:~: the Mossbauer absorption cross section 1.5 x 10- cm , f probability for and nuclei}f}JJiJ absorption, approx~ately 1, a concentration of the resonantly absorbing ··:\:}f~~...J: the sample, approximately 1. Hence, for the present case, P ~ 30!

:if{}~ 17 See Section 6.2 for a detailed discussion of the Zeeman effect. .

'.'.·>· JiJJ[ I

## 9.3 Mossbauer Effect

,,, ,,, , -3/2 g, - + -1/2 Excited 3- -----~~-- state 2 ~' ....,..... .

+1/2 ' .'"

+312 - +1/2 Ground 1--------<: -- state 2 --. Bo ' -1/2 (a) (b)

FIGURE 9.18 Hyperfine structure splitting of the nuclear eoergy levels of 57 Fe. (a) When stainless steel is used, the levels are not splil (b) 1n ordinary iron, however, both levels are split, giving rise to a hyperfine structure with six componems.

and the½ ground state of 57 Fe, and consequently the 14.4-keV line has six hyperfine structure components. Figure 9.18a shows the same levels for stainless steel, where no splitting occurs.

If both the source and absorber are not split, then clearly only a single peak will be observed, as in Fig. 9.12b. If the source is not split, but the absorber is, then as a function of velocity we will "scan,. with the single line over the hyperfine structure pattern of the absorber. In this case there is no absorption at zero velocity (see Fig. 9.19a). Finally, if both the source and absorber are split, a complicated pattern emerges, depending on the degree of overlap of the individual components as the two hyperfine st:rncture patterns are shifted one over the other; however, maximum absorption occurs at zero velocity (see Fig. 9. L9b).

In the experiment that yielded the data of Fig. 9. J7 , both the source and the absorber were split, so that a pattern of the type shown in Fig. 9.19b was obtained. Table 9.2 gives the relative intensities and known positions of the peaks as well as the positions obtainable from the results of Fig. 9 .17.

The apparent discrepancies in the known and observed positions are due . . in part to a small velocity calibration error. Materials like stainless steel, potassium ferrocyanide~ sources made by diffusing 57 Co into chromium metal, do not exhibit structure in the 14.4-keV line and give simple patterns.

In Table 9 .3 we summarize some of the numerical values pertinent to the :::-· Mossbauer effect .in 57Fe.

·.·.

·.·.

·-· ·.·.

·+.,··..· ·•..··'' \; :;:/:=:::=:~=:: .. :!\i~}~~~~f ~~~~ 398 9 Scattering and Coincidence Experiments .: ~ ~ ~ ~ ~ i ~ ~~ ~~~~~~~~~ :j)j)j)j}ffj --...---.---.--.-----.---.----.--,--,,-,------,--,---...----rr-,------y---r----i .:..-.:-..: •.:•..: •:-•-:---:--.:.-.:..-.

<:::::~~ :=::" :...: ::::=:=:= e /f?f~f Q) ·.·.·.·.·•••••••••••· ~ :}}}~ft ;0 •.·.·.· .·.·i.·.·- ·.·.·.· ;i; i:111 cu :::::::::::::::::::::: ;:: ·:::::::::::::.:=:::::::: C ;~ ::i : : : : : :: l: :::::=l:::::: (I)

Q)

«J .c ::rt~{~~~ - 6 - 4 - 2 o 2 4 6 o 2 4 6 s 10 Velocity(:;rrvsec) Velocity(~tsec) . :~ take{/{J~~l-~ FIGURE 9. 19 The expected pattern of the Mossbauer line when splitting oft he levels ..

.........

place. (a) Either the source or absorber is split; note that the Mossbauer 'line is split int~}::::~;f=::::~: six components and no absorption takes place for zero velocity. (b) When both somce ~~(}f~~~ :::;:~::~:=:~ absorber are split a complicated pattern results with maximum absorption at zero velodtyf TABLE 9.2 Position and Amplitude of Mossbaoer Peaks in 57 Fe, Including the Experimental Results osition Observed position p Amplitude (mm/s) (mm/s)

7 0 0 4 2.2 2.75 2 1.5 4.3 5.5

## 2.5 6 7.6 (?)

3 8 2 10 TABLE 9.3 Some Numerical Values Pertinent to the Fe Mossbauer Line Transition energy Ey = 14.4 x HP eV ·.·.·.·.·.·.·.·.~·- Internal conversion coefficient a= e/y 15 11111 Lifetime t = 1.4 X 10-? S Relative width l:!..v/v = 3 x 10-13 Recoil energy of free nucleus ER= 0.19 x 10-2 eV /J]ljJ)I Debye temperature (Mossbauer) en =490K Probability for recoilless transition at room temperature f 0.80 Cross section for resonant absorption ao = 15 x 10-19 crn 2 :./ ?}~;~~~ 57 )llill Natura] abundance of Fe 2.17% .'.:;::::::\.-~~- il!~

## 9.4 Detection of Cosmic Rays

A very complete description of the Mossbauer effect, including reprints of the most important papers, will be found in H. Frauenfelder's The Mo ssbauer Effect (W. A. Benjamin, New York. 1962); this reference should be fully adequate until the student finds it necessary to consult the current literature.

9.4. DETECTION OF COSI\fiC RAYS 9.4.1. Flux, Composition, and Detection of Cosmic Rays The earth is continuously bombarded by a flux of high-energy particles that originate outside of the solar system. These are mainly protons but the primary cosmic ray flux also contains a fraction of light nuclei. When these particles reach the earth's atmosphere they cause nuclear interactions so that at sea level we observe only the final products of the nuclear cascade.

The interaction of the primary protons with the oxygen and nitrogen nuclei of the atmosphere results in the production of secondaries including x± unstable particles such as Jr± mesons, mesons, and others. These in turn decay by the weak interaction into lighter particles, including muons, electrons, and neutrinos. Electrons and high-energy y-rays also interact rapidly, giving rise to electromagnetic showers as discussed in Section 8.2.6. Since the earthts atmosphere is equivalent to ten nuclear interaction lengths, all strongly interacting particles are absorbed before reaching sea level. What is observed (at sea level) is a ·'hard component'' consisting ofµ± (muons) and a "soft component'' consisting of e± and low-energy y-rays.

The total flux per unit solid angle around the vertical, crossing unit horizontal area is (9.22a)

where 75% of the flux is in the hard component The angular distribution is approximately cos2 0 (with 0 = 0 at the zenith). It is also useful to lmow 18 A goad reference on cosmic rays in general can be found online from the Particle Data Group at http://pdg.lbl.gov in the "Reviews" section under .. Astrophysics and Cosmology."

19 Some of these unstable particles were first observed and studied at high mountain altitudes or by baloon-bome detectors. Today such sobnuclear particles are produced pro- llli: :~::.

particle accelerators, but cosmic rays are still used for the srudy of the very highest ~~!/ ~;:~:: 400 9 Scattering and Coincidence Experiments lnverter Anode Discrim- Colnci- Discrim- inator dance lnator Anode Set to generat rv50 nsec gat pulse - 1 µsec Height of the stretched pulses ---1----J..-.

Cosmic j proportional to area ray of scintillator pulse PHA isions fotf ::::.:,J~§\: ·.·.-:-:-:•-:-~x?:·:-- FIGURE 9.20 Typical layout of a cosmic ray telescope and electronics. Pro, ) are als.i>!::::=:~::~®: measuring the pulse height in one of the counters (not discussed in the text shown.

that the total flux crossing unit horizontal area is

## 2.4 x 10 2 /m2-s

The mean energy of the muons is 2 GeV and falls off on the .h as E-2 • tc1denc~~:~:):~:::~:~:~: t~~tltl Cosmic ray muons can be easily detected by measu~g the coit >OVe rate between two scintillation counters placed vertically one al 1e COUil-·•··-·.·.·.·.·..-.·.·.

angu1J}]~~f other as shown in Fig. 9.20. By increasing the distance between t I~~ ters one can restrict the solid angle acceptance and also study the lvantag~!:tf{f ~~!!!!!!~!Ii distribution of the flux. Plastic scintillation counters have the a< : a of large area so that the counting rate can be several per second. · ,, but 1~-:-:-:·.·····-·% counter is placed in coincidence with the two-counter telescop >bsert~/:)~:W: ..: . : : : : : ::::~::;:~: located physically in a different location (as in Fig. 9 .21) one still he same::::::;..:=*·= . ::::::::::::::~:::-:t coincidences. 20 These occur because several cosmic rays arrive at countet~::::::::=:x•-;: ..) i!i?t~ time over the area covered by the telescope and the third "rovini' iave beif}~~w ·,-.,:·.·:·:r~~ 20Tocse are true coincidences after any accidental effects (Section 9.5.l)

:\)/~ subtracted.

}::::::i~f -:-:-:-:·=-:-W :()!I!~ .i

## 9.4 Detection of Cosmic Rays

FIGURE 9.2 l Arrangement of counters for measuring cosmic ray air showers (top view).

Namely a "shower,. of cosmic rays occurred. One finds that the rate for such showers is 1/300 of the telescope rate, given a typical counter area of

## 0.2 m2 and a displacement of 3 m

We will describe an experiment in which cosmic 'ray muons are also detected by simply using a 5-gal tank of liquid scintillator, viewed by a 2-in. photomultiplier tube. Muons traversing the tank give a large signal so that it is possible to use the singles rate, without the need to form coincidences. However, the PMT high voltage and the discriminator must be set carefully. The dimensions of the tank are d 28 cm diameter and h 35 cm height from which we can estimate an effective horizontal area of2 x [rr(d/2)2] 0.12 m2 • The singles rate is of order 25/s, in reasonable AJ agreement with Eq. (9.22b).

9.4.2. Time of Arrival of Random Events The arrival of cosmic rays is a random process, so we expect it to follow the distributions discussed in Chapter 10. In particular when the expected number of events in a given time interval is small, the observed number should obey the Poisson distribution. Let r be the average event rate namely the average number ·of events per unit time. Then the probability of observing n events in the time interval t is (rt)"e-rt P(n,t)=-- (9.23)

n!

•: = From Eq. (9.23) we recover the differential probability for an event (n 1)

:: to occur in the differential interval dt. Since (dt -+ 0), E.q. (9.23) reads dt) r dt . (9.24a)

...

21 This is of course also true for the decay of radioactive nuclei.

!ilfllfl 402 9 Scattering and Coincidence Experiments -::::::::::::::::~ \tmm~ Similarly the probability that no events (n 0) occur in the interval t is):\)f\%l \i}}f*!

= -rt P(O, t) e . (9.24-b}.:::::::::Jm: t/:;:;:;:::%.: We can test this proposition by measuring the distribution of the timei\}:~~~{ i~}{J[@~ between the arrival of adjacent events. A time interval t between events.

[J{@.~~ def in~ in tbi~ case b! requ~ng no event for °:1e ~ntei:val _t ~d an.e v~~f at the time t (m the differential dt). Thus the distribution lS given by ~~-~rtt~~~ 22 /{{:~~m:~ product of Eqs. (9.24a), (9.24b), which we write in the form .· (9.~il*1 re-''.

q (t)-= dP -= dt m=l \'\:/:~%a=:~ is sh~iji)!]Jjl]

It interesting that the above distribution is exponential; namely, 23 ~~q.)fif@~ time intervals t between adjacent events are much more probable :-:-:-:-:•:"~~::-:-~-=~ l onger ones. :\/}:::~:~ The intenJt\~~~®§ result for the case m 1 can be generalized for the time between every second event (m . 2), every mth event, etc. The derivatiqi()~~~~?J:~ _\/@W~f~ is given in Section 10.5.3 (see Eq. (10.75)), and we obtain )i}f{ ft.j (rt )m-l e-rt -'.?q{fJ~l qm(t) = r (m - 1)1 · C 9 m to = m"?.){J~@J As increases, the distribution tends a gaussian centered at t ·.·.·.·.-....· .•. .- .-..· .·J Of course one could also test F.g. (9.23) directly by measuring how ofte~(}\J?~ meaf.(}ff)~ one, two, etc., events are found within a fixed interval t. However, suring the distribution of the time intervals between event arrivals, as don§fj(~J here, is by far more practical and efficient. \{:/~;~~tr in)~ififi®fi Data are acquired by recording the time of arrival of every muon computer file. Since the mean time between counts is ,__,40 ms, a precisio6.(){[%t of 0.1 ms is sufficient and can be easily provided by the computer clocl~{\\(f~~!

adjaceri(/@f{j The file can then be analyzed by sorting the ti.me intervals between = ani{ttfil1 pulses (m 1) in time bins of 0.8 ms width. The same data are next lyzed by sorting the intervals for different values of m in correspondingij)jffJl~~!

-:)}\(Wt longer time bins. · ~JJi }1 Results obtained by a student form 1 are shown in Fig. 9 .22, form === ~ Fig. 9.23, and form l?<J in Fig. 9.24. One 1~otes how the distrib~f}j~@ tion becomes narrower as m increases. Namely the mterval between eve?.'.\}~~~i ~::f:;::: ;: ~; :-~ ::: we imply that the second count arrives after the first one with a delay between t -.-:-:-:-:-:~t r t dt.

always followed o~f:{)rn~~ f)

23This justifies the o~d proverb that one calamity is by a second See W. Bothe, Phys. Zeit. 37 520 (1936). ..{{~~~~!

.: /::~;~W.~ S.4 Detection of Cosmic Rays 403 700 ---~-- ---.---------.....----.......- -~ 600 t 119 =35.00 ms :::, [ 300 LL 0'-------'--------'------'----_._-___ .__ ___ _, 0 0.02 0.04 0.06 0.08 0.1 0.12 Arrival time (s)

FIGURE 9.22 Distribution of the time between the arrival of two cosmic ray counts. The fit is the Poisson distribution for m 1.

.. ....

400 ~---~----------------....--------, .. . ·..~ ._.

350 .... ..

...

• • •.•... .

• •, .

a- 250 ">.

c: • •.11 :Q::,) 200 ... • • .•.• r:r • • • .~.- @ • u.. • ' 150 • • • .

• •• • ~".' 100 · • ··~· "" ~ • ,., ..

## 0.05 0.1 0.15 0.2

Tlme Interval (s)

FIGURE 9.23 As described in the legend to Fig. 9.22 but form 3.

404 9 Scattering and Coincidence Experiments /11111 1600 .------,~--.-------.-----r--- --.-----. !lII 1400 -:::::::::;:::)~ • >>t~==I • • • • C: • ~ 800 • • C" • . i i it • • 600 ' • • 400 · • • • • . .

• }!iii 0 ..__ ___,.____--1._ __' ---',. _ _ ___,_ _ __,::,....,._ ___ , 0 1 2 3 4 5 6 Time interval (s)

.::;:;:::;.;:;:~~ FIGURE 9.24 As described in the legend to Fig. 9.22 but for m = 100. Note that tb;~}J¼,;::{: ·.)}@[fl distribution is centered at a mean time t ~ 3.56 s, where t = (m - 1)/r ~ 100/r.

. -::::::::::::m%~ betwee~mrnr~ 100 events is much more "stable' (relative to its mean value) than fof)J@t every second event. As can be seen from Eq. (9.24) the distributions = . '")'//••~•~%§f·l m > 1 have a maximum (dqm/dt 0) at m; t (9.27; ae the\{:~l:t~= TI1us, from the location of the peak in the distribution we can obtain ./\i\l average rate. We find that for the data shown in Figs. 9.23, and 9.24 }!IJ ~:~~~.s.

: :oo.

r ;;:~ ~:.

/max Furthennore, a fit to the exponential for m 1 (see Fig. 9.22) yields)}\~~J~~ t1;e 3.50 x 10- 2 s, or r == 28.6/s in agreement with the average rate. ··\}}f /i)!/!I 9.4.3. Measurement of the Mean Life of the Muon ..

an}//j~~ I:; The muon is not stable but decays· into an electron, a neutrino, and antineutrino: +Ve+ )J~ µ,+--+ e+ Vµ µ,- --+ e- + Ve+ Vµ- (9.28) {~~~ :::):-[= }Jt }]ij . ?:;~ )Jt

## 9.4 Detection of Cosmic Rays

The mean life, or lifetime, (i.e .• the inverse of the decay rate) for this process is of order 2.2 µs, and thus the decay is easily detectable for muons at rest. The neutrinos are not observable buL the electron (or positron)24 is energetic enough to give a clear signal of the decay. The mass of the muon is = /c-'1} mµ, 105.65 MeV ..

approximately 200 times the electron mass. Tbe maximum energy of the electron occurs when the two neutrinos recoil againsL i~ as sbown in Fig. 9.25a. This corresponds, in the rest frame of the muon, to 2 = Ee(max) ::: mµc 53 MeV.

The energy spectrum of the electrons from muon decay is shown in Fig. 9.25b.

The long lifetime for muon decay indicates that the decay does not pro ceed through the strong (nuclear) interaction but rather through the weak interaction responsible for the ",8-decay" of nuclei. However, the process ofEq. (9.28) is very important because it involves only leptons (no strongly interacting particles participate) and thus can be used unambiguously to ----- u e u,i (a} ~ ~ (b)

dNe dE mp.c2 --=53MeV / Endpoint 25 50 MeV FIGURE 9.25 (a) Configuration of the particles in µ-decay for obtaining the maxi.mum electron energy. (b) The energy spectrum of the electrons from µ.-decay.

24 To save words we will speak only of the electron even though we mean either e- ore+.

. :){tt~ : :))jJfti · :ml 406 9 Scattering and Coincidence Experiments of:i~fII calcul~te ~e Fermi weak interaction constant Gp. The ~ean life muon 1s given by --:::::::::~::::::=:=~,w.

<{@))I{I 1 1 G2F (m1nc2 )5 2?,t =:=::==I ,- (9 :::~ld .

(!lj!llll :u:nc Precise measuremenIB of~~ ~:an :< tµ, (2.19703 ± 0.00004) X 10- 6 S 9.3~!1111 and through Eq. (9.29) the value of the Penni constant25 :/\/III (9.30t{J~ Gp = I.1664 x 10-s 0ev-2 • (lie) 3 <:::: ..; '.;%::::~ ·-::::::::;:;::=:»~ _w~ li~~f~~~~, will measure the decay of muo°:s that have come to rest in the .e~lJ:~ scmtillator tank. Muons lose approximately 2 MeV of energy for exr¥:fi~~ gram per squared _centimeter of m~teri~ th~t th~y ~verse. Thus _we that muons entenng the 35-cm-high liquid scmttllator tank with e~~::f:~ st~J;f~jl[~ E µ, ;S 50 MeV will stop in ~e tank. The fraction of muons that ~o rat¢:/~Ji;f® of order 0.3% of the flux gomg through the tank. Thus~ the stoppmg = statis~¢..~ft =li Rs 0.077/ s, or 4.6 muons/min. This is adequate to obtain good accuracy for the mean life value in a reasonable time interval. ··rt }{~ The experimental arrang~meot is.s hown in_ Fig: 9.26. y&en a m~11JJj mtn:::?:~%: enters the tank the PMT gives a signal, which ts amplified and discrirrrinated. This pulse is used to start a "time-to-amplitude convert~#~({&~ w.ill}tfw.~ (TAC) circuit. IT the muon stops in the tank, then the decay electron give a second signal within a time interval of a few mean lives. The sec~j~}{@~ p~lse is used to stop the TAC, and ~e thne intei:val ~tween start and sto~Jf} ~~~ directly read out. The 60-ns delay u1 the start signal 1s to make sure that:nJJ.:::;:::W-::~ pulse will be on the stop lin~ when the st~ ~ves. ~o~ercial electro#,~W.Jtlw~ GT29Qff%=~= modules can be used to achieve the logic mdicated m Fig. 9 .26. A computer card , d es1 gne Profi e ssor ar t ill ?f C om~ 1 1 U n1 vers i trf ··2 ·-·.·.

·. ; x.

performed the TAC functions and stored the data 1n a file tn the compq~¢.fJ@: = ,..;,~t;~_f(~ memory. If no stop arrives within At 25 µs, which corresponds to . )}ff{@ 25 Note that in contrast to the fine structure constant a = e 2 /lie, which is dimensio~!ij~ii~I Gp/ (lie) 3 has dimensions of inverse energy squared. fu fact GF / (lie ) 3 has the appro~~(~:?-f& ~alue o! 1/(Mwc 2 ) 2 , where Mw is the mass of the vector bosons that mediate the ~~~tf~ mteracttons. ·-:::::: f::::: ::::~· 26 }~~ ?ne can now purchase commercial versions of TAC cards to perfonn the req~#:f funct:ions. ·:::::::::-:~~~: ··::::::;;::;:;~: 1rl1

## 9.4 Detection of Cosmic Rays

H.V.

Dlscrlmina .>------1 tor µ.-meson 2~ PMT Stop TAC Computer Scaler Delay Eledron 60na 5-gal Hquid scintillator tanK Callbratlon AGURE 9.26 Block diagram of the electronics for measuring muon decay.

mean lives. the TAC is reset and the start pulse ignored. To calibrate the TAC one applies a fixed frequency (o sciUator) signal to the discriminator ·ii input.

If the singles rate is too high, then the stop pulse may not be due to the decay of the muon that started the TAC, but to a different muon entering the tank. We call such events "accidental stops." and we can estimate their rates as follows. The singles rate is r 25/s, so that using the Poisson = = = distribution of Eq. (9.23) for n 2 and t ~t 25 µs we find for the ( accidental rate = 2 = Ra= Pa(n ' ~t) 7.8 X 10-3 s-1. (9.31)

~t This is ten times smaller than the stopping rate Rs, and does not affect the determination of the mean life as discussed later.

•: Data obtained by a student-are shown in Fig. 9.27. The data were accu mulated over five days and yielded Ns 32,000 stops in 6921 min. The .. very early events, t < 0.25 µs, were discarded, leaving a sample of 30,069 \ events di~played in 100 bins each 0.25 µs wide. The data fort ;S 5 µs show ( an exponential drop-off, as expected, and in this region are well fitted by \ : N(t) Noe-r/1: 0.25 < t < 5 µs.

}\n contrast the data for late times, t > 15 µs, are flat and are well fitted by \{ a constant N(t) C 5 < t < 25 µ.s.

:}?}~(~; :ri!ii!iB 408 9 Scattering and Coincidence Experiments ·.:::::::::::::::~: )i{}{~ ·-::;:}?r~r W£i- i\ ){:!f ·!i!i!}~f~f :/J~ii 10' • :: \ :::::?=:=:~::: ' ")!!!!11 ··~~- ·".:!iii!i]~~t :iii~- 10 Ill ' ~-- .

··::~~~~~:.-~~:½.:-~~~~~ ·; 10' --------------------------------- :•:::/:?-:={fl: O 5 10 15 20 25 .·<...tt..J..r., .f~fwl· Time (µs} FIGURE 9.27 Dar.a for 30,000 moon stops. The bin size is 0.25 µs, and the fit to the:J~i,@J~f including an exponential decay and a consrant background ~rm we show~ - ]

}\Jti/ A combined fit27 of the form ..

::::;i/?I~~i: = + C (9~~itfi~\ N (t) Noe-t/1: ··:::::::::::::=:=:~%::: yields r _ 2.088 ± 0.016 µs, No= 3410, and C = 28.8, and an excell~ijjflftf x2 = 0. 909 per degree of freedom. The contributions of the two tenns}j[{~@"{ the fit are also indicated by the dashed lines in the graph.. ·:))}f~~r ti~ We briefly disc~ss the back~ound level. Since there are 100. ch~/{~~f nels, the total accidental count 1s Na 2880, and thus the acc1den:(~.\f~\.

rate is Ra = Na/6921 min = 6.9 x 10- 3 /s in agreement with our esti.J#iji~/ f{fu~ Jijfj~f of Eq. (9.31). One recognizes that the background does not affect ·1 ·. . ·.·.·.·-·.····w···· measurement unti :.:::::::::=:=:=:m:;:=::.

Noe_,,, - C. ·: /~~- ~ ~-1;· This occ~ when I/ r - 4.7 1, which allows for a fairly long "lever to determine rµ,, .::::::::::::t~:if,.

Our value f~r the mean life is in close agreement with the acceB~ ~~~ because-::, t!ltJ{ value as given m Eq. (9.30a). The agreement is even closer ··:.·!.·f.·J,·.r·X~·~.~.;.

:e See Section 8.6.2. )Jl1-~i ·/!;)~ -:•:-:·'.·--~~

## 9.5 y-yAngular Correlation Measurements

measured value for -r:µ must be corrected for the following effect. When negative muons stop in matter, there is a finite probability that theµ,- will be absorbed by a proton in the nucleus, leading to a "capture" reaction: + + µ,- Z ~ (Z - l)* vµ,, Thus the effective mean life is shortened and given by 1 I 1 -:::=-+-, rµ, re "te where 1 / rµ and 1 / re are the rates for decay and capture, respectively. As a result the observed mean life is shorter; for mineral oil (the capture occurs mainly on carbon nuclei) and for the µ, - / µ., + composition of cosmic rays this correction is approximately 4%. Therefore, the corrected measured value in thls experiment is rµ, = 2.172 ± 0.017 µ,s. (9.33)

The error shown in Eq. (9.33) is only statistical and does not include systematic effects, in particular any uncertainty in the TAC calibration.

9.5. y-y ANGULAR CORRELATION MEASUREI\1ENTS 9.5.1. Genera) Considerations We will now discuss the measurement of the correlation in angle between two gamma rays that were emitted simultaneously from the same source.

The origin of these gamma rays is frequently the cascaded decay of a 60 6 nucleus, as in the case of Ni ( °Co) already discussed in Chapter 8. (See Fig. 8.20.) We reproduce in Fig. 9 .28 the decay scheme of this nucleus and note that the 1.333-MeV gamma ray follows the 1.172-MeV gamma ray, the lifetime of the intermediate state being only about 10- s, so that for all practical purposes the two gamma rays are coincident.

The fact that these two gamma rays are correlated in angle can be understood from the following general argument: the first gamma ray will have an angular distribution with respect to the spin axis of the nucleus; thus its obsexvation at a fixed angle 0 0 conveys information about the probability of finding the spin at so~e angle ,/J with respect to the .? :::::::::~tfJ ./U!!Ilfl 410 9 Scattering and Coincidence Experiments .·:::::::::;::::::..-1 !lll 60Co Z1 !/ll :iii ::;:;:;:;::::=.\tf III Prompt 2.505 MeV ::-::::::::::::~ ~ 4 --'-'I--- ::@W ira 2• Y, E2 1.333 MeV / E2 t=Bx 10-13 sec i'2 >:·:·:-:-:-:-:-*.. .

o+ ------o .::):}f}Jm::~ . ,:,:.:,:-=-=·=·w;.;.: FIGURE 9.28 Nuclear decay scheme of 6()Co by beta decay to 60Ni and subsequ:~~ttit.i~ g~#.@t~~f deexcitation of the 60 Ni nucleus to its ground state by the emi"ssion of two cascaded :::11 ~~ ~ rays. / direction B 0. Now the second garrnna ray also has some angular disttjfll~ ~~~ n?w bution about the spin axis that is kno~ to be at 1/t. Thus the prob~bi?,,~{j~~J~ :~Ja:;: that the second gamma ray will be enntted at an angle 0 can be fouµ~f ~sis called the angular correlation function C(0): The time coincideni§I@I I tlj¢;\~Jfit~ signal assures us that the two gamma rays have mdeed come from /1$/~ gj~f same nucleus an<L therefore, are the two gamma rays of interest. A cussion of this correlation between cascaded gamma rays is presentecf:ijf/J·Jt~t . 9 5 4 : : :::::::::::::::~:=:~ S ectton . . . ·. .· .·.·.·.·.·-·-~,,,:,,;..-.-:, In 22Na, the angular correlation arises from a much simpler roechani~'.#KJJI~~~ 8.2~/f};{fl Na is a positron emitter as is shown from the decay s~heme of Fig.

W.-#}\?JiJ The positrons are slowed down in a thin copper sheet with which 9(/:~{~~~:~{ surround the source; the slow positrons are captured by the electrons.

·.·.;.·.·.·.·.·.·.•Y_,.z• ••. , :~ {~lf~jj the _copper to form positronium, which decays by the annihilation of ~Y.~:=:::::=%::=:~ positron and electron into two gamma rays. The energy oft hese gamma ?f w~;;l)~},~~~ is precisely 0.511 MeV , and since the center mass of positr?ni~ ~-est, the two gamma rays must be directe~ m ~xactly opposite drrecU?;Mflt=~~ @.

m order to conserve momen~m as sbo:'11 m ~1g: 9.29. ·. }\{{~~~ Thus the angular correlation theoretically 1s gtven by .;{{~ <} C(0) - r ('TT' - 0) ·.·.·.·.·,•/·.@ - 0 ,14, ' • •,1 and. the observed finite width is du~ to the resolu~on of the appar~~~'.

obv10usly the two gamma rays are sunultaneous. Smee the 22 Na ang~•:;:}ff/\~ :}/J::~ijf correlation is so sharp, it is frequently used for calibration purposes.

il~fl.

ji.

## 9.5 y-yAngular Correlation Measurements

FIGURE 9 .29 Capture of a positron by an electron to form positroniurn and the subsequent annihilation of the positron-electron pair into two gamma rays.

..

Preamplifier ToHV Lead shielding (1480 kV)

- - - - - - - - - ~ ~Radioactive source ....,.,,~ Photomulllpller , lnlervals marked on circle FIGURE 9.30 Apparatus that can be used for angular cocrelatioo measurements. Two scintillation crystals mounted on photomultipliers are protected by appropriate lead shield ing. One counter assembly is fixed, whereas the other can be rotated about the position of the source.

Angular correlations may also be observed between beta and gamma rays, alpha and gamma rays, etc. This technique has proved very fruitful for the analysis of nuclear decay schemes and the assignment of spin and parity to excited nuclear levels.

We will describe a measurement of the gamma gatnma angular corre lation of 22 Na and of 60 Co. The apparatus shown in Fig. 9.30 was used; it consists of two similar gamma-ray detectors placed at equal distances from the source; one detector is fixed and the other is free to rotate around the source, varying the angle 0 between the detected gamma rays. The detector outputs are fed to a coincidence circuit, and the rate of coincident counts C(0) is measured and compare!! with the theoretical correlation function.

It is important to measure C(0) with the best possible resolution if the data are to be fitted with a polynomial in cos 0 of high order. It can be shown that C(0) must be a polynomiaJ in even powers of cos 0, the highest power being 2k, where k :S lb, l 1, h where / b is the spin of the final nuclear state and 1 1, 12 is the angular momentum (multipole) of the emitted gamma rays. Frequently the experimental measurement may be restricted to the .-:-:-:-:-:-:-:;.~z.- . :!)){~~ :}\f:~; 412 9 Scattering and Coincidence Experiments ··meas-ctrettldi.L"~lMJU?.t~o.tro.ocv.,of the coincident gamma rays, that is, C(180°) - C(90°)

a= C(90°)

The limiting factors in these experiments are two: (a) The coincidenc~/{l~f accuf(/Jfj~~ rate must be high enough to allow statistically significant data to be ra~ti{J~l mulated in a reasonable time interval. . To increase the ~oincidence th~(:)i~~:~: a stronger source may be used, the solid angle may be mc_reased, or efficiency of the detector may be improved (if it has not been maximizaj\}t@~ already). (b) The accidental rate must be kept well below the coincidenc~){t:@§~~i o_-q;_\ff@~ rate; again it depends on sow·ce strength and solid angle, but also ~f j/fl a the resolving time. Let ~Q 1 and ~n2 be the solid angles .subtended , the source by detectors (1) and (2), and let E1 and €2 be their respectiv_f)ff%~~!

'}!)f~t?.?~ efficiencies. Then the "singles~· counting rates are .

\{}f~;~ = .{!/J~~ R1 N LiQ1 1€ R2 N 6.Q2E2, (9 34f::;:;;;:~;;:-;:: ' . ·:f ?JJ:f~l th~!f!j~J1~~j where N is the number of disintegrati?ns per unit ~e _of the source. If two gamma rays are uncorrelated ( or 1f the correlatton 1s small, as happq.r~::::::t?~:}~ mostly in nuclear decay), the coincidence rate28 is )()}~fl~ (9.35~flllll M11~'22E1<2- Re= N = ~at;/f]~~lf For most experimental arrangements 6Q1 AO2 and E1 E2, so . ' .·.·.·.·.·-·.·.· -=···~ we find for the accidental rate RA, ·:\}:l=====:1f1 ~:::~~/ii!!

:~:~:E2 )~~lili RA M' and for ilie ratio ofilie acciden:: to true coincidences, .•.

- = N At. (9.38)::::::::~:~ Re ·<····--..-~~-:-; ·::::::::::~;~/,~~ FroJ.i}i~i We wish to keep this ratio small on the order of or smaller than 0.1.

(9.38) hayij}J~j Eq. we see how important it is for correlation experiments to = mC.t~ij:r a short resolving time; with 6-t 10 ns, a source as strong as 0.5 high,:{ifj~~ may be used. We also note that the detector efficiency should be )·.·i.·i.·.i'r~.~-I-1 8Tbe efficiency of the coincidence cin:uit bas been set to ,, I as it should be.

·.ur11 ·t)Ji.J ::::::'.}'.f:?":=: ·-:-:-:.::::-:~i :: :: : :~:1 .:=m,;

## 9.5 y-y Angular Correlation Measurements

since it enters Eq. (9.35) quadratically; however, the solid angle cannot be increased arbitrarily because this will destroy the angular resolution and wash out the correlation C(0).

9.5.2. The Apparatus The apparatus has been shown in Fig. 9.30, and we give here SOple addi tional details. The reader should, however, refer to Section 8.4.2, in con nection with the instrumentation and techniques of gamma-ray detection.

The detectors were Na! crystals 1 in. in diameter and 1 in. thick, mounted on RCA 6655 photomultipliers. Each was located 8 in. from the source.

Both crystals are protected from scattered radiation with lead shielding, and the movable detector can be rotated about the center in 5° intervals.

The block diagram of the electronics is shown in Fig. 9.31, where the individual units are available from a number of vendors. The units are interconnected with 50-Q coaxial cable. Manuals accompanying the amplifier, discriminator~ and coincidence modules should be con sulted, especially to achieve the smallest possible resolution time. In the ensuing dis~ussion we will assume that the circuits have been properly adjusted. · One of the outputs from each discriminator is fed to the coincidence moduJe and a second output to a scaler capable of a peak rate of 10 /s. The coincidence output is also fed to a scaler. In this way tbe "singles" in each channel and the "doubles" are counted. The delay between the two inputs to the coincidence circuit may be easily adjusted by inserting appropriate cable lengths between the discriminator and coincidence in one or the other of the channels. One foot of typical 50-Q coaxial cable corresponds to a transit time of about 1.5 ns.

Some care is required in order to properly set the discrilninator bias levels and photomultiplier high voltage. First the system is checked out with a pulser, to adjust the setting and functioning of the scaler drivers and scalers.

Next the actual signals are fed into the circuits and the discriminator outputs "looked at'' on an oscilloscope to ascertain that the pulses are "clean" and uniform. The high voltage is set by taking a plateau curve, which will not be completely flat but nevertheless should show a clear knee. If the system is 29For example, Canberra Industries (http://www.canberra.com/) and Ortec (http:// www.orteconline.com/) boU1 give details of similar setups. including cross references to their own product line.

414 9 Scattering and Coincidence Experiments (1) Scaler Discriminator driver RCA Preamplifier IH-51 IH·71 665 5 ...

Scaler r- CMC ..

. .

. ..

Coincidence ,....... Scaler Scaler ,.

N \ aI ...... IH-56 d lH ri - v 7 e 1 r CMC .' · . -· '! : 1!1 ...

. .

•,•, 1 (2) Fixed delay Scaler ..1 ·!

-A CMC ..

...

RCA p plili 6655 ream 1er Discriminator ~ler . · ·\))(/:~~~~;/.

lH-51 dnver ... -:-:-:-:-'.-:•/.•:•~• •: ; -:-::)::::ii::~~:::

## IH-71

for m~\@@9 FIGURE 9.31 Block diagram of the electronics used angular correlation ~ 1o2 CD ::J g0_ gj 101 ii> ·-g0 (.} 100 • 10- 1 .___ _. ....__ _. .__ __...__ ___,..___ __,_ __ __. ___ _, 0 5 10 15 25 30 35 }!)ittmf Deay in channel 1 (ns)

~G~RE 9.32 A delay curve for coincidenc~'i from a ~a source. Note that the ~es~-~%¥]~~~§~ tune lS on the order of 13 ns and that the acc1denral rate 1s lower than the true c01nc1~:~~if:::;~~/ rate ~y a factor of at le~t 1000. The curve through the points is a simple spline inte~l~~~1{i~ ·t:::::::?:i~~: and 1s only meant to guide the eye. · \})~@~§ sb~:~1:)j'I working properly, the "singles" rates R1 and R2 in the two channels be (almost) equal. -:-:-:-:-:-:·::--:-:~:: coincide~ce:}§~l~§ _It~ possible t~ measure the resolving ti~e of the making:::lfill cwt either by talcing a "delay curve" (see Ftg. 9.32) or by :@-I . i/8 ::::;:::::?;;:~

## 9.5 y-y Angular Correlation Measurements

TABLE 9.4 Detennination of Resolving Time from Accidental Coincidences at Counts/s (s)

Channel (I) Channel (2) Coincidence (At= C/R1R2)

2151 2056 0.06! 13.8 X 10-9 5920 6262 0.528 14.2 X L0-9 14,662 13,481 2.912 14.7 X 10-9 , 31,207 35,443 14.217 12.8 X {0- 9 of Eq. (9.36). When the latter method is used, the two counters are sepa rated by a very large distance and a separate source is placed in front of each. In view of the geometrical arrangement and the fact that an additiona1 delay of 60 ft is placed in one of the channels, all the coincidence counts are accidentals. By varying the distance between the source and the respective counter, the results given in Table 9.4 were obtained; the counting time was on the order of 10 min at each poinL We note that the resolving ti.me so obtained (column 4) is quite consistent despite the fact that the accidental coincidence.rate increased by a factor of about 2000 between measure ments~ this resolving time is also consistent with the width of the two input signals (which were about6 ns wide) and the data of Fig. 9.32.

The above results as well as those to be presented in the following two sections were obtained by students.

9.5.3. The y-y Correlation of 22Na A 100-µCi 22Na source, wrapped with a 0.001-in. brass foil is placed at the center of the apparatus. The dimensions of the source are kept at a minimum, and it is positioned as accurately as possible. Since the solid angle is ~Q [.7t X (Q.5)2]/ (8)2 ~ 4Jl' X 10-J where the dimensions are in inches {see previous section). Assuming a detector efficiency €1 ,..., ~2 r,..; 0.3, the expected rate for "'singles" is R1 ""'R2 = - 3.7 - X - ]01 - 0 X - 10 - -4 x (4n x 10-3 ) x 0.3 ~ 1000 counts/s.

4.7r :))!tJaWJ !!!!!ill '·\ ::::}:;:::~ 416 9 Scatter;ng and Coincidence Expedments Since the two gamma rays are completely correlated when the two counters;/{j{~~~ill~-[t~ \\ff are at 8 180°, the expected coincidence rate at this angle is :-:. : . : -:-=-=-=-=~-~-=--· C(0) = nb.Qf 2 = RE = 300 counts/s. (9.39)\(}ff.Jf .:;:!:!:\ }~=?i:?.i ))/ff)

The observed rates are on this order of magnitude. However, the 1.277-MeV }{:\~:~?~ gamma ray also contributes to the single rate; on the other han~ the the)\)}{ff finite size of the source and errors in geometrical alignment reduce ~ ·\{\}$}~ coincidence rate from the calculated value.

·:::::\?:{:~:§~~ We first wish to check whether the coincidence circuit is correctly .·.·.·.·.1•.. ...· ~. .· ~:·~ :))~:~a:~i~ "timed"-that is, whether the appropriate delay has been inserted so as.

...... ..-.. ; .... •.1.

to make truly coincident signals arrive at the circuit at the same time. To {{:~.{.{~ ..:. i,.?,~.

.... , ::,: this effect the movable counter is rotated to 180° and the counting rate is :)}}:~:=f~ .· ·-:-:-:-:-:-....:;;½·%· obtained as a function of the variable delay introduced into channel ( 1) ; for.\:::::~=~:=:~;~; convenience, a fixed delay of 12 ft ofc able has been introduced into chann~(\(J~®~~ (2). The data so obtained have already been given in Fig. 9.32 on a semilog. :{{{~J~i plot, which is the more appropriate representation for a delay curve. ·•), ·!. ·?. ·-~·-4~.•t.~;.•:. ~.. r. : .• :\(Jff We note that ( a) indeed, the peak counting rate occurs when.a 16-ns delay ·.;/JJi~~ is inserted in channel (1) as expected; (b)in the peak region, the delay curve is flat over at least 6 ns~ this indicates good efficiency and consequently that }(}~§§t ({ff?

small time jitters will not result in changes in the counting rate (provided the delay is set at the center of the curve); (c) the width of the curve at ·}}{ff half-maximum, which gives the resolving time of the circuit, is 13.2 ns, \)/}\ in excellent agreement with the values found in Section 9.5.2 .and what is .\ \~{~( )/J/ expected from the width of the input signals; (d ) the accidental rate is very ± }!}{(~ low; by inserting 40 ft of delay it is found to be 0.048 0.005 counts/s, \}It yielding a ratio ~-~~ 3 9 = - ilff 1 1 which is more fuM M:u~: x l03, ( .40) )

:::~~t~~c~~~:g d::~m:::i::~~ ..

~~U:i!e~:~:iz: del~~e in~~t :.:i:•:•:•:;.,.l:1..l: _ l.~_-;!,; their low peak amplitude. The stability of the system can be judged from .: ·: ·:?!Jfi the fluctuations of the coincidence rate in the flat region as well as from ./i@Jt the fluctuation of the singles rates given in Table 9.5.

We are now ready to obtain data on the angular correlation of 22 Na. · )}§tI ..

. } . ·.I · .- i ;.. ~ :·.- The movable counter is rotated in appropriate steps to either side of 180°, · _./?§/ and the doubles and singles rates are recorded. The resulting data are shown in Fig. 9.33, and in Table 9.5 some representative points are listed. · {)f II

## 9.5 y---y Angular Correlation Measurements

TABLE9.5 Representative Data on the y-y Correlation of22Na Counts/s 0 Stationary Movable Coincidences (0) counter counter Coincidence ( Coun ts/s-degree)

90 3011 3086 1.5 ± 0.1 0.21 150 2996 3071 1.5 ± 0.2 0.23 160 3013 3090 1.7 ±0.2 0:.23 170 2994 3064 3.5 ± 0.2 0.49 175 3011 3114 66.8± 1.0 9.2 178 2992 3189 148.0 ± 1.5 20.6 180 2995 3035 159.0 ± 1.6 22.l 182 3014 3178 124.0 ± 1.2 17.2 185 299l 3069 50.2± LO 7.0 190 3039 3127 3.2±0.2 0.42 200 3005 3102 2.0±0.1 0.26 210 3007 3136 1.8±0.l 0.25 (.)

CJ) 100 C: :ag> 80 .10=8.5° -¼ i:: 0 60 z<'3 gi 150 160 170 180 190 200 210 Angle between detectors {degrees)

FIGURE9.33 Angular correlation of the gamma rays from a 22Na source. The coincidence rate is plotted as a function of the angle between the two counters. Note that the full width of the correlation curve is 8.5°, which is entirely due to the angular resolution of the two counters~ the isotropic background outside the peak is very small. The curve is a Ga.ussfan fit to the peak region, with a fixed constant background, but only serves to guide the eye.

!~11/l!ii 4tB 9 Scattering and Coincidence Experiments Colwnns 2 and 3 of Table 9.5 give the singles rates for the stationary and ·:{:(/{{:JI 30 :)[/{~~t the movable counter, respectively; the coincidence rate is given in col- }iJtff umn 4. The counting time at each point was on the order of 1 min, which \\{f( provides good statistics (about 1% in the peak region).

= /}\\J Indeed we do notice a very pronounced correlation at 0 180°, with ·/)i/J@i an angular width of ±4.25°. This width is on the order of the angular ))ff(: resolution of our system, which might be taken as the angle subtended at the position of the source by one of the counters \{\@~§~~~ A0) = 0.5 = tan -+ b..9 7 .20 .

( 2 8 We therefore conclude that this correlation is compatible with C(0) 8(11: - 0).

The anisotropy as defined by Eq. (9.34) is ex= C(180°) - C(90°) _ 150 - 1.5 ~ l00 C(90°) 1.5 ' which is extremely large and compatible with a -+ oo as predicted by\({/}/ ?::}~I~~/; Eq. (9.42).

due/:/{f~f The counts observed at large angles are still real coincidences, but onei)[@)ffl mainly to the isotropic correlation of the 1.277-MeV gamma ray with of the annihilation gamma rays; it should be on the order of the correlated{://~ffj i~\:{jf@~l counts multiplied by the solid angle for one detector b.. Q ~ 10- 2 , as indeed the fact. Also, a small fraction of the background originates from)){:~~=~=}~:: •...... •. ·.·.·.·//_.t'. ..

annihilation gamma rays that have scattered through a large angle in the/\(ftf source or the converter. ' · . : · : . : · : . : · : . : · : . : . = ·. : " = ·•· : - :3 ·. . : ~ '·f - . . :: .. : . : ": : .

- ·->:-:.;-:-;. .: -:•:.-:-:-: In column 5 of Table 9.5, the coincidence rate has been divided by th~\}}[ft angular acceptance 1).0 of the movable counter as given by Eq. (9.41)///:}i}} syste#i}/i~&l Indeed, since the co~lat!on is a _functio? of 0, it is obvious that our -:\)\t~ ~~i measures C ( 0) at 0 within the differential range ±D-0.

From the results presented we conclude that 22 N a provides a very goo~:}Jf:f?& :{ /jf l try~ technique for ~ligning and adj~~tin~ the equipm en~ es~ecially since strong correlation from the annihilation gamma rays 1s quite easy to de~~ff ) ;!]~ J \[})j]~ f ·{f?~~:ii:~ 3°'rhe rate for accidentals should have been subtracted from the results of column . . mall ( Eq (9 40)) th l . ··..·:.:·/.·<.:·.?·,·I.·\;'.@-:.,t'.I: ·.:·;-:· h owever, 1t 1s so s see· . . . at we neg ect 1t.

}!ii!l ~i til

## 9.5 y-y Angular Correlation Measurements

Also, the obtained correlation provides strong evidence for the annihilation of the positron-electron pair into two gamma rays; if a differentia1 discrim inator is used after the detector, it is also possible to measure the energy of the coincident gamma rays. The angular resolution of the equipment may be easily improved by simply increasing the distance between the source and the counters. In fact. precise data on posjtron annihilation are quite sensitive to the momentum of the positronium just before it annihilates; this in turn provides iofonnation on the structure of the Fennl surface of the converter material. · 9.5.4. The y-y Correlation of 66Co Once the equipment has been adjusted and aligned (for example, with 22Na)

as described before, any correlation may be measured. A 6°Co source of the same strength as the 22 Na source (100 µCi) was placed at the center of the apparatus, and data were taken every 15°. The discriminator levels could be readjusted, but it is usually preferable to leave everything as is.

Since the 60co y-y correlation has a small anisotropy (as compared to 22Na, Eq. (9.43)) the expected coincidence rate is = 2 C(0) N(~rt.)2E ~ 4 counts/s, (9.44)

whlch is much smaller than that given by Eq. (9.39) for the same source strength. Consequently, also, the signal-to-noise ratio (Eq. (9.40)) will be only about 30. and the "accidentaJ" rate, which was 0.070 coW1ts/s, must be subtracted. Furthennore .in view of the smaller correlation, better statistical accuracy is required.

Representative data taken in one run are presented in Table 9.6 and plotted in Fig. 9.34. In column 5 the coincidence rate after the subtraction of accidentals is given, while in column 6 the rate at each angle is normalized to the rate at 90°. At each point sufficient coincidence counts were taken to give 1 % statistical accuracy (10,000 s ~ 3 h); these errorS are indicated by the error bars shown in Fig. 9.34, where we plot a(0) C(0)/ C(90°)

against angle. We see that the fractional errors on (a(0)- L) are now much larger, and on the order of 10%.

It is known from theoretical considerations that the 60Co correlation function is of the fonn C(0)

2 + 4 et(0) = --- =I+ at cos 0 a2 cos 0. (9.45)

C(90°)

420 9 Scattering and Coincidence Experiments TABLE 9.6 Representative Data on the y--y Correlation of roco Counts/s 0 Stationary MoYable Corrected C(9)

(0) counter counter Coincidences coincidences 60 2203 2129 0.880 0.810 1.080 90 2132 2157 0.820 0.750 1.000 105 2152 2127 0.857 0.787 1.049 120 2144 2130 0.864 0.794 1.059 135 2109 2125 0.886 0.816 1.088 150 2132 2136 0.933 0.863 1.151 165 2121 2123 0.931 0.861 1.148 180 2116 2124 0.944 0.874 1.165 210 2086 2134 0.889 0.819 1.087

## 1.18 - Theory

- - · Least squares tit 1.16 1.14 1.12 £~ 1.1

## § 1.08

(.)

1.06 1.02 100 120 140 160 180 Angle £J between detectors (degrees)

FIGURE 9.34 Data on the angular correlation of the two gamma rays fror correlation function C(0)/C(90°) is plotted against the angle between the t Note, however. that the ordinates begin at the value 1.00. The experiment shown, and the dashed curve is a least-squares fit to the data. The solid liI theoretical curve, which is given by the function 1 + 0.125 cos2 0 + 0.042cc 9. 5 y-y Ang u I a r Corre I at ion Measurements 421 A least-squares fit to Eq. (9.45) was made, using the entjre set of experi mental data, and the following values were obtained for the coefficients a1 and a2.

= ± = ± a1 0.190 0.08 a2 -0.04 0.08 = = The theoretical values resulting from the spin assignments I a 4 +, / b o+ 2+ and le= (see Fig. 9.28) are ...

= = a1 0.125 a2 0.042.

The correlation function that results from the above coefficients is included in Fig. 9.34; the dashed line represents the least-squares fit, and the solid line the theoretical curve.

From Fig. 9.34 we see clearly that an anisotropy in the angular distribution of the y-y coincidences from 60co exists; we obtain a = a(180°) - 1 = 0.165 ± 0.016. (9.46)

The error flags in Fig. 9.34 were set at 1.5%, but the data points scatter even more. This is not due to the "statistics," but to random fluctuations and drifts of the equipment over the long counting intervals.

31 Th.is included 21 more measurements in addition to those presented in Table 9.6.

C H .A P T E R 10 Elements from the Theory of Statistics 10.1. DEFINITIONS Statistics is the science that tries to draw inferences from a finite number of observations constituting only a sample, so as to· postulate rules that apply to the entire population from which the sample was drawn.

In the field of physics, statistics is needed (a) to fit data-that is, to esti mate the parameters of assumed frequency functions; ( b) to treat random errors; and (c) to interpret phenomena that are inherently of a statistical ii nature.

. . 10.1.1. Definition of Probability The probability of occurrence of an event can be axiomatically defined as / equal to one (= 1) if the event occurred, or equal to zero (= 0) if the f: event did not take place. An alternative definition of probability is based ::::. on the frequency of occurrence of an event. Suppose that several trials of ;::: ? the same experiment have been made; then the pi;0bability of occurrence . . - ..... ·..

~::: :.=...- : : • ,:,;-· 423 ~(.

~:::::· .t...·...·· .' ~::::: ·:::::::::=:::::::1~ _)){\~ /:::::)?}fJ:j 424 10 Elements from the Theory of Statistics ~li: . .· ·==:)!)ifi @f \li~~/{}~ of an event A, that is P(A)~ is given by the number of times event A tdtj)J/}tffa obtained divided by the total number of trials (in the limit that the number of trials approaches infinity). This definition of probability retafu~/}J@~ o~ii{}@J its full value even in the case of nonrepetitive experiments, since the trial can be considered as the first of a series of trials. \\::=:::=:=@: wtil l.iiii 1O . 1.2. Sample Space ..

Any set ofp oints that represen~ all p~ss~ble outco1n~s of~ experiment}~@J~~ sp~;:~tff~3.

a s~ple ~p.ace. Fo: ex~~le, 1f _a c~m 1s tossed twice, the· sample fi~~f~fiWi consists of the 4 points 1ndicated m Ftg. 10.1. (Sample spaces can be d di te . ) ..... -,~~~- or m. w~-u!t. e an sere or conunu~us. . _ :}\}t&Ji m;~~/fftJ½j Once the sample space for a particular expenment 1s constructed, we assign (in the sense of Definition 10.1.1) a probability Pi to each poix~,t::~\:~~ '\/t}t}~f~ of the space. From the definition of probability, we have ·::i!i!i\1/{~?t Pi > O fill s&npl~:.ipoint!; ) ,, thus Pi< 1 and the probability of occurrence of an event A is = Lf1;(A) = P(A) p;(A), Pr A LA where indicates summation over all points that include event A.

Tails Heads Heads Heads (c)• (d)e ~:::: H.f:1~5 :}/It!~ ~··.-:i::,::;::;:a:::=ffi~= {a)• (b)• ,-:::::::::;~;::~· . ·. -:-:-:-:-;-;.·;~ FIGURE JO.I Simple example of a discrete and finite sainple space._H ere the <)\{11 space pomts correspond to all possible ontcomes of "tossing a com" twice.

}/ll l ))Jr@ ..............

;.~ 10.l Definitions 425 In most situations treated by statistics, equal probability is assigned to each sample-space point, a condition we will maintain throughout this discussion. Thea Pi=-, n being the total number of sample-space points, and P(A) n(A)' ' where n(A) is the number of sample-space points containing event A.

For example, in the case of the sample space of Fig. 10.1, the probability of obtaining heads at least once is n(heads at least once) 3 P (h ead s ) = ------- = - n 4 while the probability of obtaining heads once and tails once (irrespective of order) can again be found by counting the appropriate points in the sample space of Fig. 10.1. We obtain . n(heads, tails) 2 P(heads, tails)=----=-.

n 4 10.1.3. Probability for the Occurrence of a Complex Event The probability tbat both events A and B will occur is called the joint probability P[AB] n(A and B), where n total number of sample-space points. The probability that either . A or B will occur is called the either probability + = P[A B] n(A or B)' :• :: and the probability that A will occur when it is certain that B occurred is ( ·called the conditional probability ::, P[AIB] = n(A and B).

- r · . n(B)

~:- 426 10 Elements from the Theory of Statistics . . . . . . . . . . . .

~ . . . ' . .

• • •, . • • .

I •.• .• -• • .• • • • .. • • • • . .. . .

..

. . . . . . . .-:-:-:-;-:~~ ;.. ; . ~ rh - ~ :?\}t~~:: (a) (b)

FIGURE 10.2 In the sample spaces shown it is assumed that all sample-space poinlS::;/i~I domain A contain event A. whereas all points in domain~ contain event B. (a) Therer e ~ x gi i '? s { tf / : J :: t :: l ~ ~ ~ ~ :; a ~egio11 where both event A and event B .can occur simultaneously. (b) No such \{:\:~i~j e:ictSts; events A and B are mutually exclusive.

. .}itli[~j t~lffjfj@ All these probabilities are defined in the sense of Definition 10.1.2 as ~j{@~ number of sample-space points that contain the stated condition divided \(f~@ffi~~ the total number of sample-space points allowed for by the statement.

withiij}JfW@ Figures 10.2a and 10.2b illustrate two sample spaces. All points domain A include event A while all points within domain 'B include even~f/©Wj it?{{$J B. The points contained i.n any intersection of the two domains A and include both events A and B. ··-:}=:::::=::1;@=~.· ·.:-:-:-:-:-:-:w:::t.

If such a common intersection does not exist in sample space, the twf:({t})§J :)Jf@.?~ events are mutually exclusive, and P[AB] 0.

It follows from consideration of Fig. 10.2 that + = + P[A B] P[A] P[Bl _, P[AB].

For the conditional probability Ml P[AIB] n(A intersection 'B) ):/::::~~: n('.B) • since the condition that event B occurred restricts our sample within do~- 'B. However, ::::::?~:~ ('.B) / }}:::~: i}/i@i@I ~ P[B] ::::: _n- .........

## 10.1 Definitions

and (A. . 23)

= = P[AB] n mtersection P[AIB] . P[B] P[BIA]. P[A].

(10.1)

If P[AIB] P[A], it means that the occurrence of B does not affect the probability of occurrence of A. We say that the two events A and B are independent. It then follows from Eq. (10.1) that ...

P[AB] P[A] · P[B]. (10.2)

Equation (10.2) in turn implies (when combined with Eq. (10.1))

that for independent events P[BIA] P[B].

To illustrate some of the ideas we have just expressed, consider the fol lowing. For the sample space of Fig. I 0.1 we may define: event A heads in first throw~ and event B heads in second throw. The domains are shown in Fig. 10.3, and it follows (assigning p 1/ 4 to each point) that 1 1 = -; = - P[A] P[B]

2 2 = - P[AB]

1 1 1 3 + = + = - + - - - = - P[A B] P[A] P[B] - P[AB]

2 2 4 4 '.B

## T-T H-T

FIGURE 10.3 The sample space of Fig. 10.1 including the domain A (heads in the first throw) and the domain '.B (heads in the second throw).

428 10 Elements from the Theory of Statistics = ~; = ~ P[AIB] P[BIA]

1 1 1 = = · = = P[AB] P[AIB] · P[B] P[A] · P[B].

2 2 4 Thus events A and B are not mutually exclusive but are independent.

10.1.4. Random Variable m. - To study a sample space ana l yti · c a11 y < 1 · nstea d o f geometn · ca 1 1 y ) , 1 · t 1 · s con:/ · : · :: · : · ~ . ; . : ?,;?,~~ ~~.·.·}.·.J·.·J".. .fh. r.~-h venient to use a numerical variable that takes a definite value for each every point o~ the sample space; howe~er, the same value m~y be as~ign~~ff{ff ~ <.)f::ti~i~ to several pomts. Thus, a random vanable used for the represent.anon taJ#j)Jrf@~~ a finite and discrete sample space will have a definite range and will ~~}f~l only di~crete values. As an e~ample, for the sample sp~ce of F~_g. 10.1, can assign to the random vanable x the value O for pomts (b) and (c ) (o i:i,¢./:~W:~ each of beads and tails), the value -1 for point (a) (both tails), and ~!if~~~~~ value+1 for point (d) (both heads).

:~}!:i}i?:Wi;~ 10.l~. Frequency Function } th~f }ij{J A frequency function (o f a random variable) is a function f (x) such ...../•~• •Z~· •f• f (xo) is the probability that the random variable x may take the specifi~f thf@~@f value xo. By Definition 10.1.1, f(x) gives the number of points in sample space that have been assigned the value of x of the random variabl~/i/Jf f i~!{{:~fit divided by the total number of sample-space points. The function f (x)

.· .·.·.·.·.·.¼.·.·.

defined only within the range of x and need not have a definite analy~9(tf:§ff form. For the example considered above (the sample space of Fig. 10.l)f{{:~t .......... .

. ' f(x) is just a table, as shown in Table 10.1 (see also Fig. 10.4). {{}fJ} TABLE 10.1 Example of a Frequency Function f(x) of the Random Variable x Sample-space point X f(x)

(a) -1 1 o.o (b,c) - 1 z (d) +l 1

## 10.1 Definitions

f(x)

,,....___._ _ _._ _ _._ _ ___,_)< -1 0 1 '> flGURE 10.4 The disuibution function of the discrete random variable x defined in Table 10.l.

The summation of f (x) over the entire range of x must give 1: I: J(x) 1.

aJ!

The probability that the random variable may take any value smaller or equal to x is given by F(x) f(r)

(<X and is called the distribution junction of x (or integral distribution function).

It is sometimes convenient to describe a sample space in terms of two or more random variables, a frequency function existing for each of them.

If these random variables are independently distributed in the sense of Eq. (J 0.2), the joint frequency function is If the random variable is continuously varying (for example, it describes the height of individuals), the probability of occurrence of the specific value x wheo a measurement is performed defines the frequency function f (.x) d.x of the random variable x. The random variable may now take any value within the range of its definition. Note, however, that the probability of occurrence of the exact value x is zero, while it is the probability of occurrence of some value in the infinitesimal interval dx about x that exists. For a continuously varying random variable, we have r+oo /(x) > 0 and f (x) dx = I.

./_ 430 10 Elements from the Theory of Statistics Similarly lb f(x)dx P[a < x < b] a < b and = { F(x) f(t) dt.

·+rill@~ 10.1.6. Some Definitions from Combinatorial Analysis .·\::::}f~ (a) Perm_utations. A p~nnutatio~ of n objects in groups of r obje~~-ii~fii~ defined as follows. Consider n ~bJects; any group of r of tl1~se obJeC~f?ffj when ordered, forms a permutation; the same group of r obJects, wh¢~/i~~ ordered in a different fashion, forms a new permutation. As· an exampl¢J~~fj consider the three objects: ·}()J@ . ::/;;:::::t.r.* 0, b., 0 ::\\::~:ifj 1JJ{j}§i~ There are only six possible permutations of three objects in groups of ::::::::;~:=::::?: ·:f!i!f!]JJm 0~, b.D; DO, OD; ~O. 0 ~ We state without proof that the number of possible permutations ofn obj~~(@@ .\/{tm in groups of r, n Pr, is III nP, n(n - l) · · · (n - r 1)

n! )

1I = )111 TMn nPn n! (n - r)! 1 as 1t must be. .-}:}f ~@ (b) Combinations. A combination of n objects in groups of r objects:it.{I~ ~fi~ed as any ~ou~ing of r objects out of the origi~al n. The ordethrein~j,/ri/ {W jJ/;1 Wlthlll the grouping 1S not relevant. Thus f Of the preVlOUS example ·)/)~@ are only three possible combinations . . :{!)if ):}:~i~ Db., OD, Ob..

.·.·.·.·.·.·il n r,[ n ], it}!~ The number of possible combinations of objects in groups of }fjf~ n] n. -:-:-:-:-.~ I r [ - n Pr - ---- ....

.·.·.·.- r ~ rPr - r!(n - r)l · .. } j @ ·.·.·.·».-.

·.·.·.·.-.,.,« ':/ ;:;:~~ .\(:~ . \:J@.

.:/ =:~m 1 0. 2 Freq u e n c y Fu n ct i on s of On e Va r i a b I e 431 (c) Note. Note that = = n ! n · (n - 1) ! 1! O! 1.

10.2. FREQUENCY FUNCTIONS OF

## ONE VARIABLE

10.2.1. Definitions Let us assume that a population (for example, all the possible outcomes of an experiment) can be described by a frequency function; we may attempt ::::- .1·.·.

: ~ ::: / : to find this function in two ways: (a) By the use of a mathematical model based on the definitions of the ::::: ~:::: previous section, thus obtaining a "theoretical frequency function."

: . • . · . . .: ~ ·. · ; .. (b) By observing a sample of the population and determining its ;::::· ., r .- . ·.· · .. "empirical frequency function."

r ... · • - . . . · · · t . . . · The advantage of obtaining a frequency function for a population is that f :. the few parameters invo]ved in the frequency function suffice to describe ::::: completely the entire population and thus provide as much infonnation as tlte;t~~;:~~v;e~~~y with populations that can be described by a i__j _l_ • .••• frequency function depending on a single variable. To obtain the empirical ::==··==:=_·=:::_-::::::::·_:_ frequency function it is best to divide the members of the sample into classes (d efined by the random variable) and then make a graphical plot f . or histogram of the sample. If we try to describe the histogram, the first f \ obvious features are its location and its spread.

f .

A very useful set of measures are the moments of a histogram, defined f( in the usual way (moments of forces, electric moments, etc.). Thus. if x; ~=::.. is the value of the random variable for the class i and if fi is the number {/ of events in this class, the kth moment of the empirical frequency function f/ :- about the origin is .-.·.·.

~~::·· f( I ~ kf, I = - ::::::- mk L....,, x, i' i } .

n aJI i ~[ where n is the size of the sample. Similarly, the kth moment about any f ( other point xo is ===~=::: 1"

:,,:.·.· .

~:::: = - ~L mk(xo) L_;,(x1 - xo) k fi- i::-: n alt i ½} : lrlt/.:·.

~\/ ~_.•/:,.,-_:' ...

432 10 Elements from the Theory o·f Statistics 10.2.2. Mean and Standard Deviation m;, q~{j{@ The first moment about the origin, is called· the mean and will ~·-· ....... rt denoted by m · <::=::::::::=.::=l ·°" ::)/!{ l · • 1 fi· - m - - (10 3 I-~::::.::-:::-::-:::-:.-~~::: n all i ?}}f@!

lf~ ( commonly called the "average" of x ). The second moment about the me~{f m2, is called the variance; its square root is called the standard deviatioij})fW:.

~ifJ fli and is denoted by s: s has the same dimensions as the random variable . ,--- - ---- .·.·.·.·.-..••, «."/..

1 . . .<:::::::?~:~: (lo.Jfil~ = rmi. Ii- s === - L<xi -m)2 l ri!It ~l i '.j An often used relation pertaining to s is .

2 = ~ = ~ + 2 s ~(x; - m)2 f; L(xf-2mx; m )f; •••••••• 2 = -1 ~ 2 2m~ + 2 s ~xi f; - - L,(xifi) m nalli n 2 = -1 ~ 2 2 s L., (xi Ii) - m n all i usually written as f1x2 = x2 (x) . (I0.5i{{:~ :i ::::\/:=:%=: In most cases the mean and the standard deviation are the best measurei/~:=:%=: .· .·. ·.·.·.,,._-.-,.,._ function; ~ (@~@=~ (c ontain most information) of an empirical frequency there ij/}W~ nevertheless, cases where they are very poor measures, and instead it much better to give other location measures, such as the median or ~~\t~ geometric me~, a~d so on; and other variation measures such as the ran~:?:},ili~ or the mean vanat1on, (1/n) I: fxt - ml ft, and so on. .)(;Ji~ 10.2.3. Theoretical Frequency Functions :{)~W ··::::::::::~~ :-:::::::J@ #!i~f As m_entioned before, ~ theoretical frequ~ncy function f (~) might be the discrete type--that 1s, the random vanable x takes only integer value~!{~ -:::-:::•::I-:,:W% .-::::::~~ ·1!!!{$ . ;:::)W.

· -:,:-:-'.~

## 10.2 Frequency Functions of One Variable

or of the "continuous" type. Most of the discrete random variables usually represent the number of successes, or of counts obtained, etc. In going from discrete frequency functions to continuous ones, obviously all summations are replaced by integrals.

Moments are defined as in Eq. (10.3), but instead of the empiri cal frequencies /;, the theoretical frequency function f (x) is used; the theoretical moments are designated by Greek letters, Latin letters being reserved for the empirical moments. ..

Thus, the k th moment about the origin is .r=+oo .

µ,~ xk f(x).

X=-00 The first moment about the origin gives the mean; and is denoted by µ,;.

µ, = The kth moment of a theoretical frequency .function about its mean 1s x=+oo = µ,/- µ,k (x - f (x).

x=-00 The square root of the second moment about the mean gives the standard deviation and is denoted by ..[iii: CY x=+oo µ2 (x - µ)2 f (x).

x;;::;-OO 10.2.4. The Bernoulli or Binomial Frequency Function This basic frequency function is applicable when there are only two possible outcomes of an experiment. as. for example, the occmTence of an event A or its nonoccurrence (we designate this by B). If the experiment is repeated n times, the random variable x describes the number of times event A :::: occurred. The frequency function-that is, the probability of obtaining a <· certain x~is given by .·.· r:::: n~ /(x) ----pxq11-x, (10.6)

i:::. x~(n - x)!

~} where pis the probability that event A will occur in this experiment (d efined f/ = ] - in the sense of Section 10.1.1 ); and q p is the probability that B will ...

/' ~/ happen, namely, that event A will not occur.

.'./.... ·· c:::-: ~:::.: ti!: ., .

::;::: :::;:: _,,_._.

:111 ffl 10 Elements from the Theory of Statistics • -:#}:Jj To prove Eq. (10.6), consider-the probability of obtaining event A, times in a definite sequence }:/:=:::=m AA·· · A BB··· B· --....-,' x n-x this joint probability of order n is according to Definition 10 .. 1.3 = \ x n-x ~pp ..... p_ qq_ ... • q, p q tl-X since the outcome of consecutive experiments is independent. Howeve~\ \fj als~(Aa]

any other sequence, containing the same number X of occurrences, is a satisfactory answer, since we are not interested in the order of occurrenc~/ ]fj ~{}ff of event A. Thus we must sum over all sample-space points that give @@]

occurrences; the number of all such sample-space points is given by ~~f permutations of n objects in groups of n when x of them are alike (hav~(:}~~ .)!)Jm probability p ), which is ·····0: n l · ·:::::::f:~ -))?4 . l' ....... ~ X I (n - X) ·:::::::,:~ . . . '\:?~ :):l~ completing the proof of Eq. (10.6). ·.

iri//Ji: The frequency function fulfills the normalization requirement as \}\J~ should, since · L n L1l ' , \{ }\J[~f f(x) == n~ I pxqn-x = (p + q)" = [p + (1- p)]'1 = 1.

O O X. (n X). -:-:-:-:-:-:-· (10.?f}){Ii x= x= !!ill/I 10.2.5. Moments of the Binomial Frequency Function From the definitions of Section 10.2.3, and since the range of xis from O·\ ::::=:~ -::::::::~ ro~~h~ 0 ~ t\l '°" '°"

= = fl = Pl ' µ, µ' xf (x) x n. pxqn-.t .'.:::;;;~: 1 ~ LJ x!(n. - x) ! I:-:I-;.« =txxl(nn~:;xqn-x ;c.::::l .·.'N ~ (n - l)! x-1 n- x np L, (x - l)!(n - x)! p q · x=l /[ .•.

·-=: · 10.2 Frequency Functions of One Variable 43S ~: -: :: If we let y x - 1, it foUows that :.:.·.

'°' :- 11-I " - n (n - l)l Y l(n-1)- y)

:,, µ. - p L, y.' [( n - L) - y).' p q ' -: y=O ::· :: ... + = . : , where now the sum is equal to (p qt-• l. Thus µ. np. (10.8)

Next we wish to obtain the second moment about the mean, µ1 o- 2 • We first calculate µ2given by ..· .

·.

:=.

. : . · : - . . : µ' = '° n 'x2 n. I pxqn-x_ :.=·.: 2 ~ x!(n -x)!

,', :~: :=: ::: We use ::: 2 = + x x (x - 1) x so that n I J.L2 L x(x - 1) 1( n~ )li'q"-x + µ.

•:• X. n X • { .IC= 0 ,•. n ;:: = ,r ! + t ~ x(x - 1)----p:cqn-x µ.

L; xl(n - x)!

x=2 :=· ,•,, ,,•:,,• :::. = (n - 2)! + :=.~ n(n _ l)p2 "°"'------p'-r-2qn-x µ.

t L; (.x - 2)!(n - x)I x=Z and letting y = x - 2, as before, the swn is equal to ( p + qt- 2 = l and :::= we obtain :::: ~= = + = + •.• ~ n(n - J)p2 µ. ,,2 p2 - np2 np.

.• •...• .

]i Next we use Eq. (10.5) to obtain ::: (!: µ.2 = a 2 = µ.'z - µ, 2 = -np 2 + np = np(l - p) = npq.

,:•::. · Thus ....: ..· -.· ::~· = .Jrijiq. ( 10.9)

.-.·• :. · O' ?~:~ The binomial frequency function is applicable to many physjcal sit ·:-. uations, but it is cumbersome to calculate with. When n becomes large, ...: ..

:;:: ..

;.: :=~~ .;:: ::: .;:· ;,::: ··\:::l:{ff //ij/il/1/f- , TO Elements from the Theory of Statistics .\ however, the binomial frequency function approaches either the PoissQttn~lt ~ ld(j[j j~~ the Gaussian frequency function, which will be discussed in Sectioos and t 0.2. 7. In order for the binomial frequency function I to approacn;,1 i :11 ){jj~ Poisson distribution 12 must be large, for e~ple, n > 100, but µ np must be fimte and s~all, -:})/J~ for example, p < 0.05. ·:{/{tfl }));ti~I Gaussian distribution n must be large, for example, n > 30, :/\\i{l!~IIfii j and also p must be large, for example, p > 0.05. . I Jff 10.2.6. The Poisson Freqnency Function .

This ~s still a _frequel.lcy function for the disc_r~te random vari_able x, w~~ ~escnbes, m S~tton 10.2.4, ~number of times event A will be obtrunf!:i:WI Contr'!-~tti~ tf the expenment IS repeat~d n times when n -+ oo fo_r ~lar~e n ).

anal~t@I to Eq. (_10.6), however, neither 11 _nor p appears exphc1tly m the </::::::::~ expression of the frequency funcuon, but instead only their product :::_:/)f@ y np, (10.lQ)\:=:::~ ..· .'.·.·.·.·.·x..;-·· whic~ re1:'1~ finite despite n -+ oo, since p -+ 0. The Poisson frequenci~1Jlm~ <:::::::::Jl function 1s given by \)}]@.~ yxe-Y []lft f (x) = , (10. l_lf f X. ·:?):::=:=f.:?, and it is shown in the next section that y is the mean of the distributiori.( :\:~~f=: .........· .·.·-:,,;.·.

governed by Eq. (10.11). :\::=:::~=:::: xfJ1[~l To prove Eq. (10.11), let us first note that since n is large, it (but not may be treated as a continuous variable; second, we will assume that for :g/:\:~l~~: small (differential) number of trials dn, the probability of obtaining evenf;}}lf A once is proportional to this number of trials: that is, :}}~J~:: (10.12.\-:::\::::l:;;:t~~J: P{l, dn} J..dn, where ).. is a constant. Note that Eq. (10.6) fulfills this requirement fo1f\{*f o~/({t ~ x l in the limit that p -+ 0 or q -+ 1. In terms of sample space assumption means that the density of san1ple-space points containing even({Jf~ area~_)Jff: A is uniform in the limit of a differential element of sample-space Ti/ii 1S ee, however, lhe detliled discussion in Section 10.2.9. · ·.·.·:-::;::-·-· <:::=:-... -;.;::; ::::;~~·~ .· .::::;~: ~ .·.·.,ili· ,·:::;:~~: f:::· :ii::: 10.2 Frequency Functions of One Variable 431 The Poisson frequency function then follows for all populations for which :::_:·!==:_.::::): assumption ( l 0.12) is valid.

Let P {x, n} be the probability of obtaining event A, x times in n trials, so that P{O, n} is the probability of obtaining no events A inn trials. Then \:_=_=_=_.·:.

the probability of obtaining no events inn+ dn trials is P{O,n +dn} P{O,n} · [1- P{1,dn}]

since the events are indepedn;d~e n-t. Using Eq. (10.12) we obtain + = P{O, n P{O, n} -P{O, n} . >..

dP(O, n} - dn P{O, n} · .l, which bas the solution ln P {O. n} -n}..

P{O, n} e-nl (10.13)

and use has been made of the initial condition that for n 0 P{O. O} 1.

.•.

.. In a similar manner we obtain + = + P{l, n dn} P{l, n}P{O, dn} P{O, n}P{l, dn), where the two possible either probabilities are summed. Making use again of Eq. (10.12), we may write the above result as + = + P{l, n dn} P{l, n} · [l - ).dn] P{O, n} · ).dn by further transforming and using Eq. (10.13) as well, + = dP{l, n} .lP{l, n} - ).e-nJ. 0.

dn The solution of this linear first-order equation is straightforward, leading to [! C]

= + = P{l, n] e-n). e").Ae-n).dn (nA)e-•\ (10.14)

.· making use of the initial condition P { 1, O} 0.

2Since the increase in the number of trials dn is differential, the possibility of obtaining more than one event in dn. is excluded.

438 10 Elements from the Theory of Statistics In general the following recursion formula holds + = _dP_{_x_n, _} 11.P{x, n} - >..P{(x - 1), n} 0, dn which is satisfied by (An)xe-nJ..

= -- f(x) == P{x, n} as can be verified by substitution. \{)~:~~ Thus Eq. (10.11) has been proven, and we can identify the proportion~~\)@~~!

ality constant A as the probability that event A will occur in orie trial.3 As\}!}~~ = that)})f pointed out before, however, it is only the product y )...n == ·p n may be properly defined: it is the theoretical mean of the discrete random/{:J}i~ ·.·.·.·.·.•/.•,•, variable x when the same (large) number of n trials is repeated many times/{);}~i .··\:\ff Equation (10.11) correctly fulfills the normalization requirement !tM n L =o o _ L00 -y' - _ }ii f (x) - e Y e Y eY - 1 -·-:-:-:-:-·-:-:-: x=O - x=O x! - - .

It is shown in Section 10.2.9 that Eq. (10.11) is the litniting form of}:=::l:=: .\)!ft .&}. (10.6) when p -+ 0 and n -+ oo.

.•.•.•;",."'w•-,.

. : ::::::::::::::: :: :: :: ::::::::: 10.2.7. Moments of the Poisson Frequency Function . :\~~~~~}~~~ .·.·.·.·-··.. - ..- :/:::::::;:: {/Jf Following the approach used in Section 10.2.5, the moments of the Poisso~ frequency function will be obtained by direct evaluation of the defining :}({~ \)Jf equations; note that as n-,)- oo the upper limtit o f xis also oo: X=f:00 mi: yxe-Y yxe- y .

})/)~i = = = µ, µ,1 x=O x x! x=I (x - l)!

....... _ .. ....... .

-:-:·=·=.,.=·= = = = :}Jf~ e- Yy y<x- 1) e-YyeY y.

}!\!~!~ x=l (x - l)!

:; Thus µ, = y ( 10.16) ?::::;:;: ::::::~~::: 3 P{l, l} = >..e- >.. ~ ,\ when l « 1.

TO. 2 Freq u e n c y Fu n ct i o ns of On e Va ri a b I e 439 as expected from our previous discussion. We see that through Eq. (10. l6)

we obtain the physical significance for the parameter y. Further, r -y -y)

µ; = " 00 x 2 e = "0 0 ( x(x - I) y X e + y ~ x! ~ x!

x=O x=O oo ( .x ) oo (x-2)

_ -y L Y _ -y 2 L Y -=- 2 + + + - e (x - 2)! y - e y (x - 2)! y - y y, x=2 x=2 and using Eq. (10.5) we obtain = = µ,; _ = + = µ, a2 µ,2 y2 y _ y2 y.

Thus -Jy. (10.17)

(J The close analogy of Eq. (10.16) to Eq. (10.8) and of Eq. (10.17) to Eq. (10.9) should be clear; also the derivation of these equations is completely analogous.

10.2.8. The Gaussian or Normal Frequency Function and Its Moments This is indeed a most important frequency function because (a) it is a lim iting case that many frequency functions approach; (b) the distribution of most physical observables is satisfactorily described by it; and (c) mea surements containing random errors are distributed normalt y about the true va1ue of the measured quantity.

The Gaussian distribution gives the frequency of the continuous random variable x in terms of two parameters a and b, which are the first and second moments of the frequency function. In its normalized form, the Gaussian distribution is given by (x -a)

f(x)dx = b../ l irr exp [ - 2 l b ] . dx (10.18)

!'. and is shown in Fig. 10.5. The range of the variable x is from -oo to ·: +oo. In order to show the nonnalization of Eq. (10.18), as well as to find : the moments, it is useful to know the values of the integral of x" e-ax , 440 10 Elements from the Theory of Statistics variaii~t::=:=a~:~ FIGURE 10.5 The Gaussian frequency function normalized to zero mean and unit f(x) dx = (1/v'2rr)e-x 2 f2 dx. Note that the probability of finding a value of x betweJ({Ji x1 and x2 is proportional to the corresponding area under the Gaussian. /}}~ TABLE 10.2 Value of the Integral f (n) = J 0 00 x" exp (- ax2 ) dx n f(n) n f (n)

½J tr7a 1 l/2a ¼J;r7a3 2 3 1/2a 4 ~Jn/a5 5 1/a 3 /( n ) = Joo x n exp ( -ax 2 - } d x = {2/(n) when n i . s even - oo O when n 1s odd which are summarized in Table 10.2. To obtain the moments we proceed\(:~{t :{\t as before · j+oo exp[-! (x -a) 2 1A ~ µ, = = x ] dx.

b 21'l -co 2 b We let x tb + a, dx = bdt; thus [J+oo l+co = + µ. _1_ bte-<iz/2) dt ae-<t2/2) dt] .

.j21i -oo -0()

According to Table 10.2, integrals with odd powers oft vanish, thus µ, a. (10.19):J:}.

## 10.2 .Frequency Functions of One Variable

Similarly -a)

l +c;,o [ (X 2 µ/2 = b,/ 1 ' hi -oo x2 exp -21 b ] dx with the same substitution [J+oo µ2 = _.!_ b2t2e-<r"l/2l dt r: ,/'hi 1_: 00 00 + 12 2 + 2 2 2 2abte-< 1 )dt a e-U ! >dr]' so that by using Table 10.2 we obtain [b2}Jg;" a2../2Jr] b2 µ,;_ = ~ + = + a2 and, using Eq. (l 0.5), Thus a= b. (10.20)

We see that through Eqs. (10.19) and (10.20), we obtain the physical.

s.ignificance of the parameters a and h of Eq. (10.18). Thus, Eq. (l 0.J 8)

takes the form x) 2 f (x) dx = a-..l/ 2ii exp [ - 1 ( µ, a - ] dx. (10.21)

It is sometimes useful to transform the random variable linearly so as to obtain a frequency function with zero mean and unit standard deviation; the transfonnation is x-µ. dx = -.

y=-- dy (l er and Eq. (10.18) becomes (as shown in Fig. 10.5)

f(y)dy _l_e-<i/2) dy. (10.22)

./irr 442 10 Elements from the Theory of Statistics 10.2.9. The Gaussian Frequency Function as a Limiting Case ~ JjJ/1 In the previou~ section we ~ave Eq. (10.l~) ~thout proof. We functio~:=:::=:=:*~ now show that 1t can be obtained from the binomial frequency << >)}ifJ~ Eq. (10.6), in the limit of n ~ large and lnp - xi np.

= '( n _ l )' X n- x f (x) p q .

X. n X .

If n -4' oo but np -4' µ, remains ,finite, we may write = + f (x) n(n - 1) ·. · (n - x 1) . (np)x . (l _ p)11-x )f!!!)llwl nX X t ::::;::::::~if= l[l - (1/n)] · · · (1 - (x - 1)/ n] (np)x . n f (x) = -------- - · -- · ll - p) . oo.2~tt~~.:~-.:=~ (1 - p)X X! ' • However, (1 - p)'1 [(I - p)-(1/p)]-np ~ e- µ, since from the definition of e, + 11 = lim (I z) z e z-+-0 and in the present case we have p ~ 0. Further lim 1(1- (1/n)] · · · [l - (x - 1)/n]

n-,oo (1 - p)X because p ~ 0 and xis finite; by substituting the last two expressions intqf\J:~{ //ff} Eq. (10.23) we obtain the Poisson frequency function, Eq. (10.11): }~iJI ~x:!-µ · f (x)

an~(Jl We now use the further condition that x be a continuous variable xi << th~/liJ lnp - np, namely, its deviations from the meanµ, be small; then ·-:\(lt following approximate expression is valid: - - µ, µ-x µ,-x 1 µ-x 2 = + = 2 + ....

In x In 1 x x - x ( ) ( ) ( )

## 10.2 Frequency Functions of One Variable

Hence 2]

µ (µ -x ) [ l (µ -x )

x ~ exp x exp x and ~ ~ "'x"

µ,x exp(µ, - x) exp [- (µ, x) ]- , From Stirling·s formula we have x! ~ ./fix.xxe -x and by substituting (µ,Y and x! into Eg. (10.11) we obtain µxe-µ. e-µ.x:,:e(µ,-.x) exp { -.1((µ - x)2 /xl} f(x)=--= .J'iiixxx 2 X t e ~x (µ -x)

- - - .J2 1- i ix exp [ -- 2 1 ft ] . (10.24)

Thus the binomial frequency function in its limit approaches a Gaussian frequency function with mean µ np = ..Ji ~, standard deviation a ~ (10.25)

Iµ - where x ~ npq follows from xi <<µ,and p ~ 0. From Eq. (10.25)

we see that the moments of the limiting Gaussian frequency function are the limits of the moments of the original binomial frequency function.

10.2.10. Properties of the Gaussian Frequency Function Let us now interpret the frequency function given by Eq. (10.18). We could refer to our original example of obtaining event A, x times when a choice between A or B is made n times; x then can vary from Oto n in integer values. It is easier, however, to consider the measurement with a ruler of the length of a rod; we let the continuous random variable x represent the result of one measurement. If the true length of the rod is xo, Eq. (10.18) specifies that a result between x and x dx will be obtained ·.·.·.·.·.·.··'.:~ :\\(/~ 444 10 Elements from the Theory of Statistics with a frequency 2]

1 [ 1 (x o-x ) 26)??\~l f(x) dx = a.J2n exp - 2 (j dx. ( 10 . .· :::r/i!!Iif!I~il~l ~\}}Jfi One may also say that the probability that the measurement will ')'ielcf result x" between x and x dx is given by Eq. (10.26). In simpler word${~{@f~~~ #{}J~~Ij if N m~asu~ments are performed, a result between x1 and x2 is likely be obtained m n(x1, x2) of these measurements, where - _:::\:::-===©~=~ 1x x)

(xo - ]$jj = = , N J 2i 2 [ 1 -- ] .)j;Jf~!~§ n(xi, x2) N · F(x1, x2) exp - 2 dx · 2"Jr (f XJ <5 ::::;:;::::~::~:::::;~ -~;:::::~;:;:;:~;~:~ (lo • 2 7·.JI.···-·-·.·-~-"/. ...

. . -~:::):t:1?~=~ as shown m Fig. 10.5. :}?=?:@~=~ Note that in Eqs. (10.26) and (10.27) the standard deviation o- is dete~fifli]?

thei{:~~t}~~: mined by the conditions of the measurement The applicability of ....

lie~ ·. .. · :: .· : . : - = .- :=:~.,;..=,.=_.~,.~ Gaussian distribution to the results obtained from such measurements '-~····~·· larg{. i{~}Jl in the fact that: (a) n, the number of (least) divisions of the ruler, is ·:.)Jf&.~l and (b) the errors in ~easurement lxo - x I are s~all_ as compared to x.

In Table 10.3 are given the values off (x) and 1ts mtegral, F(c), for th¢f::::\:=:=:=:::: ·//}/@{ normalized Gaussian function (Eq. (10.22)). .· dti;{\fl?- From Table 10.3, for example, we see that half of the measurements _:}}JJ/ yield a result x between - 0.690- < X < XO 0.69a of the results may yield x, such that X >XO+ 2fJ.

## 10.3 Some Numerical Values of the Normalized

an Function - .J2ii exp(-x'-/2) F(-c.c) = f~ f(x)dx f(O) == 0.3989 F(-1, 1) = 0.6826 = = f(l) f(-1} 0.2420 F(-2, 2) == 0.9554 = = /(2) f(-2) =0.0540 F(- 3, 3) 0.9974 F(-0.69, 0.69) = 0.5000

## 10.3 Estimation of Parameters and Fitting of Data

As another example we see that a result x in the small interval b.x about xo, will be obtained (0.3989)/(0.0540) = 7.4 times more frequently than + m.

a result in the same small interval ~ about xo 10.3. ESTIMATION OF PARAMETERS AND

## FITTING OF DATA

In Section 10.1 the basic definitions were given; in Section 10.2, analytic expressions for some frequency functions were obtained. We will now see how statistics can be applied to the interpretation of a measurement or an experiment.

We can consider one or more measurements to form a sample of a pop ulation that obeys a certain frequency function; we are then faced with one of two estimation problems: (a) Given the frequency function and its parameters, what is the probability of obtaining from a measurement the result x?

(b) Given the result x of a measuremen~ what are lhe parameters of the frequency function (or the frequency function itself)?

In physics we are usually faced with estimation of type (b), since a set of experimental data are obtained, and it is then desired to reduce them to a few parameters that should describe the whole population and therefore, also any new measurement that may be performed.

There are several methods for obtaining "estimators" to an unknown parameter. Some of these methods are almost subconsciously applied, but most of them can be derived from the principle of ''maximum likelihood', introduced by R A. Fisher in 1920.

10.3.1. Maximum Likelihood To apply this principle we must have knowledge of the normalized frequency functions of the variables Xi that form the data, f (x;, 0), where 0 is the parameter to be estimated and upon which the frequency function depends. We may then form the product of the frequency functions for all observed variables, .C(x1, x2, ... Xn, 0) f(xi, 0)/(xz, 0) · · · f(xn, 0), (10.28)

. ·,·.·.·.·.·.·..-.·==--~ :)\~?~~ ii/ii!/{@~ 446 10 Elements from the Theory of Statistics . )}}{@ ,c,_.JfJ Jij which is called the likelihood function for the parameter 0 (note that . ..

·.·.·.·-·..-.·.,;.,; not a frequency function for the parameter 0 ). The theorem of max.unu;'•¢, ;/f}*= the:~~f?J~: likelihood then states that the value of 0, 0*, that maximizes L (for .. '·.· . .- .-.·.-.-..:.b.

'\)i/Jj of observed data) is the best estimator of 0: re a 0) ...: ) }f }§i .v x1, x2' ... Xn' ··:<-:·:·:·:-:-:-:-.-:-: 0 '!Iii~ ae 8=0· · .~f} J% Jn practice, it is almost always convenient to work with the logarithm ,.

. J, sm ce w e n == o g N ,.

s maxi m um, so w ill al s o be . I. .

:·..·.)·.}·.··\·;;:}t:?».B·.

As an exrunple, we consider a set of n data Xi that obey a nonnal frey(,}(~* h<i..~ 'f' .. i i' @.. ·f=~-=·· quency function about a, with a standard deviation a; let us seek the value for the parameter a: \ :/ ~::~::: cr~exp[-Ha~x )2]. (10.24~/I = 1 f(x;,a)

Then TI L := f(x;, a)

i ::::l and )2 1 a - x· logL -nlog (cr.J2rr°) - ~n ( a r t=l aw n --~a- oa - (f i=l Setting (oW)J(aa) 0 leads to the estimat '"'a n * :: -t;~ -Xi =0 = 0 · :1111 L.J Iii (12 or 1 ~ )}[:::: a· ,le = - ~ Xi - (10.31) ·. ' n :: i :::~ ~ ~ t :f n 1 Thus if a set of measurements is distributed normally, the best estimatoi·:)t} (first}it: for the true value of the parameter is the mean of the measurements ....

.,.,..

moment) · ::::::~~~;:

## 10.3 Estimation of Parem-eters and Fltting of Data

Similarly we may obtain the estimator, (T*, for a, by differentiating &:j. (10.30) with respect to er t[(a-x;) (a-x;)]

aw=-~+ aa a 2 CT • Cf aw /oct = and selling 0 gives (10.32)

where, in Eq. (10.32), a should be replaced by its estimator a* given by Eq. (10.31). Again we obtain the familiar result that the best estimator for the standard deviation of the theoretical frequency function is given by the second moment (about the mean) of the observed measurements.

The principle of maximum likelihood can be further extended to give the variance S2 of the estimator 0~; that is, if the determination of estimators 0* is repeated, the values so obtained will have a standard deviation S, wbere a2iv s = - a0 (10.33)

2 2 · We may apply Eq. (10.33) to our sample of measurements that obeys a normal frequency function, where W was given by Eq. ( 10.30). We obtain 1 2W Ln l n = - = = si- aa2 a2 a2.

Thus the standard deviation of the estimator will be (J' = (10.34)

S .jn' where n is the number of measurement.c; used for obtaining each estimator.

Equation (10.34) is a weU-known result that we wiU obtain again when we discuss tbe combination of errors in Section 10.4.

10.3.2. The Least-Squares Method Until now we have discussed tbe case where all n measurements are made on the same physical quantity whose true vaJue is a, for example, the data of 448 10 Elements from the Theory of Statistics .) !!11111 ·.·.·.·.·.---~~ ~ r /,!

/i 1 l

## I I

1 1 I ..__~.___.___ __. ....__ _ -i_;i,: X1 ~ x 3 Xi obtain~4,(\i~§t FIGURE 10.6 Least-squares fit of a two-dimensional curve to a set of data points /:::~J&, for different values of x. Note that each data point has associated with it a different errof ·-:\{/;:la as indicated· by the flags; this is taken into accounl when forming the least-squares sum.

. . ::: Iii Eq. (10.29). However, consider now a set of measurements yielding values( :}i:~~~ Yl, yz, .. . , y,, depending on another variable x; the corresponding tru~{)~?i values of y, which we designate by y, are assumed to be a function of x arici){{~{!

.· .· .· . I · l .·---~ l ·-·.

of one or more parameters av common to the whole sample. Thus we write/{:}~f} Yi = y(xi; aa, ... , a,). (10.35}; Further, each measurement Yi has associated with it a standard deviatimf: ::::=:?::::: ai, which is not the same for each point. This situation is shown in Fig. 10.6/ )){}j It is possible that the form of Eq. (10.35) is known or may be correctly}\jf inferred from the physics of the process under investigation, in which case)!}}@ the estimation is reduced to finding the best estimators for the parameters\\}!{f av. If, however, the form of Eq. (10.35) is not known, various functional/)!@f i W6:}\if!

relationships must be assumed, for example, a polynomial of order k.

then speak of a are\:i(}l fitting cw-veto the data. Even though special techniques follov.ring\\?t \ developed in Section 10.3.4 to ascertain whichcw-ve fits best, the discussion is generally applicable. ..)}j{J The method of least squares follows directly from the assumption tha(//}~; ·.·.·.·.·,/,,.•. .~ ·.

each individual measurement Yi is a me1nber of a Gaussian population witl:({}~:~~: a mean given by the true value of Yi, y(xi; a,J; for the standard deviation))f§i '·.· .·.•."..•,;,.· of this Gaussian we use the experimental error O'i of each measurement{({{~: Then in analogy to Eq. (10.29) we write for the frequency function of y({)ff!

1 { 1 y· - y(Xt. a>.) } ·:!/!!iiiIf@i§)

= ..fiii < f(y;; x;; ai.) exp -- [ ' ' ] , {10.36}/$.

a, 2n 2 C1i JI l0.3 Estimation of Parameters and Fitting of Data 449 and in analogy with Eq. (10.28) we form the likelihood function IT £.,(y1 · · · Yn; XL··· Xn; a1) f (y;; x1; a,\).

i=I at We seek the estimators that maximize this function, or its logarithm W ..

W log£., a1T = _ tlog (a;£)-~ [YI - Y:x;; (10.37)

i=l i=l I Since the values of ai are fixed by the measuremen~ the estimators a~ are those values of a>.. that minimize the sum .,..,< _ ~ [Yi - y(x;; a1)]

i....J 2 • (10.38)

JYl, - i==l O"; that is, those that give the "least-squares sum." They are obtained by solving the simultaneous equations A= 1 to v.

10.3.3. Application of the Least-Squares Method to a Linear Functional Dependence The simplest case of functional dependence y(x) is the linear one: y = ax +h.

If we assume that every measurement y; has the same standard deviation (statistical weight), we may obtain the estimators a* and b* that minimize Eq. (10.38) in closed form.

= = · · · = = Since a1 0-2 an a, instead of Eq. (10.38) we need only rru.runuze ~ L[yi - (a+ bx;)J2 .. (10.39)

i=l 450 10 Elements from the Theory of Statistics Hence a:R.

- = L)Yi - + = -2 (a bxi)] 0 aa i=l 8:R. L = n + = -:--b -2 {[yi - (a bxi)]Xi} 0, a . .

1= which after some rnanipulation4 leads to * LX[ LYi - LXi L(XiYi)

a--------- --- - nr :_x; - L,Xi LXi b* _ n L,(XJYi) - LYi I:xi - n L x'f - L E Xi Xi • The standard deviations for the above estimators may be obtained by ajf \~~:(:~t~= )/\tf~j extension of Eq. (10 .33 ), which now yields a symmetric square matrix · . ·:::::::::J~~; a2w 1 a 2M .·::::\:::::~:=~tj H).v = --- = ---. (10.42):::=::~:=:~:=~ 2 )i)}!J}Ji aa>-oaµ 2cr aa>-aa~ · The elements of the inverse matrix give the variance of the estimator$\{}1?

10.4{/J}t a*. A complete discussion of this error matrix is given in Section fof(fft suffice it to say here that the usually given expressions (Eqs. (10.43))

roo~(\ff the standard deviation of the estimators (Eqs. (10.41)) are the square of the diagonal elements of B-1 (see Eq. (10.63)). We then obtain ·:\/]{/ ,_--- I:xl aa• = J(H-l)aa = cr n I:xl- LXi LXi CTb• = j(H-l)bb = u / " n .

V 2 n ~xi - Ext I:x1 In case cr1 i= a2 =f= • • • # crn, it is M and not ::R that must be minimized/}}]%:~f J·f··(···l-"t·@~· Clearly, such calculations are best done using computer programs ..

fact, many packages and self-contained programs that are designed )~/)~§ft handle these kinds of problems are available (both commercially afr~)~~~§ .}}!t~t{ 4 . N o . t e that the second of the above equations is by no means equal to the first oif ~ :-:-:•:•:-"..-:,.:.-,: multiplied by x·. ·:r;:/iJ~?r"'i~ .II

## 10.3 Estimation of Parameters anji'Fitting of Data

through "shareware"). In this book, we default to MATLAB (see

## Appendix B), which is in fact well suited for dealing with problems formu

lated in tenns of matrices. For the problem of linear (or, more generally, polynomial) function fitting with equa_Uy weighted data points, MAlLAB provides the polyfit utility for exactly this purpose.

For more general problems, the reader is referred to /other textbooks on the subject of data analysis. for example, the problem of linear fitting with unequally weighted data points is discussed in Chapter S of Nume rical Methods for Physics, 2nd ed., by Alejandro Garcia (Prentice-Hall, Englewood Cliffs, NJ, 2000). A program linreg for this task, is described and the code is available onJ.ine from the publisher as a MATLAB m-file, c++ as well as in the languages and FORTRAN.

10.3.4. Goodness of Fit; the x2 Distribution We have seen how the least-squares method, as a consequence of the prin ciple of maximmn likelihood, may be used to fit a curve to a set of data.

Once the curve has been foun~ however, the necessity to ascertain quan titatively how good the fit is arises. This is important especially if the functional dependence is not known, a poor fit might indicate the neces sity for fitting with a curve of higher order, or a poor fit might indicate inconsistencies in the data.

Similarly, we may wish to test whether a certain hypothesis is supported by the data, in which case the goodness of the fit may establish the level of confidence with which the hypothesis should be accepted.

Let us first suppose that we know the true functional relationship of y to x, that is, y(x) f (x); we may then form the least-squares sum - ~ [y; - y(x,)]2 M (10.38)

-~ 2 .

a.

i=l The range of M is 0 < M < +oo but we would be sw-prised if :J'v( 0 and would be equally surprised if M was extremely large. Thus we have already a quantitative indication as to how well the data fit the known (or assumed) curve y f (x).

If a new set of data pertaining to the same experimental situation is obtained, and Eq. (10.38) is again formed, a new value M will result.

·· Oearly, if enough such measurements are repeated, each time yielding a value for M, we will obtain the frequency function for M. Once the :• :•:•:•:•:-:. .: . .: , ,: :: : : : : : :: : = :=:=:: :/:=::::::::::; . ·.·.·.·.-.·.·.. · . .· 452 10 Elements from the Theory of Statistics ·:/:/::::::; lli~i frequency function is known, it is .then easy to tell what the probability of; obtaining a specific M is. We may, for example, calculate that in 95% of..\!)/f the cases M < Mo; if then a specific set of data yields '.Ms > ·Mo, we know j((fi that such data should be obtained only in 5% of the experiments and can::}{\\ therefore be rejected. · ·.· {{}/ Obtaining the frequency function for the least-squares sum in this way -{))j )}if@ is obviously impractical. Nevertheless, it is true that the distribution of = be}\!Jf~ M is independent of the curve y f (x) and of G"i, and can therefore are(\\1fJ calculated theoretically; it depends only on the number n of points that x2 ·!/){t compared, and is called the distribution (pronounced "chi-squared") _..

:::::::::::~~~:: '.J\i(v/2)-l exp(-M/2) \\}} :f :{ {:~ = = (10.44)

f(M}d'M 2v/2r(v/2) d'M f (x2) dx2, where v is the number of "degrees of freedom" of M. In the present cas~/{{:(:~:~ we set v=n } because this is the number of truly independent points being compared~j))Jj ~ In Eq. (10.44) (x) is the "gamma function," which for positive intege~))\:~3.f arguments5 is simply .. /\{{j = . · · . . · ·. . · ·. . · · . . · · . . · · - • - • ·.. ... ....... _ . . . .

r(n) (n - l)!. ::::::::::=:=:::=t -: :: ~ ~ i~ ~~ ~ ~~ ~ ~~~~~~~~i Consider next that y f (x) is not known. but that a two-parameter\{:}ff (\Jft curve is fitted to n data points, yielding estimators a* and b*. Then on~f fo nns again the least-squares sum :JV[ using y f (x; a*, b*) but now tli~/)){~f k)}i]J frequency function for the M values is given by Eq. (10.44) with the th~)//It degrees of freedom reduced by the number of estimators obtained from data, that is, ·.·/!}){~ v = n - 2 · · {!ii///~~IliI The x2 distribution may also be used for comparing the frequency of\)jf} occurrence of a class of events with the theoreti_cal frequency (function). Le(}\/}~~ an~:f\)f~~~~{ us consider, for example, 100 measurements of a radioactive sample, - = .·.·.·.·.•,.•. ....l " ..' .t.r divide the sample into seven classes, with mean value N 85 counts/~{:\J{:~~:~ 5Toe general definition of the gamma function is fo00 r (z) :::: 1 2 - 1 exp(-t) dt; for more details see any te~t on advanced calculus.

}}j~

## 10.3 Estimation of Parameters and Fitting of Data

TABLE 10.4 Observed and Expeccerl Frequencies of the Results of 100 Measurements of a Radioactive Sample Class 0-75 75-79 79-83 83-87 87-91 91-95 95-oo Co ants/min Oi 15 11 15 15 18 12 14 Qbgerved freq e; 13 12 15 16 16 13 l5 Expected freq (e; - o;) 2 /el 0.307 0.083 0 0.062 0.25 0.077 0.067 x2 ..

and approximately equal expected frequencies; the resulting frequency of o, the experimental observations in each class is given in Table 10.4. Next we obtain from the data the estimators for the parameters of a Gaussian = /N, (1) µ* N. (2) er*= and (3) the overall normalization, namely, I: o; = L e,; thus the degrees of freedom of x 2 are four, corresponding to seven classes less three estimators. From the Gaussian distribution we calculate the expected frequencies ei for each class; they are also given in Table 10.4.

In complete analogy with the least-squares sum~ Eq. (10.38), we form the x2 sum ~ (ei - o;)

2 = X ~ 2 • e.

i= l z Note that x2 is now a discrete variable, since frequencies of classes are compared; however, Eq. (10.44), which holds for a continuously vari able x2 • is valid provided the number of classes n ~ 5 and the expected frequencies ei > 5.

For this experiment we obtain 2 = x o.846, = x2 and we explained before that v 4. From a table of the distribution we :· find that in 93% of the cases the x2 distribution would be larger than the result obtained here. Thus one may suspect that the data are "too good" a fit to the estimated Gaussian.

The x2 distribution of Eq. (10.44) for different degrees of freedom is shown in Fig. 10. 7. Tables of this distribution may be found in refer ence manuals, or easily calculated in any number of computer programs.

It should not be surprising that when. the number of degrees of freedom Iii!

·. ijjlf 454 10 Elements from the Theory of Statistics liil!iii]i!

tt~ :.;)/!!!){ 0 1 2 3 4 5 6 7 8 9 10 11 12 FIGURE 10.7 The frequency function for the distribution of x2 , for different degrees }):~[fit }/?f~~ of freedom. All curves are nonnalized to the same unit area. Note that for large v the x_2 {:}~:~:f~ distribution approaches a Gaussian. · .·_ (/@il~i increases v > 30, the x2 distribution approaches a Gaussian 6 with mean/}/ff 10.4. ERRORS AND THEIR PROPAGATION 10.4.1. Introduction When we perform a measurernent of a physical quantity x, it can be:/:}~:~tt· expected that the result obtained, x1, will differ from x; this difference.))J{f randon(/l~\t is the error of the measurement and consists of a systematic and a the(/}@\: contribution. Suppose, now, that the measurement is repeated under same conditions n times; then the results will be distributed (in mos(/\}} Xn cases) normally about a mean x with a standard deviation a-. The difference{:)f??

between i and the true value x is then the systematic error, and the standar&;}jjf~ } deviation a of the Gaussian is a measure of the dispersion of the resul~}/iJ~f :)}lff~ due to the random error. · The object of the measurement, however, is the determination of thij(\Jff:§ whetheti\Jf{§§ unknown true value x; since this is not possible, we seek to find .., ,.~.·.· x lies between certain limits, or whether the true value x is distribute4 ,·.

·.· .-...., §~i ..

,·:\:ttf~~~ 6It is really the distribution of /ii.2 that approaches the Gaussian with mean µ, :.?/{~~~§ \t@jja .J(2v - 1) and unit standard deviation (R. A. Fisher's approximation). ·.

:;)/1~@1 il l ·.·.·.:.. .. .. w ~ ~ 1 0. 4 Errors and Their Pro p·a g at ion 455 about some mean x* with a standard deviation a*. Note that in a rig orous sense, this statement is incorrect, since the unknown true value x is not distributed~ but is fixed; what we mean is that the probability, x x'\ x > x*, etc., is given by the normal frequency function with mean i and a µ2, the second moment of the measured data about their meanx.

Thus, by repeating the measurement several times, it is possible in prin ciple to circumvent the random errors because (a) a knowledge-.of i and a contains all possible infonnation about the unknown true value x, and (b) as n increases, the second moment should decrease as 1/~ and may be made arbitrarily small. On the other hand. the systematic errors can not be extracted from a set of identical measurements. They can either be estimated by the observer or be judged from a performance of the same measurement with a different technique. Therefore, it is unadvisable to reduce the random errors much below the expected limits of the systematic errors. In what follows we will discuss only the treatment of random errors and work under the assumption that the results of the measurements follow a normal distribution.

Until now we have considered the simple case where the unknown value x is directly measured and an error ax can be associated with the measurement; that is, the frequency function of x depends only on one variable: (i -x)

f~)=~a= ~P [ --I -- ] · J21r<Ix 2 0- Most frequently, however, the unknown value xis not directly measured, and we distinguish two cases: (a) x is an explicit function of the quantities Y1, y2, ... , Yn that are measured and have with them associated errors <11, a2, .. . , an. Namely, X ¢(Yi, Y2, · · ·, Yn), (10.45)

and it is desired to find the estimator x* and its standard deviation ax.

(b) xis an implicit function of other unknown variables u1, u2, ... , um, and of the quantities Y1, )'2, .. . , Yn that are measured and have with them associated errors a1, <12, ... • an. Namely, <J,(x; u1. u2, ... , Um; YI_, Y2, ... , Yn) 0, (10.46)

456 10 Elements from the Theory of Statistics ur' and it is desired to find the estimators x*, u;' ... ' u!z and-the symmetric = + error matrix O'ij(i, j 1, ... , m 1). Such an example was treated in

## Section 10.3.3, and we know that at least m 1 sets of measurements are

required to obtain the m 1 estimators.

The techniques for obtaining the best estimators were discussed in

## Section 10.3. In this section we will discuss how the random error of

may be determined from knowledge of the errors of tbe independent vari ables Yn ~ this procedure is frequently referred to as the combination or the propagation of the errors of the measured values Ytt.

10.4.2. Propagation of Errors Let us first assume x to be an explicit function of the measured Yn as discussed previously (Section (10.4.1)): X = ¢(YI, Y2,. · ·, Yn). (10.45)

By applying the maximum likelihood method, it can be shown that the estimator x* is obtained by using the mean values, µ,n, of the measured Yn (provided 7 the Yn are distributed normally). Here the mean values µ,n are obtained from r different measurements 1 , .

=-;: L<YnY- /J,n i=l Thus x* = ¢(y1, Y2, -· ·, Yn) = ¢(µ1, /J,2, · · ·, Jl,n). (10.47)

Next we make a Taylor expansion of Eq. (10.45) about x*, through first order Yh 7 Clearly if x is variable, all measurements are made so as to correspond to the same pointx.

## 10.4 Errors and Their Propagation

where [04'/oyn]µ means evaluation of the derivative at the point about which we expand-that is, (/L 1, µ,2, . . . , /1,n). We can now form the sec ond moment of the distribution of the xi values as they result from the observed Yn i values. The superscript i here refers to the r different sets of measurements: ax 2 = ; l ~ ~ (x - x' · ) 2 ')

i=l ~ [(:4>) (:4>) y~l = y{) + ... + (µ,. - (/Lt - i=l YI µ, Yn 11 a4> a¢ 1 L r . .

YD + 2 - - - (µ, t - Yi) (µ,2 - + · · · ( ) ( )

oy1 µ, 8y2 JL r i=l (a<t,) (a¢) (a¢) (a¢)

2 2 a2x = - a2l + - 2 + · · · + 2 + · · · · ay2 a2 2 - a - a al2 oy1 µ. JL Yi µ. Y2 µ, (10.48)

Equation (10.48) is the most general expression for the propagation of errors. If we assume that the errors are uncorrelated, namely, O'IJ 0 when i -:/= j, we can obtain the results for the simplest functional relationships: (a) Addition = + + · · · + x Yl Y2 Yn a:c = Jal + a} + · · · +a,~. (10.49)

(b) Subtraction Yl - Y2 Jcrl ax= + aJ. (10.50)

(c) Multiplication X Yt X Y2 X · · · X Yn 458 10 Elements from the Theory of Statistics cJ<j> ) /J,2 X • · · Jl,n ay1 µ, = crf 2 + • •· + a-; 2 <5x X (µ,2 · · · /J,n) X (µ,1/J,2 · • • ) (10.51)

(;:Y +(;:Y-~---+(::f.

.f:11 =x· ( d) Division Y1 x=- Y2 (10.52)

(10.53)

From the above examples we see that in general the errors are combined in quadrature-that is, it is thae,i r squares that are added. Consequently, if the error in one of the variables is large, it will dominate all other terms and :\If!

the error of x, ax, will be almost equal to err, despite good measurements made on the other independent variables.

Our simple rule for the case of addition, Eq. (10.49), may be used to iiil/!li/i obtain in a different way the result derived in Eq. (10.34). Let a variable <1tr x be measured and let the mean of a set of measurements be Xi, with a ........... ·.· standard deviation ai; if this set of measurements is repeated under identical .:::::;:::~: conditions, a new mean result ii # ii will be obtained. but let the standard deviations be equal, that is, a j Ui. If n such sets of measurements are perfo rme~ the new estimator for x wif:I be :11:1 ·\i[fi x* = -(i1 + i2 + ···in), n, ')i~i~I~~i )Ji~ and thus Gt)=~- II

## 10.4 Errors and Their Propagation

Hence, from Eq. (10.48) or (10.49), 2 r;; /(a1 )2 (a2)2 a*= + + ... + (a11 ) = a=_< !_ __ (lO.S4)

x n n n n-;;z Namely, the standard deviation of the mean of n measurements of a Jn, Gaussian distribution is u / where u is the standard deviation of the individual measurements. ., 10.4.3. Example of Calculation of Error Propagation As an example, let us consider an experiment to determine Stefan's constant b, from the relation E=bT4, where the following values of E and T were obtained with the indicated standard deviations: T (K)

800(1 ±0.02) (3.Q ± 0.3) X 104 1000(1 ± 0.02) (8.0 ± 0.8) X 104 1200(1 ± 0.02) (15.6 ± 0.6) X 104 We wish to calculate the estimator b* and hs standard deviation ab, There are two ways to proceed in this case. We either may calculate bj from each of the "1!ee sets of measurements and then combine these values to obtain b* = bj, but weighing each bj according to its standard deviation, or we may use least squares in the observed variables E and T4 • Note that a mean of T or E of the three listed measurements makes no sense whatsoever since each measurement is made for a different T.

We will follow the first procedw·e, and we first obtain the error on T4 from the known error on T. For this we should use the general expression, Eq. (10.48), but since <I> = T4 is a function of only one variable, 8 simple differentiation gives the desired result directly d</> - 3 b..</> - 4 .D..T 4 (10.55)

dT - T ¢ - T .

81f we choose to write q, T x T x T x T, we may not apply Eq. (10.51), since these variables are correlated; use of Eq. (10.48) and cr1r = crt gives back the result of Eq. (10.55).

. ?::::::;;;:;: 460 10 Elements from the Theory of Statistics ~llil TABLE l 0.5 An Example of a Calculation of Propagation of Errors • , ...... • ............J Ji Set of data 1 0.41 X 1012 7.3 X 10-S 0.08 0.13 :: ::::::~:::: 2 1.0 X 1012 8.0 X 10-S 0.08 0.13 -:,:-:-:•:•:. .; ..

3 2.0 X 1012 7.8 X 10-S 0.04 0.06 )i!i!ili~~ ifj We note from Eq. (10.54) that it is easier to work with relative errors, and :}}~~~: \\l~!

we thus fonn Table 10.5, where )~:;: ::/:: :I~:;I:;~ ar) - [a~4)r [a:)r since the errors in T and E are uncorrelated. ·:/J):)t -:-:-:.~:-:·:~ :\(~~?- For the best estimator of b, we will use the mean of the three measure-· ments but weighed in inverse proportion to the square of their standard {/~~~~ devi a t1 0n (see Secti on 10.3.3). Thus :-:::::::::::::~~:!:==~~j -~)~:~~~:~~ - = 1 + + · -8 = -8 .:? :: : : ::::::: b 6 (7.3 8.0 4 X 7.8) X 10 7.75 X 10 ; ':: :: : : ::::::::: . :-:-:-;.:-:. .: . .: .)/~~:~=~=~= . ·. ................ · •, for a(b) we used Eq. (10.49), :j(fl~ ,:-:-:•:.-:-:-: ...

::::::::::::::: cr(b) == ~J cr2 (b1) + o- 2 (b2) + 4cr2(b3) .· · :: . . · : · : . . : · · : . . : · · . : . . - • : . . : . .·- : . . : . : . : · ... : ... · . : .

-:-:-:-:.-::.:-:. .

://i~~~~~~ or the convenient approximation : · : . . : · : · . . - : . : . .. . : . . . : . . . : . .. . : . . - : .- . : . - : .. - : . - . : .

[cr(b1)] [a(b2)] [a(b3}] . .:;:::::~=~== a~) == ! 2 2 4 2 = . ·.·.·.· . . -·. .· .. · . .

+ + 0 043 . ))~~~~~~~~~ b 6 b1 bi b3 . , :-:-:-:--:•:•::.

~::::::~::::: :,;-:-:~:-:-: ..

so that the final result is = ± 8 4 2 b* 7.75(1 0.043) x 10- W /°K -m • 10.4. . 4. Evaluation of the Error Matrix ://t In the two previous sections we have discussed the case where only ·.·.·-·,# one unknown variable x was sought. We will now consider the random :\::~:',JX-.1":. ..

::::::::~ :/ ::~~ .-:::::::;. .

## 10.4 Errors and Their Propagation

errors when several unknown variables are simultaneously estimated or measured.

When only one variable is measured, we know how to obtain from the data the second moment about the mean 2 = - 1 ~ 2 a L./i - xj) .

n.

i=l ')

If now p variables are simultaneously measured in an experiment, we must form the p ( p 1) /2 second moments about the mean; for example, if we measure x, y, and z, we must calculate the six expressions fJ:u: = .!_ L<x - x1)(i - Xi); Clyy = ... ; Uzz = · · · ; n .

z=l fJxy = -1 ~ " (x - - X/ ) (y - - Yi)= fJyx; (10.56)

i= I = · · · = = ... = <l'xz. 0-zx; Uyz Gzy· (In this notation, the dimensionality of a quantity a pq is that of the product a; pq. Hence, has the same dimensions as axx. We avoid the notation a;_y, etc., because it misleads one to think that C1xy, for example, is positive definite.) ff the distribution of the variables x, y, and z is normal, then these six moments form the symmetric error matrix; if the variables are uncorrelated, the matrix is diagonal.

Clearly, the error matrix must be known if it is desired to apply Eq. (10.48). Consider, for example, that from the measured variables x, y, and z we wish to obtain a new unknown u and its standard deviations a(u), where u ¢(x, y, z). (10.57)

Then the values of a ] that were obtained from the data with the help of Eq. (10.56) are substituted iu Eq. (10.48) along with the partial derivatives of u, which are obtained from Eq. (10.57).

Conversely, if the frequency function of the three variables x, y, and z, and thus of u, is known, /(u) f[<J> (x, y, x)]

462 10 Elements from the Theory of Statistics it is possible to calculate theoretically the elements of the error matrix through the usual expression jff /½(x,y)= j(x,y, z)xydxdydz (10.58)

or Jf f /,l,2(x, y) (x, y, z)(µ,x - x)(µ,y - y) dx dy dz, where (jxy µ2(x, y), etc.

In most practical application.c;, however, it is difficult to use Eq. (10.56)

or (10.58). Equation (10.56) may not be usable because the unknown vari ables may not be measured directly (although they are measured implicitly); also, extensive data are required to yield meaningful results, and the cal culation is cumbersome. Equation (10.58) may not be usable because the multidimensional integrals are frequently too difficult to calculate. Instead, the method of maximum likelihood provides an easy way for obtaining the error niatrix.

As already discussed in Section 10.3~ if the set of data Xi, Yi, . .. , Zi has been measured, and the estimators for the m unknown variables 0a, 0b, ... , 0m are sought, we may fonn the likelihood function .C(x1, x2, ... , Xn, YI, Y2, , . ·, Yn, ... Zl, Z2, ... , Zn; Ba, 0b, ... , 0m)

= f (xi, YI, ... , z 1; Ba, 0b, ... , 0m) f (x2, Y2, ... , z2; 0a, 0b, ... , Om)· · · X f (Xn, Yn, . ·. , Zn; 0a, 0b, ... , 0m), where f is the frequency function of the measured variables and is usually 0;, 0;, ... ,0 : assumed to be a product of Gaussians. Then the estimators are given by the values that simultaneously maximize .C, namely, :~L:.e;... .. e,: :~1;.e; .... e:.

= (10.59)

= · · · = O, requiring the solution of m coup.led equations. Equation (10.41) is a simple example of such a solution of Bq. (10.59). We note that the number of independent data points taken, n, must be larger than or equal to m.

...-.: ·:

## 10.4 Errors and Thei-.r Propagation

The elements of the error matrix can be obtained from the inverse of the matrix (10.60)

where the second-order partial derivatives must be calculated at the values of the estimators, and W log A.J. We have = 1 <Ikf (H);, , where the rule for matrix inversion 1s -t i+J· Det ( ji minor of H)

(H )" =(- 1) (10.61)

rJ Det and the minor is the matrix resulting from H when the jth row and ith column are removed; obviously, the inverse matrix does not exist unless f= DetH 0.

We will now apply this method of obtaining the error matrix to the simple example treated in Section l 0.3.3. The measured variables are x and y. and estimators are sought for the variables a and b; we assume that xis known exactly and that y is distributed normally for each measurementt and related to x through y a +bx.

Using Eq. (10.37), we have {-~[y; - .(,=fr[ b)i2}]

-~exp y(xi; a, i=l a, 2rr 2cr; and = = - -n ~ l ~ [Yi - (a + bxi) ] 2 W log L lo g(21t) - .L..)og ai - 2 .L..J .

a, i=l i=l = = · · · = To simplify the calculations we assume a1 a2 an, so that a2w n a2w I:xi a2w Lxt - oa = 8aab = ~; - = 2 u2 ; - 8b2 u2 .

Hence (10.62)

464 10 Elements from the Theory of Statistics and r] · (I> = : 1)xf) - Det H [ n Thus \{:~if which gives the results stated in Eq. (10.43); the indices v, J.l stand for ..

10.4.5. The Monte Carlo l\'lethod \?§f} It is clear that the calculation of the propagation of errors may become · \J~t;.

extremely invol;,es1, especially when the frequency functions of the vari-.

ables cannot be ~xpressed analytically and when intermediate processes of }}@~t· statistical nature take place. It is then preferable to use computer programs }!/ff based on the so-called uMonte Carlo" method. ·· . - . : < ·.· : . : - : .; ~ ~ : • ~ .. • :.=•::.,:• .·.·.•r,.·.•.,•. )/fJ By this technique, we follow a particular event through the sequence .·.·.·r. .• ,_.•,.•.

of processes it rnay undergo. For each process, all possible outcomes are \}It ·}\ff weighed according to the frequency function and divided into x classes of }{f\ equal probability. Then, from a table of these classes, one class is selected at random: for example, by looking up a table of x random numbers . .( {}} The outcome of this process is incorporated in the progress of the event -\\}/ until a new decision point is reached, when again random selection is ·) }}{ ·ittr made. Thus, at the end of the sequence of all processes, certain final con- ' d.itions will be reached from the initial conditions with which we started {/?!

and through the intermediary of the random choices made at each decision ){\( )\f\ point. ..

We follow in this fashion several events, always starting with the same ·:}t{· initial conditions, but because of the random choices, the final conditions · })f?

....... ,;.·.

\}ft will be spread over some range. If enough events have been followed .

\}}f through, we are able to find the frequency function of the combined process /i?

and of its parameters, namely, the mean and the standard deviation for the· .

final conditions that result from a given set of initial conditions. ·}}§fa -)/§f For more discussion, including examples with accompanying com- )Jl~ puter codes, the reader is referred to the material listed at the end of this ..

## 10.5 The Statistics of Nu c I ear Counting

10.5. THE STATISTICS OF NUCLEAR COUNTING In many experiments related to nuclear physics, we count the particles or photons emitted in the decay of a nucleus. Usually only a very small fraction of the total sample undergoes such decay. The decay of one nucleus is a comp]etely random phenomenon, yet from the number of counts in a given time mterval, we may detennine the decay probability of this species of nuclei or unstable particles. We have aheady made use of these"'concepts in Chapters 8 and 9.

10.5.1. The Frequency Function for the Number of Deays We start with the assumption that the decay of one nucleus is purely ran dom and the probability (unnormalized) for decay in a time interval !J,.t is proportional to !)..t and some constant >.. with dimensions of inverse time : Pd >..!)..t • (10.64)

If we have a sample of N nucleit since the presence of one nucleus does not affect the decay of another, the probability that one nucleus out of the sampk of N nuclei will decay, in time /)..t, is P(l, !)..t) lNb.t. (10.65)

Equation (10.65) is completely analogous to Eq. (I 0.12) of Section 10.2.6, which leads to the Poisson distribution; the only difference is that the product Nt of Eq. (10.65) is the equivalent of the number of trials n of Eg. (10.12). Consequently the probability (frequency function) for obtaining n decays in a time interval t is e-).Nt (N At)n P(n, t) = t (10.66)

n.

The first moment of Eq. (10.66) (in the discrete unknown variable n), as we know from Eq. (10. I 6), is n lNt. (10.67)

9E. Schwcidler, 1905~ this assumption bas been proven absolutely correct from the agreement of experiment with the deductions following from Eq. (10.64) as developed in the following paragraphs.

::!l!lil!lilt~ .: :::::::::::::=:: 466 10 Elements from the Theory of Statistics ·!)}ft :=:=:::; ... : :: : : = '' ~ ••••• -4 • .... . r n/ \{j)j)jj@j Since t is the average number of decays per unit time (the average decay rate), we find the physical significance of the constant parameter A. That.)\}/ is, N).., gives the average decay rate of the sample; N is the total number of}}{\: \\/J nuclei in the sample.

Similarly, the second moment about the mean of Eq. (10.66), as we·:\/Hi :.{}@} know from Eq. (10.17), is ex;::io~n.

Hence ilie very frequently u:; = en_ (10 :{}~~~ rr 'V ,68) ,·.:,:-:•:-......

V fL }:J~:: n/ = /}Jj Note, however, that t N).. is~he theor~tical average rate, which is \)J~ usually unknown (unless A and 1'{.a re precisely lmown for the sample under consideration). The average rate that we measure, R = n/t (counts -:}tf per unit time), will, in general, differ from the true rate NA = n/t, but' • ·: ' \ • J • ~~ • -. : r .. ~ .

}\@ if n is large, R will be distributed normally about NA. (See Eq. (10.66a).

below. ) -:::::::::~-:;j ::::::::;~~:: From the considerations of Section 10.2.9, it is clear that when the total )}~~~ \fl~~!

number of observed counts n is large, Eq. (10.66) is well approximated by a Gaussian with mean µ, = N At a:nd standard deviation a = ./Nfi: .:{}J <:::::::::::: = 1 [ (N)..t - n) ]

P(n, t) --;::==== exp - ---- / ,J2nN)..,t 2NAt ( l O· 6 6a) li/1.l ·.·.·.·.·.. ·.

n}2] :: :::::::::: = 1 [ (ii - > .· :: . : · : .· :: .. · : . : - : . : .

exp - . (lo. 6 6b) }\?

,.Jiiin, 2n ••••••. .< 9/.

Thus, unless we are dealing with very few counts, Gaussian statistics may be safely applied.

Finally, we summarize here some simple consequences of Eq. (10.64)

1/1 for a single nucleus: ·~~)~~i~~i (a) If the probability for decay in dt is )ti~ Pd(dt) =}.. dt, :::::::::~~ ))f ?)t (b) then the probability for not decaying (survival) in the time interval fromt=0tot=tis ~ )\~~~~i )\i~~~§ = e-J.t)

Ps(t) ·.\ ,·?.·.; . -~.......~ r (for proof see Eq. (10.13)). }}1 . ·-:::;:-;:~ ::::::~~~

## 10.5 The Statistics of Nuclear Counting

(c) The probability for decay in dt at time tis Pd(t,dt) e->..r'Adt.

(d) Tbe probability for decay in the time interval from t 0 tot =tis = = Pd(t) l - Ps(t) 1- e-M.

Note that only (c) is properly nonnalized, so that fo00 fo00 = = Pd(t) dt e-i,,_ dt I.

Expressions (b) and (d) ~e, correctly, always < I and reduce to O and 1, respectively, as t approaches infinity. As to expression (a), we must keep in mind that it bolds only for At such that )..f:d << l.

10.5.2. Behavior of Large Samples Having obtained the frequency functions, we may Iiow examine the behav ior of the total sample. From Eq. ( l 0.67) we see that given a sample of N nuclei, on the average, in a time interval fl.t there will be n )..N At decays; that is, the total sample will be decreased by an amount -AN= N'AD..t. (10.69)

Equation (10.69) then leads to the differential equation for the number of nuclei in the sample dN - = -}..dt with solution N(t) Noe-M, (10.70)

= = where No is the nwnber of nuclei at time t 0. Frequently r 1 /).. is used for the exponent in Eq. (10.70)~ r is called the lifetime of that particular species of nuclei and is the time in which the population of the sample is Toe princip)es and fonnulas in this section have already been used in Section 8.6.

. ·. .. · .. .· . . .. · , .. . · .. . . · . . . . - · . . . .- . . - . - - . .· .

·}}}}f ..............· .. · ---·.

:iiii!i{}f~ 468 10 Elements from the Theory of Statistics . : :: : : ::: :: :::::::::: . ·· ..·· . .. · . . . · .. ............... · · . . . . - · -..·- . , · reduced to 37% (1 / e) of its original value. The half-life . : . : · . . : . : · . : . .· : .. : .· : . . : . · · : . - : · : · . : . .- : ·. . : . .- · : . . : . · : • - : . : · · ::: : ::: : :: ::::::::: = [1n. ~] = · · . . · · . . · · ... · · . . · · - .· · . . · - - .. - · . - .· · . - · · .: : : : : : : :::::::::::: -r112 -r 0.693-.: :. : . : •:.: -: -:-:- :·: -:-:-:•:- :-:-:•:•:• )tilt~!

gives the time in which the population of the sample is reduced to half its ~~i~~~~~~ii~ original value. Using Eq. (10.70) we find, for the decay rate as a function }· .j· \.~·. .. .....· .·.•.·., -: :: : : =::: :::::::::; .·.·.·. . -...................: of time, that )i}/ii!~!il~ d N - = = = R(t) - AN(t) -ANoe->..t, (10.71) ··{{J~~:~~ dt ·.·.·.·.·,-.•,•.·.· !/i!/ilil~ which has the same time dependence as (10.70). Experimentally we·.

\/i}f usually measure R (t) and obtain a curve as shown in Fig. (10.8); from such a /{Jlf plot i.. may be obtained. If the sample contains two or more different speci~ · of nuclei with different decay constants J... 1, .\.2, •.. , the time dependence /{)~}~~ of the decay rate is no longer the simple exponential ofEq. (10.71); instead : .. } . ! . {i . i~)~. f .. . t .r } • . J ~~ = R(t) = - A1NJe- ' 1 A2NJe-A2 ' - t - ·•• • >> If, however, A1 J...2, then forsmallt (that is, t "" l/i..1) R(t) is dominated ·}}if~~~ by the first tenn; for large t (for example, t "-' l/J...2), R(t) is dominated by .·/.·.{·.·:,]'~/,.•t,.•i. .•~ ..• i .: : : : ~::: :;:~;::;:;:; ··:\iflft ·.·.·.·.-,.-.....- .·.·. .· }flll . :~:~:~:~:i:i:~:}~:; ·.·.·.·.--.....- ..- .---..

.) !!]lll~~~~ •.::· .:=·.:- = . : .. = ... :: . : . : . : ,_ : .._ : . ; , : .. ;. . , ; ,, I !J i////ljfi j]/!

.z. -::::::::::::::::::: :~ .·.·.·.·.·.·.·••••.• 0 :-:-:-:-:-:•:-:-:•: :}}ft: as 0.50 ~ -_J _ :\:/ff~ (D l a: I

## 0.25 I

o.___ ____I _ .....___....__ ___ _. _____ _ ________ T112 ~ 2r112 3r112 4,112 Elapsed time FIGURE 10.8 Exponential decay of a sample of radioactive nuclei. The abscissa is ):}~%=~ /::::/ti~:; calibrated in units of the half-life of the sample; the lifetime is also indicated.

\ .}11 ......, ...~ ..

## 10.5 The Statistics of Nuclear Counting

200 \'\ __ 100 ' , -....-._ -.., '\ -~ - - --- -~ - 50 '\ h - -- \ t---.

-- C \ \ r--- ~ ~ ~ \ ~ \ s \ 0 4 8 12 Time (hr)

FIGURE 10.9 The decay curve for a sample containing two species of radioactive nuclei.

each decaying with a different lifetime. Note that the composite decay curve a is the sum of curves b and c.

the second term. This is shown in Fig. 10.9, which gives the decay curves on a semilogarithmic plot. See also Section 8.6.3, in particular Fig. 8.37.

Another situation of interest arises when nuclei of species A decay into species B with a constant ).A; nuclei B, however. decay in tum into species C with a constant AB, Le~ at time t 0, the number of nuclei of species A be No and that of species B be 0.

Then the number of nuclei of species A as a function of time is still given by Eq. (10.70), NA Noe-'J...111 However, for the number of nuclei of species B, the following differential equation holds: dNa -- = +).ANA -)..BNiJ.

dt The solution of this first-order linear differential equation is straight = = forward, and with the initial condition Nn(t 0) 0) we have NB No AA [e-AAt - e-.\.st]. (10.72)

As - AA 0::::sT::~: :BS~ti~~i= !!ilillii!

e :t: :~;:~_:: it must~. irres~ctive vhether AA > AB or AB > AA. Equation (10.72) correctly reduces to \\}~j} = = = (jf}{ 0 fort 0 and t oo. The two limiting cases for the decay rate n B to C can also be obtained from Eq. (10.72) if we take into account : ){/ft }/ttt : RBc(t):::: NB"-B· Thus >> for AB AA Rsc (t) ~ NoAAe->..Ar for AA >> J..B RBc(t) ~ NoABe- >..8~ 0 5.3. Testing of the Distribution of Radioactive Decay; the Distribution of the Time Intervals between Counts s frequently desirable to test whether a sample of counting data does .eed come from the decay of radioactive nuclei, that is, that it follows the '.{@f:J ;} quency function of Eq. (10.66). A very sensitive test can be devised if plot the distribution of the time intervals between successive decays, or :)))§? }} [:)if (.

~ry second~t hird, etc., decay. This method was applied to the distribution /)ff~ the arrival times of cosmic rays in Section 9.4.2. ~~?

First we obtain the distribution of the titne intervals between two succes- \ :}({:( ~?.

:}Jtf :\: ·e decays. Let t 0 when a decay occurs; we then seek the probability = = \/I\ ·\· it no decay occurs until t t, but a decay occurs within d t at t t. This = )j{f ){ >bability is given by Eq. (10.66) with n 0, multiplied by Eq. (10.65); = = P(t, dt) qi (t) dt e-NAt NJ.. dt. (10.73)

n ( 10. 73) indicates that the shortest time intervals between two are much more frequent than the longer ones; this is true for any events, since they obey Eq. (10.64) and is shown in Fig. 9.22.

t we consider the distribution of the time intervals between every , third, etc., mth count. In practice this arises when the counts from ut of a "scaling circuit" are recorded. Consider, therefore, a circuit one output count for every m input count. If the true rate is r, then ut rate R is related to r by NJ..= r Rm.

1Compare this equation with the probabi1ity for the decay of a single nucleus, as given ;ection 10.5.l(c).

..

## 10.5 The Statistics oi Nuclear Counting

0 when an output pulse arrives~ and let Qm (t) be the probability other output pulse arrives in the time interval t~ qm (t) dt will then e probability that this other output pulse arrives at t (between t and t).

other output pulse will arrive if the input counts n ~ m, so that ·.·.·- .:::::: Loo .Lco (rt)11e- rr = = Qm(t) P(n,t) n!

':, n~m n~m (10.74)

~e the last equality follows from the normalization of Eq. ( l 0.66)

Lco P(n, t) 1.

n==O by considering the sample space of Fig. 10.10 we see that the set of s Qm(t) is a subset of Qm(t dt), so that any sample-space point ging to Qm (t d t) but not to Qm (t) represents an output count een t and t dt. Thus Q,n(t)

. .

. . . . . . . - . . - .

. . ... .

' . . _. . ' ·.: : :' ·. : ' : : :. : : ·.

IB 10.10 Sample space indicating the domain Qm(t), which contains all points londing to the an·ival of an output count in the time interval from O to I after the us coant. This domain forms a subset of Qm (t + dt). which contains all points >onding to the arrival of the output COWlt in the time interval from O to t + d1. The = + of the outpal count at tis qm (l) Qm (t dt) - Qm<t).

>~-:-:-:-: -,.:,:,:-:-:• 10 Elements from the Theory of Statistics or : !Ill dQm(t)

·:;:::::::;: qm ( t) = dt . .. ......••..

Taking the derivative of Eq. (10.74)

n. n. . ·.·.·.·-·.,/'.,,; n= 0 n-Lm-1 n-Lm-1 (rtte-rz (rt)11-le-rt =r -r n! (n-1)! · n= l By replacing in the second sum n by l n - 1, we see that only the last }/~~ )\}f!

term of the first sum survives, so that :11 q.,,(t) = r (rtr-';-rt. (10.75)

(m - ) ! .:\/}~ = = Equation (10.75) correctly reduces to Eq. (10.73) form 1 (since r ))~~~~ N)...). Form~ 2, Eq. (10.75) has a maximum at dqm(t)/dt 0, or •)•{• }" §".~ '/,:,I }(Jj [r2(m - 1) (rt)m-2e-rt] - [r2{rt)m-1 e-rt] 0. .

}///I~ii = ~ = Hence t (m - 1) / r and for large m, t m / r 1 / R. Thus we see that.

·;i()f the most probable time interval is not the shortest one, but.instead approa- ches the mean time interval between output counts 1 / R; that is, the scaling ){jf~~ circuit regularizes the counts. Equation (10.75) is shown in Fig. 10.11 for\ /}{ :i{fl :!}l~~~ :'.iiiiiI~l Iii ./i!i!f~~ /}if ',•.•#-'r,.•A•_r 1 2 3 4 rt ·})}{~ .·.·.·.·~. . ..· , FIGURE 10.11 The probability qm (t) that the mth count will follow any original counf/~::::~ the(::~::::~ at the time interval t. Note that the abscissa is calibrated in units of rt where r is ·.·.·.·.·-~. ........ ,.

unscaled rate of events; form large the curves approach a Gaussian with mean {rt) :::: m/j~:~~ or {t) = m/ r. -: · - . : · : . : · : . : · : .- :: .. : . : .. : .. : .. : ... ~ ,.

\ Jll )ii

## 10.6 Referen·c~-~;::}}?.~

. .: .:,· .· different values of m. Comparison of these curves with experimental data has been presented in Section 9.4.2.

10.6. REFERENCES There are many texts, both elementary and advanced, on the subject of statistics, data fitting, treatment of errors, and computational modeling. The references given below were consulted for the preparation of this chapter.

L. Lyons, A Practical Guide to Dala Analysis for Physical Science Students. Cambridge Univ. Press, Cambridge, UK. 1994. A succint guide with pleoty o( examples.

J. R. Taylor.An Introduction to Error Analysis, secood ed., University Science Books, Sausalito. CA.

## 1997. A thorough treatment with application& to the pbysicw sciences

B. P. Roe, Probability and Statistics in ExperimenJal Physics, Springef"-Vcrlag, Berlin, J9 92. A slightly more advanced and mathematical text.

P. G Hoel, Introduction w Molhematicnl Statis1lcs, Wtley, New Yock, 1958. The presentation of Sections 10. l and 10.2 follows Hoel closely.

A. L. Garcia, Nwnerical Methods for Physics, second ed., Preo.tice-Hall, Eoglewood Cliffs, NJ. 2000.

A geo.craJ text including chapters on data analysis and Monte Cado techoiques. with plenty of coding examples in MATLAB. FORTRAN, and C++.

H. Gould andJ. Tobochnik, An introduction to Computer Simulation Methods: Applications to Phy~ical Systems, second ed., Addisoo-Wesley, Reading, MA. 1996. A text devoted to simulations, with extensive use of Monte CarJo methods, with programming examples in BASIC, FORTRAN, C, and PASCAL . . . . . · .. . . ' . . • . . . . . . · . . . - . · .. . . - . . . . . . . . - . . . - .. . ... - . .- . . . .. . .- . . - . - . " - . - ' . · . .. ~ . .

·)} ~=~=~=~=~:~: ·.·.·.·.·--.~. .- -·.· ):):~:~:~:i:~{ .·.•.·.--~.·. . ·•·.

## APPENDIX A

Students We gratefully acknowledge the many students who have contributed the data used to illustrate these experiments.

Students from the University of Rochester: • R. Armstrong, class of 1994 • W. Lama, class of 1966 • D. Boyd, class of 1963 • T. Londergan, class of I 965 • C. Border, c1ass of 1994 • E. May, class of 1962 • M. Dobbins, class of 1994 • S. McColl, class of 1962 • R. Dockerty, class of 1962 • T. Middleton, class of 1994 • P. D,O nofrio, class of 1962 • R. Nebet class of 1962 • K. Douglass, class of 1964 • P. Nichols, class of 1963 • E. Glover, class of 1961 • D. Owen, class of 1963 • R. Harris, class of 1963 • D. Peters, class of 1962 • E. Holl·oyd, class of 1966 • S. Pieper, class of 1965 • M. Klein, class of 1962 • W. Rakreungdet, class of 2000 • D. Kohler, class of 1962 • J. Ree~ class of 1961 476 A Students • A. Rosen, class of 1962 • M. Thomas, class of 1994 • T. Safford, class of 1994 • J. Traer, class of 1994 • D. Sawyer, class of 1963 • T. Wagner, class of 1961 • P. Schreiber, class of 1962 • T. Walters, class of 1962 • D. Stanchfield, class of 1995 • J. S. Weaver, class of 1962 • D. Statt, class of 1963 • J. Witkowski, class of 2001 • R. Stevens, class of 1963 • E. Yadlowski, class of 1962 Students from Rensselaer Polytechnic Institute: • Daniel Bentz, class of 1996 • Kristen Rybij, class of 2003 • Jeff Fedison, class of 1994 • Jeffrey Schneider, class of • Adam Grossman, class of 2002 2003 • Jackie Krajewski, cJass of 2005 • Joseph Schreier, class of 2003 • Jane Krenke1 , class of 2003 • Peter Thies, class of 1996 • Katie Newhall, class of 2005 • Tristan Ursell, class of 2003 • John Orrell, class of 1997 • Jeff Wereszczynsk.i, class of • Ryan Quiller, class of 2003 2004 • Herman Riese, class of 2003 • Jeff Yu, class of 1997 C)

## APPENDIX B

A Short Guide to MATLAB The experiments described in this book can be analyzed with any of a wide number of computer programs. All that is needed is the ability to sort and plot data. and basic statistical analysis. We have chosen to illustrate the analyses using MATLAB: Although it is a very sophisticated package, a relatively inexpensive student edition that is more than adequate for all of our illustrations is available.

11ris appendix collects some infonnation that should help you navi gate your way through MATLAB. The MATLAB User's Guide is a very useful reference, but there is much more in there than you will need for these experiments. Also remember that you can get help online from http://www.mathworks.com. This site includes a long, searchable list of frequently asked questions, and it is likely that yours is among them. This site also offers you access to programs donated by other users, which you can download and use or modify yourself.

/::::::::~~ 478 B A Short Guide to MATLAB B.1. A MATLAB REVIEW an~~:t\(ff The following is a brief summary of key MATLAB commands \[}[}1~ procedures.

Input Modes. Commands can be executed one by one in the command-\ :}/:~{ tbe)))Jt{~ line mode in MATLAB or you can write a program consisting of note~/\)lJ appropriate command lines in a convenient word processor such as in Windows or emacs on a Unix system, and store it as a file with the ".m'\\\ifJ ...... ..... ,,-~ \{t~J f extension such as programname.m. .

.·.·.·.·l',.'r4·,.- Data Input. Lists of data points are usually input as one-dimensional::;\}:~~~:= ·.·.·.·.~-......• ;J"

matrices (vectors). You can do this in a command line within MATLAB: ):}}~~~=?

II : [[ ~. : i.; ~. :\ .

4] ; )

(The semicolon at the end of the line is not necessary, but if you do no(}];:~ include it, then MATLAB will echo values.) You can also store data in}{)ff~ . . '' ' . ·,:,:.:,:. . :·~..: , .~~·: ASCII columns m a file with the .dat' extension, such as mydata.dat. lit{:(;~;f ~;: the x data are in the first column and the y data are in the second column:)Jti~~ of your ASCII file, then you would use the following commands to load i(}J]@ //f}( into your MATLAB session: J//////11~~ ;lo:ad: :my :d:a :t:a: .~ d: a;t i !!11111!

Simple Arithmetic. To get an online list of simple functions, type he~i}{{}{~f elfun. Formatting for simple calculations with numbers is straigbtforward;{{/~Jf a/bf)\ffl Addition is a+b, subtraction is a-b, multiplication is a*b, division is and raising to a power is a"b. Scientific functions include: · ';::\\}ft • abs(x) for absolute value • round(x) to round to the nearest integer • real(x) to take the real part of a complex number • sign(x) to find the sign (it returns 1~ -1, or 0)

• log{x) for the natural logarithm • log10(x) for the logarithm to base 10 • sq rt(x) to find the square root B.1 A MATLAB Review 479 as well as lhe familiar trigonometric and hyperbolic functions and their inverses, sin(x). cos(x), tan(x}, asin(x), acos(x), atan(x), sinh(x~, cosh(x}, tanh(x}, and so on.

Vector Construction. The easiest way to create a vector with regularly spaced elements is with the command x (start: increment: last)

where start is the first element of a vector~ last is the Jast element, and increment is the step size between the elements. For example, x={O:0.1:1)

creates the vector X = (a 0.1 0.2 0.3 0.4 0.5 0,6 0.7 0.8 0.9 1.0)

(The parentheses "( )" are optional, or they could be replaced with brackets "[ J".) This is also equivalent to using the function linspace(start,last,numberl, where number is the nwnber of entries in the vector. If you would like to define a vector where the increments are loga rithmic, i.e., separated by a constant factor instead of a constant difference, use logspace(start,last,number).

A"ay Arithmetic. To get an online list of matrix functions, type help elm.a!. For operations between a scal.ar and an array, addition, subtraction, multiplication, and division of an array by a scalar look just like simple arithmetic, and the operation applies to every member of the array.

For operations between two arrays oft he same length, addition, subtrac tion, multiplication, and division apply on an element-by-element basis, but the syntax for multiplication and division is different than that for sim ple arithmetic. Multiplication is written a.*b and division is a./b, where a and b are vectors of the same length. (Multiplication and division without the dot correspond to normal matrix multiplication and division.)

Data Analysis. There are· some simple MATLAB functions for caJcu- lating often-used quantities for analyzing a vector x of data values: • length(x) returns the number of elements in the vector • sum(x) adds all lhe elements in the vector • mean(x) averages all the elements in the vector • std(x) finds the standard deviation of the elements.

Note that std(x) is equivalent to sqrt(sum(fx-mean(x)) .... 2)/(length(x)-1 )).

The command [n,x]=hist(y,nb) takes a vector y of data values, calculates a histogram with nb equally spaced bins, and returns vectors n and x, which give the frequencies and midpoints, respectively, of the binned data.

480 B A Short Guide to MATLAB cussed, along with reference to MATLAB, in Section 10.3.3. · {\)f When the data points are equally weighted, all of the operations nee- (/\{ }{/ft essary to fit a polynomial to a set of (x,y) data points are· included in the command p=polyfit(x,y,m), where m .is the order of the polynomial. A fit to /{)}} a straight line is therefore p=po(yfit{x,y,1). The vector p holds the best-fit ·.?{}} )J(ff values in order of decreasing polynomial order. For exainple, if m=2, then · \)Jt you are fitting to a quadratic function ax2 + bx + c and polyfit returns p=[a,b,cJ. ·t::::~:;?

/}jf@H The values of the fitted function can be computed for a set of x values x1 using the command yl=polyval(p,xl ). (If you want to compute the fitted ;}j}if function at the data points, just use something like yfit=polyval{p,x).) ·;}]fl ))!lJ If the data points are not equally weighted, then you can use Garcia's function linreg to fit to a line. Note that you can retrieve this code from the·. {!)ff!

. :-:-:-;~. .; ..J ; MATLAB Web site. . :::}i;:?

_:(/l~i :Nonlinear Least-Sqltares Fitting. If you cannot express the function :{//f: you want to fit as a polynomial, then you cannot use polyfit or finreg. If the· ·}f/ii function is still linear in the fitting parameters, though, you can use matrix ._\:if~ techniques to solve the equations. However, it may·be simpler just to resort to numerical techniques to minimize x2 directly. You are forced into this )jJf( situation if the function is nonlinear in the fitting parameters anyway. For }}{?!

example, if you want to fit some decay data to y Ae- xt>.., then you can -:\{){ instead fit a straight line to logy log A - x / ).., but ift here is a background :)){( = + ;}(\?

term, as in y Ae-xf").. B, then you must use numerical techniques.

Defining the x 2 function in MA1LAB is quite straightforward, and there :))ffi is a l\.1ATLAB function called fminsearch, which will do all the hard work }{{)

of finding the values of the parameters that minimize the x 2 function. (See; ))f{ :(JI\ for example~ Section 8.6.2.)

\//?

Simple Plots. There are several simple variations on the plot command · that will give you everything you need for these experiments. If you really '}({: )}{!: want to do more, see the next section of this appendix. · • plot(y) plots the column values of y versus index. It autoscales the axes. Points are connected by solid lines.

• plot(x,y) plots vector y (vertical) versus vector x {horizontal) on an autoscaled plot. Points are connected by solid lines.

• plot{x,y,' linetype') allows you to specify the type of line that connects the points of the type of symbol that is printed on a data point. For '4linetype" use '4-,'' ":," "w -,"or"-.'' for solid, dotted, B . 2 M a king Fa n c y PI o ts in MATLAB 481 dashed, or dot-dash lines, respectively, or use".," "o," "x," "+,"

or "*" for the corresponding plot symbol.

• bar(y) draws a bar graph of the elements of y versus index.

• bar(x,y) draws a bar graph of y at the locations specified by vector x.

• stairs(y) and stairs(x,y) draw "stairstep" histogram plots.

You can plot more than one set of data, or data and a fit, by specify ing more than one set of vectors in plot. For example, plot(x,y,'o',x,yfit,·-·)

plots "data" vector y versus x as little circles, and then overplots the ''fit" vector yfit as a solid line through the points. Another way to over lay plots is to hold a plot and then just repeat the plot command with new vectors. When you are finished collecting overlays, use the command hold off.

Simple labels are put on the graph using the commands • xlabel(' label on the x-axis't • ylabel(' label on the y-axis'~ • title(' title for your plot' t • text(x,y,' some text') puts some text at point (x,y)

• legend( 'string 1', 'string2: ... ) labels different sets of data added to the same plot To print your plot on the default printer, use print Printing to files or to other printers will depend on which system you are using to run MATLAB.

Consult the online help or the User's Manual for details.

B.2. MAKING FANCY PLOTS IN MATLAB It is simple to make MATLAB plots with the default ~baracteristics. Some times, however, that is not quite what you want,/especially if you are preparing a formal lab report. _/ You can also, of course, consult the Mathworks Web page help directly for some hints. For example, if you want to know how to add Greek char acters to your plot, click "Tech Support Solution Search" on the Web page, and search for keywords "Greek AND plot" You will find "492 How can I place Greek characters in my plot?" in the search results list. Clicking on this solution tells you not only how to do it, but also tells you how to get an m-file, which will make a chart for you that shows the mappings for all the various Greek letters and symbols.

!i//:!11 482 B A Short Guide to MATlAB • !ii/I/ lj You can dress up plots quite a bit in MATLAB using what is called \(@{ "handle graphics." Every plot, and plot element, has a ''handle'~ that you can access in order to change properties of the corresponding element- }}/~f :/){?: Most plotting commands return the value of the handle if you ask for it. · For example, h=plot(x,y); will return a value for the handle h that can be ))j}~{ used with the command set for modifying properties of the plot. Refer to .)))})

./!fl/Ji the on-line documentation for more information. ~

## APPENDIX C

Laser Sa/e ty Laser radiation can be dangerous, and in particular it can result in serious and pennanent damage to the eye. Thus it is important to .be aware of the hazards involved and to follow the rules for safe ~ .e10iaoperation oflasers.

Explicit rules and standards are given in publication ANSI 2136.+-1986 of the American National Standards Institute (1430 Broadway, New York, NY 10018).

The damage a laser can cause depends on the level of the emitted power for CW lasers and on a combination of power and energy for pulsed lasers.

The energy per unit area is a better measure of the hazard from direct irradiation. The most serious danger, however, from laboratory lasers in the visible and near infrared (i.e., Nd: YAG) is that they can be focused by the eyeball onto the retina where they will create a permanent blind spot.

This is particularly serious for infrared lasers where the beam is invisible.

Thus protective IR absorbing glasses (typically of optical density 4) must always be worn in rooms where IR lasers or beams are present.

Lasers with power below 1 m \V are classified as Class 1 lasers. At this power level the exposure in the time it talces for the eye to ''blink,"

484 C Laser Safety approximately 0.25 s, is considered safe. The HeNe laser used in this laboratory is a Class 1 laser. Still one should never stare directly into the beam, or let a specularly reflected ray enter the eye. No eyeg~es are needed but one must use common sense and remain alert. The 'rasers installed in commercial scanners to which the public is exposed are Class I devices. One advantage of the HeNe is that the beam is clearly visible so one is aware of stray beams. Stray beams result from reflection off the various optical elements and other smooth surfaces; they should be blocked or minimized.

Lasers with more than 1-mW power are generally classified as Class 4 devices, as are most pulsed lasers. Nd:YAG and argon-ion lasers can easily deliver several watts of power. Such lasers will cause permanent eye damage instantaneously before one is aware of it. In the case of Class 4 lasers only qualified trained personnel can enter the laser room, which must be kept locked with appropriate signs indicating laser operation. The nitrogen pulsed laser emits in the ultraviolet at).. 337 run. UV is invisible but can be absorbed by plexiglass, so that ordinary safety glasses are not effective; certain materials (i.e., a business card) will fluoresce and can be used to locate the beam. Similarly, IR beams are located with special -.fluorescent cards and/or with IR viewers.

The need for obeying safety rules and procedures around lasers is a real one, and not a "bureaucratic whim.'' Never look into a laser beam, be aware of the stray beams, and wear glasses when required. Do not let others be exposed to your laser.

## APPENDIX D

Radioactivity and Radiation Safety In a series of experiments on quantum physics, the student comes in contact with radioactive sources. either while srudying the properties of the nucleus itself or when using the sources to obtain energetic beams of alpha or beta particles or gamma radiation. As is well known, radi ation can be harmful to humans, and therefore precautions must be taken against undue exposure to it, and in the handling of radioactive materials.

In addition to the naturally occurring radioisotopes (which have long lifetimes), a great variety of isotopes have been produced artificially and many of them can be purcbased._A convenient table of radioisotopes, many of which, like 60co, 22 Na, and 137 Cs, are quite standard for training, testing, and calibration purposes, is available online from the Particle Data Group (PDG) at Lawrence Berkeley National Laboratory: http://pdg.lbl.gov/2000/sourcesrppbook.pdf 0 Radioactivity and Radiation Safety \)ff with separate information for the different decay schemes, of each radio- isotope. Much rnore detailed information is available from the National )/)f Nuclear Data Center (NNDC) at Brookhaven National Laboratory. This · \ /{/ information includes level and decay schemes, radiations emitted, and )){} \))f thorough documentation on using the various online programs made available to the user: ~ .)}ff /iii!

http:/ /www.nn de. bn I.gov/ nn d c /nud at/ .· · : / In the handling of radioactive materials the following regulations should '}:}~?

-:-:-:-:·:~; al ways b e observed : ·. ::::::::;;/: i~1?=~~::::s.

~;:~rii~~?~~~f I betas, etc.).

## 4. Use gloves when danger of contamination exists

## 5. Use tongs for handling strong samples (but only if you can do so

safely).

## 6. In case of a spill, wash it off immediately

## 7. Report all accidents and mishaps connected with radioisotopes

## 8. Do not take radioactive sources out of the laboratory

Radiation is harmful to living organisms because by ionization it destroys individual cells, and also because it may induce genetic changes, It seems established that low levels of radiation do not produce permanent injury, but the effect is assumed to be cumulative. A genetic change, on the other hand, can be produced by low-level radiation as well as by high-level }}?)

}\ff radiation, but it should not be forgotten that human beings have always · \){f been exposed to cosmic rays and natural radioisotopes.

/?}?

In all establishments where some potential radiation hazard might pre-.· ))ff vail there must exist an agency (the health physics group) that is responsible for personnel and area monitoring, and for source custody. The health ){@l /)ff physics groups keeps a record of radioactive sources and other hazards,.

••• 4 ... .,,.

and of radiation accidents, and in general helps in the enforcement of safe ./ /{~~~~ \(if procedures. It should be clear, however, that the sole responsibility for enforcement of proper practices rests with the individual who has been· )?f~ .)J@ granted the privilege to work with a radioactive source. The aversion of /Jf; many scientists to observe strict rules is a common phenomenon, but it . ''.· .·,-.•.•J"

must not be imitated by the student. ·\::::ii::~ ;:1 D Radioactivity and Radiation Safety 487 Two peculiar aspects of harm from radiation need speciaJ mention and warning: (a) radiation is neither visible nor painful; hence one may not be aware of having been exposed unless proper detectors are used; and (b) in general it is too late to do anything after one has been exposed.

Excluding nuclear reactors and particJe accelerators, the most serious radiation hazards come from X-ray machines.and from taking internally a small amount of radioactive material from a source used in a laboratory.

The PDG publishes online an excellent summary of the writs and con version factors for raruation and radiation doses, as well as recommended exposure limits and radiation protection procedures: http://pdg.lbl;90v/2000/radiorppboolcpdf Finally, we conclude witl{some remarks about radiation shielding. This is important not only for ~{sonnel protection, but also to reduce back grounds in an experiment in which the primary radiation from a source is not meant to be detected.

The purpose of shielding is to attenuate the radiation beam. If the beam consists of charged particles, they do lose energy as they cross matter, and if the shield is sufficiently thick the beam will be completely stopped.

Since the energy loss is proportional to the number of atomic electrons Z of the shielding material, Iow-Z materials have a larger stopping power per (nucleon) gram. On the other hand, the higher the density, the higher the stopping power per unit length of shielding.

The attenuation of a gamma-ray beam, however, is different; no grad ual energy loss occurs, but there exists a finite probability (c ross section)

for an interaction. Interactions (electromagnetic) of a gamma-ray beam with matter are either the photoelectric effec~ Compton scattering, or pair production, depending on the energy of the beam. As. explained in detail in Chapter 8 through a series of such processes a fraction of the beam becomes completely absorbed in the material used for shielding. Since the interaction probability is proportional to the amount of material present, we have -- = IK, hence I = l oe -KX , = = where x is the length of the shield, K 1/L rr,pNo is the absorption coefficient, and L is the radiation length (L 0.51 cm for lead).

!/;///ii D Radio,activity and Radiation Safety ,I f the beain consists of particles with strong interactions~ such as neutrons -.-:-:-:.:-:-.

:{;~{:; :s:a:!::O?sii::~~:et::;:::t:::::: ii/ii ·\\!)

source is distance; since the inverse square law holds, keeping at a 10-m distance dilutes -the flux over the value it had at contact with the ource;- .\{:} ·/{\j (assuniing·an-extent of 5 cm) by a factor of 40,000; for gamma ra:fs such· \}j attenuation is equivalent to shielding by 7 cm of lead. .

..··..-·..··..-·..,,. '.,, .,' ·tr@ \JiH ,!/ii <::::::;:;::- ::;::::::~~:: ..

··<-:-:-:. .; -- ..··..··..··..··_- . · ._ . . _ - . ) 11111 ·.·.·.-.-,.· } ·111 /iJJ J!i _,,, ~=}~}?; .·.·.·.·J ::;:::::; :\~i~~i .·.·.·~"J ·..··..··..··,."-,..,•.

• t •• • • •• ·,·.· •• •,•.·,:,.;:• • • • ~;:~:;:~:\ •• • ·:-·

## APPENDIX E

....

·.·, Optical Detectiitfl: Techniques If we are going to do experiments with light. we have to learn how to measure it. There are several properties of light that can be measured, for example, its intensity. wavelength, or degree of polarization. In this section we discuss ways lo measure the intensity, either as energy per unit time or number of photons per unit time.

In order to work with intensity quantitatively. we need to convert it to a voltage level that can be recorded or digitized or so on. However, the simplest option, namely photograph.ic film, still lets you distinguish "dark"

from "light" and bas some advantages. We discuss it first.

E.1. PHOTOGRAPmc FILM Photographic film uses light and che.m,jcal reactions to record light intensity. It of course has some obvious drawbacks. For example, itis hard ~l i]!!if 490 E Optical Detection Techniques -':.:; .:: !!!!/i!]I~l!

_·i\/\fi to convert this record into a voltage, although film-scanning machines are built for this purpose. Another disadvantage is that it is inconvenient to )j(!J~Ji :/)JI~ record large amounts of data this way, unless some fast and efficient scan- rung method is available. On the other hand, film has some great advantages \ }!)/ \/t~i~ as well.

--- .·.·.·.·.·.·.·.·-·.

First of all, film is economical. You can record light intensity)bver {{:/{{ quite a large area for very little money. Astronomers, for example, photo- ·:/\!){}j \}Jl~ graph large sections of star fields on a single photographic plate, giving an }i\@f[~ accurate and reliable record, all for only a few dollars (in film) per picture.

}:/Jl~ Secondly, film gives you data that you can easily relate to. Distances .....

,',·.·.·,;•.,. .,,,,.;".

between images are true, at least to the extent of your focusing device, and}{/~:~~{: {/}f~~ you can remeasure or check them easily. There can be an abundance of data if)}{@{j on a single photograph, and you can always go back to the same picture ·}}!J~tt you want to recheck things.

J(i~Jt Most importantly, however, film has outstanding position resolutio~ - . } .. \ . J ... J..,._ ~ .. .

especially for its price. This resolution is limited by the grain size of the ·~ ..... ..

' ',/'.,.

fl~ and 10 µ.mis simple to achieve while 1 µ,mis routine with a little care. ..: \/}~~;}~~ many·: ))t~~~it What is more, this resolution can be achieved simultaneously over .·.·.·--./·,.. ........J ..

centimeters of distance. This is almost impossible to achieve with direct}:/::~:=::[:: .: . : . : . :" :--~·:-:~- electronic means, and can be quite important to astronomers measuring· \ {{{ti star maps and to optical spectroscopists measuring precise wavelengths. \ {/}\ \/ff} An important trade-off is between resolution and speed. A film like Kodak Tech-Pan can be used routinely for 1-µm resolution or smaller, but·/ }}~f?

it takes a lot of photons to convert a grain. Thus, such a film is limited to )\jj~f cases of rather large light intensity or where you can afford long exposure./ /\f times. Somewhat faster films, like Kodak Pan-~ are much faster, and still :)))}) ))i\lf give resolutions perfectly suitable for 1nost applications.

//ttt )i!{lfi E.2. PHOTOMULTIPLIER TUBES )i}!lf }/:f~;:j The photomultiplier tube (sometime shortened to "phototube" or PMT)

• ·.·.·.·,r..,•~4'.I:_,, is probably the oldest device for converting optical photons directly into.-))f~t ./{~ti electrical signals. It does this 'vvitb very high efficiency and is very reliable, :\lf{1 Some can detect single photons and easily distinguish the signal from back- ){itf ground noise. Others are made to measure beams of light. Photomultiplier }\J~§: tubes have been in development for more than 50 years, and have evolved .

.·.·.-,.,,., .,., into lots of varieties, some of which are quite sophisticated. The basic)}~:~~:} .·.·.·.•r,.,-...-.,,. .

·::::::?:~~:J: operation, though, is simple.

E.2 -P-hotoinultiplier Tubes 491 The photomultiplier tube is bas·ed .on two:effects,-both of which involve the emission of eJectrons from t):le surface of materials. The first is the photoelectric effect, where a Pfo to-p: -is-:- absorbed by· an electron on the material surfac~. The electron ~~ eme~es·w ith some small kinetic e?ergy; thus a photoo 1s "converted" m~ electron. The second effect 1s that when an electron of some moderate'::energy :-strikes a surfac~ a number of electrons are emitted (This process· is· called '~secondary entlssion.")

Secondary emission is used to multiply-::the :·initial electron ihto a large number of secondary electrons. All of.this takes-place on surfaces enclosed within an evacuated glass rube, hence, the· nru;ne photomultiplier tube.

A schematic photomultiplier tube is shown in ·Fig: B. l. The photoelectric effect acts at the front surface, or face, of~(? PMT, and there one photon is converted into one electron (with a certi.i.if efficiency less than I). There is a potential difference of 100-300 V between Ul~ fac~ and the first "stage" of rv ·Vlji~ii\i\is the tube, and this accelerates the electron~ f~300 e V electron strikes the first stage. it emits mor:e electrons;· ·wb.i'th:.-ai~- accelerated to ifug~s the next stage, and so on. These ma:teri~s: :th~('~c( ~ - are called "dynodes" since they act both as acceptors of d~dtotis (i.~./:anodes) and emitters of electrons (i.e., cathodes). Aftetse\#eral_(us~lly ~tween 6 and 14) stages, a significant number of electrons e~ie~gl~ pfa~·o f the incident photon. Electrical connections are made with the out.side worlcfby pins that penetrate the glass envelope on the end. : some The front window of the PMT is made of glass or ·other transparent material. A thin layer of some optically active_m aterial ·is ev·aporated on the inner surface of the window. Th.is layer,· ~all~~ the photocathode, is semitransparent and is usually brownish in c·olor. If _the· tube breaks and air fills the inside, the photocathode oxidizes away aild the brownish col.or ilisappears. In thls case, the photomultiplier tube will never work again.

C-d,o_w_ __~ _G_ra_ss_en_v_a_Io_p_e _____ __, Anode out Photon ' e Dynodes Photocathode Connection pins FIGURE E. l How a photomultiplier tube works. The connection pins are used to supply high voltage to the individual dynodes. and to extract the a.node output.

492 E Optical Detection Techniques !!

· . .· · . . · · . .· · . .· ·• .· · . . . · .. . · ·. ..· · i-:/:i::\:::@:::;.::::i: A photon incident on the window penetrates it if it can. In fact, glass :wvind:o:w; tu:b~es b;e!co:m°e£ ver~y in~eff~icie~nt i0n th:e: n;ea~r U;V~ be:ca=use~ phsoto·n=s w~ith ••· .·.·.·.·.·-·.·.· !~fl~!

}J special windows made of quartz or CaF2 are necessary, and the dewtes :/ )

\/?}/ become very expensive.

.','.·.·. .· .:,.·. . ·.· ..

If the photon penetrates the window~ it reaches the photocathode and has-· ·. !{:}if :/)j/ a chance to eject an electron through the photoelectric effect Recall that ........." -;;,;~,~ ..

in the photoelectric effect, a photon of energy hv gives rise to an electron }})~:\]

.///1t of kinetic energy T given by l!I T hv - ¢, . )

where 4> i~ called the ~'work function" and represents the energy needed:.: ( )I~f /:}jf~f:~~ to remove the electron from the surface. Several different materials are used for photocathodes, but all are designed to have work functions small enough so that optical photons can eject electrons. It is in fact jlard to find materials for which </> is less than ~2 e V, so photomultipliers become quite insensitive at the red end of the visible spectrum.

The probability that ·an incident photon ejects an electron from the tii;~7ii:£;~; !:i;;::~~i!l!if Ed!~~: la!1f jl~Jl~li reasons. Figure E.2, taken from the Burle photomultiplier tube handbook, ..} }!{{?

s ·::;;nitt\ shows the '.'spectral sensitivity" (in lnA/W) for various combinations ·\{(If of windows and photocathodes. Manufacturers tend to quote S rather than QE since it is closer to what th~ PMTs actually measure. By shin- :: )/j@{ji ing so much light energy per unit time (P) on the face of the PMTY ancf' \{/// ·_j({{f measuring the current ( I) of electrons coming off the photocathode, they ~ llJ dete7e !_ = Nclectron X e/t = Ne1ectroo X = QE X ~.

P Nphoton X hv/t Nphoton hc/e . 1.24 ·)~:\;~~~~:~ ' -::::::::==~~;~:=~ .}\\?~~=~ where S is written in mA/W and ).. is in nanometers. Curves of constant /:)}~ff QE are drawn in on Fig. E.2. Typical quantum efficiencies are maximum • • .- : ,: -: -: < m the blue region and range upward of 25% or so. .

:}!/:~~j{-:~~4~:~--~~ Now let's return to Fig. E.1 and see how the photomultiplier tube arnpli-·.}{!~J~ fies the signal. The incident photon has ejected an electron with something}:\\i~~~~ E.2 Photomultiplier Tubes 493 e l---+-~=-,..~~~~=:.:..=--J------l --- 6 1-----#-----,'-,~.;:;i==-=,.___,.....p-i~-----1 t: ---- ')

(D

## C

0 -- a.

U) 8 ~\\{\~- Cl) ?,.o/o~-- s ' e - n 6 ,, ,,. ...

,,. .., .2 4 300 400 500 600 700 Wavelength~Nanometers FIGURE E.2 Spectral sensitivity ( .. absolute responsibility'1 and quantum efficiency (QE)

for some photomultiplier tnbe windows and ph'otocathodes. From the Burle photomultiplier tube handbook. available on tine at http://www.burle.com/.

like an electronvolt of kinetic energy. This electron is accelerated to the first dynode and strikes it The dynodes are constructed out of materials that give a significant mean number of electrons out for each that strikes the surface. This multiplication factor Dis a strong function of the incident electron energy, and is roughly linear with energy up to a few hundred electron volts or so for most materia]s used in PMTs.

There is clearly some randomness associated with the operation of a photomultiplier. The quantum efficiency, for example, only represents the probability that a photon will actually eject an electron. The result is that the output voltage pulse corresponding to an input light signal will have random fluctuations about a mean value. We therefore frequently talk in terms of the "mean number of photoelectrons" NpE that correspond to a particular signal.

Assuming that Poisson statistics dominate, th.is number will dominate the size of the fluctuations, since the number of electrons ejected in subsequent 494 E Optical D ete cti on T ec hniq u es stages will be larger. That is, the fra.ctional rms width of the signal fluctu ations should be given by ~/N pE = 1~. This can be particularly ;!({ff )/Jf important if the signal corresponds to a very low light level, i.e., a small ~ .{//~J value of NpE. In this case, there is a probability e-NpE that there will be no ·:;j(!{/l photoelectrons ejected and the signal will go unobserved.

r ·.·.·.·.·-·----.· The gain g of a photomultiplier tube is the number of electron~t the /:}ff back (i.e., at the anod~) for a single incident photon. So, for an n-stage }\}}~; ~ ~ :111 ill~ 8 8 I dz · · · X 8,, 8", o \(j~l!

where we tacitly assume that is the same at each stage~ i.e., all dynodes )}!Jl are identical and the potential difference across each stage is the same. If 8 is propo1tional to V, then these assumptions 1 predict that g is proportional )?J§§f }j/Jl~ vn.

to Thus if you want to keep the gain constant to 1% in a 10-stage : ·:;{]§@; photomultiplier tube, you must keep the voltage constant to 0.1 %. This is not particularly easy to do. · /:;:;:~~==::; .....z ...

·/}}fl!

The accelerating voltage is usually applied to the individual stages by a single external high-voltage DC power supply, and a multilevel voltage· }Ji}~~ ·://J?

divider. The voltage divider has output taps connected to each stage through :)//fl the pins into the tube. This is connected to the circuit that extracts the /@Jj signal from the anode. The extraction circuit and voltage divider string are housed together in the photomultiplier tube "base,'' and their design will \))}\ vary depending on the application. The base is usually some sort of closed \ }\~) ){!\{ box with a socket that attaches to the tube pins. Two examples of base circuits, taken from the Philips photomultiplier tube handboo~ are shown ·}}}~)

in Fig. E.3. If the signal is more or less continuous, and, for example, a ·) )\\ meter reads the current off the anode to groun~ you must use the negative ) \}\ ?ttr high-voltage configuration that the anode is at (or near) ground. If the $0 output is pulse-like, such as when ~'flashes" of light, or perhaps individual .){~tr :{}Jf photons, are detected intermittently, then it is usually best to use the positive high-voltage configuration since that leaves the photocathode at ground. :.}\})

·)}~?

In this case, an RC voltage divider at the anode output allows fast pulses :\/J?

to reach the counter, but the capacitor protects the downstream electronics ·.·.·.·-·%·.· from the high DC voltage. _,... }}::~~~:: .<!)~it!!

\{ff 1These assumptions are almost always wrong. We are using them just to illustrate the .//f~f general performance of the PMT. For actual gain calculations, yon must know the specific \J{f characteristics of the PMT.

E.2 Photomultiplier Tubes 495 vh1 ,-------------~---- (+)

FIGURE E.3 'fypical photomultiplier base circuits. The upper figure shows connections for a positive high·voltage configuration, while the lower shows negative high voltage.

No matter what circuit is used, either those in Fig. E.3 or otherwise, you must choose the resistor values carefully. Although lhe stage voltages only depend on the relative resistor values, you must make sure the average current passing through the rlivider string is much larger than the signals passing through the PMT. Otherwise, the electrons in the multiplier will draw current through the resistors and change the voltage drop across the stage. Even if this is a small change, it can affect the gain by a lot since the gain depends on voltage to a large power.

On the other hand, you cannot make the resistors arbitrarily small so the divider current gets very large, because this would require a large and expensive high-current, high-voltage DC power supply. What is more, the power dissipated in the divider string, i.e., 12 R, gets to be enormous, malci.ng things very hot. Trade-offs must be made, and always keep your eye on the gain.

496 E Optical Detection Techniques E.3. PHOTODIODES Photodiodes are an alternative to photomultipliers. Both turn light directly into electrical signals, but there are distinct differences. _First, let's learn how photodiodes work.

Recall our discussion about diodes in Section 3.1.4. A piece qf bulk silicon is essentially an insulator. Only thermally excited electroiit:can ·/J%} few of them at room temperature. By adding n-or p-type dopants, lots more · )Jff charge carriers can be created, and it is a much better conductor. A piece of .\i/{If silicon doped non one end and p on the other, a pn junction, only conducts _:/}?f in one direction. If a "reverse" voltage is applied, only a tiny current flows, ..•• ,.,-~,,11.,. )}ii}i due to the small number of thermally ex.cited electrons.

})it A photodiode uses light (photons) to excite more electrons than those \/Jl}i excited thermally. This is possible if the photon energy is larger than the band gap. Thus, the "reverse" voltage current would increase if you shine · !)}~} /\1*f light on the diode. This is the principle of the photodiode.

The actual mechanism is a bit more complicated, because ofb ow excited )}~~;~ :•\•}• , ..i. J"•f •}.

electrons actually conduct. So~ for example, for a given applied voltage, · the output current is not very linear with intensity. That is, if you double .: . ? ·.· . ? ·r iI''": :.. :~. .:." .

the light intensity, the output current does not change by quite a factor of 2 :{}{} :)/f?

(over the "noisen from the thennal electrons). Furthermore, a photodiode \){}f can work if there is no applied voltage, reverse or otherwise. This all means tbatyou must calibrate yourphotodiode response if you want a quantitative _}/?)

\!}){ measure of the light intensity.

A popular form of photodiode puts a large region of pure, or "intrinsic, n ·.\ (\/ silicon in between the p and n ends. Th.is increases the active area and )(ff )){?

decreases the thermal noise current. These photodiodes are called p-i- n or "pin" diodes ·::::::=:::=:::: Now let's ·look at a clear advantage that photodiodes have over photo- · :/}{()

tubes. The energy gap in silicon is 1.1 eV , so photons with wavelengths . -){if! )i\J/ up to ~ 1.1 µ,m can be detected. This is well past red and into the IR. · :}@~Ii Photomultiplier tubes become inefficient at around 600 nm (see Fig. E.2)

or so because of the work function of the photocathode. The band gap ./)jf .·/?ff of germanium (another popular semiconductor) is 0.72 eV, so germanium ·\\}f photodiodes reach).. ~ 2 µm. So, if you need to detect red light, you probably want to use a photodiode, and not a photomultiplier tube. :}/) )f!l?:~ Another big advantage of photodiodes over photomultiplier tubes is cost..

A photomultiplier tube with voltage divider circuitry, high-voltage supply, }}Jf .] I E.3 Photodiodes 497 and mechanical assemblies can easily cost upward of $2000. A photodiode costs around $1, and is very easy and cheap to instrument.

Photodiodes can also be made with very small active areas (say 50 µ.m across). This along with their low cost makes "photodiode arrays" practi cal. These are lines of photodiodes, separately instrumented, that measure photon position along the array. Such things are frequently used in spec trographic instruments. A typical example might be 1024 25 µ.m x 2.5 mm photodiodes arranged linearly in a single housing with readout capability, as discussed in Section 5.5. The cost for such a device is typically less than a thousand dollars.

Of course, photomultipliers have some advantages over photodiodes.

The biggest is the relative signal-to-noise ratio. A microwatt of incident light power gives around a 1-µA signal in a photodiode, but around 1 A in a photomultiplier tube. This big enhancement in signal is due to the large gain ("-'lot> or more). Thermally excited electrons are plentiful in a photodiode, but rarely does such an electron spontaneously jump off the photocatbode in a photomultiplier. Therefore, the noise is a lot larger in a photodiode. Thus, the signal-to-noise ratio is much worse in a photodiode.

So, if you need to detect very low light intensities ("photon counting"

for example), you probably want to use a photomultiplier tube, and not a photodiode.

Pbotomultipliers also give a more linear response, particularly if care is given to the base design. Some of these relative advantages and dis advantages are shown in Table E.1. Another advantage of photodiodes is that they work in high magnetic fields. Photomultiplier tubes rely on electrons with ~ 100-300 e V energy to follow the electric field lines to the dynodes. A few-gauss magnetic field disturbs the trajectories enough to render the PMT useless. In most cases. magnetic shielding solves the problem, but sometimes this is impractical and photodiodes are used instead.

TABLE E.1 Photomultiplier Tubes Versus Photodiodes If you are Then your choice should likely be interested in ... Photomultiplier Pbotodiode Low cost Red sensitivity Low intensity Linearity 498 E Optic al Detection Tee hniqu es 1111111 Finally, we mention that photosensitive transistors, or phototransistors,. {\({]

are also available. They use the natural amplification features of the tran. . } }}~{:!

/\jJ}~ sistor to get a --100 times larger signal than the photodiode. Of course.

:;\{!~~I the transistor also amplifies the noise, so there is no improvement in the, !:)j{@ sensistivity at low intensities. · 4J I@ :\\if ,-::::::=:::; )/~i~t .·.·.--.·-·.·.

·):i:}}~: jff .·.·.·.·.•.· .::::::;::::: -:-:-:•:•:•: .-:-:-:-:. .: • .::::::::::; .::::::::::: :::::::;::: .·.·.·. .· -·· ::::::::::: , ,· · . .- · . - - ·- ~ ·. ..·- ., ::::::::::, ,-:::::;:::: ·:::::::::: ·:ff ,:-I:·~: .-:-:·~: ':)!ti \Ji .·.·.-.;- \@ }!~/ )l ·.-.•.•.1 <Jif ,:::::"/, ..

· . . . - . .- • ~, .. .. J

## APPENDIX F

Constants Table F.1 of fundamental constants is taken from the "Reyjew of particle properties," published in Plrys. Rev. D 50 (1994). The uncertainties in the values are very small and can be neglected for the experiments in th.is book.

TABLE F.1 Fundamenr.al Constants Quantity Symbol Value Speed of Jight in vacuum 299792458 mis Planck's constant h 6.6260755 X 10-J4 J S n/2Jr 6.5821220x 10-22 MeV s Electroo charge e l.60217733x 10-19 C lie 1.97327053x 10-13 MeV m Vacaum permittivity 8.8541878 t7 x 10-12 F/m '=O Vacuum penncability µo 4.rr x 10-7 N/A2 Electron mass tne 0.51099906 MeV/c2 Proton mass mp 938.27231 MeV/c Deuteron mass md 1875.61339 MeV/c2 Atomic ma.c;s umt u 931.49432 MeVJc2 Rydberg energy hcR 13.605698 l eV Bohr rnagneton µB en/2m~ 5.78838263x 10-ll MeVrr Nuclear magneton /1-N = eh/2mp 3.15245166xl0-14 MeVff Avogadro constant No 6.0221367 x 10 23 atoms/mole Boltzmann constant k 1.380658 X 10-23 J/K ,--._ .... .

•) _ ••) 4 "' -:x )I ·.".:-

## APPENDIX G

Exercises ..

The following exercises may be used.

## 1. The following table lists data points for the decay rate (in count-Js)

of a raclioactive sowce: nme Rate Time Rate Time Rate (s) (s-1) (s} (s-1) (s) (s-1)

## 0.6 18.4 2.0 3.02 3.6 l.72

## 0.8 10.6 2.4 2.61 4.0 1.61

l.2 8.04 2.8 2.08 4.2 1.57

## 1.6 6.10 3.0 1.50 4.3 1.85

a. Plot the data using an appropriate set of axes, and determine over what range of times the rate obeys the decay law R Roe-1 /r.

b. Estimate the value of Ro from the plot.

C. Estimate the value of t' from the plot d. Estimate the value of the rate you expect at t 6 s.

## 2. An experiment determines the gravitational acceleration g by

measuring the period T of a pendulum. The pendulum has an adjustable 502 G Exercises length L. These quantities are related as =2rr!f.

A researcher measures the following data points in some arbitrary units.

Data.

point L T 1 0.6 1.4 2 1.5 1.9 3 2.0 2.6 4 2.6 2.9 5 3.5 3.4 One of these data points is obviously wrong. Which one?

## 3. Consider the following simple circuit:

"in o~ -_-i Let the input voltage Yin be a sinusoidally varying function with amplitude Vo and angular frequency w.

a. Calculate the gain g and phase shift tP for the output voltage relative to the input voltage.

b. Plot g and </J as a function of cv/wo where wo 1/R C. For each of these functions, use the combination of linear or logarithmic axes for g and for ¢ that you think are most appropriate.

## 4. Consider the following simple circuit:

VOi,( G Exercises 503 Yio Let the input voltage be a sinusoidally varying function with amplitude Vo and angular frequency w.

a. Calculate the gain g and phase shift </> for the output voltage relative to the input voltage.

b. Plot g and¢ as a function of w/wo where wo = R/ L. For each of these functions, use the combination of linear or logarithmic axes for g and for <I> that you think are most appropriate. ~

## 5. Consider the following not-so-simple circuit:

C L a. What is the gain g for very low frequencies w? What is the gain for very high frequencies? Remember that capacitors act like dead shorts and open circuits at high and low frequencies, respectively, and inductors behave in just the opposite way.

b. At what frequency do you suppose the gain of this circuit is maximized?

c. Using the rules for impedance and the generalized voltage divider, determine the gain g(w) for this circuit and show that your answers to (a) and (b) are correcl

## 6. Suppo~e that you wish to detect a rapidly varying voltage signal

However, the signal. is superimposed on a large DC voltage leve] that would damage your voltmeter if it were in contact with it. You would like to build a simple passive circuit-that allows only the high-frequency signal to pass through.

a. Sketch a circuit using only a resistor R and a capacitor C that would do the job for you. Indicate the points at which you measure the input and output voltages.

504 G Exercises b. Show that the magnitude of the output voltage equals the magnitude of the input voltage, multiplied by .jl 1/w2R2C2 ' where w is the (angular) frequency of the signal.

c. Suppose that R := 1 kQ and the signal frequency is 1 MHz := ~ 10 /s. Suggest a value for the capacitor C.

.·)i}jfg

## 7. An electromagnet is designed so that a 5-V potential difference drives

·)/{?{ 100 A through the coils. The magnet is an effective inductor with an induc- tance L of 10 MHz. Your laboratory is short on space, so you put the DC. ){J{{:} \f)l~~ power supply across the room with the power cables along the wall. You.

notice that the meter on the power supply must be set to 6 Vin order to get ))@§t~ ./}t~~~§?.

5 Vat the magnet. On the other hand, you are nowhere near the limit of :\/{:§Jj the supply, so it is happy to give you the power you need.

Is there any reason for you to be concerned? Where did that volt go~ ?••• ' )•••f•~ §,.• ••J §'., ;'",.},. J4 and what are the implications? If there is s01nething to be concerned about,._}}~~~~~ ·-:-:-:•:4;.. .; ::;-:•/.

suggest a so1 u tion. \)}~~?-a

## 8. You are given a low-voltage, high-current power supply to use for an ./:}~tf!

))j}Jt experiment. The manual switch on the power supply is broken. (The power )//??

supply is kind of old, and it looks like someone accidently hit the switch ..

with a hammer and broke it off.) You replace the switch with s01netbing .}\\\\ /{\{J you found around the lab, and it works the first time, but never again.

When you take it apart, the contacts seem to be welded together, and you :;}}/~{~ know it wasn't that way when you put it in. What happened? (Hint: Recall \)}})

that the voltage drop across an induct.or is L di/d t, and assume the switch){){{ disconnects the circuit over 1 ms or so.) · :}){~~?

.\J//f

## 9. The following table is from the Tektronix Corp. 1994 catalog

·:))If\ selection guide for some of their oscilloscopes: Model Bandwidth Sample rate Resolution 1ime bases 2232 100 MHz 100 MS/s 8 bits Dual 2221A 100 MHz 100 MS/s 8 bits Single 2212 60 MHz 20 MS/s 8 bits Single 2201 20 MHz 10 MS/s 8 bits Smgle -:-:-:-:-:-~·:·:~- .· {)Ji~§?- You are looking at the output of a waveform generator on one of these)!jl;~;~{ the))JiiI~ oscilloscopes. The generator is set to give a ±2-V sine wave output. If sine-wave period is set at 1 µ,s, the scope indeed shows a 2-V amplitude/:}l~§?i JI G Exe r c i s e s 505 However, if the period is 20 ns, the amplitude is I V. Assuming the oscilloscope is not broken, which one are you using?

## 10. You want to measure the energies of various photons emitted in a

nuclear decay. The energies vary from 80 keV to 2.5 MeV , but you want to measure two particular lines that are separated by 1 keV . If you do this by digitizing the output of your energy detector, at least how many bits does your ADC need to have?

an

## 11. Pulses emitted randomly by a detector are studied on oscillo

scope: The vertical sensitivity is 100 mV/div and the sweep rate is 20 ns/div.

The bandwidth of the scope is 400 l\.fHz. The start of the sweep precedes n.

the trigger point by 10 ns, and the input impedence is 50 a Estimate the pulse riseti.me. What could you say about the riseti.me if the bandwidth were 40 MHz?

b. Estimate the trigger level.

c. These pulses are fed into a charge-integrating ADC, also with 50 input impedence. The integration gate into the ADC is 100 ns long and precedes the pulses by 10 ns. Sketch the spectrum shape digitized by the ADC. Label the horizontal axis, assuming pC of integrated charge corresponds to one channel.

d. The ADC can digitize, be read out by the computer, and reset in 100 µs. Estimate the number of counts in the spectrum after 100 s if the average pulse rate is 1 kHz. What is the number of counts if the rate is I tvfrlz?

## 12. A detector system measures the photon emission rate of a weak light

source. The photons are emitted randomly. The system measures a rate of 10 kHz, but the associated electronics requires 10 µs to register a photon, and the system will not respond during that time. What is the true rate at which the detector observes photons?

I /!//If G Exercises . . ~ - ://:::~:=:

## 13. You measure the followmg voltages across some resIStor with a

three-digit DMM. As far as you know, nothing is changing so all the \ \:}} measurements are supposed to be of the same quantity VR . .) )}):

## 2.31 235 2.26 2.22 2.30

## 2.27 2.29 2.33 2.25 2.29

a. Determine the best value of VR from the mean of the measurements.

b. What systematic uncertainty would you assign to the measurements?

c. Assuming the fluctuations are random, detemrine the random uncertainty from the standard deviation.

d Somebody comes along and tells you that the true value of V R is 2.23. What can you conclude? · :))}:f -:: ::: ?:*-:=::; 14. (From G L. Squires, Practical Physics, third ed., Cambridge . :/}}~)

( 1985).) In the fallowing examples, q is a given function of the independent . :}J~ti .\)i!f measured quantities x and y. Calculate the value of q and its uncertainty fJq, assuming the uncertainties are all independent and random, from the. . })t} \)if: given values and uncertainties for x and y. .

a. q = x 2 for x = 25 ± 1. ::::::::::::::::: b. q = x ~ 2y for x = 100 ± 3 and y = 45 ± 2. )i}J)

c. q = x Iny for x = 10.00 ± 0.06 and y = 100 ± 2. {{/?

= ¾ = ± }\Jfi d. q 1 - for x 50 2.

./!}JJ/

## 15. Police use radar guns to catch speeders. The guns measure the fre-

quency f of radio waves reflected off of cars moving with speed v. This / //~)

Jo differs from the emitted frequency because of the Doppler effect }}}{ :~d for a e& moving away at :.o tat 2~tionfil unrertruncy m~t ilie 111111 ·.:(//!

radar guns achieve to measure a car's speed to 1 mph?

:\\f{

## 16. The period T of a pendulum is related to its length L by the relation

If.

/II!

T rr }@ff where g is the acceleration due to gravity. Suppose you are measuring g :)\~f: from the period and length of a particular pendulum. You have measured i/1111 G Exercises 507 the length of the pendulum to be I. 1325±0.0014 m. You independently measure the period to within an uncertainty of 0.06%, that is, ST/ T 6 x 10-4. What is the fractional uncertainty (i.e., % uncertainty) in g, asswning that the uncertainties in Land Tare independent and random?

## 17. You have a rod of some metal and you are changing its temperature

T. A sensitive gauge measures the deviation of the rod from its nominal length l 1.500000 m. Assuming the rod expands linearly with tempera ture, you want to detennine the coefficient of linear expansion a, i.e., the change in length per Kelvin, and the actual length lo before any tempera ture change is applied. The measurements of the length deviation Al as a function of the temperature change AT are as follows: .t..T (K) ~l (~Lffi) LiT(K) .ti.I (µm) 6.T(K) t;.t (µm)

## 0.8 70 2.2 llO 3.6

LO 110 2.6 150 3.8 170 l.2 130 2.8 120 4.2 160

## 1.6 100 3.0 130 4.4

## 1.8 130 3.4 160 5.0

Plot the points and draw three straight lines through them: • The line that best seems to go through the points.

• The line with the largest reasonable slope.

• The line with the smallest possible slope.

Use your own estimates by eye to determine these lines. (Do not use a fitting program.) Use the slopes and the intercepts of these lines to determine ± 8a and lo ± Mo.

ct

## 18. For the previous problem, use the method of least squares to fit the

data for l:::..l as a function of /:l. T to a straight line. Use the fitted slope and the uncertainty to detennine the coefficient of linear expansion a. Also calculate the uncertainty Sa. A:Ie band estimates just as good as a fitting program? What are the relative advantages or disadvantages?

## 19. Suppose you wish to measure the gravitational acceleration g by

using something like the "Galileo" experiment That 1s, you drop an object from some height h and you know that the distance it falls in a time t is given by ½gt2 . For a given experimental ru~ the fractional uncertainty in = = his 8h/ h 4% and the fractional uncertainty int is 8t/t 1.5%. Find the fractional uncertainty in g from these data, assuming the uncertainties are random and uncorrelated.

## 20. You want to measure the value of an inductor L. First, you measure

the voltage V across a resistor R when l.21 ±0.04 mA flows through it and 508 G Exercises with this resistor and a capacitor C and get r =RC= 0.463 ± 0.006 ms. \ \))} Finally~ you hook the capacitor up to the inductor and measure the oscillator. {{}if = = ± \i{fjJ~i frequency w l/~ 136 9 kHz. What is the value of L1 nd its \\f}f uncertainty? u

## 21. A simple pendulum is used to measure the gravitational acceleration _:}}}/:}

.}/f}f g. The period T of the pendulum is given by ]Ill T 1nff (1 = + 2 filn ~)

Y\f&fJ for a pendulwn initially released from rest at an angle 0o. (Note that T-.;;.

2:,r,JY:Ti as 0o -+ 0.) The pendulum length is L = 87.2 ± 0.6 cm. The··=\/lJf~ )!}{ff} period is determined by measuring the total time for 100 (round trip) swings.

a. A total time of 192 sis measured, but the clock cannot be read to better than ±100 ms. What is the period and its uncertainty?

b. Neglecting the effect of a finite value of 0o, detennine g and its uncertainty from these data. Assume uncorrelate~ random uncertainties.

c. You are told that the pendulum is released from an angle less than 10°. What is the systematic uncertainty in g from this infonn ation?

d. Which entity (the timing clock, the length measurement, or the unknown release angle) limits the precision of the measurement?

## 22. The ,8-decay asymmetry, A, of the neutron has been measured by / /{{\

Bopp et al. Phys. Rev. Lett. 56, 919 (1986) who found that )}{({ c:~::~:ifu, This vfilue ~tte:tly b::~::e:r::~ :~. =lier results.

is 11111111 .\({ff\ The neutron lifetime~ -r, has also been measured by several groups, and the )}]ff: results are not entirely consistent wi~ each other. The lifetime is given by

## 5163.7 s

r= 1 3)..2 and has been measured to be 918 14 s by Christenson et al., Phys. Rev. D 5, 1628 (1972), G Exercises 509 881 ± 8 s by Bondarenko et al., JETP Lett. 28, 303 ( 1978), 937 18 s by Byrne et al. • Phys. Lett. B 92, 274'(1980), and

## 887.6 ± 3.0 s by Mampe et al.. Phys. Rev. Lett. 63, 593 (1989)

Whlch, if any, of the measurements of r are consistent \ivith the result for A? Which, if any, of the measurements of -,; are inconsistent with the result for A'! Explain your answers. A plot may help.

.,

## 23. The "weighted average'' of a set of numbers is

(7.1)

where the "weights" w1 l/o}.

a. Prove that this definition for the weighted average is the value x2 that minimizes .

b. Use propagation of errors to derive the uncertainty in the weigbted average.

## 24. Let's suppose you have some peculiar dice which each have

faces. The faces are numbered from Oto 9. You throw eight of these dice at a time and record which numbers land face down on the table. You repeat this procedure (i.e., throwing the dice) 50 times.

a. For how many throws do you expect there to be exact!y three dice landing with either face 1 or face 5 landing face down?

b. What is the average number of <lice you expect to land with either face 1 or face 5 down, for any particular throw? What is the standard deviation uncertainty in this number?

c. Use the Poisson approximation to calculate the same number as in (a).

d. Use tbe Gaussian approximation to calculate the same number as in (a).

## 25. A radioactive source emits equa.Uy in all directions, so that the inten

sity falls off like l / r2 where r is the distance to the source. You are equipped with a detector that coW1ts only radioactivity from the source, and nothing else. At r I m, the detector measures 100 counts in 10 s.

a. What is the count rate, and its uncertainty, in counts per second?

b. What do you expect for the fractional uncertainty in the count rate if you count for 100 s instead of 10?

510 G Exercises c. Based on the original 10-s measurement, predict the number of counts you should observe, and its uncertainty, if the detecto~ moved to a distance of 2 m and you count for 1 min.

of a radioactive source. With the source near the detector. you detect 100 )\ { counts in 25 s. To measure the background count rate, you take the source -) \)

very far away and observe 25 counts in 25 s. Random counting uncertainties }(!)

dominate. ~=g: }/)

::;:;> a. ::~;~~::;:: and its uncertainty when the · /~ b. What is the count rate (in counts/s) and its uncertainty when the . ) ){ :: fi :~~1iif.t ii =~~~::::::~~::::::::::.to How long must you run the experiment?

## 27. An experimenter is trying to determine the value of "absolute zero"

in degrees Celsius using a pressure bulb and a Celsius thermometer. She assumes that the pressure in the bulb is proportional to the absolute tem perature. That is, the pressure is zero at absolute zero. She makes five measurements of the temperature at five different pressures: =~;: :i:}~ Usea s trrught ~ruu:~ of ::so;:: zero, and ira ).~_/i_l_l uncertaintyt,h fer ofoml: othweisneg d ;a.ta. v:es

## 28. Fit , y)

5 :a::o~::8 9 132 147 :d ·:d line p!:6~e :·:tt=:;:e. )

to as traight !Ii :\.·i.·f.·,." ' a. Does it look like a straight line describes the data well?

b. Study this further by plotting the deviations of the fit from the </: )!} data points. What does this plot suggest? .

c. Try fitting the points to a quadratic form, i.e., a polynomial of -:-:-:-: {i degree 2. Is this fit significantly better than the straight line?

. ·.· .·r ([If:

## 29. The following results come from a study of the relationship between

high school averages and the students' overall average at the end of the first }} ·.-,.. ...

\/ ::::~ :;:::; -:-:-~ ..! !ii G Exe r c is e s 511 year of college. In each case, the first number of the pair is the high school average, and the second is the college average.

78,65 80,60 85,64 77,59 80,56 82,67 81,66 89,78 87,71 80,66 85,66 87,76 84,73 87,63 74,5& 91,78 81,72 91,74 86,66 90,68 ')

a. Draw a scatterplot of the college average against the high school average.

b. Evaluate the correlation coefficient. Would you conclude there is a strong correlation between the grades students get in high school and the grades they get in their first year of college?

## 30. Using the data in Table 2. 1, draw a scatterplot of electrical

conductivity versus thermal conductivity for various metals. (Electrical conductivity is the inverse of electrical resistivity.) Calculate the linear correlation coefficient.

## 31. Graph the ratio of the Poisson distribution to the Gaussian distribu

tion for mean valuesµ,= 2 and forµ= 20. Use tlris to discuss where the Gaussian approximation to the Poisson distribution is applicable. Repeat the exercise~ but compare the Gaussian approximation directly to the binomial distribution with p ½-

## 32. Consider blackbody radiation

a. Show that the wavelength at which the intensity of a blackbody radiator is the greatest is given by "Wien's displacement law":

## 2.9 10-3

AJIUlX (m) T (K) • Him: You will need to solve an equation like xex /(ex - 1) A >> for some value A. If A 1 then this is trivial to solve, but you can be more exact using MA1LAB. In MA1LAB you would use the Hfunction" fzero to find the place where f(x) A(ex - I) - xex crosses zero.

b. Stars are essentially blackbody radiators. Our sun is a uyellow"

star because its spectrum peaks in the yellow portion of the visible light. Estimate the surface temperature of the sun.

## 33. A particular transition in atomic neon emits a photon with wave

length A 632.8 nm.

512 G Exercises a. Calculate the energy E of this photon.

b. Calculate the frequency v of this photon.

c. An optical physicist tells you the "line width" of this transition is ti v 2 GHz. What is the line width b.. E in terms of energy?

d. Use the Heisenberg uncertainty principle to estimate the lifetime 6.t of the state that emitted the photon.

e. How far would a photon travel during this lifetime?

f. Suppose the neon is contained in a narrow tube 50 cm long, with mirrors at each end to reflect the light back and forth and "trap" it in the· tube. What is the nominal "mode number" for 632.8-nm photons, that is, the nwnber of half-wavelengths that fit in the tube?

g. What is the spacing in frequency between the nominal mode number m, and the wavelength corresponding to the modem I?

h. Compare the mode spacing 8v (part G) with the line width 6.v. )){if i. What is this problem describing?

..· ::::::::;:;;~~;

## 34. Estimate the ''transit time" for a typical photomultjplier tube. That }/}]~

}!)%1 is, how much time elapses between the photon ejecting an electron from ..

the photocathode and the pulse emerging from the anode? Assume the ·}()@] )[!}ff photomultiplier has 10 stages and 2000 V between cathode and anode, :\//?: divided equally among all stages, and that the dynodes are each separated .}{jf} by 1 cm.

## 35. Some high-quality photomultipliers can detect the signal from a . \ }//:

single photoelectro~ and cleanly separate it from the background noise. )}}{t ))j\J} Such a PMT is located some distance away from a pulsed light source, so that on the average, the PMT detects {NpE) photoelectrons. If (NpE) << 1 :))\?!

and No pulses are delivered, show that the number of pulses detected by {((@ })\I the photomultiplier is given by {Npe,}No. ·

## 36. A photomultiplier tube observes a flash of green light from an Ar+ ·)!(}f

laser. (Assume the photons have wavelength)..= 500nm.) The photomul· ·}{/\ tiplier is a 10-stage tube, with a RbCsSb photocathode. The voltages are )()f = \(ff~ set so that the first stage has a secondary emission factor 01 5, while the = :/)1~~ other 9 stages each have 8 2.5. The laser delivers some huge nun1ber of.

·,·.·.·.·,·.~..-,, anq ://it ~ photons to a diffusing system, which isotropically radiates the light, only a small fraction of them randomly reach the photomultiplier. On the )?{§f :}\Ji~~; average, 250 photons impinge on the window for each flash of the laser.

a. What is the average number of electrons delivered at the anode output of the photomultiplier tube, per laser flash?

G Exercises 513 b. Assume these electrons come out in a rectangular pulse 20 ns wide. What is the height of the voltage pulse as measured across a 50-Q resistor?

c. You make a histogram of these pulse heights. What is the standard deviation of the distribution ·displayed in the histogram?

d. Suppose the photomultiplier tube is moved four times farther away from the source. For any given pulse of the laser, what is the probability that no photons are detected? ..

## 37. A Geiger counter is a device that counts radioactive decays, typically

used to find out whether something is radioactive. A particular Geiger counter measures 8.173 background counts per second; i.e., this is the rate when there are no known radioactive sources near it. Your lab partner hands you a piece of material and asks you whether it is radioactive. You place it next to the Geiger counter for 30 sand it registers a total of 253 counts.

a. What do you tell your lab partner?

b. What do you do next?

## 38. The Tortoise and the Hare have a signal-to-noise problem. A very

weak signal sits on top of an enormous background. They are told to deter mine the signal rate with a fractional uncertainty of 25%, and they decide to solve the problem independently. The Tortoise dives into it and rakes data with the setup, and he determines the answer after running the appa ratus for a week. The Hare figures she is not only faster than the Tortoise, but smarter too, so she spends two days reducing the background in the apparatus to zero, without affecting the signal. She then gets the answer after running the improved setup for one hour. (The Hare really is a lot smarter than the Tortoise, at least this time.)

Assuming Poisson statistics, a. What is the signal rate?

b. What is the Tortoise's background rate?

## 39. Consider the passive filters shown in Fig. 3.11

a. Determine the gain as a function of w 2rr v for each filter.

b. Plot the gain as a function of w/wc for the three low-pass filters.

Define the critical frequency we using the simplest combination of the two components in the circuit, that is, we 1/ RC, we = I/ , Jle, or we = R / L. It is probably best to plot all three on the same set of log-log axes: II 514 G Exercises c. Do the same as (b) for the high-pass filters. ·:-:-:-:-:-: :~ J~ R Jii ·-::;:::::;::: :/' 1111 .'./ I!~ . :::::::=:::: ~: :~::: ::: :~:! :~:: Ill :! ~::0? .

~~

## 41. A particle detector gives pulses that are 50 m V high when measured

as a voltage drop across a 50-Q resistor. The pulse rises and falls in a time span of 100 ns or less. Unfortunately, there are lots of noisy motors in the.

laboratory and the ground is not well isolated. The result is that a 10-mV , 60-Hz sine wave is also present across the resistor, and adds linearly with the pulses.

a. D~r!a~w~ a: s:i~m:pule: :c~ir:c:usi4 including the 50-Q resistor and a single -:::-:-:-:- :;::.::~::::·f::~~:::a::~e Iii!j b.

·_::::::::~:

## 42. You are measuring a quantity Q that is proportional to some small ))(

voltage. In order to make the measurem.ent, you amplify the voltage using }/j )(@ a negative feedback amplifier, as discussed in Section 3.5.

. ·:::::::~: -/?f a. Show that the gain g of the full amplifier circuit can be written as 1 ( 1 )] {/} g = go [ 1 - a/3 + 0 a2f32 , ./{[i~fil ·:::::::z: )~~~iii~~ ·:-:-:,: ..: . .: II G Exercises 515 where go = 1/ fJ and a >> 1 is the internal amplifier gain, f3 is the feedback fractio~ and afJ >> l.

b. You measure Q with such an amplifier, with f3 0.01. The temperature in I.he lab fluctuates by 5°F while you make the measurement, and the specification sheet for the opamp tells you 4 4 that its gain varies between 2.2 x 10 and 2.7 x 10 over this temperature range. What is the fractional uncertainty in. . Q due to this temperature fluctuation?

## 43. A 22Na radioactive source emits 0.511- and 1.27-MeV y-rays. You

have a detector placed some distance away. You observe a rate of 0.511- MeV photons to be 2.5 x 103/s, and of 1.27-MeV photons to be 103/s, with just air between the source and the detector. Calculate the rate you expect for each y-ray if a 1/2-in.-thick piece of iron is placed between the source and the detector. Repeat the calculation for a 2-in.-thick lead brick.

## 44. A radioactive source is situated near a particle detector. The detector

counts at a rate of 104/s, completely dominated by the source. A2-cm-thick slab of aluminum (density 2.7 gm/cm ) is then placed between the source and the detector. The radiation from the source must pass through the slab to be detected a. Assuming the source emits only 1-MeV photons, estimate the count rate after the slab is inserted.

b. Assuming the source emits only 1-MeV electrons, estimate the count rate after the slab is inserted.

## 45. Consider a smaJJ rectangular surface far away from a source. The

surfa ce is normal to the direction to the source, and subtends an angle a horizontaJly and f3 vertically. Show that the solid angle subtended is given ~fJ.

by

## 46. A photomultiplier tube with a 2-in. active diameter photocathode is

located 1 m away from a blue light source. The face of the PMT is nonnal to the direction of light. The light source isotropically emits 10 photons/s.

Assuming a quantum efficiency of 20%, what is the count rate observed by the photomultiplier?

## 47. Two scinti1lation detectors separated by 3 m can measure the "time

of-flight,, for a particle crossing both of them to a precision of ±0.20 ns.

Each detector can also measure the differential energy loss d E / dx constant/{ 32 , f3 = vJ c, to ±10%. For a particle with a velocity of 80% the speed of light (i.e., f, 0.8), how IQany individual detectors are needed 516 G Exercises along the particle path to detennine the velocity v using d E / dx to the same precision as is possible with time-of-flight?

## 48. A Cerenkov detector is sensitive to particles that move faster than

the speed of light in some medium, i.e., particles with f3 > 1/ n, where n is the index of refraction of the medium. When a particle crosses such a detector, it produces an average number of detected photons given by (1- } µ K ).

f3 fl 2 The actual number of detected photons for any particular event obeys a Poisson distribution~ so the probability of detecting no photons when the mean isµ., is given bye-µ,. When 1-GeV electrons (/3 = 1) pass through the detector~ no photons are observed for 31 out of 19,761 events. When 523-MeV /c pions (/3 0. 9662) pass through, no photons are observed for 646 out of 4944 events. What is the best value of the index of refraction n as determined from these data? What is peculiar about this value? (You might want to look up the indices of refraction of various solids, liquids, and gases.)

Index Absorption coefficient, 300-301 Barium. 355 AC circuits, 93-96 Barrier-layer detector, 345 ADC. See Analog-to-digital Beams, atomic. See specific types, converter techniques Airy equation, 190 Beams, laser. See Lasers Alpha particles, 306, 324, 325f, Bernoulli distribution, 433-434 351-354 Berry's phase,_21{}-213, 213f Amplifiers, operational, 1I 9--120 Besse] functions, 58, 190 Analog-to-digital converter (ADC), Beta ·decay, 20 113 Bifurcations, 1~3, 137-138 Angular momentum, addition of, Binomial distribution, 433-436, 40, 226f, 228 443 Atomic structure. See specific Birefringent materials, 203 particles, effects Bismuth, 66, 68 Atomic vapors, 1-13 Blackbody radiator, 511 Autocollirnation, 27 Bloch magnetic susceptibility, 267 Avalanche detectors, 347 Bohm-Aharonov effect, 211 Avogadro's number, 300 Bobr magneton, 216 Bohr model, 10, 21, 22 Bohr, N., 20- BabineCs principle, 184 Boltzmann constant, 47, 124, 125, Balmer series, 2, 25, 29-33, 235, 131 235f Boltzmann distribution, 48, 73, 154 Band theory, 49-54, 72 Boltzmann, L .• 45 Bandpass filters, 103, 122, 133 Boron, 101 518 Ind ex Bose-Einstein statistics, 45 Crimping, 107 Bragg curve, 305,353, 354f Crosssection,define~298- 299 Bremsstrahlung, 304, 316-319 Crystal efficiency, 378 Brewster angle, 161, 161f, 162 Crystals. See Semiconductors, Bridge circuit, 276-278, 289 52-56 Brillouin surfaces, 52 Current density, 55 Brownian motion, 5 Current, electric, 90 Cyclotron, 64 Capacitance, 93, 95 Capacitors, 93-98 DAC. See Digital-to-analog Cavity, 151. See Lasers converter Cesium, 360 Darlington pair., 59n7 Chaos, 133-143 Data analysis, 149, 445-453 Charged particles, 10. See specific DC power supplies, 108-109 particles dE/dx curve, 349, 353 Chi-square distribution, 451--454 Dead time, l 15~ 332, 333 Cherenkov detector, 516 Decay rate, 354, 405, 466,468,501 Circuit theory~8 9-104, 116-119 Degrees of freedo~ 452, 453 Circular apertures, 191f, 188-191 Delay curve, 414 Coaxial cables, 104-107 Delta rays, 305 Coincidence experiments, 367--418 Deuterium, 235f Combinatorial analysis, 430--431 Diffraction, 164,179 Compton, A., 370 calculation of, 185 Compton scattering, 313-314, circular aperture and, 188-191 369-385 gratings and, 180, 192- 198, 217 experimental design, 375-378 prism and, 30 K-N formula and, 313 resolving power and, 217 shifts in, 371 specroscopy. See Spectroscopy wavelength and, 371 slit and, 180-184 Computer interfaces, 147 -149 See also specific effects, Conduction bands, 54, 72-74 equipment Confocal resonator, 158 Digital multimeters, 110 Conservation laws, 20 Digital oscilloscope, 116 Constant deviation instruments, 33 Digital-to-analog converter (DAC), Cosmic rays, 399-409 114 Coulomb-barrier effects, 298 Digitizers, 113-115 Coulomb force, 20, 21 Diodes, 99-102 Coulomb potential, 34n15, 218 bifurcations and, 142 ln·dex 519 chaos and, 143 current and, 90 circuits with, 13 9-144 drift velocity, 55 current through, 80 energies of. See Energy levels, I -V characteristic of, 139 atorruc oscilloscope traces, 130 excited states, 20 p-njunctions, 78,100,345 fractional charge, 10 properties of, 78 ground state, 20 recombination regime, 79 holes, 54, 76, 347-348 reverse bias on, 101 ions and, 319, 320f semiconductors and, 78, 100 magnetic moment of, 224-228 symbol for, 100 matterand,298-319 Dirac theory, 39, 224n mean free path, 63 Direction cosines, 186 one-dimensional problem, 50 Dop an ts, IO 1 orbits of, 218, 367 Doppler effects, 16 l, 245n, 387 positrons and, 319. 320f radiation length. 319 reduced mass, 233 Eddy currents, 57 scattering angle of, 316 Einstein, A .• 153 semiconductors and, 72 Electric current, 90 solids and, 45-88 Electric-dipole transition, 221, thermal motion. 123 222n9 wells and, 50 Electric field, 2 Energy levels, atomic, 20, 49, Electric potential, 90 152-154,203,227,254,337, Electrical conductivity, 511 353. See also specific particles Electrical resistance, 55 Error analysis, 454--464 eddy current technique, 57 ESR. See Electron spin resonance metals and, 54 Estimation of parameters, 445-453 physics of, 56 Exponential growth, 134 temperature and, 63 Extrinsic carriers, 72 Electromagnetic cascade, 320 Electromagnetic radiation, 312 Electron spin resonance (ESR) f -number, 190 spectrometry, 254, 283-290 Fabry-Perot apparatus, 172-177, Electrons, 40-43, 254-292~ 322f 217,239,239L241 angular momentum of, 220 Far-field amplitude, 188 bremsstrahlung, 316-320 Farad, unit, 93 charge on, 1, 4, 10 Faraday effec~ 201, 203, 205f, coupling of, 40-43 207f, 210 520 Index Faraday's law, 57 Gage number, 105n Feather's rule, 378 Gain curve, 157 Feedback,negative, 119 Gain function, 125 Feigenbaum, M., 137 Gamma function, 452 Feigenbaum number, 138, 143, Gamma rays, 328f, 336, 337, 339, 144 409-421 Fermi constant, 406 angular correlation of, 411--413, Fermi-Dirac statistics, 45-49 417f, 419-421 Fenni distribution, 73 anisotropy,412,418 Fermi energy, 47, 53f, 73- 75 attenuation of beam. 487 Fenni particles, 4 7 coincidence rate, 412 Femri weak interactio~ 406 coincidence circuit, 416 Fermi's golden rule, 258 decay scheme, 338, 339 Filter circuit, I 04 electron-positron pairs, 298 Fine structure, 36-39 gamma-gamma correlation, Floating tenninals, 108 409-411, 415-4 I 9 Fluorescence,247,248f low-energy, 371 Foucault pendulum, 211 pulse-height spectrum of, 375 Fourier analysis, 133, 316 recoil effects, 387 Fourier optics, 180, 198 spectra, 378 Fourier transform, 95, 188, 198 Gaseous ionization detectors, Frank-Hertz experiment, 1, 10--19 320-333 apparatus for, 2, 12, 14, 15 Gaussian approximation, 509 beam current, l 7f Gaussian distribution, 132,436, excitation potential, 16 439 ion current, 19 as linliting case, 439-442 oscilloscope display of, 17 binomial frequency function, preferred elements for, 13 433 wiring diagram for, 15 moments of, 434-438 Fraunhofer diffraction, 180 normal distribution and, 455 Free-electron gas, 72 properties of, 443 Free induction decay, 271 Gauss's law, 302 Free radicals, 284 Geiger counter, 320-333, 510 Free spectral range, 157 cylindrical, 321f Frequency bifurcations, 133- 138 dead time of, 332, 333 Frequency filters, 102-104 plateau region, 329, 331 Frequency functions, 431-445 Germanium, 54, 74 Fresnel diffraction, 180 Goodness of fit, 451-454 -·-: Gratings, 25, 180. See also Impurities, 72. 74. 101 Diffraction Indium, 356-359 Ground, electric, 90 Inductance,defined,99 Ground state, 11 Inductors, 98-100, 141 Gyromagnetic ratio, 255 Input registers, 115 Insulators, 53 Interferometry, 167, 172. See Hadronic particles, 10 specific types Half-life, 354 Intrinsic carriers, 72, 7 4 Hall coefficient, 65, 66, 70 Inverse matrix, 450 Hall effect, 63-70 Ion current.. 16 Hamiltonian operator, 51 Ionization chamber, 321, 323-326, Heliurn,20, 160, 160f Helmoltz coils, 275, 286 Ionization potential, 13, 14. 18 Hennite polynomials, 158 Isotope shift, 215n, 228, 232, 234f hfs . See Hyperfine structure High-field magnets, 85 High-pass filter, 122 Jarrell-Ash spectrometer, 235f High-resolution filters, 177 Johnson noise, 122, 125, 126£, 129 Holes, electron, 54, 72, 75 Junctions, 75- 78. See Huygens-Fresnel principle, 185 Semiconductors Hydrogen, 20,235f Balmer series of, 29 Kimball-Slater spacing, 52 hydrogen-deuterium shift, 234 Klein-Nishina formula, 313, 374, orbits in, 22 384,385 spectra of, 20 Klystron, 286 Hyperfine structure (hfs), 215-216, Knock-on electrons, 305 228- 238 Doppler effect, 238 Lande g factor, 225 isotope shift, 228, 232 Larmor precession, 260 of mercury, 238 Lasers1 151-177 of rubidium, 246-247 beam profile, 165-167 cavity, 155 Image-fonning detectors, 296 collimation of beam, 164 Image plane, 199 defined, 170 Impedance, 95 Fabry-Perot interferometer, characteristic, 106 172-177 coax.i al cable, 104 HeNe laser, 159-162 522 Index Lasers (continued) magneticresonance,251-293 interferometers and, 172 optics and, 200 lasing medium, 154 refractive indices, 203 Michelson interferometer, 168 spectral lines and, 221 f principle of operation, 152-156 spin and, 256f properties of beams, 156 Malthus theory, 134 safety, 483-484 Marginal oscillator circuit, 276, spatial filtering, 201 281-282 telescope, 164 MATLAB programs, 132, 149, See also specific parameters. 342,358,451,477,482,511 effects Maximum likelihood methods, Latches, 115 445--447 Lattices, 52, 389. See also Crystals Maxwell-Boltzmann distribution, LCR circuit, 99 237 Least-squares method, 29, Maxwell's equations, 58 447-451,480 Mean,defined,432 Lifetime, of nuclei, 467 Mean free path, 7, 70 Light, 201-210. See also specific Meissner effect, 83 effects, instruments Mercury, 42f, 33-43, 43f, 232f, Linear devices, 99 238 Linear functional dependence, Metals, resistivity, 54, 56, 72 449-451 Meters, types of, 109 Load buffering, 122 Michelson interferometer, 167, Lock-in amplifier, 144-146, 208 168f, 171 Logistic map, 133-138 Microscope, parallax errors, 5 Longitudinal modes, 156 Microwave cavity, 289 Lorentz transfonnation, 374, 390 Millikan oil drop experiment, Low temperature approximation, 2-10 74 Minority carriers, 7 6 Lyman series, 24 Monte Carlo method, 464 Mossbauer effect, 385-399 Multiple-beam interferometer, 217 Magic tee circuit, 286, 289f Multiple scattering, 310-311 Magnetic-dipole transitions, 252, Muons, 404-409 255-261 Magnetic fields anomalous effects, 229n Negative feedback, 119, 120f light, 201 Neon, 160, 160f magnetic moment, 219f, 261 f Neutrinos,404,405 . .

,' .·~. ,• ,: :-· ,·· ; .• : . ,; \)

. ,.}~~~:-:/~ :_.

• •• 4 • • • Neutrons, 296, 355, 508 spin and 229-Jl'lt:J .,.,s:.:·f·: i/{::./::::: ·.

, ~~',&cy.4 _ J~.-.,:-~-·-:-:-·-·.·.·.·.·. ·•· n-p junctions, 76, 345, 346f statistics for, 465-473'-:: //\ .·.

'tmicki{ :::: ;:: Noise, I 02, 119, 146 See also specific p . .

Y. •••••••• '.>• (>:::: :· Johnson noise, 1.22 effects ... , .::.: Nyquist noise, 122 Null methods, 264 ..· . :-::::::: :::: r~jection, 146 Nyquist noise, 122 ::-::·:-::::::<:::::::: .

spatiaJ filtering, 201 temperature and, 124 Nonlinear components, 133 Occupied states, 73 ....: : Nonlinear methods, 480 Ohm's law 54 55 64 l 04 . ·.;:-:: ,. • t ' '"

Nonna! distribution. See Gaussian Oil drop method. See Millikan oil distribution drop experiment Nuclear magnetic resonance Operational amplifiers. 121 f.

(NMR). 146,267,283 119-121 bridge circujt, 277-279 Optical detection .techniques, detection of, 277-279 489-498 : .· · · . · ESR. See Electron spin Optical experiments--;179~213 resonance Optical fiber, 21 lf ..

free induction decay, 270-273 Optical spectroscQpy; 20 .

line width, 266-267 Organic free radicals, 284 marginal oscillator circuit, Organic scintillators, 334 281-282 OrthogonaJ triads, 211 protons and, 278f, 280f, 273-282 Oscilloscopes, 110-113, 117 pulsed, 270-273, 279-281 bandwidth, 113 Rabi experiments, 254 digital, 116 spin and. See ESR; Spin Fourier analysis, 133 transverse relaxation ti.me, 267 ion current, 16 Nuclear magneton, 229 tock·in amplifier, 208 Nuclear resonance radiation, 389, Output coupler, 159 Nucleus, atomic decay of, 409, 410f, 465-467 p-ojuoction, 75, 79, 100-101,345 electron-positron pairs, 298 _p-n-pjunction, 77 half-life, 354-363 p-n-p transistor, 77, 102 mean free path, 298 Pair production, 312, 3l4 moments, 230, 230f, 262-273 Paraelectric materials, 268 NMR. See Nuclear magnetic Parallel circuitry, 91 resonance Paramagnetism, 268, 284 nucleons, 229n Parameter estimation, 445-453 524 Index Particles, 50, 295-365. See specific Prism spectrometers, 25 types Probability theory, 423-427 Paschen series, 24 Proportional counter, 327 Pashen-Back effect, 228 Protons, 273-283, 278t 280f, 283f Pauli principle, 41 Pulse-height spectrum, 337 peak-to-total ratio, 378 Pulse transmission, I 05 Period doubling, 137, 142n Pennutations, 430 Phase space, 46n Quadrupole transitions, 36 Phase transitions, 98, 144-146, Quality factor, defined, 277 210-213 Quantization, defined, 1 Phonons, emission of, 389 Quantum efficiency, 492 Photodiodes, I 66f, 165-167, Quantum electrodynamics, 21 496-498 Quantum number, 22, 203 Photoelectric effect, 312 Quarks, charge on, 10 Photofraction, 378 Photographic film, 489 Photomultiplier tube, 490-497 Rabi frequency, 273 quantum efficiency, 492 Radiation, 36 spectral sensitivity, 492 absorption of, 10, 153 transit time for, 512 blackbody, 511 Photons, 152,245,295,312,343 diffraction of. See Diffraction Pinhole, 190, 191 discrete, I 0 Planck's constant, 21, 152 electromagnetic, 312 Plastic scintillators, 334 electrons and, 318 Pockels effect, 203 energy of. See Energy levels, Poincare, H., 135 atomic Poisson approximation, 509 photons and, 312 Poisson distribution, 357,436 quanta of, 20 Poisson statistics, 493 radioactivity and, 323-363, Polarization, 153, 179,180,201, 485-488 202,205,210 safety, 485-488 Polonium, 298 spectral analysis. See Population growth, 134 Spectroscopy Population inversion, 154, 160 standing waves, 156 Positronium, 419 use of, 296 Positrons, 312 waves. See Waves Power supplies, 108-109 See also specific effects, types.

Poynting vector, 373 equipment Radiofrequency field, 260-262 Selection rules, 35-36, 222, 226, Random events, 401-409 252 Random variables, 428 Self-absorption,237 Random walks, 123 Semiconductors, 71-81 Range, of particle, 308 bulk detectors, 345 Rayleigh range1 158 diodes. See Diodes Recombination regime, 79 dopants, 72, 74, 101 Recursion methods, 438 electrons and, 72 Reflection coefficient, I 06 energy bands and, 72 Reflection grating spectrometer, extrinsic carriers, 72 25, 26 Fermi level, 7 5 Refractive indices, 25, 203 Hall effect, 63-70 Relative phase, 97 holes, 54, 72, 76 Relativistic particles, 304 impurities, 72, 74,101 Relaxation, of moments, 262-267 junctions, 75-78 Resistivity. See Electrical properties of, 71-78 resistance valence band, 53, 72 Resonance,99, 141,264, See also specific types 284,390 Sensitive volume, 349 Resonant frequency, 141 Series circuits, 91 Rotation, of fields, 259-262 Shockley array, 52 Rubidium, 218, 243-246 Signal analyzer. 142 Russell-Saunders coupling, 40 Signal-to-noise ratio, 419 Rutherford cross-section, 310 Silver, 363-364 Rutherford experiments, 367 Single-mode fiber, 212 Rydberg constant, 22, 29 Slater-Kimball spacing, 52 Slits, diffraction in, 180-184 Snelrs law, 162 Sample space, 424-426 Sodium, 33-43, 53, 54 Saturation spectroscopy, 243, 245, Solder, use of, 1I TT 262-265 Solenoid, 59 Scanning spectrometers, 177 Solid angle, defined, 368 Scattering experiments, 367-421, Solid-state detectors, 344-353 See specific types, effects Solid-state materials, 46 Schrodinger equation, 20, 34, 233 Spatial filtering, 201 energy eigenvalues, 50-51 Spectroscopy, 2, 146, 147f, 177 hydrogen-like atom, 34 crossover lines, 245 stationary states, 218 diffraction. See Diffraction Scintillation counter, 333-344 gratiags,25-28, 198 526 Index Spectroscopy (continued) Temperature hfs. See Hyperfine structure conductivity and, 511 high-resolution, 215-250 intrinsic carriers,. 74 line width, 237f, 236-238 low temperature approximation, magnetic fields, 221 f 74 photomultiplier tube, 493f noise and, 125,512 rubidium, 243-250 resistivity and, 63, 105 selection rules, 35-36 viscosity and, 7 self-absorption in, 237f Thermocouples, 16 sensitivity, 493 Thermodynamic properties, 45 spectral lines, 215, 22lf, 228, Thomas precession, 224n 236,237f Thomson cross-section, 313, 314f, See also specific types. 372 elements Time-dependentperturbation,257 Spherical wavelets, 185 Time-to-amplitude converter, 406 Spin, 39 Time-to-analog converter, 114 ESR. See Electron spin Transfonn plane, 199 resonance Transistors, 99-102 magnetic field and~ 256f Transmission grating, 199 NMR. See Nuclear magnetic Transverse modes, 158 resonance Turbulence, 133 nucleus, 256f spin-lattice effects, 265 spinning sample technique, Uncertainty principle, 267, 387nll statistics and, 45 Valence band, 72 Stability analysis, 135n Vapors, atomic, I Standing waves, 156,289,432 Variance,defined,432 Stationary states, 218 Verdet constant, 204, 204f, 207, Statistical mechanics, 45 Statistics, theory of, 423-473 Viscosity, 7 Stefan constant, 459 Stellar spectra, 36 Voltage divider, 92, 94f, 96f Stem-Gerlach experiment, 220n Stirling's formula, 443 Waves, 22 Stokes equation, 3, 7, 10n8 antisymmetric, 45 Superconductors, 81-88 diffraction of. See Diffraction Sweep generator, 111 generation of, l 09-111, 116, 128 . . . .... . . .. . .

. .::. · .· .· :-. .

i::{::: . = .- . . . . . .. . ... Index ~ . , phase, 187 YBCO. superc<tQd'i~cw.r ia, 85-88 . . .

radiation and. See Radiation recording of, 114 Young LWb•slit expep.ment, .

: - wave function, 211 193f See also specific parameters, types 2.ecman effect. 203, Wien displacement law, 511 215-228 •.

Work function, 13,492 magneticresonance,254 mercury and, 238-242( X-rays, 372 Mossbauer effect, 396 Xenon-methane counter, 392 normal,223
