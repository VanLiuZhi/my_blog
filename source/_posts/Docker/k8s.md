---
title: Kubernetes(k8s) 运用
date: 2019-04-05 00:00:00
tags: [linux, docker, note]
categories: web开发
---

Kubernetes(k8s) 运用

<!-- more -->

## K8S DashBoard服务

创建服务后通过代理访问

1. 创建服务
kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v1.10.1/src/deploy/recommended/kubernetes-dashboard.yaml
kubectl create -f kubernetes-dashboard.yaml

2. 开启代理
kubectl proxy 或 kubectl proxy &

访问:
http://localhost:8001/api/v1/namespaces/kube-system/services/https:kubernetes-dashboard:/proxy/

3. 登录

配置文件

    Mac: $HOME/.kube/config
    Win: %UserProfile%\.kube\config

创建令牌
{% codeblock%}
kubectl -n kube-system describe secret $(kubectl -n kube-system get secret | grep admin-user | awk '{print $1}')
{% endcodeblock %}

## 安装

安装总结：
1. 关闭各种服务，保证安装和集群建立的成功
2. 安装docker和k8s组件，并保证开启启动
3. 每台机器上都是一样的，当然master如果不参与负载，可以不装部分组件
4. 使用kubeadm部署Kubernetes，完成集群初始化

```
关闭SeLinux，由于太复杂，关了
SELinux(Security-Enhanced Linux) 是美国国家安全局（NSA）对于强制访问控制的实现，是 Linux历史上最杰出的新安全子系统。NSA是在Linux社区的帮助下开发了一种访问控制体系，在这种访问控制体系的限制下，进程只能访问那些在他的任务中所需要文件。
```

`sed -i 's/SELINUX=*/SELINUX=disabled/' /etc/selinux/config`或修改配置 `/etc/selinux/config` SELINUX=disabled

配置cgroup drive

Cgroups是control groups的缩写，是Linux内核提供的一种可以限制、记录、隔离进程组（process groups）所使用的物理资源（如：cpu,memory,IO等等）的机制。最初由google的工程师提出，后来被整合进Linux内核。Cgroups也是LXC为实现虚拟化所使用的资源管理手段，可以说没有cgroups就没有LXC。
保证docker 和 kubelet的 cgroup 一致，Cgroup Driver:Cgroupfs 与 Systemd。查看（dockerk可以看到cgroup，kublete就不一定有了，这种情况就统一成一样的吧）
` cat /usr/lib/systemd/system/kubelet.service.d/10-kubeadm.conf` 可能会在 `/etc/systemd/system/kubelet.service.d`
`docker info`
修改docker的deamon.json 

```
{
  "exec-opts": ["native.cgroupdriver=systemd"]
}
```

或者修改kublete，去配置文件里面，环境变量设置加上
`Environment="KUBELET_CGROUP_ARGS=--cgroup-driver=systemd"`

安装 kubelet & kubeadm & kubectl

使用yum命令安装

kubelet:运行在cluster所有节点上，负责启动POD和容器
kubeadm:用于初始化cluster，通过它完成k8s的初始化
kubectl:kubectl是kubenetes命令行工具，通过kubectl可以部署和管理应用，查看各种资源，创建，删除和更新组件

## kubespray 安装方法

并不是很推荐的一种方式，应为换源的原因，kubespray的版本往往和镜像不一致，而且你找到的别人的安装总结都是用自己或别人的，总的来说这是一个不错的工具，但是在天朝局域网下特别难用，最好就是锁定kubespray版本，然后使用阿里云制作自己的镜像，然后kubespray里面把谷歌的镜像换成自己制作的。

批量换源

grc_image_files=(
kuberspray/extra_playbooks/roles/dnsmasq/templates/dnsmasq-autoscaler.yml
kuberspray/extra_playbooks/roles/download/defaults/main.yml
kuberspray/extra_playbooks/roles/kubernetes-apps/ansible/defaults/main.yml
kuberspray/roles/download/defaults/main.yml
kuberspray/roles/dnsmasq/templates/dnsmasq-autoscaler.yml
kuberspray/roles/kubernetes-apps/ansible/defaults/main.yml
)

grc_image_files=(
kubespray/roles/download/defaults/main.yml
kubespray/roles/kubernetes-apps/ansible/defaults/main.yml
)

grc_image_files=(
kubespray/roles/download/defaults/main.yml
)

