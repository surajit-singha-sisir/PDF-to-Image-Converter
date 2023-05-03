## About the Application
This is a web application that allows users to upload a PDF file and convert it into a series of images (one image for each page of the PDF file). These images are then displayed on the web page along with a "Preview" button that allows users to view each image in a separate window. Additionally, we've added a new feature that allows users to download all of the converted images as a single zip file.

Overall, this web application could be useful for anyone who needs to convert a PDF document into a series of images, such as someone who wants to create a slideshow or a presentation based on a PDF file. By providing a simple, user-friendly interface, our application makes it easy for users to perform this conversion without needing to install any additional software on their computer.

## Screenshots

1. Main "Desktop Version UI" of the Tool<br><br>
![2023-05-04_04h33_14](https://user-images.githubusercontent.com/48810102/236066078-4d57c002-6718-4cdf-aa69-36a9c3f723b6.png) <br>
<br>
2. PDF file after upload or dragged to the input area.<br><br>
![image](https://user-images.githubusercontent.com/48810102/236068453-75e90063-9428-44c0-93cd-340b22bbade0.png)
 <br>
<br>
3. After Convert Complete. Upper Page<br><br>
![image](https://user-images.githubusercontent.com/48810102/236068489-18d39075-4f85-4d75-8dcf-57ce9f3571d4.png) <br>
<br>

4.Down page after Conversion completed. There have a zip file button.<br><br>

![2023-05-04_04h35_22](https://user-images.githubusercontent.com/48810102/236066785-630c4e52-edef-4680-aa99-95d9a897a95d.png)<br><br>

5. All images contain on the PDF is showing below. You can Get the perticular image file clicking the download button.<br><br>
![2023-05-04_04h35_32](https://user-images.githubusercontent.com/48810102/236067166-d5c9d408-4b10-40ab-b17f-3a14a367d782.png)<br><br>

6. If you clicked on the image download link. Then perticular image open in a blank window.<br><br>
![2023-05-04_04h36_38](https://user-images.githubusercontent.com/48810102/236067399-4979976f-e3c5-43f6-9957-7a4e09ef0c72.png)<br><br>

7. If you are trying to download all images into a single zip file. It will open your Download Manager(IDM - in my case) or Browser default Download manager.<br><br>
![2023-05-04_04h36_22](https://user-images.githubusercontent.com/48810102/236067611-472300a0-db3d-422b-afed-21ccdea5b545.png)<br><br>

8. In Mobile Version it also view a pretty cool UI. Mobile View-1:<br><br>
![2023-05-04_04h37_07](https://user-images.githubusercontent.com/48810102/236067851-8f7f48b0-24c4-497f-91db-a3ac99c09513.png)
<br><br><br>
Mobile View-2:<br><br>
![2023-05-04_04h37_17](https://user-images.githubusercontent.com/48810102/236067874-c21ef4be-598d-421e-84b5-98c9b0af6a00.png)
<br><br>

## Requirements Libraries
- aiohttp==3.8.4<br>
- aiosignal==1.3.1<br>
- amqp==5.1.1<br>
- anyio==3.6.2<br>
- asgiref==3.6.0<br>
- deprecation==2.1.0<br>
- distlib==0.3.6<br>
- Django==4.1.6<br>
- form==0.0.1<br>
- hpack==4.0.0<br>
- httpcore==0.16.3<br>
- httpx==0.23.3<br>
- hyperframe==6.0.1<br>
- idna==3.4<br>
- multidict==6.0.4<br>
- packaging==23.1<br>
- pdf2image==1.16.3<br>
- Pillow==9.5.0<br>
- sqlparse==0.4.3<br>
- tqdm==4.64.1<br>
- tzdata==2023.3<br>
- urllib3==1.26.14<br>
- virtualenv==20.23.0<br>


## Install The Requirements

Run the commands on your Terminal.
```
pip install -r requirements.txt
```

This tool is developed by [Surajit Singha Sisir](https://www.facebook.com/SurajitSinghaSisir)
