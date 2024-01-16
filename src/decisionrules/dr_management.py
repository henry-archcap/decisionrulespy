import requests

from .custom_domain import *
from .exceptions import *

class ManagementApi():    

    def __init__(self, management_api_key, custom_domain: CustomDomain = None):
        self._management_api = management_api_key
        self._custom_domain = custom_domain
        self._header = self.header_factory(self._management_api)


    def header_factory(self, api_key):
        return {"Authorization": f"Bearer {api_key}"}


    def url_factory(self):
        if self._custom_domain is not None:
            return f"{self._custom_domain.custom_domain_protocol.value}://{self._custom_domain.custom_domain_url}/api"
        else:
            return "https://api.decisionrules.io/api"


    def get_call(self, get_url):
        response = None

        response = requests.get(get_url, headers=self._header)

        return response.json()
        

    def get_rule(self, rule_id, version = None):
        url = None
        if version is not None:
            url = f"{self.url_factory()}/rule/{rule_id}/{version}"
        else:
            url = f"{self.url_factory()}/rule/{rule_id}"

        return self.get_call(url)



    def get_space(self, space_id):
        url = f"{self.url_factory()}/space/items"

        return self.get_call(url)



    def create_rule(self, space_id, data):
        url = f"{self.url_factory()}/rule/{space_id}"

        response = None

        
        response = requests.post(url, json=data, headers=self._header)
        return response.json()


    def update_rule(self, rule_id, version, data):
        url = f"{self.url_factory()}/rule/{rule_id}/{version}"

        response = None

        
        response = requests.put(url, json=data, headers=self._header)
        return
        

    def delete_rule(self, rule_id, version):
        url = f"{self.url_factory()}/rule/{rule_id}/{version}"

        response = None

        requests.delete(url, headers=self._header)
        return


    def get_ruleflow(self, ruleflow_id, version = None):
        url = None
        if version is not None:
            url = f"{self.url_factory()}/rule-flow/export/{ruleflow_id}/{version}"
        else:
            url = f"{self.url_factory()}/rule-flow/export/{ruleflow_id}"

        print(url)

        return self.get_call(url)


    def create_ruleflow(self, data):
        url = f"{self.url_factory()}/rule-flow/import"

        response = None
        response = requests.post(url,json=data, headers=self._header)
        return response.json()


    def update_ruleflow(self, ruleflow_id, version, data):
        url = f"{self.url_factory()}/rule-flow/{ruleflow_id}/{version}"

        response = None

        response = requests.put(url, json=data, headers=self._header)
        return


    def delele_ruleflow(self, ruleflow_id, version = None):
        if version is not None:
            url = f"{self.url_factory()}/rule-flow/{ruleflow_id}/{version}"
        else:
            url = f"{self.url_factory()}/rule-flow/{ruleflow_id}"
        

        response = None

        requests.delete(url, headers=self._header)
        return


    def export_ruleflow(self, ruleflow_id, version = None):
        url = None
        if version is not None:
            url = f"{self.url_factory()}/rule-flow/export/{ruleflow_id}/{version}"
        else:
            url = f"{self.url_factory()}/rule-flow/export/{ruleflow_id}"

        return self.get_call(url)


    def import_ruleflow(self, data, ruleflow_id = None, current_version = None):
        url = None
        if ruleflow_id is None and current_version is None:
            url = f"{self.url_factory()}/rule-flow/import"
        elif ruleflow_id is not None:
            url = f"{self.url_factory()}/rule-flow/import/?new-version={ruleflow_id}"
        elif ruleflow_id is not None and current_version is not None:
            url = f"{self.url_factory()}/rule-flow/import/?overwrite={ruleflow_id}&version={current_version}"

        response = None

        response = requests.post(url=url, json=data, headers=self._header)

        return response.json()


    def change_rule_status(self, ruleId, status, version):
        url = f"{self.url_factory()}/rule/status/{ruleId}/{status}/{version}"

        response = requests.put(url=url, headers=self._header)

        return response.json()

    def getItems(self, tags):

        tagsQuery = ",".join(map(str, tags))

        url = f"{self.url_factory()}/tags/items/?tags={tagsQuery}"

        response = requests.get(url)

        return response.json()

    def updateTags(self, ruleId, data, version=None):
        
        url = ""

        if version is not None:
            url = f"{self.url_factory()}/tags/{ruleId}"
        else:
            url = f"{self.url_factory()}/tags/{ruleId}/{version}"

        response = requests.patch(url, data=data)

        return response.json()

    def deleteTags(self, ruleId, version=None):

        url = ""

        if version is not None:
            url = f"{self.url_factory()}/tags/{ruleId}"
        else:
            url = f"{self.url_factory()}/tags/{ruleId}/{version}"

        requests.delete(url)

        return