for file in ${grc_image_files[@]} ; do
    sed -i 's/gcr.io\/google_containers/registry.cn-hangzhou.aliyuncs.com\/szss_k8s/g' $file
done

for file in ${grc_image_files[@]} ; do
    sed -i 's/gcr.io\/google_containers/registry.cn-hangzhou.aliyuncs.com\/szss_k8s/g' $file
done

quay_image_files=(
./kubespray/extra_playbooks/roles/download/defaults/main.yml
./kubespray/roles/download/defaults/main.yml
)

quay_image_files=(
kubespray/roles/download/defaults/main.yml
)

for file in ${quay_image_files[@]} ; do
    sed -i 's/quay.io\/coreos\//registry.cn-hangzhou.aliyuncs.com\/szss_quay_io\/coreos-/g' $file
    sed -i 's/quay.io\/calico\//registry.cn-hangzhou.aliyuncs.com\/szss_quay_io\/calico-/g' $file
    sed -i 's/quay.io\/l23network\//registry.cn-hangzhou.aliyuncs.com\/szss_quay_io\/l23network-/g' $file
done

安装失败清理 或者用清理命令

sudo rm -rf /etc/kubernetes/
sudo rm -rf /var/lib/kubelet
sudo rm -rf /var/lib/etcd
sudo rm -rf /usr/local/bin/kubectl
sudo rm -rf /etc/systemd/system/calico-node.service
sudo rm -rf /etc/systemd/system/kubelet.service
sudo systemctl stop etcd.service
sudo systemctl disable etcd.service
sudo systemctl stop calico-node.service
sudo systemctl disable calico-node.service
sudo docker stop $(docker ps -q)
sudo docker rm $(docker ps -a -q)
sudo service docker restart

其他命令

CONFIG_FILE=./kubespray/inventory/inventory.cfg python36 ./kubespray/contrib/inventory_builder/inventory.py ${IP[*]}
ansible-playbook -i hosts.ini /etc/kubespray/reset.yml

1. 流程总结

虚拟机: vagrant virtual box，虚拟的操作都使用vagrant，最好是使用一个Vagrantfile文件来启动和管理集群，这样比较方便

网络配置: 使用私有网络，所有虚拟机处在相同的子网当中，相互之间能通信，也能和外网通信

系统配置：检查虚拟机网络是否联通，完成相关配置（最好不要用临时配置的方式）

开始安装：下载kubespray，开始安装

参考：https://www.one-tab.com/page/HIr4mKK3SBKJJBDk5bNz_A

2. 虚拟机

使用vagrant来管理虚拟机，下面是一个配置文件，vagrant使用ruby来编写配置文件

```ruby
Vagrant.configure(2) do |config|
  # 如果需要三台就(1..3)的形式
  (1..3).each do |i|
    config.vm.define "cluster#{i}" do |node|
      node.vm.box = "centos_k8s"
      node.vm.hostname = "cluster#{i}"
      node.vm.network "private_network", ip: "192.168.59.#{i}"
      # 映射目录 根据自己实际情况配置
      # node.vm.synced_folder "../var/www/cluster", "/var/www/cluster"
      node.vm.provider "virtualbox" do |v|
        v.name = "cluster#{i}"
        v.memory = 512
        v.cpus = 1
      end
    end
  end
end
```

find /etc/kubespray -name '*.yml' | xargs -n1 -I{} sed -i "s/gcr\.io\/google_containers/gcr\.mirrors\.ustc\.edu\.cn\/google-containers/g" {}
find /etc/kubespray -name '*.yml' | xargs -n1 -I{} sed -i "s/gcr\.io\/google-containers/gcr\.mirrors\.ustc\.edu\.cn\/google-containers/g" {}
find /etc/kubespray -name '*.yml' | xargs -n1 -I{} sed -i 's/quay\.io/quay-mirror\.qiniu\.com/' {}

find /etc/kubespray -name '*.yml' | xargs -n1 -I{} sed -i "s/mirrorgooglecontainers\/google-containers/registry\.cn-hangzhou\.aliyuncs\.com\/google_containers/g" {}
find /etc/kubespray -name '*.yml' | xargs -n1 -I{} sed -i "s/mirrorgooglecontainers\/google-containers/registry\.cn-hangzhou\.aliyuncs\.com\/google_containers/g" {}
find /etc/kubespray -name '*.yml' | xargs -n1 -I{} sed -i 's/quay\.io/quay-mirror\.qiniu\.com/' {}

