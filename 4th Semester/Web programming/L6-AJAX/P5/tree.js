// Crează nodul li pentru folder sau fișier
function createNode(item) {
  const li = document.createElement('li');
  li.textContent = item.name;
  li.dataset.path = item.path;

  if(item.type === 'dir') {
    li.classList.add('folder');
    li.addEventListener('click', function(e) {
      e.stopPropagation();
      if(li.classList.contains('open')) {
        // închide folderul
        li.classList.remove('open');
        const childUl = li.querySelector('ul');
        if(childUl) childUl.remove();
      } else {
        // deschide folderul
        li.classList.add('open');
        const childUl = document.createElement('ul');
        li.appendChild(childUl);
        loadDirectory(item.path, childUl);
      }
    });
  } else {
    li.classList.add('file');
    li.addEventListener('click', function(e) {
      e.stopPropagation();
      loadFileContent(item.path);
    });
  }

  return li;
}

// Încarcă conținut director prin AJAX și populează containerul ul
function loadDirectory(path, container) {
  const xhr = new XMLHttpRequest();
  xhr.open('GET', 'get_directory.php?path=' + encodeURIComponent(path), true);
  xhr.onload = function() {
    if(xhr.status === 200) {
      const items = JSON.parse(xhr.responseText);
      items.forEach(item => {
        const node = createNode(item);
        container.appendChild(node);
      });
    } else {
      container.textContent = 'Eroare la încărcarea directorului';
    }
  };
  xhr.onerror = function() {
    container.textContent = 'Eroare la conexiunea cu serverul';
  };
  xhr.send();
}

// Încarcă conținut fișier prin AJAX și îl afișează în <pre>
function loadFileContent(filePath) {
  const xhr = new XMLHttpRequest();
  xhr.open('GET', 'read_file.php?file=' + encodeURIComponent(filePath), true);
  xhr.onload = function() {
    if(xhr.status === 200) {
      document.getElementById('file-content').textContent = xhr.responseText;
    } else {
      document.getElementById('file-content').textContent = 'Eroare la încărcarea fișierului.';
    }
  };
  xhr.onerror = function() {
    document.getElementById('file-content').textContent = 'Eroare la conexiunea cu serverul.';
  };
  xhr.send();
}

// La încărcarea paginii, încarcă conținutul directorului rădăcină (folderul scriptului)
window.onload = function() {
  const treeRoot = document.createElement('ul');
  document.getElementById('tree-root').appendChild(treeRoot);
  loadDirectory('C:/xampp/htdocs/AJAX', treeRoot);
};


/*
// Creează nodul li pentru folder sau fișier
function createNode(item) {
    const $li = $('<li></li>').text(item.name).attr('data-path', item.path);

    if (item.type === 'dir') {
        $li.addClass('folder').on('click', function (e) {
            e.stopPropagation();
            const $this = $(this);
            if ($this.hasClass('open')) {
                $this.removeClass('open').children('ul').remove();
            } else {
                $this.addClass('open');
                const $childUl = $('<ul></ul>');
                $this.append($childUl);
                loadDirectory(item.path, $childUl);
            }
        });
    } else {
        $li.addClass('file').on('click', function (e) {
            e.stopPropagation();
            loadFileContent(item.path);
        });
    }

    return $li;
}

// Încarcă conținut director prin AJAX și populează containerul ul
function loadDirectory(path, $container) {
    $.ajax({
        url: 'get_directory.php',
        method: 'GET',
        data: { path: path },
        dataType: 'json',
        success: function (items) {
            $.each(items, function (i, item) {
                const $node = createNode(item);
                $container.append($node);
            });
        },
        error: function () {
            $container.text('Eroare la încărcarea directorului.');
        }
    });
}

// Încarcă conținut fișier prin AJAX și îl afișează în <pre>
function loadFileContent(filePath) {
    $.ajax({
        url: 'read_file.php',
        method: 'GET',
        data: { file: filePath },
        success: function (data) {
            $('#file-content').text(data);
        },
        error: function () {
            $('#file-content').text('Eroare la încărcarea fișierului.');
        }
    });
}

// La încărcarea paginii, încarcă directorul rădăcină
$(document).ready(function () {
    const $treeRoot = $('<ul></ul>');
    $('#tree-root').append($treeRoot);
    loadDirectory('C:/xampp/htdocs/AJAX', $treeRoot);
});


*/