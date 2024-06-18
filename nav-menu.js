function openNav() {
    document.getElementById("mySidenav").style.width = "350px";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
}

function createTestZone() {
    let testDiv = document.createElement("div");
    testDiv.id = "test-zone";
    document.body.appendChild(testDiv);
}

createTestZone();

let allHTML = `<ul>`;
let level2List = document.getElementsByClassName("lvl2");
if (level2List.length > 0) {
    for (let a = 0; a < level2List.length; a++) {
        const lvl2Item = level2List[a];
        const lvl2ID = lvl2Item.getAttribute("id");
        const lvl2Text = lvl2Item.innerHTML;

        allHTML += `<li><a href="./#${lvl2ID}">${lvl2Text}</a></li>`;

        let level3List = lvl2Item.parentElement.getElementsByClassName("lvl3");
        if (level3List.length > 0) {
            allHTML += `<ul>`;
            for (let a = 0; a < level3List.length; a++) {
                const lvl3Item = level3List[a];
                const lvl3ID = lvl3Item.getAttribute("id");
                const lvl3Text = lvl3Item.innerHTML;
                allHTML += `<li><a href="./#${lvl3ID}">${lvl3Text}</a></li>`;

                let level4List =
                    lvl3Item.parentElement.getElementsByClassName("lvl4");
                if (level4List.length > 0) {
                    allHTML += `<ul>`;
                    for (let a = 0; a < level4List.length; a++) {
                        const lvl4Item = level4List[a];
                        const lvl4ID = lvl4Item.getAttribute("id");
                        const lvl4Text = lvl4Item.innerHTML;
                        allHTML += `<li><a href="./#${lvl4ID}">${lvl4Text}</a></li>`;

                        let level5List =
                            lvl4Item.parentElement.getElementsByClassName(
                                "lvl5"
                            );
                        if (level5List.length > 0) {
                            allHTML += `<ul>`;
                            for (let a = 0; a < level5List.length; a++) {
                                const lvl5Item = level5List[a];
                                const lvl5ID = lvl5Item.getAttribute("id");
                                const lvl5Text = lvl5Item.innerHTML;
                                allHTML += `<li><a href="./#${lvl5ID}">${lvl5Text}</a></li>`;

                                let level6List =
                                    lvl5Item.parentElement.getElementsByClassName(
                                        "lvl3"
                                    );
                                if (level6List.length > 0) {
                                    allHTML += `<ul>`;
                                    for (
                                        let a = 0;
                                        a < level6List.length;
                                        a++
                                    ) {
                                        const lvl6Item = level6List[a];
                                        const lvl6ID =
                                            lvl6Item.getAttribute("id");
                                        const lvl6Text = lvl6Item.innerHTML;
                                        allHTML += `<li><a href="./#${lvl6ID}">${lvl6Text}</a></li>`;
                                    }

                                    allHTML += `</ul>`;
                                }
                            }

                            allHTML += `</ul>`;
                        }
                    }

                    allHTML += `</ul>`;
                }
            }

            allHTML += `</ul>`;
        }
    }
}
allHTML += `</ul>`;

let nav = document.getElementById("nav");
let testZone = document.getElementById("test-zone");
nav.innerHTML += allHTML;
testZone.innerHTML += allHTML;
