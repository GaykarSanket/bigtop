%define ranger_name ranger

Name: ranger
Version: %{ranger_version}
Release: %{ranger_release}
Summary: ranger
URL: http://ranger.apache.org/
Group: Development/Libraries

License: ASL 2.0
Source0: apache-%{ranger_name}-%{ranger_base_version}-src.tar.gz
Source1: do-component-build

%description
this is description about ranger

%prep
%setup -n apache-%{ranger_name}-%{ranger_base_version}

#BIGTOP_PATCH_COMMANDS

%build
bash %{SOURCE1}
#bash $RPM_SOURCE_DIR/do-component-build

%install
echo  %{buildroot}
mkdir -p %{buildroot}
mkdir -p -m 0755 %{buildroot}/etc/
mkdir -p -m 0755 %{buildroot}/etc/ranger/

echo %_builddir

#cp -r %{_builddir}/apache-ranger-0.7.1 %{buildroot}/etc/ranger

tar -xzvf %{_builddir}/apache-ranger-0.7.1/target/ranger-0.7.1-admin.tar.gz -C %{buildroot}/etc/ranger
tar -xzvf %{_builddir}/apache-ranger-0.7.1/target/ranger-0.7.1-atlas-plugin.tar.gz -C %{buildroot}/etc/ranger
tar -xzvf %{_builddir}/apache-ranger-0.7.1/target/ranger-0.7.1-hbase-plugin.tar.gz -C %{buildroot}/etc/ranger
tar -xzvf %{_builddir}/apache-ranger-0.7.1/target/ranger-0.7.1-hdfs-plugin.tar.gz -C %{buildroot}/etc/ranger
tar -xzvf %{_builddir}/apache-ranger-0.7.1/target/ranger-0.7.1-hive-plugin.tar.gz -C %{buildroot}/etc/ranger
tar -xzvf %{_builddir}/apache-ranger-0.7.1/target/ranger-0.7.1-kafka-plugin.tar.gz -C %{buildroot}/etc/ranger
tar -xzvf %{_builddir}/apache-ranger-0.7.1/target/ranger-0.7.1-kms.tar.gz -C %{buildroot}/etc/ranger
tar -xzvf %{_builddir}/apache-ranger-0.7.1/target/ranger-0.7.1-knox-plugin.tar.gz -C %{buildroot}/etc/ranger
tar -xzvf %{_builddir}/apache-ranger-0.7.1/target/ranger-0.7.1-migration-util.tar.gz -C %{buildroot}/etc/ranger
tar -xzvf %{_builddir}/apache-ranger-0.7.1/target/ranger-0.7.1-ranger-tools.tar.gz -C %{buildroot}/etc/ranger
tar -xzvf %{_builddir}/apache-ranger-0.7.1/target/ranger-0.7.1-solr-plugin.tar.gz -C %{buildroot}/etc/ranger
tar -xzvf %{_builddir}/apache-ranger-0.7.1/target/ranger-0.7.1-src.tar.gz -C %{buildroot}/etc/ranger
tar -xzvf %{_builddir}/apache-ranger-0.7.1/target/ranger-0.7.1-storm-plugin.tar.gz -C %{buildroot}/etc/ranger
tar -xzvf %{_builddir}/apache-ranger-0.7.1/target/ranger-0.7.1-tagsync.tar.gz -C %{buildroot}/etc/ranger
tar -xzvf %{_builddir}/apache-ranger-0.7.1/target/ranger-0.7.1-usersync.tar.gz -C %{buildroot}/etc/ranger
tar -xzvf %{_builddir}/apache-ranger-0.7.1/target/ranger-0.7.1-yarn-plugin.tar.gz -C %{buildroot}/etc/ranger

cp -r %{_builddir}/apache-ranger-0.7.1 /home/sanki

%files
/etc/ranger
