# Brdf
The scripts of fitting leaf-level BRDF.
# Roughness Calculator
## download exe
[Roughness Calculator.exe](https://mdeve5-my.sharepoint.com/:f:/g/personal/smiler488_mdeve5_onmicrosoft_com/EinlQE3gEbJDkKV9QG6coBwBISQqmcEKQ1_H-DMzzM58Yw?e=ps2qZT)
## Introduction
![image](https://user-images.githubusercontent.com/76147378/233330409-13dd52e5-1afb-45a4-a0bc-552e8764b721.png)
<p>RC (*roughness calculator*) is an open-source blade surface roughness calculation software based on python. RC aims to provide a way to quantify surface roughness parameters and accelerate the use of BRDF models in simulating leaf light distribution. As an open-source software, RC allows other users to modify code based on the original code.</p>
#principle
<p>Here, we will briefly introduce the principle of RC. The first step is to create an x-y coordinate system and import the section image. In the second step, the image is denoised using the binarization method to obtain a clean image. The third step involves converting the image into a grayscale format to obtain the edge of the leaf section and the edge after Gaussian filtering. In the fourth step, the area and perimeter are calculated based on the edge of the leaf section. The fifth step involves using the lasso tool to obtain the intersection of the drawing area and the edge of section, enabling the determination of the length of the region of interest. Then the roughness is calculated in the sixth step using a formula.</p>
## Interface
<p>In order to facilitate the use, we designed a visual interface and compiled python code into RC. The interface of RC is shown in Figure 1. The interface of RC consists of the following components:</p>
·The software logo and name are located in the upper left-hand corner of the interface.
·The center of the left side of the interface displays the image processing area.
·The three buttons located in a row beneath the left side of the interface provide access to the functional areas, which include "upload," "calculate," and "lasso select."
·The right side of the interface displays the results of the image calculations.

![image](https://user-images.githubusercontent.com/76147378/233330445-9560ce49-d866-4fe3-abb5-f2e52a2b6b26.png)
<p>Figure 1. The interface of the RC.</p>
## Operate
<p>We introduce how to use RC based images of leaf sections to calculate the roughness of the leaf surface. The operates as follows:</p>
<p>1.Click "upload", we can select the image from folder in the pop-up window;</p>

![image](https://user-images.githubusercontent.com/76147378/233330484-30bdd531-8c5f-4480-8f9f-28adc647d685.png)
<p>Figure 2. The pop-up interface of upload window.</p>
<p>2.Click "calculate", we can obtain the raw area, processed area, inner length, outer length, and roughness of the whole section;</p>

![image](https://user-images.githubusercontent.com/76147378/233330514-0143823e-f20b-440f-aea3-3f325f61ac23.png)
<p>Figure 3. The interface after calculated parameters of the whole region.</p>
<p>3.Click "lasso select", we can lasso the region of interest, and the RC will automatically calculate the inner length, outer length, and roughness of the lassoed region.</p>

![image](https://user-images.githubusercontent.com/76147378/233330545-5d167fbd-14ce-4d95-9314-7abfda3d92a9.png)
<p>Figure 4. The interface after calculated parameters of the lassoed region.</p>
<p>(**Notes**: A row of buttons above the interface of lasso are reset original view, back to previous view, forward to next view, move view, zoom, configure subplots, edit parameter and save figure.)</p>
<p>The leaf surface of monocots and dicots is quite different; therefore, it was important to evaluate the performance of the software for both types of plants. We analyzed the roughness of monocots (maize and rice) and dicots (populus and cotton) to evaluate the applicability of the RC. We established a linear regression between the roughness obtained by RC and the leaf roughness parameters fitted by the BRDF model. As shown in figure 5, the results showed that RC provided a reliable method to quantify the roughness of the leaf surface ($R^2 >0.82$).</p>   

![image](https://user-images.githubusercontent.com/76147378/233330570-ade102bb-dbf6-4e97-b6e9-280a369689a7.png)
<p>Figure 5. The relationship between the ρ and σ of maize, populus, cotton and rice. ρ is obtained by RC based on the image of leaf section. σ is fitted by the BRDF model based on leaf. </p>

---
<p>The primary objective of this software design was to enable the quantification of roughness parameters in the BRDF model of the leaf. In addition to determining the roughness of the leaf surface, the software can also extract other parameters, such as area, length, and circumference, for various objects. </p>

