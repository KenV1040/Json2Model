class CveCirclLu {
	String Modified;
	String Published;
	Map<String, dynamic> access = {};
	String assigner;
	double cvss;
	String cwe;
	String id;
	Map<String, dynamic> impact = {};
	String last-modified;
	List<dynamic> references = [];
	String summary;
	List<dynamic> vulnerableConfiguration = [];
	List<dynamic> vulnerableConfigurationCpe22 = [];
	List<dynamic> vulnerableProduct = [];

	CveCirclLu.fromJson({Map<String, dynamic> data}) {
		this.Modified = data['Modified'];
		this.Published = data['Published'];
		this.access = data['access'];
		this.assigner = data['assigner'];
		this.cvss = data['cvss'];
		this.cwe = data['cwe'];
		this.id = data['id'];
		this.impact = data['impact'];
		this.last-modified = data['last-modified'];
		this.references = data['references'];
		this.summary = data['summary'];
		this.vulnerable_configuration = data['vulnerable_configuration'];
		this.vulnerable_configuration_cpe_2_2 = data['vulnerable_configuration_cpe_2_2'];
		this.vulnerable_product = data['vulnerable_product'];
	}
}