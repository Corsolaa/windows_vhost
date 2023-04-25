import os
import sys


def get_url():
    print("Please insert the website URL that you want to add to XAMPP")
    print("(without a toplevel domain):")
    website_url = input() + ".test"
    return website_url


def set_windows_host(host_url):
    hosts_path = os.environ['WINDIR'] + r"\System32\drivers\etc\hosts"
    try:
        file = open(hosts_path, "a")
        file.write("\n127.0.0.1 " + host_url)
    except PermissionError:
        sys.exit("No admin rights.")


def set_xampp_vhost(host_url):
    while True:
        print("\nPlease input your XAMPP root directory path:")
        print(r"(C:\xampp is mine!)")
        vhost_directory = input()
        if vhost_directory == "":
            vhost_directory = r"C:\xampp"
        if vhost_directory[-1] == "\\":
            vhost_directory = vhost_directory[:-1]
        vhost_directory += r"\apache\conf\extra\httpd-vhosts.conf"
        if os.path.exists(vhost_directory):
            break
        print("not a correct path....")
    with open(vhost_directory, "a+") as file:
        # TODO make it so it puts localhost peace there also.
        file.write("\n\n<VirtualHost *:80>\n"
                   f"    DocumentRoot 'C:/xampp/htdocs/{host_url}'\n"
                   f"    ServerName {host_url}\n"
                   "</VirtualHost>")


if __name__ == '__main__':
    url = get_url()
    set_windows_host(url)
    set_xampp_vhost(url)
