from src.app.controllers import event_type_controller, event_model_controller, quotation_controller,\
                                supplier_controller, service_controller, venue_controller, \
                                structure_controller


def init_routes(app):
    app.route('/quotation', methods=['POST'])(quotation_controller.add_quotation)
    app.route('/quotations', methods=['GET'])(quotation_controller.get_all_quotations)
    app.route('/quotation/<id>', methods=['GET'])(quotation_controller.get_quotation)
    app.route('/quotations/client/<client_id>', methods=['GET'])(quotation_controller.get_all_quotations_from_client)
    app.route('/quotation/<id>', methods=['PUT'])(quotation_controller.update_quotation)
    app.route('/quotations/<id>', methods=['DELETE'])(quotation_controller.delete_quotation)
    app.route('/quotation/client/<client_id>', methods=['GET'])(quotation_controller.get_quotations_by_client)

    app.route('/event_type', methods=['POST'])(event_type_controller.add_event_type)
    app.route('/event_type', methods=['GET'])(event_type_controller.get_event_type)
    app.route('/event_type/<id>', methods=['GET'])(event_type_controller.get_single_event_type)
    app.route('/event_type/<id>', methods=['PUT'])(event_type_controller.update_event_type)
    app.route('/event_type/<id>', methods=['DELETE'])(event_type_controller.delete_event_type)

    app.route('/event_model', methods=['POST'])(event_model_controller.add_event_model)
    app.route('/event_model', methods=['GET'])(event_model_controller.get_event_model)
    app.route('/event_model/<id>', methods=['GET'])(event_model_controller.get_single_event_model)
    app.route('/event_model/<id>', methods=['PUT'])(event_model_controller.update_event_model)
    app.route('/event_model/<id>', methods=['DELETE'])(event_model_controller.delete_event_model)

    app.route('/supplier', methods=['POST'])(supplier_controller.add_supplier)
    app.route('/supplier', methods=['GET'])(supplier_controller.get_supplier)
    app.route('/supplier/<id>', methods=['GET'])(supplier_controller.get_single_supplier)
    app.route('/supplier/<id>', methods=['PUT'])(supplier_controller.update_supplier)
    app.route('/supplier/<id>', methods=['DELETE'])(supplier_controller.delete_supplier)

    app.route('/service', methods=['POST'])(service_controller.add_service)
    app.route('/service', methods=['GET'])(service_controller.get_service)
    app.route('/service/<id>', methods=['GET'])(service_controller.get_single_service)
    app.route('/service/<id>', methods=['PUT'])(service_controller.update_service)
    app.route('/service/<id>', methods=['DELETE'])(service_controller.delete_service)

    app.route('/venue', methods=['POST'])(venue_controller.add_venue)
    app.route('/venue', methods=['GET'])(venue_controller.get_venues)
    app.route('/venue/<id>', methods=['GET'])(venue_controller.get_venue)
    app.route('/venue/<id>', methods=['PUT'])(venue_controller.update_venue)
    app.route('/venue/<id>', methods=['DELETE'])(venue_controller.delete_product)

    app.route('/structure', methods=['POST'])(structure_controller.add_structure)
    app.route('/structure', methods=['GET'])(structure_controller.get_structure)
    app.route('/structure/<id>', methods=['GET'])(structure_controller.get_single_structure)
    app.route('/structure/<id>', methods=['PUT'])(structure_controller.update_structure)
    app.route('/structure/<id>', methods=['DELETE'])(structure_controller.delete_structure)
