from django.shortcuts import render, redirect

vocabulary_data = [
    {'word': 'Apple', 'translation': 'แอปเปิ้ล', 'word_type': 'Noun'},
    {'word': 'Banana', 'translation': 'กล้วย', 'word_type': 'Noun'},
    {'word': 'Cat', 'translation': 'แมว', 'word_type': 'Noun'},
    {'word': 'Sunshine', 'translation': 'แสงแดด', 'word_type': 'Noun'},
    {'word': 'Running', 'translation': 'การวิ่ง', 'word_type': 'Verb'},
    {'word': 'Happy', 'translation': 'มีความสุข', 'word_type': 'Adjective'},
    {'word': 'Book', 'translation': 'หนังสือ ', 'word_type': 'Noun'},
    {'word': 'Blue', 'translation': 'สีฟ้า', 'word_type': 'Adjective/Noun'},
    {'word': 'Computer', 'translation': 'คอมพิวเตอร์', 'word_type': 'Noun'},
    {'word': 'Water', 'translation': 'น้ำ', 'word_type': 'Noun'},
    {'word': 'Jump', 'translation': 'กระโดด', 'word_type': 'Verb/Noun'},
    {'word': 'Dog', 'translation': 'สุนัข', 'word_type': 'Noun'},
    {'word': 'Beautiful', 'translation': 'สวยงาม', 'word_type': 'Adjective'},
    {'word': 'Music', 'translation': 'เพลง', 'word_type': 'Noun'},
    {'word': 'Car', 'translation': 'รถยนต์', 'word_type': 'Noun'},
    {'word': 'Friend', 'translation': 'เพื่อน', 'word_type': 'Noun'},
    {'word': 'Walk', 'translation': 'เดิน', 'word_type': 'Verb/Noun'},
    {'word': 'Elephant', 'translation': 'ช้าง', 'word_type': 'Noun'},
    {'word': 'Dance', 'translation': 'เต้นรำ', 'word_type': 'Verb/Noun'},
    {'word': 'Rainbow', 'translation': 'รุ้ง', 'word_type': 'Noun'},
    {'word': 'Mountain', 'translation': 'ภูเขา', 'word_type': 'Noun'},
    {'word': 'Carsick', 'translation': 'เมารถ', 'word_type': 'Adjective'},
]

vocabulary_data_list = vocabulary_data[:]


def Index(request):
    search_query = request.GET.get('q', '')

    # Sort the vocabulary data for display
    sorted_vocabulary_data = sorted(vocabulary_data_list, key=lambda x: x['word'].lower())

    # Find the index of the search query in the sorted list
    index = -1
    for i, data in enumerate(sorted_vocabulary_data):
        if data['word'].lower() == search_query.lower():
            index = i
            break

    # Initialize previous and next words
    previous_word = None
    next_word = None

    if index >= 0:
        if index > 0:
            previous_word = sorted_vocabulary_data[index - 1]
        if index < len(sorted_vocabulary_data) - 1:
            next_word = sorted_vocabulary_data[index + 1]

    # Check if the search query partially matches any word
    partial_matches = [data for data in sorted_vocabulary_data if search_query.lower() in data['word'].lower()]

    return render(request, 'index.html',
                  {'search_query': search_query,
                   'previous_word': previous_word, 'next_word': next_word,
                   'partial_matches': partial_matches})


def Create_or_update(request):
    mode = request.GET.get('mode', 'create')

    if request.method == 'POST':
        word = request.POST.get('word')
        translation = request.POST.get('translation')
        word_type = request.POST.get('word_type')

        if mode == 'create':
            # Create a new entry
            data = {'word': word, 'translation': translation, 'word_type': word_type}
            vocabulary_data_list.append(data)
        elif mode == 'update':
            # Update the existing entry
            get_word = request.GET.get('word', None)
            if get_word:
                for data in vocabulary_data_list:
                    if data['word'] == get_word:
                        data['word'] = word
                        data['translation'] = translation
                        data['word_type'] = word_type

        return redirect('index')

    # Get Form Update
    if mode == 'update':
        get_word = request.GET.get('word', None)
        if get_word:
            vocabulary_data_to_update = None
            for data in vocabulary_data_list:
                if data['word'] == get_word:
                    vocabulary_data_to_update = data
                    break
            if vocabulary_data_to_update:
                return render(request, 'create_or_update.html',
                              {'mode': 'update', 'vocabulary_data': vocabulary_data_to_update})

    return render(request, 'create_or_update.html', {'mode': mode})


def Delete(request):
    get_word = request.GET.get('word', None)
    if get_word:
        for data in vocabulary_data_list:
            if data['word'] == get_word:
                vocabulary_data_list.remove(data)
                return redirect('index')
