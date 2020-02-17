class CveCirclLu {
	List<dynamic> product = [];
	String vendor;
	CveCirclLu.fromJson({Map<String, dynamic> data}) {
		this.product = data['product'];
		this.vendor = data['vendor'];
	}
}