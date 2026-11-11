# CAHAYA – วัดช้างให้ WebAR 3D (MVP)

ชุดต้นแบบนี้ประกอบด้วยเว็บไซต์ AR ที่ใช้ **ภาพโปสเตอร์ของผู้ใช้เป็น Image Target** กับโมเดลเจดีย์ 3 มิติ `.glb` ที่สร้างขึ้นเป็นตัวอย่างเชิงศิลป์ (ไม่ใช่การบันทึกสถาปัตยกรรมจริงแบบแม่นยำ)

## ไฟล์ในชุด

- `index.html` — หน้า WebAR สำหรับเปิดกล้องและสแกนโปสเตอร์
- `preview.html` — ดูและหมุนโมเดล 3D โดยไม่ต้องใช้กล้อง
- `assets/target-wat-chang-hai.jpg` — ภาพโปสเตอร์ต้นฉบับสำหรับพิมพ์/สแกน
- `assets/wat-chang-hai-stupa.glb` — โมเดล 3D สไตล์เจดีย์และอาคารตัวอย่าง
- `tools/build_model.py` — สคริปต์ต้นฉบับสำหรับสร้างโมเดล (Python, numpy, trimesh)
- `assets/targets.mind` — **ยังไม่รวมในไฟล์ ZIP** ต้องสร้างจากภาพโปสเตอร์ตามข้อ 2 เพื่อให้ AR ตรวจจับได้จริง

## วิธีเปิดใช้งานจริง

### 1. ทดลองดูโมเดล 3D ก่อน

อัปโหลดไฟล์ทั้งหมดไปที่ GitHub repository (เช่น `wat-chang-hai-webar`) แล้วเปิด Settings → Pages → Deploy from a branch → main / root เพื่อให้ได้ลิงก์ HTTPS เช่น `https://YOURNAME.github.io/wat-chang-hai-webar/preview.html`

หรือเปิดด้วย local web server ที่รองรับ localhost ในคอมพิวเตอร์ เช่น `python -m http.server 8000` แล้วเข้า `http://localhost:8000/preview.html`

**หมายเหตุ:** ใช้การเชื่อมต่ออินเทอร์เน็ตเพื่อโหลด A-Frame จาก CDN

### 2. สร้างไฟล์จดจำภาพ `targets.mind` (จำเป็น)

1. ไปที่เครื่องมือทางการของ MindAR: https://hiukim.github.io/mind-ar-js-doc/tools/compile/
2. เพิ่มภาพ `assets/target-wat-chang-hai.jpg` จากชุดนี้
3. กด **Start** แล้วรอให้ประมวลผลและตรวจจุดสังเกตที่กระจายตัวบนภาพ
4. กด **Download** เพื่อรับไฟล์ `.mind`
5. เปลี่ยนชื่อไฟล์เป็น `targets.mind` และวางลงในโฟลเดอร์ `assets/` ข้างไฟล์รูปภาพและไฟล์ `.glb`
6. อัปโหลดไฟล์ `assets/targets.mind` ขึ้น GitHub อีกครั้ง

> เครื่องมือต้องแปลงภาพก่อนเพราะการจดจำภาพต้องอาศัยข้อมูล feature points ไม่ได้ใช้รูป JPEG ตรง ๆ ในขั้นตอนสแกน และภาพต้นฉบับต้องเหมือนภาพที่นำไปพิมพ์ ไม่ตัดภาพหรือเปลี่ยนเลย์เอาต์

### 3. ทดสอบสแกน AR

1. ใช้เครื่องพิมพ์พิมพ์ภาพ `target-wat-chang-hai.jpg` หรือเปิดภาพบนคอมพิวเตอร์/โทรศัพท์อีกเครื่อง
2. เปิด `https://YOURNAME.github.io/wat-chang-hai-webar/` ด้วยโทรศัพท์ที่มีกล้อง
3. กด **เริ่มสแกน AR** และอนุญาตการใช้กล้อง
4. ส่องไปที่ภาพโปสเตอร์ให้เห็นภาพครบทั้งแผ่น ในที่แสงเพียงพอ และไม่สะท้อนแสง
5. เมื่อระบบจับภาพได้ จะเห็นโมเดลลอยออกจากระนาบโปสเตอร์ ใช้ปุ่มหมุน/ย่อ/ขยาย

**ข้อจำกัด:** ไม่สามารถสแกนภาพโปสเตอร์ซึ่งแสดงบนหน้าจอเดียวกับกล้องโทรศัพท์ได้ จำเป็นต้องมีแผ่นพิมพ์หรือจออีกเครื่อง และไม่มี QR Code ที่ภาพต้นฉบับ

## สิ่งที่ทำได้ใน MVP

- รองรับภาพเป้าหมายหนึ่งภาพ (วัดช้างให้)
- เล่นโมเดล 3 มิติตัวอย่างเมื่อจับภาพได้
- ปุ่มหมุน ย่อ ขยาย รีเซ็ต ข้อมูล และปิดกล้อง
- หน้า Preview 3D ที่ไม่ต้องใช้การสแกน

## สิ่งที่ยังไม่ทำ / ขอบเขตถัดไป

