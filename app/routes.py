from flask import Blueprint, request, jsonify
from datetime import datetime
from thefuzz import fuzz
from .models import db, Liste, ListeMorale, PepThomsonIndiv

bp = Blueprint('bp', __name__)

@bp.route('/data', methods=['POST'])
def add_data():
    data = request.json
    # Logic to determine which model to use based on 'Type_de_personne' or other criteria
    new_data = Liste(**data)  # Example for 'Liste', adapt as needed
    db.session.add(new_data)
    db.session.commit()
    return jsonify({'message': 'Data added successfully', 'id': new_data.id})

@bp.route('/data', methods=['GET'])
def get_all_data():
    datas = Liste.query.all()  # Adapt this as needed for dynamic model selection
    data_list = [{'id': data.id, 'Prenom': data.Prenom, 'Nom': data.Nom, 'Date_de_naissance': data.Date_de_naissance.strftime('%Y-%m-%d') if data.Date_de_naissance else None, 'Lieu_de_naissance': data.Lieu_de_naissance, 'Nationalite': data.Nationalite, 'Cin': data.Cin} for data in datas]
    return jsonify(data_list)

@bp.route('/data/<int:data_id>', methods=['GET'])
def get_data_by_id(data_id):
    data = Liste.query.get_or_404(data_id)  # Adapt this as needed for dynamic model selection
    data_response = {'id': data.id, 'Prenom': data.Prenom, 'Nom': data.Nom, 'Date_de_naissance': data.Date_de_naissance.strftime('%Y-%m-%d') if data.Date_de_naissance else None, 'Lieu_de_naissance': data.Lieu_de_naissance, 'Nationalite': data.Nationalite, 'Cin': data.Cin}
    return jsonify(data_response)

@bp.route('/data/<int:data_id>', methods=['PUT'])
def update_data(data_id):
    data = Liste.query.get_or_404(data_id)  # Adapt this as needed
    update_fields = request.json
    for key, value in update_fields.items():
        setattr(data, key, value)
    db.session.commit()
    return jsonify({'message': 'Data updated successfully'})

@bp.route('/data/<int:data_id>', methods=['DELETE'])
def delete_data(data_id):
    data = Liste.query.get_or_404(data_id)  # Adapt this as needed
    db.session.delete(data)
    db.session.commit()
    return jsonify({'message': 'Data deleted successfully'})

@bp.route('/data/filter', methods=['POST'])
def filter_names_date():
    data = request.json
    input_nom = data.get("Nom", "")
    input_prenom = data.get("Prenom", "")
    input_date_naissance = data.get("Date_de_naissance", "")
    type_de_personne = data.get("Type_de_personne", "")

    # Check if the feature for 'Moral' type is not available
    if type_de_personne == "Morale":
        return jsonify({'message': 'This feature is not available yet'})

    datas = Liste.query.all()
    scored_results = []
    
    for data_item in datas:
        nom_ratio = fuzz.ratio(input_nom.capitalize(), data_item.Nom.capitalize() if data_item.Nom else "")
        prenom_ratio = fuzz.ratio(input_prenom.capitalize(), data_item.Prenom.capitalize() if data_item.Prenom else "")

        # Initialize the date of birth ratio
        date_naissance_ratio = 0
        a = 1 if input_nom else 0
        b = 1 if input_prenom else 0
        c = 2 if input_date_naissance else 0

        # Calculate the date of birth ratio if a date is provided
        if input_date_naissance:
            input_date = datetime.strptime(input_date_naissance, '%Y-%m-%d')
            db_date = data_item.Date_de_naissance
            if db_date:
                db_date = db_date.strftime('%Y-%m-%d')
                db_date = datetime.strptime(db_date, '%Y-%m-%d')
                if input_date.month == db_date.month:
                    date_naissance_ratio += 50
                if input_date.year == db_date.year:
                    date_naissance_ratio += 50

        # Calculate total ratio
        total_ratio = ((nom_ratio * a) + (prenom_ratio * b) + (date_naissance_ratio * c)) / (a + b + c) if (a + b + c) > 0 else 0

        # Append to results if the total ratio meets the threshold
        if total_ratio >= 60:
            scored_results.append({
                'id': data_item.id,
                'nom': data_item.Nom.capitalize() if data_item.Nom else "",
                'prenom': data_item.Prenom.capitalize() if data_item.Prenom else "",
                'date de naissance': str(data_item.Date_de_naissance),
                'nom_similarity_ratio': nom_ratio,
                'prenom_similarity_ratio': prenom_ratio,
                'date_naissance_similarity_ratio': date_naissance_ratio,
                'average_similarity_ratio': total_ratio,
                'input_nom_capitalized': input_nom.capitalize() if input_nom else "",
                'input_prenom_capitalized': input_prenom.capitalize() if input_prenom else "",
                'input_date_naissance': input_date_naissance
            })

    # Sort the results by average similarity ratio in descending order
    scored_results.sort(key=lambda x: x['average_similarity_ratio'], reverse=True)
    return jsonify(scored_results)


