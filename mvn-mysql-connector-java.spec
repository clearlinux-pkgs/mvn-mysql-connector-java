#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-mysql-connector-java
Version  : 5.1.38
Release  : 2
URL      : https://github.com/mysql/mysql-connector-j/archive/5.1.38.tar.gz
Source0  : https://github.com/mysql/mysql-connector-j/archive/5.1.38.tar.gz
Source1  : https://repo1.maven.org/maven2/mysql/mysql-connector-java/5.1.38/mysql-connector-java-5.1.38.jar
Source2  : https://repo1.maven.org/maven2/mysql/mysql-connector-java/5.1.38/mysql-connector-java-5.1.38.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: mvn-mysql-connector-java-data = %{version}-%{release}

%description
MySQL Connector/J @MYSQL_CJ_VERSION@
This is a release of MySQL Connector/J, Oracle's dual-
license JDBC Driver for MySQL. For the avoidance of
doubt, this particular copy of the software is released
under the version 2 of the GNU General Public License.
MySQL Connector/J is brought to you by Oracle.

%package data
Summary: data components for the mvn-mysql-connector-java package.
Group: Data

%description data
data components for the mvn-mysql-connector-java package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/mysql/mysql-connector-java/5.1.38
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/mysql/mysql-connector-java/5.1.38/mysql-connector-java-5.1.38.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/mysql/mysql-connector-java/5.1.38
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/mysql/mysql-connector-java/5.1.38/mysql-connector-java-5.1.38.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/mysql/mysql-connector-java/5.1.38/mysql-connector-java-5.1.38.jar
/usr/share/java/.m2/repository/mysql/mysql-connector-java/5.1.38/mysql-connector-java-5.1.38.pom
