import os
wdir=os.getcwd()

def istio_installation():
    istio_dir = os.path.join(wdir,"istio-1.16.1")  
    os.chdir(istio_dir)
    bin_dir = os.path.join(istio_dir,"bin")
    #export 'PATH=${bin_dir}:$PATH"
    os.environ["PATH"] = f"{bin_dir}:{os.environ['PATH']}"
    os.system("kubectl create ns istio-system")
    os.system("istioctl install")
    os.system("kubectl label namespace default istio-injection=enabled")   

def kiali_setup():
    kiali_dir = "istio-1.16.1/samples/addons/"
    kiali_dir = os.path.join(wdir, kiali_dir)
    os.chdir(kiali_dir)
    os.system("kubectl create -f kiali.yaml")
    os.system("kubectl create -f prometheus.yaml")

def kiali_vs_gw():
    os.chdir(wdir)
    os.system("kubectl create -f kiali-vs-gw.yml")

def deploy_application():
    os.chdir(wdir)
    os.system("kubectl create -f full-deploy.yml")

# deploy_application()

#istio_installation()
kiali_setup()
kiali_vs_gw()
deploy_application()