@bp.route('/data/filter/morale', methods=['POST'])
def filter_names_date_morale():
    data = request.json
    input_nom = data.get("Nom", "")
    input_prenom = data.get("Prenom", "")
    input_date_naissance = data.get("Date_de_naissance", "")
    type_de_personne = data.get("Type_de_personne", "")

    # Process only for 'Morale' type
    if type_de_personne != "Morale":
        return jsonify({'message': 'Invalid type of person. This endpoint is only for "Morale" type.'}), 400

    datas = ListeMorale.query.all()
    scored_results = []
    
    for data_item in datas:
        nom_ratio = fuzz.ratio(input_nom.capitalize(), data_item.Nom.capitalize() if data_item.Nom else "")
        prenom_ratio = fuzz.ratio(input_prenom.capitalize(), data_item.Prenom.capitalize() if data_item.Prenom else "")
        
        date_naissance_ratio = 0
        a = 1 if input_nom else 0
        b = 1 if input_prenom else 0
        c = 2 if input_date_naissance else 0

        if input_date_naissance:
            input_date = datetime.strptime(input_date_naissance, '%Y-%m-%d')
            db_date = data_item.Date_de_naissance
            if db_date:
                db_date = db_date.strftime('%Y-%m-%d')
                db_date = datetime.strptime(db_date, '%Y-%m-%d')
                if input_date.month == db_date.month:
                    date_naissance_ratio += 50
                if input_date.year == db_date.year:
                    date_naissance_ratio += 50

        total_ratio = ((nom_ratio * a) + (prenom_ratio * b) + (date_naissance_ratio * c)) / (a + b + c) if (a + b + c) > 0 else 0

        if total_ratio >= 60:
            scored_results.append({
                'id': data_item.id,
                'nom': data_item.Nom.capitalize() if data_item.Nom else "",
                'prenom': data_item.Prenom.capitalize() if data_item.Prenom else "",
                'date de naissance': str(data_item.Date_de_naissance),
                'nom_similarity_ratio': nom_ratio,
                'prenom_similarity_ratio': prenom_ratio,
                'date_naissance_similarity_ratio': date_naissance_ratio,
                'average_similarity_ratio': total_ratio,
                'input_nom_capitalized': input_nom.capitalize() if input_nom else "",
                'input_prenom_capitalized': input_prenom.capitalize() if input_prenom else "",
                'input_date_naissance': input_date_naissance
            })

    scored_results.sort(key=lambda x: x['average_similarity_ratio'], reverse=True)
    return jsonify(scored_results)


@bp.route('/pep_thomson_indiv/filter', methods=['POST'])
def filter_pep_thomson_indiv():
    data = request.json
    input_first_name = data.get("FirstName", "")
    input_last_name = data.get("LastName", "")
    input_dob = data.get("DOB", "")
    

    pep_thomson_indivs = PepThomsonIndiv.query.all()
    scored_results = []

    for indiv in pep_thomson_indivs:
        first_name_ratio = fuzz.ratio(input_first_name.capitalize(), indiv.FirstName.capitalize() if indiv.FirstName else "")
        last_name_ratio = fuzz.ratio(input_last_name.capitalize(), indiv.LastName.capitalize() if indiv.LastName else "")
        
        dob_ratio = 0
        a = 1 if input_first_name else 0
        b = 1.5 if input_last_name else 0
        c = 2 if input_dob else 0

        if input_dob:
            input_date = datetime.strptime(input_dob, '%Y-%m-%d')
            db_date = indiv.DOB
            if db_date:
                db_date_str = db_date.strftime('%Y-%m-%d')
                db_date = datetime.strptime(db_date_str, '%Y-%m-%d')
                if input_date.month == db_date.month:
                    dob_ratio += 50
                if input_date.year == db_date.year:
                    dob_ratio += 50

        # Calculate total ratio
        total_ratio = ((first_name_ratio * a) + (last_name_ratio * b) + (dob_ratio* c) ) / (a + b + c) if (a + b + c) > 0 else 0

        # Append to results if the total ratio meets the threshold
        if total_ratio >= 60:
            scored_results.append({
                'UID': indiv.UID,
                'FirstName': indiv.FirstName,
                'LastName': indiv.LastName,
                'DOB': str(indiv.DOB),
                'Category': indiv.Category,
                'first_name_similarity_ratio': first_name_ratio,
                'last_name_similarity_ratio': last_name_ratio,
                'dob_similarity_ratio': dob_ratio,
                'average_similarity_ratio': total_ratio
            })

    # Sort the results by average similarity ratio in descending order
    scored_results.sort(key=lambda x: x['average_similarity_ratio'], reverse=True)
    return jsonify(scored_results)
