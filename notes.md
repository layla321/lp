# ICCV 2023 (Virtual)
Notes and work related to the [2023 International Conference on Computer Vision](https://iccv2023.thecvf.com/)

Trends:
- Moving beyond images:
  - To 3d, video, animation
- Incorporating other modes
  - Language
  - Audio
  - Robotics
- Common tasks:
  - Generate an image from a text input
  - Generate a video from a text input
  - Generate a video from an image
  - Segment an image
  - Classify an image
  - Detect in an image
  - Search and trim a video from a text input
  - Construct a 3d scene from 2d image or video

Reflections:
- What's the point? Why its great here. (exceptions like DeepMind of course). Entertainment, metaverse, kid's videos
- Data quantity over all else, including adding new mediums
- Trying to slightly improve a metric on a reference dataset (few of them)
- Deep learning is the only option - Traditional methods question
- [Red circle paper](https://openaccess.thecvf.com/content/ICCV2023/html/Shtedritski_What_does_CLIP_know_about_a_red_circle_Visual_prompt_ICCV_2023_paper.html)

## Highlight Presentations
- [Segment Anything](https://openaccess.thecvf.com/content/ICCV2023/html/Kirillov_Segment_Anything_ICCV_2023_paper.html)
  - Amazing capability to segment via input text, point(s) on the image, or automatically without input
  - Required determining the task, creating the training dataset, and building the model
  - [Repo](https://github.com/facebookresearch/segment-anything/tree/main)
- [Sigmoid Loss for Language Image Pre-Training (SigLIP)](https://openaccess.thecvf.com/content/ICCV2023/html/Zhai_Sigmoid_Loss_for_Language_Image_Pre-Training_ICCV_2023_paper.html)
  - "Basically an improvement over CLIP" 
- [Adaptive Testing of Computer Vision Models](https://openaccess.thecvf.com/content/ICCV2023/html/Gao_Adaptive_Testing_of_Computer_Vision_Models_ICCV_2023_paper.html)
- [VQ3D: Learning a 3D-Aware Generative Model on ImageNet](https://openaccess.thecvf.com/content/ICCV2023/html/Sargent_VQ3D_Learning_a_3D-Aware_Generative_Model_on_ImageNet_ICCV_2023_paper.html)
- [Scale-MAE: A Scale-Aware Masked Autoencoder for Multiscale Geospatial Representation Learning](https://openaccess.thecvf.com/content/ICCV2023/papers/Reed_Scale-MAE_A_Scale-Aware_Masked_Autoencoder_for_Multiscale_Geospatial_Representation_Learning_ICCV_2023_paper.pdf)
  - Method for building segmentation models that can succcessfully infer on a variety of ground sample distances
- [CDUL: CLIP-Driven Unsupervised Learning for Multi-Label Image Classification]([https://app.imagina.com/iccv-2023/363127](https://openaccess.thecvf.com/content/ICCV2023/html/Abdelfattah_CDUL_CLIP-Driven_Unsupervised_Learning_for_Multi-Label_Image_Classification_ICCV_2023_paper.html))
- [V3Det: Vast Vocabulary Visual Detection Dataset](https://openaccess.thecvf.com/content/ICCV2023/html/Wang_V3Det_Vast_Vocabulary_Visual_Detection_Dataset_ICCV_2023_paper.html)
- [OmniLabel: A Challenging Benchmark for Language-Based Object Detection](https://openaccess.thecvf.com/content/ICCV2023/html/Schulter_OmniLabel_A_Challenging_Benchmark_for_Language-Based_Object_Detection_ICCV_2023_paper.html)
- [Chinese Text Recognition with A Pre-Trained CLIP-Like Model Through Image-IDS Aligning](https://openaccess.thecvf.com/content/ICCV2023/html/Yu_Chinese_Text_Recognition_with_A_Pre-Trained_CLIP-Like_Model_Through_Image-IDS_ICCV_2023_paper.html)
- [Red circle paper](https://openaccess.thecvf.com/content/ICCV2023/html/Shtedritski_What_does_CLIP_know_about_a_red_circle_Visual_prompt_ICCV_2023_paper.html)
- Washington Post article on Tesla crashes

## Presentations Attended

### Keynotes
- Dorsa Sadigh - Interactive Learning in the Era of Large Models
- Pushmeet Kohli - The potential of AI in advancing science and the importance of ensuring AI's responsible use

### Adversarial Attacks
- [Robust Mixture-of-Expert Training for Convolutional Neural Networks](https://openaccess.thecvf.com/content/ICCV2023/html/Zhang_Robust_Mixture-of-Expert_Training_for_Convolutional_Neural_Networks_ICCV_2023_paper.html)
  - Analysis of attacks on the router in a mixture of experts model and how to make the routing more robust
- [Set-level Guidance Attack: Boosting Adversarial Transferability of Vision-Language Pre-training Models](https://openaccess.thecvf.com/content/ICCV2023/html/Lu_Set-level_Guidance_Attack_Boosting_Adversarial_Transferability_of_Vision-Language_Pre-training_Models_ICCV_2023_paper.html)
- [CleanCLIP: Mitigating Data Poisoning Attacks in Multimodal Contrastive Learning](https://openaccess.thecvf.com/content/ICCV2023/html/Bansal_CleanCLIP_Mitigating_Data_Poisoning_Attacks_in_Multimodal_Contrastive_Learning_ICCV_2023_paper.html)
- [Robust Evaluation of Diffusion-Based Adversarial Purification](https://openaccess.thecvf.com/content/ICCV2023/html/Lee_Robust_Evaluation_of_Diffusion-Based_Adversarial_Purification_ICCV_2023_paper.html)
- [The Victim and The Beneficiary: Exploiting a Poisoned Model to Train a Clean Model on Poisoned Data](https://openaccess.thecvf.com/content/ICCV2023/html/Zhu_The_Victim_and_The_Beneficiary_Exploiting_a_Poisoned_Model_to_ICCV_2023_paper.html)
- [TIJO: Trigger Inversion with Joint Optimization for Defending Multimodal Backdoored Models](https://openaccess.thecvf.com/content/ICCV2023/html/Sur_TIJO_Trigger_Inversion_with_Joint_Optimization_for_Defending_Multimodal_Backdoored_ICCV_2023_paper.html)

## 3D from Multi-View and Sensors 1
- [Multi-Modal Neural Radiance Field for Monocular Dense SLAM with a Light-Weight ToF Sensor](https://openaccess.thecvf.com/content/ICCV2023/html/Liu_Multi-Modal_Neural_Radiance_Field_for_Monocular_Dense_SLAM_with_a_ICCV_2023_paper.html)
  - Interesting approach to scene reconstruction with light-weight equipment 
- [ScanNet++: A High-Fidelity Dataset of 3D Indoor Scenes](https://openaccess.thecvf.com/content/ICCV2023/html/Yeshwanth_ScanNet_A_High-Fidelity_Dataset_of_3D_Indoor_Scenes_ICCV_2023_paper.html)
  - Seems like a small improvement. Not a method I'm familiar with. 

### Generative AI
- [CLIPascene: Scene Sketching with Different Types and Levels of Abstraction](https://openaccess.thecvf.com/content/ICCV2023/html/Vinker_CLIPascene_Scene_Sketching_with_Different_Types_and_Levels_of_Abstraction_ICCV_2023_paper.html)
  - Interesting way to make sketches with varying specifications
- [LD-ZNet: A Latent Diffusion Approach for Text-Based Image Segmentation](https://openaccess.thecvf.com/content/ICCV2023/html/PNVR_LD-ZNet_A_Latent_Diffusion_Approach_for_Text-Based_Image_Segmentation_ICCV_2023_paper.html)
  - Segmentation approach with the help of generated images
- [TexFusion: Synthesizing 3D Textures with Text-Guided Image Diffusion Models](https://openaccess.thecvf.com/content/ICCV2023/html/Cao_TexFusion_Synthesizing_3D_Textures_with_Text-Guided_Image_Diffusion_Models_ICCV_2023_paper.html)
- [Scalable Diffusion Models with Transformers](https://openaccess.thecvf.com/content/ICCV2023/html/Peebles_Scalable_Diffusion_Models_with_Transformers_ICCV_2023_paper.html)
- [VQ3D: Learning a 3D-Aware Generative Model on ImageNet](https://openaccess.thecvf.com/content/ICCV2023/html/Sargent_VQ3D_Learning_a_3D-Aware_Generative_Model_on_ImageNet_ICCV_2023_paper.html)
  - Really cool way to generate 3d images from 2d images by learning depth

### Vision, Graphics, and Robotics
- [Adding Conditional Control to Text-to-Image Diffusion Models](https://openaccess.thecvf.com/content/ICCV2023/html/Zhang_Adding_Conditional_Control_to_Text-to-Image_Diffusion_Models_ICCV_2023_paper.html)
- [Factorized Inverse Path Tracing for Efficient and Accurate Material-Lighting Estimation](https://openaccess.thecvf.com/content/ICCV2023/html/Wu_Factorized_Inverse_Path_Tracing_for_Efficient_and_Accurate_Material-Lighting_Estimation_ICCV_2023_paper.html)
- [Manipulate by Seeing: Creating Manipulation Controllers from Pre-Trained Representations](https://openaccess.thecvf.com/content/ICCV2023/html/Wang_Manipulate_by_Seeing_Creating_Manipulation_Controllers_from_Pre-Trained_Representations_ICCV_2023_paper.html)
- [3D Implicit Transporter for Temporally Consistent Keypoint Discovery](https://openaccess.thecvf.com/content/ICCV2023/html/Zhong_3D_Implicit_Transporter_for_Temporally_Consistent_Keypoint_Discovery_ICCV_2023_paper.html)

### Recognition, segmentation, and shape analysis
- Segment Anything
- Shape Analysis of Euclidean Curves under Frenet-Serret Framework
- Unmasking Anomalies in Road-Scene Segmentation
- High Quality Entity Segmentation
- Towards Open-Vocabulary Video Instance Segmentation
- Beyond One-to-One: Rethinking the Referring Image Segmentation
- Multiple Instance Learning Framework with Masked Hard Instance Mining for Whole Slide Image Classification
- [Scale-MAE: A Scale-Aware Masked Autoencoder for Multiscale Geospatial Representation Learning](https://openaccess.thecvf.com/content/ICCV2023/papers/Reed_Scale-MAE_A_Scale-Aware_Masked_Autoencoder_for_Multiscale_Geospatial_Representation_Learning_ICCV_2023_paper.pdf)
  - Method for building segmentation models that can succcessfully infer on a variety of ground sample distances 
- Progressive Spatio-Temporal Prototype Matching for Text-Video Retrieval
- LogicSeg: Parsing Visual Semantics with Neural Logic Learning and Reasoning
- ASIC: Aligning Sparse in-the-wild Image Collections

## Papers/Posters Reviewed
- [CDUL: CLIP-Driven Unsupervised Learning for Multi-Label Image Classification]([https://app.imagina.com/iccv-2023/363127](https://openaccess.thecvf.com/content/ICCV2023/html/Abdelfattah_CDUL_CLIP-Driven_Unsupervised_Learning_for_Multi-Label_Image_Classification_ICCV_2023_paper.html))
  - Interesting look at using unsupervised learning for unknown objects
- [Parallel Attention Interaction Network for Few-Shot Skeleton-Based Action Recognition](https://openaccess.thecvf.com/content/ICCV2023/html/Liu_Parallel_Attention_Interaction_Network_for_Few-Shot_Skeleton-Based_Action_Recognition_ICCV_2023_paper.html)

## Related Work and References
- [Conference Newsletter (Wednesday)](https://www.rsipvision.com/ICCV2023-Wednesday/)
- [Conference Newsletter (Thursday)](https://www.rsipvision.com/ICCV2023-Thursday/)
- [Conference Newsletter (Thursday)](https://www.rsipvision.com/ICCV2023-Friday/)
