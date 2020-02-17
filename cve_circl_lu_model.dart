class cvecircllu {
	List<dynamic> product = [];
	String vendor;
	cvecircllu.fromJson({Map<String, dynamic> data}){
		this.product = data['product'];
		this.vendor = data['vendor'];
	}
}