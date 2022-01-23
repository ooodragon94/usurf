img1 = im2double(imread('img (1).jpg'));
img2 = im2double(imread('img (2).jpg'));
img3 = im2double(imread('img (3).jpg'));
img4 = im2double(imread('img (4).jpg'));
img5 = im2double(imread('img (5).jpg'));

[rGx1, rGy1] = gradient(img1(:,:,1));
[gGx1, gGy1] = gradient(img1(:,:,2));
[bGx1, bGy1] = gradient(img1(:,:,3));

grad_img1x = cat(3,rGx1,gGx1,bGx1);
grad_img1y = cat(3,rGy1,gGy1,bGy1);

[rGx2, rGy2] = gradient(img2(:,:,1));
[gGx2, gGy2] = gradient(img2(:,:,2));
[bGx2, bGy2] = gradient(img2(:,:,3));

grad_img2x = cat(3,rGx2,gGx2,bGx2);
grad_img2y = cat(3,rGy2,gGy2,bGy2);

[rGx3, rGy3] = gradient(img3(:,:,1));
[gGx3, gGy3] = gradient(img3(:,:,2));
[bGx3, bGy3] = gradient(img3(:,:,3));

grad_img3x = cat(3,rGx3,gGx3,bGx3);
grad_img3y = cat(3,rGy3,gGy3,bGy3);

[rGx4, rGy4] = gradient(img4(:,:,1));
[gGx4, gGy4] = gradient(img4(:,:,2));
[bGx4, bGy4] = gradient(img4(:,:,3));

grad_img4x = cat(3,rGx4,gGx4,bGx4);
grad_img4y = cat(3,rGy4,gGy4,bGy4);

[rGx5, rGy5] = gradient(img5(:,:,1));
[gGx5, gGy5] = gradient(img5(:,:,2));
[bGx5, bGy5] = gradient(img5(:,:,3));

grad_img5x = cat(3,rGx5,gGx5,bGx5);
grad_img5y = cat(3,rGy5,gGy5,bGy5);

m_imgx = median(cat(4, grad_img1x, grad_img2x, grad_img3x, grad_img4x),4);
m_imgy = median(cat(4, grad_img1y, grad_img2y, grad_img3y, grad_img4y),4);

Rout = poisson_solver_function_dirichlet(m_imgx,m_imgy,img1(:,:,:)); % nabla^2 Rout = div ([rGx, rGy]), boundary condition : img(:,:,1)
imwrite(Rout,'Rout.png');