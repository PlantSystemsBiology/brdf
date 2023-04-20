# brdf
The scripts of fitting leaf-level BRDF.
# roughness calculator
## introduction
![image0](https://user-images.githubusercontent.com/76147378/233319230-95a2c578-a422-4516-908d-fc7b21dbc5e6.png)
<p>RC (*roughness calculator*) is an open-source blade surface roughness calculation software based on python. RC aims to provide a way to quantify surface roughness parameters and accelerate the use of BRDF models in simulating leaf light distribution. As an open-source software, RC allows other users to modify code based on the original code.</p>
#principle
<p>Here, we will briefly introduce the principle of RC. The first step is to create an x-y coordinate system and import the section image. In the second step, the image is denoised using the binarization method to obtain a clean image. The third step involves converting the image into a grayscale format to obtain the edge of the leaf section and the edge after Gaussian filtering. In the fourth step, the area and perimeter are calculated based on the edge of the leaf section. The fifth step involves using the lasso tool to obtain the intersection of the drawing area and the edge of section, enabling the determination of the length of the region of interest. Then the roughness is calculated in the sixth step using a formula.</p>
## interface
<p>In order to facilitate the use, we designed a visual interface and compiled python code into RC. The interface of RC is shown in Figure 1. The interface of RC consists of the following components:</p>
·The software logo and name are located in the upper left-hand corner of the interface.
·The center of the left side of the interface displays the image processing area.
·The three buttons located in a row beneath the left side of the interface provide access to the functional areas, which include "upload," "calculate," and "lasso select."
·The right side of the interface displays the results of the image calculations.
![image1](https://user-images.githubusercontent.com/76147378/233319206-43fa5334-1114-4048-8248-29c19c1d48a7.png)
<p>Figure 1. The interface of the RC.</p>
## operate
<p>We introduce how to use RC based images of leaf sections to calculate the roughness of the leaf surface. The operates as follows:</p>
<p>1.Click "upload", we can select the image from folder in the pop-up window;</p>
![image2](https://user-images.githubusercontent.com/76147378/233319171-8fa5a2d6-9cc4-4003-967d-eca9a43b6a63.png)
<p>Figure 2. The pop-up interface of upload window.</p>
<p>2.Click "calculate", we can obtain the raw area, processed area, inner length, outer length, and roughness of the whole section;</p>
![image3](https://user-images.githubusercontent.com/76147378/233319146-1271baf5-dd0c-4edb-b4c2-c526c16ba589.png)
<p>Figure 3. The interface after calculated parameters of the whole region.</p>
<p>3.Click "lasso select", we can lasso the region of interest, and the RC will automatically calculate the inner length, outer length, and roughness of the lassoed region.</p>
![image4](https://user-images.githubusercontent.com/76147378/233319119-c67c3098-aa2e-4d65-a00d-5c4bf3700caf.png)
<p>Figure 4. The interface after calculated parameters of the lassoed region.</p>
<p>(**Notes**: A row of buttons above the interface of lasso are reset original view, back to previous view, forward to next view, move view, zoom, configure subplots, edit parameter and save figure.)</p>
<p>The leaf surface of monocots and dicots is quite different; therefore, it was important to evaluate the performance of the software for both types of plants. We analyzed the roughness of monocots (maize and rice) and dicots (populus and cotton) to evaluate the applicability of the RC. We established a linear regression between the roughness obtained by RC and the leaf roughness parameters fitted by the BRDF model. As shown in figure 5, the results showed that RC provided a reliable method to quantify the roughness of the leaf surface ($R^2 >0.82$).</p>   
![image5](https://user-images.githubusercontent.com/76147378/233319087-746e7920-1856-4299-bc83-aeee6aaa549a.png)
<p>Figure 5. The relationship between the ρ and σ of maize, populus, cotton and rice. ρ is obtained by RC based on the image of leaf section. σ is fitted by the BRDF model based on leaf. </p>
---
<p>The primary objective of this software design was to enable the quantification of roughness parameters in the BRDF model of the leaf. In addition to determining the roughness of the leaf surface, the software can also extract other parameters, such as area, length, and circumference, for various objects. </p>

