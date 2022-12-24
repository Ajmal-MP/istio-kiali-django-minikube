# istio-kiali-django-minikube
- This project deploy Django application in Minikube cluster and setup Istio service mesh and setup kiali dashbord so we can monitor traffic to our Django web-application 

## Requirements

- Minikube 😄 ✨ 📌 👍 
- Python 🐍
- kubectl

## Start minikube

Run minikube with 4 cpu and memory of 4GB

```bash
  minikube start  --cpus=4  --memory=4000
```

![App Screenshot](https://images.ctfassets.net/w1bd7cq683kz/2qZ0Ll6qoEHq7Anx2lVnK1/3fdfb78454b07be02c6277059e721137/minikube.png)


## Execute the python script 

when we run istio-setup.py the following things are happen:

- setup istio and istio ingress in name space istio-system
- setting up kiali dashbord and creating virtual service and gateway for kiali dashbord
- deploying Django web application in default name space also create service, virtual service, etc

```bash
  python istio-setup.py
```

After some time  all deployment are done 


If you are using minikube you want to set external ip for the services so we want to create a tunnel in minikube with our host for that

```bash
  minikube tunnel 
```

Check the external ip of istio-ingress 

```bash
  kubectl get svc -n istio-system 
```

out put

```bash
Copy code
NAME                      TYPE         CLUSTER-IP       EXTERNAL-IP   PORT(S)                                                                      AGE
istio-ingressgateway      LoadBalancer 10.101.34.80     172.16.1.19   15021:31380/TCP,80:31390/TCP,443:31392/TCP,31400:31400/TCP,15443:31393/TCP   23h
istio-pilot               ClusterIP    10.98.131.221    <none>        15010/TCP,15011/TCP,8080/TCP,9093/TCP                                        23h
istio-policy              ClusterIP    10.105.91.77     <none>        9091/TCP,15004/TCP,9093/TCP                                                  23h
istio-sidecar-inject
```

here we can see the <b>EXTERNAL-IP</b> of istio-ingressgateway just copy the EXTERNAL-IP

## Accessing kiali-dashbord and django web application in browser

To acces website from browser you want to add DNS in you host for the edit the /etc/hosts file like given below

```bash
  172.16.1.19  kiali.aj.com
  172.16.1.19  web.aj.com
```

Remember 172.16.1.19 is the external ip of my istio-ingressgateway 

Finally you can access the kiali dashbord in

[http://kiali.aj.com](http://kiali.aj.com)

![App Screenshot](https://www.linkpicture.com/q/Screenshot-from-2022-12-25-02-05-41.png)


Also the django web application in 

[http://web.aj.com](http://web.aj.com)


![App Screenshot](https://www.linkpicture.com/q/Screenshot-from-2022-12-25-02-10-49.png)


## Feedback

If you have any feedback, please reach out to us at m.pajmal@gmail.com