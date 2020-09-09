# framework structure
![](./git_img/structure.jpg)


# Prepartion
## Download weight
[Yolo_obj_weights.h5](https://drive.google.com/file/d/1NqbM5jsrSCPd25o2YSzQ0n4hv_QGKuXb/view?usp=sharing)

## put it in the following path

```cmd
./app/utils/model_data/
```
## change the hostname in runserver.py

# Run Server
```cmd
python runserver.py
```

# requests.post
requests.post with json (your image url)
(return json(result text, and result image url))
```cmd
http://<your host>:8080/post
```
# result (by POST MAN)
![](./git_img/result.jpg)