- **Admin Dashboard / การล็อกอิน / ฐานข้อมูล:** ยังไม่ได้พัฒนาใน ZIP นี้
- **เพิ่มภาพ AR แบบไม่ต้องแตะโค้ด:** เป็นฟีเจอร์ในเฟสถัดไป
- **สร้างโมเดลเจดีย์ตรงกับวัดจริง:** ต้องทำ 3D modeling จากภาพถ่ายหลายมุมหรือแบบอาคารที่ได้รับอนุญาต
- **ไฟล์ .mind ที่ประมวลผลสำเร็จ:** ยังต้องทำขั้นตอนที่ 2 ก่อนจึงจะสแกนได้
- ต้องทดสอบการเปิดกล้องจริงบน iOS Safari และ Android Chrome ผ่าน HTTPS พร้อมไฟล์ `.mind`

## แนวทางสร้างแพลตฟอร์มเต็ม

- Frontend: GitHub Pages หรือ Cloudflare Pages
- Runtime AR: MindAR 1.2.5 + A-Frame 1.6.0 (CDN)
- Backend: Cloudflare Workers (API + authentication)
- Data: Cloudflare D1 สำหรับรายการ AR, revision และสิทธิ์ผู้ใช้
- Object storage: Cloudflare R2 สำหรับโปสเตอร์, GLB, `.mind` และภาพตัวอย่าง
- Target compilation: สร้างใน browser-admin ผ่านเครื่องมือ Compiler ที่ผ่านการทดสอบ ก่อนอัปโหลดไฟล์ `.mind` ลง R2
- ควรเก็บ target เดิมและโมเดลเดิมแบบ versioned ระหว่างการอัปเดต และมีหน้ากด Publish/Unpublish
- สำหรับผู้ชมจำนวนมาก โหลดเฉพาะ asset ที่จำเป็นต่อรายการ AR หนึ่งรายการ เพื่อลดเวลารอและการใช้หน่วยความจำ

## ข้อควรตรวจเมื่อใช้งานจริง

- ภาพโปสเตอร์มี feature points กระจายอย่างสม่ำเสมอ (ด้านบนขาวโล่งจึงต้องทดสอบจริง)
- พิมพ์บนวัสดุไม่สะท้อนแสง แสงพอและรูปไม่ถูกบัง
- GLB ควรมีขนาดเหมาะสมต่อมือถือ และมีการทดสอบประสิทธิภาพ
- เว็บเป็น HTTPS เสมอ เว้นแต่ทดสอบใน localhost
- เคารพลิขสิทธิ์ภาพโปสเตอร์ และสิทธิ์ในการใช้โมเดลอาคาร
- ตั้งค่า CSP/CORS กับไฟล์ใน R2 เมื่อย้าย assets ไปคนละโดเมน

## เอกสารอ้างอิงทางการ

- MindAR: https://hiukim.github.io/mind-ar-js-doc/
- Compiler: https://hiukim.github.io/mind-ar-js-doc/quick-start/compile/
- A-Frame gltf-model: https://aframe.io/docs/1.8.0/components/gltf-model.html
- Cloudflare R2: https://developers.cloudflare.com/r2/objects/upload-objects/

## ตัวช่วยอัปโหลด GitHub อัตโนมัติบน Windows

ชุดนี้มี `START_UPLOAD_WINDOWS.bat` และ `deploy.ps1` เป็นตัวช่วยสำหรับ **สร้าง Repository ใหม่ + อัปโหลดไฟล์ + ขอเปิด GitHub Pages** ในรอบเดียว (ไม่ได้อัปโหลดจาก ChatGPT ไปยัง GitHub ด้วยตัวเอง)

1. ติดตั้ง **Git for Windows** จาก https://git-scm.com/downloads/win และ **GitHub CLI** จาก https://cli.github.com/ (ทำเพียงครั้งแรก)
2. แตกไฟล์ ZIP บนคอมพิวเตอร์ Windows แล้วดับเบิลคลิก `START_UPLOAD_WINDOWS.bat`
3. ทำขั้นตอนลงชื่อเข้าใช้ GitHub ที่ปรากฏบนหน้าจอ (สคริปต์ไม่ต้องการรหัสผ่านหรือ Token ที่ส่งให้ผู้อื่น)
4. ระบบใช้ชื่อ Repository `wat-chang-hai-webar` บนบัญชีที่เข้าสู่ระบบ สร้างแบบ **Public** สำหรับ GitHub Pages และตั้งค่า Publish จาก `main / root`
5. เมื่อเผยแพร่แล้ว เปิดลิงก์ `https://ชื่อบัญชี.github.io/wat-chang-hai-webar/preview.html`

**ความปลอดภัย:** ถ้า Repository ชื่อเดียวกันมี branch/ข้อมูลอยู่แล้ว สคริปต์จะหยุดแทนการเขียนทับ และไม่แตะ Repository เก่าอื่น ๆ

**สำคัญ:** การอัปโหลดไม่เท่ากับ AR ใช้ได้ทันที เพราะต้องสร้าง `assets/targets.mind` เพิ่มสำหรับตรวจจับรูปต้นฉบับ หากยังไม่มีไฟล์นี้ หน้า Preview 3D ใช้ได้ แต่การสแกนรูป AR ยังใช้ไม่ได้