## kubeadm 安装(精简版)

官方安装工具

### 环境准备

所有机器都要执行

1. 设置主机名hostname，管理节点设置主机名为 master，其它设置为node

```
sudo hostnamectl set-hostname master
```

2. 然后配置/etc/hosts

```
192.168.59.101 master

192.168.59.102 node1

192.168.59.103 node2
```

3. 关闭防火墙、selinux和swap

```
sudo systemctl stop firewalld

sudo systemctl disable firewalld

sudo setenforce 0

sudo sed -i "s/^SELINUX=enforcing/SELINUX=disabled/g" /etc/selinux/config

sudo swapoff -a

sudo sed -i 's/.*swap.*/#&/' /etc/fstab
```

4. 配置内核参数，将桥接的IPv4流量传递到iptables的链

```
sudo touch /etc/sysctl.d/k8s.conf && sudo vim /etc/sysctl.d/k8s.conf

net.bridge.bridge-nf-call-ip6tables = 1

net.bridge.bridge-nf-call-iptables = 1

执行：
sudo sysctl --system
```

5. 配置国内yum源

```
sudo yum install -y wget

sudo mkdir /etc/yum.repos.d/bak && sudo mv /etc/yum.repos.d/*.repo /etc/yum.repos.d/bak

sudo wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.cloud.tencent.com/repo/centos7_base.repo

sudo wget -O /etc/yum.repos.d/epel.repo http://mirrors.cloud.tencent.com/repo/epel-7.repo

sudo yum clean all && sudo yum makecache
```

配置国内Kubernetes源

```
sudo touch /etc/yum.repos.d/kubernetes.repo && sudo vim /etc/yum.repos.d/kubernetes.repo

[kubernetes]

name=Kubernetes

baseurl=https://mirrors.aliyun.com/kubernetes/yum/repos/kubernetes-el7-x86_64/

enabled=1

gpgcheck=1

repo_gpgcheck=1

gpgkey=https://mirrors.aliyun.com/kubernetes/yum/doc/yum-key.gpg https://mirrors.aliyun.com/kubernetes/yum/doc/rpm-package-key.gpg
```

配置 docker 源

```
sudo wget https://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo -O /etc/yum.repos.d/docker-ce.repo
```

至此，环境准备工作完成，处理主机名称设置不一样，其它操作每天机器执行都是一样的

### 软件安装

1. 安装docker

```
sudo yum install -y docker-ce-18.06.1.ce-3.el7

sudo systemctl enable docker && sudo systemctl start docker

查看安装：
sudo docker –version

Docker version 18.06.1-ce, build e68fc7a
```

2. 安装kubeadm、kubelet、kubectl

```
sudo yum install -y kubelet kubeadm kubectl
sudo systemctl enable kubelet
```

kubeadm init --kubernetes-version=1.15.2 --apiserver-advertise-address=192.168.59.101 --image-repository registry.aliyuncs.com/google_containers --service-cidr=10.1.0.0/16 --pod-network-cidr=10.244.0.0/16

### 部署master节点，node节点加入集群

Your Kubernetes control-plane has initialized successfully!

To start using your cluster, you need to run the following as a regular user:

  mkdir -p $HOME/.kube
  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
  sudo chown $(id -u):$(id -g) $HOME/.kube/config

You should now deploy a pod network to the cluster.
Run "kubectl apply -f [podnetwork].yaml" with one of the options listed at:
  https://kubernetes.io/docs/concepts/cluster-administration/addons/

Then you can join any number of worker nodes by running the following on each as root:

kubeadm join 192.168.59.101:6443 --token r7j6o4.1mkpzrbwk4sfvtu0 --discovery-token-ca-cert-hash sha256:250470943e4c877f2dbfcb5be4e369a7a074c24bcd833628b326a999e968a6c7

wget https://raw.githubusercontent.com/kubernetes/dashboard/v1.10.1/src/deploy/recommended/kubernetes-dashboard.yaml

sed -i 's/k8s.gcr.io/loveone/g' kubernetes-dashboard.yaml
sed -i '/targetPort:/a\ \ \ \ \ \ nodePort: 30001\n\ \ type: NodePort' kubernetes-dashboard.yaml

kubectl create clusterrolebinding admin-user –clusterrole=cluster-admin –serviceaccount=kube-system:admin-user

